# Day 1 — S3: Performance Fundamentals

## Experiment 1: Matrix size 256 × 256

### Observations

1. The first iteration was slower than the remaining iterations in both updated runs.
2. The overall mean latency was approximately 0.0306 ms in both runs.
3. The p50 was approximately 0.0318 ms, showing consistent typical performance.
4. The p99 varied more between runs than the mean and p50.
5. The last 100 iterations had relatively stable latency measurements.

### Conclusion

Initial iterations may include first-call overhead and should not automatically be treated as representative of steady-state performance. Warm-up helps reduce this effect. Repeated runs and percentiles help us understand performance consistency and occasional slow operations.

## Experiment 2: Matrix size 1024 × 1024

### Results

- Mean latency: 1.55985 ms
- p50 latency: 1.54377 ms
- p95 latency: 1.61299 ms
- p99 latency: 1.74879 ms
- Last 100 mean: 1.54985 ms
- Last 100 p99: 1.60335 ms

### Comparison with 256 × 256

- Mean increased from approximately 0.03059 ms to 1.55985 ms (about 51 times).
- p95 increased from approximately 0.03196 ms to 1.61299 ms.
- p99 increased from approximately 0.03534 ms to 1.74879 ms.

### Three-line Takeaway

1. Warm-up is necessary because initial iterations can include overhead and may not represent steady-state performance.
2. Reporting only mean latency can hide occasional slow operations, so p50, p95 and p99 should also be reported.
3. Repeated measurements and percentiles help evaluate both performance and consistency.

## Fundamental Definitions

- **Latency:** The time taken by a system to complete one operation or respond to one request.
- **Throughput:** The number of operations or requests a system can process in a given amount of time.
- **Warm-up:** Running a system before measurement to reduce the effect of initial overhead.
- **Tail latency:** The latency of the slowest portion of requests, commonly described using p95 and p99.
- **p50:** The median; 50% of operations complete within this time.
- **p95:** 95% of operations complete within this time; the slowest 5% take longer.
- **p99:** 99% of operations complete within this time; the slowest 1% take longer.

**Why mean can hide poor user experience:** A few very slow requests can affect some users significantly even when the average latency looks acceptable.
