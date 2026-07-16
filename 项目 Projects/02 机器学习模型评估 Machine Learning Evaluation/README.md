# Machine Learning Evaluation

This repository is a compact, reproducible demonstration of model selection and evaluation for simulated linear-regression data. It is a portfolio project about evaluation workflow—not a production machine-learning system, an AutoML platform, or a real-world prediction study. Every run generates its dataset locally with `sklearn.datasets.make_regression`; no external data download or protected course file is required.

## What I implemented

I implemented two complementary workflows. First, I compare Ridge (L2) and Lasso (L1) regularization across six alpha values. I record training and validation MSE, coefficient L2 norm, and the number of nonzero coefficients. I select alpha separately for each model using validation MSE, then evaluate each selected model once on a held-out test set. I also export validation-focused figures for error, coefficient shrinkage, and Lasso sparsity.

Second, I implemented nested cross-validation for Ridge. A `Pipeline(StandardScaler(), Ridge())` keeps preprocessing inside each fold. Five outer folds estimate the performance of the selection procedure; a three-fold inner `GridSearchCV` chooses alpha from the same six candidates. Fold-level MSEs, selected alphas, an aggregate summary, and a figure are exported.

## Evaluation workflow

```text
Simulated data generation
  -> train / validation / test split (60% / 20% / 20%)
  -> StandardScaler fit on training features only
  -> alpha selection by validation MSE
  -> one final evaluation on the held-out test set
```

The ordinary comparison deliberately does not plot a test-set sweep across alpha values. This keeps the public presentation aligned with the selection rule and reduces the risk that test results influence human tuning decisions.

```text
Outer 5-fold cross-validation
  -> inner 3-fold GridSearchCV on the outer-training fold
  -> fold-specific scaling and alpha selection in a pipeline
  -> evaluation on the untouched outer-test fold
```

## Verified results

The current public scripts were run successfully on 2026-07-16. Both methods selected `alpha = 1.0` using validation MSE. Ridge achieved validation MSE 259.1249 and final test MSE 256.7029, with 30 nonzero coefficients. Lasso achieved validation MSE 258.7168 and final test MSE 252.0955, with 17 nonzero coefficients. These values describe this one simulated split only; they are not a general model ranking.

For nested CV, the mean outer-fold MSE was 250.3671 (sample standard deviation 35.4783). The five inner-loop selections were 1.0, 0.001, 0.001, 1.0, and 0.1. The variation is reported to show that tuning outcomes can change across resampled training folds.

## Reproducibility

Use Python 3.11+ and install the dependencies:

```powershell
python -m pip install -r requirements.txt
python src\ridge_lasso_experiment.py
python src\nested_cv_demo.py
```

The fixed random seed is 42. Generated CSV files are written to `results/`; PNG figures are written to `figures/`. The workflow has been validated from this public repository structure. See [docs/reproducibility.md](docs/reproducibility.md) for the tested package versions and verification record.

## Limitations and repository boundary

The data are simulated; this is a regression-only demonstration with no external validation dataset. A fixed seed does not recreate every historical software environment, and split indices are generated at runtime rather than persisted. Nested-CV stability statements apply only to the configuration in this repository and do not establish real-world performance.

This repository excludes course materials, course notebooks, assignment or submission files, private reports, and course experiment subprojects with unconfirmed attribution. The private archive informed the source audit only and is not a runtime dependency. Attribution is based on the recorded internal source policy and existing files; an independent authorship declaration and original Git history are unavailable. License: Not yet specified.
