# Reproducibility record

## Environment

The public scripts were run successfully from the repository root on 2026-07-16 with Python 3.11.9. The verified packages were NumPy 2.4.6, pandas 3.0.3, matplotlib 3.11.0, and scikit-learn 1.9.0. `requirements.txt` provides compatible lower bounds. It does not claim to recreate the unavailable historical environment exactly.

## Run

```powershell
python -m pip install -r requirements.txt
python src\ridge_lasso_experiment.py
python src\nested_cv_demo.py
```

Both scripts use random seed 42. All paths are relative to the repository root.

## Outputs

`ridge_lasso_experiment.py` writes `ridge_lasso_metrics.csv`, `ridge_lasso_summary.csv`, and three PNG figures. `nested_cv_demo.py` writes `nested_cv_fold_results.csv`, `nested_cv_summary.csv`, and one PNG figure. CSV files are written to `results/`; figures are written to `figures/`.

## Verification

Both commands completed successfully in the public project directory. The nested-CV mean outer-fold MSE was 250.367053 and its sample standard deviation was 35.478253. The current selected-model metrics match the historical result values to the displayed precision.

The project is **basically reproducible, but lacks a historical dependency lock**. The original dependency manifest and persisted split indices are unavailable. Runtime data come from `make_regression`.
