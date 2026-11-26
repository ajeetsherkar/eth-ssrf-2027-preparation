# S4 — Math and Statistics: Distributions of Latency

## Dataset
- Project: TransitNexus
- Benchmark: PyTorch CPU FP32, 640x640, batch size 1
- Measurement scope: End-to-end prediction from an already-decoded BGR frame, including preprocessing, inference, NMS and Python predictor overhead
- Number of measurements: 200
- Source: `benchmark/results/pytorch_baseline/end_to_end/end-to-end-run-1/20261126_120207_latency.csv`

## Descriptive Statistics
| Metric | Result |
|---|---:|
| Mean | 47.044 ms |
| Median | 46.693 ms |
| P95 | 49.157 ms |
| P99 | 56.612 ms |
| Minimum | 43.727 ms |
| Maximum | 62.008 ms |

## Distribution Analysis
1. Most measurements are concentrated around 46–47.5 ms.
2. The mean is slightly higher than the median, suggesting that a few slower measurements pull the average upward.
3. The distribution has a right tail extending to 62.008 ms. Possible explanations include OS scheduling delays, cache misses and memory-management activity. These causes have not been independently verified.

## Outlier Assessment
- Threshold: 2 x median = 93.386 ms.
- Measurements above this threshold: 0 out of 200 (0%).
- Policy: Retain all measurements and report the tail. Do not silently remove slow observations.
- Note: The 2 x median threshold is distinct from the boxplot's conventional 1.5 x IQR rule.

## Figures
- `benchmark/results/pytorch_baseline/statistical_summary/s4_end_to_end_histogram.png`
- `benchmark/results/pytorch_baseline/statistical_summary/s4_end_to_end_boxplot.png`

## Limitations
- This analysis covers one end-to-end benchmark launch.
- Possible causes of the right tail have not been isolated experimentally.
- No measurements were removed.
