# Day 1 — S4: Math and Statistics
## Topic: Descriptive Statistics

### 1. Formulas

**Mean:** Sum of all observations divided by the number of observations.

Mean = Σx / n

**Median:** Middle value after sorting the data. For an even number of observations, take the average of the two middle values.

**Sample Variance:** Average squared deviation from the mean, dividing by n − 1.

s² = Σ(x − x̄)² / (n − 1)

**Sample Standard Deviation:** Square root of sample variance.

s = √s²

**Percentile (NumPy default — linear interpolation):**

h = (n − 1) × p

Here, p is the percentile expressed as a fraction. Interpolate between the values at the lower and upper positions.

### 2. Given Dataset

Data = 12, 13, 13, 14, 15, 15, 16, 18, 25, 40

Number of observations (n) = 10

Sum = 181

### 3. Calculations by Hand

**Mean:**

Mean = 181 / 10 = 18.1

**Median:**

There are 10 observations, so take the average of the 5th and 6th values.

Median = (15 + 15) / 2 = 15

**Sample Variance:**

Mean = 18.1

Sum of squared deviations = 656.9

Sample variance = 656.9 / (10 − 1)

Sample variance = 72.9889 ≈ 72.99

**Sample Standard Deviation:**

s = √72.9889

s ≈ 8.54

**95th Percentile (p95):**

h = (10 − 1) × 0.95 = 8.55

Using zero-based indexing:
- Position 8 = 25
- Position 9 = 40

p95 = 25 + 0.55 × (40 − 25)

p95 = 33.25

### 4. NumPy Verification

Python code:

```python
import numpy as np

d = [12, 13, 13, 14, 15, 15, 16, 18, 25, 40]

print(
    np.mean(d),
    np.median(d),
    np.var(d, ddof=1),
    np.std(d, ddof=1),
    np.percentile(d, 95)
)
```

Verified output:

- Mean = 18.1
- Median = 15.0
- Sample variance = 72.9889
- Sample standard deviation = 8.5434
- p95 = 33.25

### 5. Effect of the Outlier

The outlier 40 increased the mean to 18.1, while the median remained 15 because the median depends on the middle values rather than the magnitude of extreme values.

### Key Takeaway

The mean is affected by extreme values, while the median is more resistant to outliers. Variance and standard deviation measure data spread, and percentiles help understand the distribution of observations.
