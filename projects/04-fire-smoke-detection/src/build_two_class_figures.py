#!/usr/bin/env python3
"""Rebuild public two-class README figures from sanitized CSV files only."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

LOG = logging.getLogger(__name__)
ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"

RUN_ORDER = ["v1_640", "v2_640", "v2_960"]
RUN_LABELS = {
    "v1_640": "v1 640",
    "v2_640": "v2 640",
    "v2_960": "v2 960",
}


def configure() -> None:
    plt.rcParams.update(
        {
            "font.size": 11,
            "axes.titlesize": 16,
            "axes.labelsize": 12,
            "legend.fontsize": 10,
            "figure.dpi": 180,
            "savefig.dpi": 180,
        }
    )


def save(fig: plt.Figure, filename: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / filename, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def annotate_bars(ax: plt.Axes, bars, fmt: str = ".3f", offset: float = 0.01) -> None:
    for bar in bars:
        value = bar.get_height()
        label = format(value, fmt)
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + offset,
            label,
            ha="center",
            va="bottom",
            fontsize=10,
        )


def checkpoint_comparison() -> None:
    data = pd.read_csv(RESULTS / "two_class_checkpoint_metrics.csv")
    labels = ["v1 640", "v2 640", "v2 960"]
    x = np.arange(len(data))
    width = 0.34

    fig, ax = plt.subplots(figsize=(10, 5.625))
    bars1 = ax.bar(x - width / 2, data["mAP50"], width, label="mAP50")
    bars2 = ax.bar(x + width / 2, data["mAP50_95"], width, label="mAP50–95")
    ax.set_title("Two-class checkpoints on the same v2 validation split")
    ax.set_ylabel("Metric")
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 0.58)
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False)
    annotate_bars(ax, bars1, ".3f", 0.009)
    annotate_bars(ax, bars2, ".3f", 0.009)
    fig.tight_layout()
    save(fig, "two_class_checkpoint_comparison.png")


def per_class_figures() -> None:
    data = pd.read_csv(RESULTS / "two_class_per_class_metrics.csv")
    data["run_id"] = data["run"].map(
        {
            "Development v1 — 640": "v1_640",
            "Development v2 — 640": "v2_640",
            "Development v2 — 960": "v2_960",
        }
    )
    x = np.arange(3)
    width = 0.34
    labels = ["v1 640", "v2 640", "v2 960"]

    for field, title, ylabel, filename, ylim in [
        (
            "recall",
            "Per-class recall on the same v2 validation split",
            "Recall",
            "two_class_per_class_recall.png",
            (0, 0.72),
        ),
        (
            "mAP50_95",
            "Per-class localization quality on the same v2 validation split",
            "mAP50–95",
            "two_class_per_class_map50_95.png",
            (0, 0.34),
        ),
    ]:
        pivot = (
            data.pivot(index="run_id", columns="class", values=field)
            .loc[RUN_ORDER]
        )
        fig, ax = plt.subplots(figsize=(10, 5.625))
        fire = ax.bar(x - width / 2, pivot["fire"], width, label=f"Fire {ylabel.lower()}")
        smoke = ax.bar(x + width / 2, pivot["smoke"], width, label=f"Smoke {ylabel.lower()}")
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_xticks(x, labels)
        ax.set_ylim(*ylim)
        ax.grid(axis="y", alpha=0.25)
        ax.legend(frameon=False)
        annotate_bars(ax, fire, ".3f", 0.012 if field == "recall" else 0.007)
        annotate_bars(ax, smoke, ".3f", 0.012 if field == "recall" else 0.007)
        fig.tight_layout()
        save(fig, filename)


def dataset_evolution() -> None:
    data = pd.read_csv(RESULTS / "two_class_dataset_statistics.csv")
    fields = ["positive_samples", "negative_samples", "fire_boxes", "smoke_boxes"]
    labels = ["Positive\nsamples", "Negative\nsamples", "Fire\nboxes", "Smoke\nboxes"]
    x = np.arange(len(fields))
    width = 0.34

    fig, ax = plt.subplots(figsize=(10, 5.625))
    bars1 = ax.bar(
        x - width / 2,
        data.iloc[0][fields].astype(float),
        width,
        label="Development v1",
    )
    bars2 = ax.bar(
        x + width / 2,
        data.iloc[1][fields].astype(float),
        width,
        label="Development v2",
    )
    ax.set_title("Two-class dataset evolution")
    ax.set_ylabel("Count")
    ax.set_xticks(x, labels)
    ax.set_ylim(0, float(data[fields].max().max()) * 1.18)
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False)
    annotate_bars(ax, bars1, ".0f", 20)
    annotate_bars(ax, bars2, ".0f", 20)
    fig.tight_layout()
    save(fig, "two_class_dataset_evolution.png")


def targeted_review() -> None:
    data = pd.read_csv(RESULTS / "two_class_targeted_smoke_review.csv")
    wanted = ["positive", "negative", "ambiguous", "exclude"]
    rows = data.set_index("outcome").loc[wanted]
    labels = ["Positive", "Negative", "Ambiguous", "Excluded"]
    values = rows["count"].astype(float).to_numpy()

    fig, ax = plt.subplots(figsize=(10, 5.625))
    bars = ax.bar(labels, values)
    ax.set_title("Targeted small/distant-smoke review outcomes")
    ax.set_ylabel("Candidate count")
    ax.set_ylim(0, values.max() * 1.18)
    ax.grid(axis="y", alpha=0.25)
    annotate_bars(ax, bars, ".0f", 6)
    ax.text(
        0.99,
        0.97,
        "15 / 396 positives (3.8%)",
        transform=ax.transAxes,
        ha="right",
        va="top",
    )
    fig.tight_layout()
    save(fig, "targeted_smoke_review_outcomes.png")


def progression_figures() -> None:
    data = pd.read_csv(RESULTS / "two_class_training_curves.csv")

    v1 = data[data["run_id"] == "v1_640"]
    fig, ax = plt.subplots(figsize=(10, 5.625))
    ax.plot(v1["epoch"], v1["mAP50"], label="mAP50", linewidth=2)
    ax.plot(v1["epoch"], v1["mAP50_95"], label="mAP50–95", linewidth=2)
    ax.axvline(
        33,
        linestyle="--",
        linewidth=1,
        label="Retained best checkpoint: epoch 33",
    )
    ax.set_title("Development v1 native training progression")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Metric")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    save(fig, "v1_native_training_progression.png")

    for field, filename, title, ylabel in [
        (
            "mAP50",
            "v2_map50_training_progression.png",
            "v2 training progression on the shared dataset",
            "mAP50",
        ),
        (
            "mAP50_95",
            "v2_map50_95_training_progression.png",
            "v2 localization progression on the shared dataset",
            "mAP50–95",
        ),
    ]:
        fig, ax = plt.subplots(figsize=(10, 5.625))
        for run_id, label in [("v2_640", "v2 640"), ("v2_960", "v2 960")]:
            run = data[data["run_id"] == run_id]
            ax.plot(run["epoch"], run[field], label=label, linewidth=2)
        ax.set_title(title)
        ax.set_xlabel("Epoch")
        ax.set_ylabel(ylabel)
        ax.grid(alpha=0.25)
        ax.legend(frameon=False)
        fig.tight_layout()
        save(fig, filename)


def governance_pipeline() -> None:
    steps = [
        "Source-media\nregistration",
        "SHA-256 exact-\nduplicate control",
        "Modality and\nsemantic review",
        "Annotation\nreview",
        "Temporal\ngrouping",
        "Scene/event\nadjudication",
        "Cluster-aware\nsplit planning",
        "Dataset\nfreezing",
        "Training and\nevaluation",
    ]
    coords = [
        (0.17, 0.80),
        (0.50, 0.80),
        (0.83, 0.80),
        (0.83, 0.50),
        (0.50, 0.50),
        (0.17, 0.50),
        (0.17, 0.20),
        (0.50, 0.20),
        (0.83, 0.20),
    ]

    fig, ax = plt.subplots(figsize=(12, 6.75))
    ax.axis("off")
    for index, (step, (x, y)) in enumerate(zip(steps, coords)):
        ax.text(
            x,
            y,
            step,
            ha="center",
            va="center",
            bbox={
                "boxstyle": "round,pad=.55",
                "fc": "#f5f7fa",
                "ec": "#62748a",
            },
            fontsize=10,
        )
        if index < len(steps) - 1:
            nx, ny = coords[index + 1]
            ax.annotate(
                "",
                xy=(nx, ny),
                xytext=(x, y),
                arrowprops={
                    "arrowstyle": "->",
                    "lw": 1.4,
                    "color": "#62748a",
                    "shrinkA": 50,
                    "shrinkB": 50,
                },
            )
    ax.set_title("Data governance pipeline", pad=20)
    fig.tight_layout()
    save(fig, "data_governance_pipeline.png")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rebuild two-class public README figures from sanitized CSV files."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check expected input files without writing figures.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Alias for --dry-run for publication QA.",
    )
    args = parser.parse_args()

    required = [
        RESULTS / "two_class_checkpoint_metrics.csv",
        RESULTS / "two_class_per_class_metrics.csv",
        RESULTS / "two_class_dataset_statistics.csv",
        RESULTS / "two_class_targeted_smoke_review.csv",
        RESULTS / "two_class_training_curves.csv",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        for path in missing:
            LOG.error("Missing input: %s", path)
        return 1

    if args.dry_run or args.check:
        print("Inputs found. Figures would be written to:", FIGURES)
        return 0

    configure()
    checkpoint_comparison()
    per_class_figures()
    dataset_evolution()
    targeted_review()
    progression_figures()
    governance_pipeline()
    print("Generated two-class public figures in:", FIGURES)
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    raise SystemExit(main())
