# Final portfolio audit

## Positioning and data source

The project demonstrates reproducible regularized-regression evaluation: validation-based alpha selection, L1/L2 coefficient behavior, and nested cross-validation. Runtime data are generated with `make_regression`; the public repository has no external course-data dependency. A private archive was read only as an audit source and was not used as a script input.

## Code and evaluation audit

The original public candidates used a simulated 300-by-30 dataset (8 informative features, noise 15, seed 42), 60/20/20 splits, and a scaler fit only on training data. They selected alpha by validation MSE. Their nested-CV implementation used 5 outer folds, 3 inner folds, `Pipeline(StandardScaler(), Ridge())`, and positive outer-fold MSE calculated after `neg_mean_squared_error` tuning.

The public rewrite retains those core settings and results while replacing `os`/absolute-path handling with `pathlib`, explicit output directories, focused functions, and standard `main()` guards. The old primary MSE figure displayed all-alpha test curves. The rewrite removes those curves and writes test MSE only for the validation-selected model. This is not data leakage: the historical selection logic already used validation MSE. Removing the test sweep reduces the risk of indirect human tuning against test outcomes.

Nested CV is correctly isolated: each outer-test fold stays outside its inner search, and scaling occurs inside the pipeline. No result file is unexplained by the current scripts. The current runs reproduced the migrated numerical results exactly to the reported precision.

## Verified results

| Workflow | Verified result |
| --- | --- |
| Ridge | alpha 1.0; validation MSE 259.124939; final test MSE 256.702927; 30 nonzero coefficients |
| Lasso | alpha 1.0; validation MSE 258.716850; final test MSE 252.095471; 17 nonzero coefficients |
| Nested CV | outer-fold MSE mean 250.367053; sample SD 35.478253 |

Nested-CV inner selections by outer fold were 1.0, 0.001, 0.001, 1.0, and 0.1. Values are from the current public-directory run and agree with the migrated historical outputs.

## Attribution and publication boundary

The migration source policy classifies the two core scripts and their outputs as self-built experiment materials. This is supporting evidence, not an independent authorship declaration. Original Git history and a separate author declaration are unavailable, so no license has been added. Course materials, notebooks, submission files, private reports, and experiment subprojects with unconfirmed attribution are excluded.

## Reorganization record

The legacy public candidate files were SHA-256 checked against their migration manifest before removal. Their legacy code, result, and figure locations were replaced by the public `src/`, `results/`, and `figures/` structure. The code files were rewritten rather than byte-for-byte moved; their original checksums therefore remain audit evidence only. Newly generated results are not copied historical artifacts.

## Public safety and reproducibility

The final static scan found no drive-specific paths, personal identifiers, email addresses, credentials, private-archive references, restricted course files, or files above 5 MB. No broken Markdown links were found. Figures were visually checked against their CSV inputs. The project is **basically reproducible, but lacks a historical dependency lock**.

Suggested commit message: `feat: add reproducible machine learning evaluation portfolio`
