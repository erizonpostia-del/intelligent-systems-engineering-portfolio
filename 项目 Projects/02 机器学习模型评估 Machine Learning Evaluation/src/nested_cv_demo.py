"""Estimate Ridge model-selection performance with nested cross-validation."""

from __future__ import annotations

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

matplotlib.use("Agg")
import matplotlib.pyplot as plt


RANDOM_STATE = 42
ALPHAS = (0.001, 0.01, 0.1, 1.0, 10.0, 100.0)
DATASET_CONFIG = {"n_samples": 300, "n_features": 30, "n_informative": 8, "noise": 15.0, "random_state": RANDOM_STATE}
OUTER_FOLDS = 5
INNER_FOLDS = 3
RIDGE_COLOR = "#0F4D92"
MEAN_COLOR = "#B64342"


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


def save_plot(fig: plt.Figure, figures_dir: Path, stem: str) -> None:
    """Save the README-ready raster figure without duplicate exports."""
    fig.tight_layout()
    output_path = figures_dir / stem
    fig.savefig(output_path.with_suffix(".png"), dpi=300)
    plt.close(fig)


def output_directories() -> tuple[Path, Path]:
    """Create and return public output directories relative to this source file."""
    project_root = Path(__file__).resolve().parents[1]
    results_dir, figures_dir = project_root / "results", project_root / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)
    return results_dir, figures_dir


def make_dataset() -> tuple[np.ndarray, np.ndarray]:
    """Generate the same simulated regression data used in the comparison demo."""
    return make_regression(**DATASET_CONFIG)


def run_nested_cv(features: np.ndarray, target: np.ndarray) -> pd.DataFrame:
    """Tune alpha inside each outer-training fold and score the held-out fold."""
    outer_cv = KFold(n_splits=OUTER_FOLDS, shuffle=True, random_state=RANDOM_STATE)
    inner_cv = KFold(n_splits=INNER_FOLDS, shuffle=True, random_state=RANDOM_STATE)
    pipeline = Pipeline([("scaler", StandardScaler()), ("ridge", Ridge())])
    records: list[dict[str, float | int]] = []
    for fold, (train_index, test_index) in enumerate(outer_cv.split(features, target), start=1):
        search = GridSearchCV(
            estimator=pipeline,
            param_grid={"ridge__alpha": ALPHAS},
            scoring="neg_mean_squared_error",
            cv=inner_cv,
            refit=True,
        )
        search.fit(features[train_index], target[train_index])
        prediction = search.predict(features[test_index])
        records.append(
            {
                "outer_fold": fold,
                "selected_alpha": float(search.best_params_["ridge__alpha"]),
                "outer_test_mse": mean_squared_error(target[test_index], prediction),
            }
        )
    return pd.DataFrame.from_records(records)


def save_figure(results: pd.DataFrame, figures_dir: Path) -> None:
    """Plot outer-fold MSEs and their mean without exposing inner test data."""
    apply_figure_style()
    fig, ax = plt.subplots(figsize=(6.8, 4.3))
    ax.plot(
        results["outer_fold"],
        results["outer_test_mse"],
        marker="o",
        markersize=6,
        linewidth=2.0,
        color=RIDGE_COLOR,
        label="Outer-fold MSE",
    )
    ax.axhline(
        results["outer_test_mse"].mean(),
        color=MEAN_COLOR,
        linestyle="--",
        linewidth=1.7,
        label="Mean outer-fold MSE",
    )
    ax.set(xticks=results["outer_fold"], xlabel="Outer fold", ylabel="Mean squared error", title="Nested cross-validation outer-fold results")
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.7)
    ax.tick_params(direction="out", length=4, width=0.8)
    ax.legend(loc="upper left")
    save_plot(fig, figures_dir, "nested_cv_results")


def main() -> None:
    """Run nested CV and write fold-level and aggregate public results."""
    results_dir, figures_dir = output_directories()
    features, target = make_dataset()
    results = run_nested_cv(features, target)
    summary = pd.DataFrame(
        [{"outer_folds": OUTER_FOLDS, "inner_folds": INNER_FOLDS, "mean_outer_test_mse": results["outer_test_mse"].mean(), "std_outer_test_mse": results["outer_test_mse"].std(ddof=1)}]
    )
    results.to_csv(results_dir / "nested_cv_fold_results.csv", index=False)
    summary.to_csv(results_dir / "nested_cv_summary.csv", index=False)
    save_figure(results, figures_dir)
    print(results.to_string(index=False))
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
