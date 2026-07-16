# Methodology

## Scope

This project uses a simulated linear-regression task to demonstrate evaluation mechanics. `make_regression` generates 300 samples with 30 features, 8 informative features, Gaussian noise of 15, and random seed 42. These conditions support a controlled comparison; they do not represent a business, scientific, or external benchmark dataset.

## Ridge and Lasso comparison

Ridge applies L2 regularization and typically shrinks coefficients continuously. Lasso applies L1 regularization and can set coefficients exactly to zero. The comparison records both coefficient L2 norm and the count of nonzero coefficients so that the two regularization behaviors can be inspected alongside predictive error.

The data are split 60%/20%/20% into training, validation, and test partitions. `StandardScaler` is fit only on the training features, then transforms validation and test features. This prevents the validation and test distributions from influencing fitted scaling statistics.

Each candidate alpha (0.001, 0.01, 0.1, 1.0, 10.0, 100.0) is fitted on the same training partition. The minimum validation MSE selects alpha independently for Ridge and Lasso. The test partition is then used once per selected model. The metrics table intentionally contains no test MSE for the full alpha grid, and the primary error figure contains training and validation curves only. Therefore, alpha selection is not based on test performance.

## Nested cross-validation

The second workflow estimates the performance of the entire selection process rather than a model selected on one fixed validation partition. A shuffled 5-fold outer `KFold` creates evaluation folds. For each outer-training fold, a 3-fold inner `KFold` drives `GridSearchCV` over the same alpha candidates. The estimator is `Pipeline([StandardScaler(), Ridge()])`, so scaling is refitted within every inner training fold and when the selected pipeline is refit on the outer-training fold.

`GridSearchCV` uses `neg_mean_squared_error`, which follows scikit-learn's convention that higher scorer values are better. The final recorded outer-fold quantity is ordinary, positive MSE computed with `mean_squared_error` on the untouched outer-test fold.

The reported outer-fold mean summarizes expected error for this simulated configuration. Its sample standard deviation describes variation among five folds, not uncertainty over every possible dataset or a claim about real deployment. The current experiment supports statements about this workflow's mechanics, the observed coefficient shrinkage, and the observed fold variation. It cannot establish a generally superior regularizer, identify real features, or make a business-performance claim.
