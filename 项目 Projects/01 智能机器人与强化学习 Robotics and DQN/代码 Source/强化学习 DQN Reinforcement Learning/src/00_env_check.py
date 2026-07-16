"""Check FlappyBird-v0 LIDAR environment health."""

from __future__ import annotations

import argparse
from pathlib import Path

import gymnasium as gym
import numpy as np

import flappy_bird_gymnasium  # noqa: F401
from wrappers import make_flappy_env


ROOT = Path(__file__).resolve().parents[1]


def describe_obs(prefix: str, obs: np.ndarray) -> None:
    print(f"{prefix} shape: {obs.shape}")
    print(f"{prefix} dtype: {obs.dtype}")
    print(f"{prefix} min: {float(np.min(obs)):.6f}")
    print(f"{prefix} max: {float(np.max(obs)):.6f}")
    print(f"{prefix} mean: {float(np.mean(obs)):.6f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--max-steps", type=int, default=10000)
    args = parser.parse_args()

    print("Raw environment probe")
    raw_env = gym.make("FlappyBird-v0", use_lidar=True)
    raw_obs, raw_info = raw_env.reset(seed=args.seed)
    print("raw action space:", raw_env.action_space)
    print("raw observation space:", raw_env.observation_space)
    describe_obs("raw reset observation", np.asarray(raw_obs))
    print("raw reset info:", raw_info)
    raw_env.close()
    print("ObservationSanitizeWrapper is enabled for all project scripts.")

    env = make_flappy_env(use_features=False, reward_shaping="none")
    obs, info = env.reset(seed=args.seed)
    print("wrapped action space:", env.action_space)
    print("wrapped observation space:", env.observation_space)
    describe_obs("wrapped reset observation", obs)
    print("wrapped reset info:", info)

    total_reward = 0.0
    steps = 0
    score = int(info.get("score", 0))
    terminated = False
    truncated = False
    while not (terminated or truncated) and steps < args.max_steps:
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += float(reward)
        steps += 1
        score = int(info.get("score", score))

    print("random episode total reward:", round(total_reward, 4))
    print("random episode steps:", steps)
    print("random episode score:", score)
    env.close()
    print("environment closed successfully")


if __name__ == "__main__":
    main()

