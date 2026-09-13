"""Environment wrappers for FlappyBird LIDAR DQN experiments."""

from __future__ import annotations

from dataclasses import dataclass
from collections import deque
from typing import Any

import gymnasium as gym
import numpy as np
import flappy_bird_gymnasium  # noqa: F401 - registers FlappyBird-v0


class ObservationSanitizeWrapper(gym.ObservationWrapper):
    """Convert observations to float32 and clip small LIDAR overshoots."""

    def __init__(self, env: gym.Env):
        super().__init__(env)
        shape = env.observation_space.shape
        self.observation_space = gym.spaces.Box(
            low=0.0,
            high=1.0,
            shape=shape,
            dtype=np.float32,
        )

    def observation(self, observation: Any) -> np.ndarray:
        obs = np.asarray(observation, dtype=np.float32)
        return np.clip(obs, 0.0, 1.0)


class LidarFeatureWrapper(gym.ObservationWrapper):
    """Append obstacle features to the original 180-D LIDAR vector.

    The raw LIDAR remains intact. Added values are only observations for the
    neural network; this wrapper never chooses or changes actions.
    """

    def __init__(self, env: gym.Env):
        super().__init__(env)
        if env.observation_space.shape != (180,):
            raise ValueError(
                f"LidarFeatureWrapper expects 180-D observations, got {env.observation_space.shape}"
            )

        self.feature_dim = self._extract_features(np.ones(180, dtype=np.float32)).shape[0]
        self.observation_space = gym.spaces.Box(
            low=0.0,
            high=1.0,
            shape=(180 + self.feature_dim,),
            dtype=np.float32,
        )

    def observation(self, observation: Any) -> np.ndarray:
        lidar = np.asarray(observation, dtype=np.float32)
        lidar = np.clip(lidar, 0.0, 1.0)
        features = self._extract_features(lidar)
        return np.concatenate([lidar, features]).astype(np.float32)

    @staticmethod
    def _safe_stats(values: np.ndarray) -> list[float]:
        if values.size == 0:
            return [1.0, 1.0]
        return [float(np.min(values)), float(np.mean(values))]

    def _extract_features(self, lidar: np.ndarray) -> np.ndarray:
        lidar = np.clip(np.asarray(lidar, dtype=np.float32), 0.0, 1.0)
        diffs = np.abs(np.diff(lidar))
        danger_idx = float(np.argmin(lidar)) / max(1.0, float(lidar.size - 1))

        features: list[float] = [
            float(np.min(lidar)),
            float(np.max(lidar)),
            float(np.mean(lidar)),
            float(np.std(lidar)),
            float(np.min(lidar[70:111])),   # forward cone
            float(np.min(lidar[:60])),      # upper sector
            float(np.min(lidar[120:])),     # lower sector
            danger_idx,
            float(np.max(diffs)) if diffs.size else 0.0,
        ]

        sectors = [
            lidar[:45],
            lidar[45:90],
            lidar[90:135],
            lidar[135:],
        ]
        for sector in sectors:
            features.extend(self._safe_stats(sector))

        for start in range(0, 180, 15):
            window = lidar[start : start + 15]
            features.extend(self._safe_stats(window))

        return np.clip(np.asarray(features, dtype=np.float32), 0.0, 1.0)


class FrameStackObservationWrapper(gym.Wrapper):
    """Stack the last N observations to expose motion trends to DQN."""

    def __init__(self, env: gym.Env, num_stack: int):
        super().__init__(env)
        if num_stack < 1:
            raise ValueError("num_stack must be >= 1")
        self.num_stack = int(num_stack)
        self.frames: deque[np.ndarray] = deque(maxlen=self.num_stack)
        base_shape = env.observation_space.shape
        if len(base_shape) != 1:
            raise ValueError(f"FrameStackObservationWrapper expects 1-D observations, got {base_shape}")
        self.observation_space = gym.spaces.Box(
            low=0.0,
            high=1.0,
            shape=(base_shape[0] * self.num_stack,),
            dtype=np.float32,
        )

    def _get_observation(self) -> np.ndarray:
        return np.concatenate(list(self.frames)).astype(np.float32)

    def reset(self, **kwargs: Any):
        obs, info = self.env.reset(**kwargs)
        obs = np.asarray(obs, dtype=np.float32)
        self.frames.clear()
        for _ in range(self.num_stack):
            self.frames.append(obs)
        return self._get_observation(), info

    def step(self, action: int):
        obs, reward, terminated, truncated, info = self.env.step(action)
        self.frames.append(np.asarray(obs, dtype=np.float32))
        return self._get_observation(), reward, terminated, truncated, info


@dataclass(frozen=True)
class RewardShapingConfig:
    name: str = "none"
    alive_bonus: float = 0.0
    pass_pipe_bonus: float = 0.0
    death_penalty: float = 0.0
    safe_lidar_bonus: float = 0.0


class RewardShapingWrapper(gym.Wrapper):
    """Optional mild reward shaping for training only."""

    def __init__(self, env: gym.Env, config: RewardShapingConfig):
        super().__init__(env)
        self.config = config
        self._last_score = 0

    def reset(self, **kwargs: Any):
        obs, info = self.env.reset(**kwargs)
        self._last_score = int(info.get("score", 0))
        return obs, info

    def step(self, action: int):
        obs, reward, terminated, truncated, info = self.env.step(action)
        shaped = float(reward)
        shaped += self.config.alive_bonus

        score = int(info.get("score", self._last_score))
        score_delta = max(0, score - self._last_score)
        shaped += self.config.pass_pipe_bonus * score_delta
        self._last_score = score

        if self.config.safe_lidar_bonus:
            lidar = np.asarray(obs[:180], dtype=np.float32)
            forward_clearance = float(np.min(lidar[70:111]))
            shaped += self.config.safe_lidar_bonus * forward_clearance

        if terminated or truncated:
            shaped -= self.config.death_penalty

        return obs, shaped, terminated, truncated, info


def get_reward_shaping(name: str) -> RewardShapingConfig:
    if name == "none":
        return RewardShapingConfig(name="none")
    if name == "mild":
        return RewardShapingConfig(
            name="mild",
            alive_bonus=0.01,
            pass_pipe_bonus=0.5,
            death_penalty=1.0,
            safe_lidar_bonus=0.002,
        )
    raise ValueError(f"Unknown reward shaping config: {name}")


def make_flappy_env(
    *,
    render_mode: str | None = None,
    use_features: bool = False,
    reward_shaping: str = "none",
    frame_stack: int = 1,
) -> gym.Env:
    env = gym.make(
        "FlappyBird-v0",
        use_lidar=True,
        render_mode=render_mode,
        disable_env_checker=True,
    )
    env = ObservationSanitizeWrapper(env)
    if use_features:
        env = LidarFeatureWrapper(env)
    if frame_stack > 1:
        env = FrameStackObservationWrapper(env, frame_stack)
    shaping = get_reward_shaping(reward_shaping)
    if shaping.name != "none":
        env = RewardShapingWrapper(env, shaping)
    return env


