# Audited validation results

## Selection by highest validation mAP50-95

| Condition | Epoch | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|---:|
| Standard | 40 | 0.58295 | 0.53123 | 0.53969 | 0.31296 |
| From3Class | 40 | 0.63734 | 0.53157 | 0.56365 | 0.32864 |

## Separate mAP50 peak

| Condition | Epoch | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|---:|
| Standard | 45 | 0.62147 | 0.51475 | 0.54002 | 0.31190 |
| From3Class | 41 | 0.65535 | 0.52117 | 0.56376 | 0.32720 |

## Final complete epoch

| Condition | Epoch | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|---:|
| Standard | 50 | 0.62883 | 0.50296 | 0.53512 | 0.30997 |
| From3Class | 50 | 0.63911 | 0.52584 | 0.54876 | 0.31786 |

Every value is validation-only and comes from one archived run per condition. The mAP50 and mAP50-95 peaks occur at different epochs; they are intentionally not combined into a single synthetic “best” row.
