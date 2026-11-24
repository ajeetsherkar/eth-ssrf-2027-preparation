# S4 — Confidence Intervals and Bootstrap

## Task 1: Why One Number Is Not a Result

A single benchmark number is not enough because the same program
can produce different execution times across repeated runs.

Reasons for variation:
- CPU load from other applications
- Background processes
- Memory usage
- Operating system scheduling
- Hardware and system noise

Therefore, multiple runs provide a more reliable picture of
program performance than one measurement.

## What Is a 95% Confidence Interval?

A 95% confidence interval (CI) is a range calculated from sample
data to estimate an unknown population parameter.

In simple words, instead of reporting only one estimated value,
we report a range that communicates uncertainty.

If we repeatedly collect samples and calculate intervals using
the same method, approximately 95% of those intervals will
contain the true population parameter.

## Example

Estimated median execution time: 123 ms
Illustrative 95% confidence interval: 119–127 ms

These are example values, not actual benchmark measurements.
