"""Shared configuration, seed, artifact, and evaluation helpers for extension runs."""

from __future__ import annotations

import csv
import hashlib
import json
import platform
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import gymnasium
import numpy as np
import torch

from wrappers import make_flappy_env


ROOT = Path(__file__).resolve().parents[1]
OBSERVATIONS = {
    "raw_1frame": {"use_features": False, "frame_stack": 1, "expected_input_dimension": 180},
    "raw_4frame": {"use_features": False, "frame_stack": 4, "expected_input_dimension": 720},
    "feature_1frame": {"use_features": True, "frame_stack": 1, "expected_input_dimension": 221},
    "feature_4frame": {"use_features": True, "frame_stack": 4, "expected_input_dimension": 884},
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def set_all_seeds(seed: int) -> dict[str, Any]:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    return {
        "python_random": seed,
        "numpy": seed,
        "torch_cpu": seed,
        "torch_cuda": seed if torch.cuda.is_available() else None,
        "torch_deterministic_algorithms": False,
        "cudnn_deterministic": bool(torch.backends.cudnn.deterministic) if torch.cuda.is_available() else None,
    }


def make_env(variant: str, seed: int):
    if variant not in OBSERVATIONS:
        raise ValueError(f"Unknown observation variant: {variant}")
    spec = OBSERVATIONS[variant]
    env = make_flappy_env(use_features=spec["use_features"], frame_stack=spec["frame_stack"], reward_shaping="none")
    env.action_space.seed(seed)
    obs, info = env.reset(seed=seed)
    actual = int(np.prod(env.observation_space.shape))
    if actual != spec["expected_input_dimension"]:
        env.close()
        raise RuntimeError(f"Dimension mismatch for {variant}: expected {spec['expected_input_dimension']}, got {actual}")
    return env, obs, info


def append_csv(path: Path, row: dict[str, Any], fields: list[str]) -> None:
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        if not exists:
            writer.writeheader()
        writer.writerow(row)


def prepare_run(config: dict[str, Any]) -> tuple[str, Path, dict[str, Any]]:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = f"{stamp}_{config['algorithm']}_{config['observation_variant']}_seed{config['train_seed']}"
    run_id = base
    index = 1
    while (ROOT / "runs" / run_id).exists():
        index += 1
        run_id = f"{base}_{index:02d}"
    run_dir = ROOT / "runs" / run_id
    for name in ["checkpoints", "figures"]:
        (run_dir / name).mkdir(parents=True, exist_ok=False)
    record = dict(config)
    record["run_id"] = run_id
    (run_dir / "config.yaml").write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    manifest = {
        "created_at": utc_now(),
        "files": [
            {"file": str(path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(path)}
            for path in sorted((ROOT / "src").glob("*.py"))
        ],
    }
    (run_dir / "source_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return run_id, run_dir, record


def environment_snapshot() -> dict[str, Any]:
    packages: dict[str, str | None] = {"torch": torch.__version__, "gymnasium": gymnasium.__version__, "numpy": np.__version__}
    try:
        import flappy_bird_gymnasium
        packages["flappy_bird_gymnasium"] = getattr(flappy_bird_gymnasium, "__version__", None)
    except Exception as exc:  # records the actual import state without failing an otherwise usable run
        packages["flappy_bird_gymnasium"] = f"unavailable: {exc}"
    return {
        "timestamp": utc_now(), "os": platform.platform(), "python": sys.version,
        "executable": sys.executable, "cpu": platform.processor(), "cuda_available": torch.cuda.is_available(),
        "cuda_version": torch.version.cuda, "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        "packages": packages,
    }


def write_environment(run_dir: Path) -> None:
    snapshot = environment_snapshot()
    (run_dir / "environment.json").write_text(json.dumps(snapshot, indent=2), encoding="utf-8")


def evaluate(model: torch.nn.Module, algorithm: str, variant: str, run_id: str, checkpoint_hash: str, train_seed: int, seeds: list[int], split: str, device: torch.device, output: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    fields = ["run_id", "split", "checkpoint_sha256", "algorithm", "observation_variant", "train_seed", "eval_seed", "episode_index", "score", "total_reward", "episode_length", "terminated", "truncated", "success_score_ge_10", "epsilon", "evaluation_timestamp"]
    model.eval()
    for index, seed in enumerate(seeds, start=1):
        env, obs, info = make_env(variant, seed)
        done = False
        score = int(info.get("score", 0))
        reward_total = 0.0
        steps = 0
        terminated = truncated = False
        while not done:
            obs_t = torch.as_tensor(obs, dtype=torch.float32, device=device).unsqueeze(0)
            action = int(model(obs_t).argmax(dim=1).item())
            obs, reward, terminated, truncated, info = env.step(action)
            score = int(info.get("score", score)); reward_total += float(reward); steps += 1
            done = bool(terminated or truncated)
        env.close()
        row = {"run_id": run_id, "split": split, "checkpoint_sha256": checkpoint_hash, "algorithm": algorithm, "observation_variant": variant, "train_seed": train_seed, "eval_seed": seed, "episode_index": index, "score": score, "total_reward": reward_total, "episode_length": steps, "terminated": terminated, "truncated": truncated, "success_score_ge_10": score >= 10, "epsilon": 0.0, "evaluation_timestamp": utc_now()}
        append_csv(output, row, fields); rows.append(row)
    return rows


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    scores = np.asarray([row["score"] for row in rows], dtype=np.float64)
    return {"count": int(scores.size), "mean": float(scores.mean()), "median": float(np.median(scores)), "standard_deviation": float(scores.std()), "min": int(scores.min()), "max": int(scores.max()), "success_score_ge_10_count": int((scores >= 10).sum()), "success_rate": float((scores >= 10).mean())}
