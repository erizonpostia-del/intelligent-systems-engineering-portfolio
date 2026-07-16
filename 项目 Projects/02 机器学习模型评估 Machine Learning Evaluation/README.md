# Machine Learning Evaluation

I built this project to work through two parts of regression evaluation that are easy to get wrong in a small experiment: choosing hyperparameters without consulting the test set, and estimating the performance of the whole selection procedure rather than one fitted model. The data are generated at runtime with `sklearn.datasets.make_regression`, so the repository is self-contained and does not represent a real business or scientific prediction task.

## What I implemented

I compared Ridge (L2) and Lasso (L1) regression across six alpha values: 0.001, 0.01, 0.1, 1.0, 10.0, and 100. I recorded training and validation MSE, coefficient L2 norm, and the number of nonzero coefficients. This lets me examine the error trade-off alongside the different ways the two penalties shrink coefficients.

I separated the data into training, validation, and test partitions at 60%/20%/20%. I fit `StandardScaler` on training features only, then applied it to the validation and test partitions. I chose alpha using validation MSE, then evaluated each selected model once on the held-out test set. Keeping those decisions separate is the central design choice in the first workflow.

I also added a nested cross-validation example for Ridge. Its 5-fold outer loop estimates the performance of selection and fitting, while a 3-fold inner `GridSearchCV` selects alpha. I used `Pipeline(StandardScaler(), Ridge())` so scaling is fit separately inside each fold instead of leaking information across a split.

## Evaluation workflow

```text
Simulated data generation
  -> train / validation / test split (60% / 20% / 20%)
  -> StandardScaler fit on training features only
  -> alpha selection by validation MSE
  -> final evaluation on the held-out test set
```

The ordinary comparison plots training and validation curves only. I left the test-set sweep out of the public results because it can encourage decisions based on information that should remain reserved for final evaluation.

```text
Outer 5-fold cross-validation
  -> inner 3-fold GridSearchCV on each outer-training fold
  -> fold-specific scaling and alpha selection in a pipeline
  -> evaluation on the untouched outer-test fold
```

## Results from the verified run

I ran the public scripts successfully on 2026-07-16. Both models selected `alpha = 1.0` from validation MSE. Ridge produced validation MSE 259.1249 and final test MSE 256.7029, with 30 nonzero coefficients. Lasso produced validation MSE 258.7168 and final test MSE 252.0955, with 17 nonzero coefficients.

The nested-CV mean outer-fold MSE was 250.3671, with a sample standard deviation of 35.4783. The inner loop selected 1.0, 0.001, 0.001, 1.0, and 0.1 across the five outer folds. That variation is useful here: it shows that the selected alpha can change when the available training data change.

These values come from one simulated configuration. They do not establish that either regularizer is generally better.

## Run the project

Use Python 3.11+ and install the dependencies:

```powershell
python -m pip install -r requirements.txt
python src\ridge_lasso_experiment.py
python src\nested_cv_demo.py
```

The seed is 42. The scripts write CSV files to `results/` and PNG figures to `figures/`. [docs/reproducibility.md](docs/reproducibility.md) records the tested package versions and the verification result.

## Scope and repository boundary

This is a simulated regression example with no external validation dataset. The split indices are generated at runtime, and a fixed seed does not recreate every historical software environment. The nested-CV result applies to this setup, not to deployment performance or real feature importance.

I kept course materials, course notebooks, assignment and submission files, private reports, and unconfirmed course subprojects outside this repository. [docs/project_notes.md](docs/project_notes.md) summarizes the public scope and license status. License: Not yet specified.
