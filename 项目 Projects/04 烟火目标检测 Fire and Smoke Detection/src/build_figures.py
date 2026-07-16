"""Regenerate portfolio figures from audited public CSV files only.

This script does not load a dataset, model, checkpoint, or training environment.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
COLORS = {"Standard": "#3568A8", "From3Class": "#C26A3A"}


def configure() -> None:
    plt.rcParams.update(
        {
            "figure.dpi": 200,
            "savefig.dpi": 220,
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "legend.fontsize": 9,
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )


def selected_rows() -> pd.DataFrame:
    metrics = pd.read_csv(RESULTS / "validation_best_metrics.csv")
    return metrics.loc[metrics["selection_metric"] == "mAP50-95"].copy()


def save(fig: plt.Figure, name: str) -> None:
    FIGURES.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(FIGURES / name, bbox_inches="tight")
    plt.close(fig)


def map_comparison(rows: pd.DataFrame) -> None:
    conditions = rows["condition"].tolist()
    x = range(len(conditions))
    width = 0.34
    fig, ax = plt.subplots(figsize=(9, 5))
    for offset, metric, label, hatch in [(-width / 2, "map50", "Validation mAP50", ""), (width / 2, "map50_95", "Validation mAP50-95", "//")]:
        values = rows[metric].tolist()
        bars = ax.bar([i + offset for i in x], values, width, label=label, color="#3568A8" if metric == "map50" else "#C26A3A", hatch=hatch)
        ax.bar_label(bars, labels=[f"{value:.3f}" for value in values], padding=3, fontsize=9)
    ax.set_xticks(list(x), conditions)
    ax.set_ylim(0, 0.7)
    ax.set_ylabel("Validation metric")
    ax.set_title("Archived validation mAP at each run's highest mAP50-95 epoch")
    ax.text(0.5, -0.18, "Single archived run per condition; validation only.", transform=ax.transAxes, ha="center", va="top")
    ax.legend(frameon=False)
    save(fig, "validation_map_comparison.png")


def precision_recall(rows: pd.DataFrame) -> None:
    conditions = rows["condition"].tolist()
    x = range(len(conditions))
    width = 0.34
    fig, ax = plt.subplots(figsize=(9, 5))
    for offset, metric, label, hatch in [(-width / 2, "precision", "Validation precision", ""), (width / 2, "recall", "Validation recall", "//")]:
        values = rows[metric].tolist()
        bars = ax.bar([i + offset for i in x], values, width, label=label, color="#3568A8" if metric == "precision" else "#C26A3A", hatch=hatch)
        ax.bar_label(bars, labels=[f"{value:.3f}" for value in values], padding=3, fontsize=9)
    ax.set_xticks(list(x), conditions)
    ax.set_ylim(0, 0.8)
    ax.set_ylabel("Validation metric")
    ax.set_title("Archived validation precision and recall\n(at each run's highest mAP50-95 epoch)")
    ax.text(0.5, -0.18, "Single archived run per condition; metrics do not establish a universal winner.", transform=ax.transAxes, ha="center", va="top")
    ax.legend(frameon=False, loc="upper right")
    save(fig, "precision_recall_comparison.png")


def progression(condition: str, filename: str) -> None:
    table = pd.read_csv(RESULTS / filename)
    fig, ax = plt.subplots(figsize=(9, 5))
    series = [("map50", "Validation mAP50", "#3568A8"), ("map50_95", "Validation mAP50-95", "#C26A3A"), ("precision", "Validation precision", "#4F8A5B"), ("recall", "Validation recall", "#8A5BA8")]
    for column, label, color in series:
        ax.plot(table["epoch"], table[column], marker="o", markersize=2.5, linewidth=1.6, label=label, color=color)
    ax.set_xlim(1, 50)
    ax.set_ylim(0, 0.8)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Validation metric")
    ax.set_title(f"{condition}: archived validation progression")
    ax.text(0.5, -0.18, "One archived run; unsmoothed values from the audited per-epoch CSV.", transform=ax.transAxes, ha="center", va="top")
    ax.legend(ncol=2, frameon=False, loc="lower right")
    save(fig, f"training_progression_{condition.lower()}.png")


def main() -> None:
    configure()
    rows = selected_rows()
    map_comparison(rows)
    precision_recall(rows)
    progression("Standard", "standard_epoch_metrics.csv")
    progression("From3Class", "from3class_epoch_metrics.csv")


if __name__ == "__main__":
    main()
