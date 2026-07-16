"""Compare Ridge and Lasso on a reproducible simulated regression task.

Alpha is selected exclusively with validation-set MSE.  The held-out test set
is evaluated once for each selected model and is never used to rank alphas.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

matplotlib.use("Agg")
import matplotlib.pyplot as plt


RANDOM_STATE = 42
ALPHAS = (0.001, 0.01, 0.1, 1.0, 10.0, 100.0)
DATASET_CONFIG = {
    "n_samples": 300,
    "n_features": 30,
    "n_informative": 8,
    "noise": 15.0,
    "random_state": RANDOM_STATE,
}
COLORS = {"Ridge": "#0F4D92", "Lasso": "#B64342"}


def apply_figure_style() -> None:
    """Apply a consistent publication-oriented style without changing plotted content."""
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "DejaVu Sans", "Liberation Sans"],
            "font.size": 10,
            "axes.titlesize": 13,
            "axes.labelsize": 11,
            "axes.linewidth": 0.8,
            "axes.spines.right": False,
            "axes.spines.top": False,
            "legend.frameon": False,
            "legend.fontsize": 9,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
        }
    )


def save_figure(fig: plt.Figure, figures_dir: Path, stem: str) -> None:
    """Save the README-ready raster figure without duplicate exports."""
    fig.tight_layout()
    output_path = figures_dir / stem
    fig.savefig(output_path.with_suffix(".png"), dpi=300)
    plt.close(fig)


def output_directories() -> tuple[Path, Path]:
    """Create and return the public results and figures directories."""
    project_root = Path(__file__).resolve().parents[1]
    results_dir = project_root / "results"
    figures_dir = project_root / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)
    return results_dir, figures_dir


def make_dataset() -> tuple[np.ndarray, np.ndarray]:
    """Generate the fixed simulated regression dataset."""
    return make_regression(**DATASET_CONFIG)


def split_and_scale(
    features: np.ndarray, target: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Make 60/20/20 splits and fit the scaler on training features only."""
    x_train_val, x_test, y_train_val, y_test = train_test_split(
        features, target, test_size=0.20, random_state=RANDOM_STATE
    )
    x_train, x_validation, y_train, y_validation = train_test_split(
        x_train_val, y_train_val, test_size=0.25, random_state=RANDOM_STATE
    )
    scaler = StandardScaler()
    return (
        scaler.fit_transform(x_train),
        scaler.transform(x_validation),
        scaler.transform(x_test),
        y_train,
        y_validation,
        y_test,
    )


def build_model(model_name: str, alpha: float) -> Ridge | Lasso:
    """Instantiate one supported regularized linear model."""
    if model_name == "Ridge":
        return Ridge(alpha=alpha)
    if model_name == "Lasso":
        return Lasso(alpha=alpha, max_iter=100_000, tol=1e-4, random_state=RANDOM_STATE)
    raise ValueError(f"Unsupported model: {model_name}")


def evaluate_candidates(
    x_train: np.ndarray,
    x_validation: np.ndarray,
    y_train: np.ndarray,
    y_validation: np.ndarray,
) -> pd.DataFrame:
    """Fit every candidate on training data and record non-test diagnostics."""
    records: list[dict[str, float | int | str]] = []
    for model_name in ("Ridge", "Lasso"):
        for alpha in ALPHAS:
            model = build_model(model_name, alpha)
            model.fit(x_train, y_train)
            coefficients = model.coef_
            records.append(
                {
                    "model": model_name,
                    "alpha": alpha,
                    "train_mse": mean_squared_error(y_train, model.predict(x_train)),
                    "validation_mse": mean_squared_error(
                        y_validation, model.predict(x_validation)
                    ),
                    "coefficient_l2_norm": float(np.linalg.norm(coefficients, ord=2)),
                    "nonzero_coefficient_count": int(np.count_nonzero(np.abs(coefficients) > 1e-8)),
                }
            )
    return pd.DataFrame.from_records(records)


def evaluate_selected_models(
    candidates: pd.DataFrame,
    x_train: np.ndarray,
    x_test: np.ndarray,
    y_train: np.ndarray,
    y_test: np.ndarray,
) -> pd.DataFrame:
    """Select one alpha per model by validation MSE, then evaluate it once on test."""
    selected_rows: list[dict[str, float | int | str]] = []
    for model_name, model_candidates in candidates.groupby("model", sort=False):
        selected = model_candidates.loc[model_candidates["validation_mse"].idxmin()]
        model = build_model(model_name, float(selected["alpha"]))
        model.fit(x_train, y_train)
        selected_rows.append(
            {
                "model": model_name,
                "selected_alpha": float(selected["alpha"]),
                "validation_mse": float(selected["validation_mse"]),
                "final_test_mse": mean_squared_error(y_test, model.predict(x_test)),
                "coefficient_l2_norm": float(np.linalg.norm(model.coef_, ord=2)),
                "nonzero_coefficient_count": int(
                    np.count_nonzero(np.abs(model.coef_) > 1e-8)
                ),
            }
        )
    return pd.DataFrame.from_records(selected_rows)


def save_figures(candidates: pd.DataFrame, figures_dir: Path) -> None:
    """Export validation-focused diagnostic figures without test-set sweeps."""
    apply_figure_style()

    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    for model_name, rows in candidates.groupby("model", sort=False):
        ax.plot(
            rows["alpha"],
            rows["train_mse"],
            marker="o",
            markersize=5.5,
            linewidth=2.0,
            color=COLORS[model_name],
            label=f"{model_name} train MSE",
        )
        ax.plot(
            rows["alpha"],
            rows["validation_mse"],
            marker="o",
            markersize=5.5,
            linewidth=2.0,
            linestyle="--",
            color=COLORS[model_name],
            label=f"{model_name} validation MSE",
        )
    ax.set(
        xscale="log",
        yscale="log",
        xlabel="Regularization strength (alpha)",
        ylabel="Mean squared error (log scale)",
        title="Training and validation MSE by alpha",
    )
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.7)
    ax.tick_params(direction="out", length=4, width=0.8)
    ax.legend(loc="upper left", ncol=2, columnspacing=1.2, handlelength=2.2)
    save_figure(fig, figures_dir, "ridge_lasso_validation_curve")

    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    for model_name, rows in candidates.groupby("model", sort=False):
        ax.plot(
            rows["alpha"],
            rows["coefficient_l2_norm"],
            marker="o",
            markersize=5.5,
            linewidth=2.0,
            color=COLORS[model_name],
            label=model_name,
        )
    ax.set(xscale="log", xlabel="Regularization strength (alpha)", ylabel="Coefficient L2 norm", title="Coefficient shrinkage by alpha")
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.7)
    ax.tick_params(direction="out", length=4, width=0.8)
    ax.legend(loc="upper right")
    save_figure(fig, figures_dir, "coefficient_norms")

    lasso_rows = candidates.loc[candidates["model"] == "Lasso"]
    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    ax.plot(
        lasso_rows["alpha"],
        lasso_rows["nonzero_coefficient_count"],
        marker="o",
        markersize=5.5,
        linewidth=2.0,
        color=COLORS["Lasso"],
    )
    ax.set(xscale="log", xlabel="Regularization strength (alpha)", ylabel="Nonzero coefficients", title="Lasso sparsity by alpha", ylim=(-1, DATASET_CONFIG["n_features"] + 1))
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.7)
    ax.tick_params(direction="out", length=4, width=0.8)
    save_figure(fig, figures_dir, "lasso_sparsity")


def main() -> None:
    """Run the validation-based Ridge/Lasso comparison and export its artifacts."""
    results_dir, figures_dir = output_directories()
    features, target = make_dataset()
    x_train, x_validation, x_test, y_train, y_validation, y_test = split_and_scale(features, target)
    candidates = evaluate_candidates(x_train, x_validation, y_train, y_validation)
    selected = evaluate_selected_models(candidates, x_train, x_test, y_train, y_test)
    candidates.to_csv(results_dir / "ridge_lasso_metrics.csv", index=False)
    selected.to_csv(results_dir / "ridge_lasso_summary.csv", index=False)
    save_figures(candidates, figures_dir)
    print(selected.to_string(index=False))


if __name__ == "__main__":
    main()
