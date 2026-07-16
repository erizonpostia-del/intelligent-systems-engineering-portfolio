"""Algorithm variants used by the isolated extension workspace."""

from __future__ import annotations

import torch
from torch import nn

from networks import DuelingDQN


ALGORITHMS = {
    "vanilla_dqn": {"dueling": False, "double": False},
    "double_dqn": {"dueling": False, "double": True},
    "dueling_dqn": {"dueling": True, "double": False},
    "double_dueling_dqn": {"dueling": True, "double": True},
}


class VanillaDQN(nn.Module):
    """Single-stream MLP Q-network used by vanilla and Double DQN."""

    def __init__(self, obs_dim: int, action_dim: int, hidden_dims: tuple[int, ...]):
        super().__init__()
        layers: list[nn.Module] = []
        last = obs_dim
        for width in hidden_dims:
            layers.extend([nn.Linear(last, width), nn.ReLU()])
            last = width
        layers.append(nn.Linear(last, action_dim))
        self.network = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


def algorithm_spec(algorithm: str) -> dict[str, bool]:
    try:
        return ALGORITHMS[algorithm]
    except KeyError as exc:
        raise ValueError(f"Unsupported algorithm: {algorithm}") from exc


def build_network(algorithm: str, obs_dim: int, action_dim: int, hidden_dims: tuple[int, ...]) -> nn.Module:
    spec = algorithm_spec(algorithm)
    if not spec["dueling"]:
        return VanillaDQN(obs_dim, action_dim, hidden_dims)
    return DuelingDQN(obs_dim, action_dim, hidden_dims)


def next_state_value(algorithm: str, online: nn.Module, target: nn.Module, next_obs: torch.Tensor) -> torch.Tensor:
    """Return the target-side bootstrap value without silently reshaping tensors."""
    if algorithm_spec(algorithm)["double"]:
        next_actions = online(next_obs).argmax(dim=1, keepdim=True)
        return target(next_obs).gather(1, next_actions)
    return target(next_obs).max(dim=1, keepdim=True).values
