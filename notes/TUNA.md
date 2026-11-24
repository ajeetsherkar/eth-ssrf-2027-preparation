# TUNA — Problem and Motivation

1. Software tuning helps systems find configurations that provide better performance.
2. Autotuning uses optimizers to test different configurations and select the best-performing one.
3. In cloud environments, hardware resource sharing and performance variability can make measurements noisy.
4. Noise and unstable configurations can cause autotuning to select configurations that perform poorly when deployed.
5. Therefore, finding configurations that are both high-performing and stable is an important challenge.

## Noise vs Variance

**Noise:** Unwanted disturbances that affect system performance measurements, such as background processes, CPU load, or resource sharing.

**Variance:** A statistical measure that tells us how much repeated measurements differ from their average. Low variance means consistent results, while high variance means widely spread results.

**Cloud example:** Other applications sharing a cloud server may consume CPU or memory, affecting execution time.

**Laptop example:** Background applications like Chrome may consume resources and increase ML model execution time.

**Key difference:** Noise is an unwanted disturbance; variance measures the spread of the observed results.

## Three Unfamiliar Terms

1. **System-under-Test (SuT):** The application or system whose performance is being tested. In the TUNA paper, PostgreSQL is an example of a SuT.

2. **Coefficient of Variation (CoV):** A measure of relative variability. It is calculated as (Standard Deviation / Mean) × 100%. A higher CoV indicates greater variation in measurements.

3. **Service Level Agreement (SLA):** An agreement between a service provider and customer that defines expected service levels, such as performance, availability, and reliability.

## 2. Background — Software Tuning and Performance Variability

### 2.1 Performance Variability

- Performance variability means that the same application can show different performance across repeated runs, even when its configuration remains unchanged.
- Possible causes include software non-determinism, hardware differences, resource sharing and interference from background workloads.
- In cloud environments, other virtual machines sharing the same infrastructure can affect performance.
- On a laptop, background applications, CPU usage, memory pressure and thermal throttling can affect execution time.

### 2.2 Noise vs Variance

- **Noise:** An unwanted disturbance that affects system performance measurements.
- **Variance:** A statistical measure of how much repeated measurements differ from their average.
- Example: A background application consuming CPU resources can introduce noise. The resulting differences in measured latency contribute to variance.
- Key difference: Noise is a possible cause; variance describes the spread of observed measurements.

### 2.3 Software Tuning and ML-based Tuning

- Software tuning means finding configurations that provide better system performance.
- ML-based tuning uses machine learning techniques to help search for good configurations.
- An optimizer suggests a configuration, the application runs, its performance is measured, and the result guides the next suggestion.
- Noisy measurements can mislead the optimizer into selecting a configuration that only appeared to perform well.

### 2.4 Online vs Offline Tuning

**Online tuning:**
- Changes configurations while the application is running.
- Incorrect configurations can affect the live system.
- It can be difficult to manage because changes may interrupt application behaviour.

**Offline tuning:**
- Tests different configurations separately from the live application.
- The best configuration can be selected and applied later.
- TUNA primarily focuses on offline tuning.

### 2.5 Two Important Goals of an Autotuner

1. **Discover an optimal configuration:** Find a configuration that provides the best performance.
2. **Rate of convergence:** Find a good configuration using fewer evaluations and less time.

An autotuner should not only find a good configuration but should also find it efficiently.

### 2.6 Why Cloud Noise Is a Problem

- Different machines can have different performance characteristics.
- Other workloads running on shared infrastructure can interfere with execution.
- Performance can change because of resource usage and environmental conditions.
- Existing noise-handling methods may assume a specific noise distribution, such as Gaussian noise.
- Real cloud noise can be more unpredictable and may not follow these assumptions.

### 2.7 Main Takeaways from the Background

1. The same application and configuration can produce different performance measurements.
2. Noise can mislead an autotuner and affect the configuration it selects.
3. Both online and offline tuning are sensitive to environmental noise.
4. An autotuner must find configurations that perform well and converge efficiently.
5. Reliable tuning must account for performance variability across machines and changing workloads.

### 2.8 Connection to TransitNexus

- We will compare PyTorch and ONNX Runtime under controlled conditions.
- We will keep model weights, benchmark video and machine environment consistent.
- We will repeat measurements to understand performance variability.
- We will record latency statistics instead of relying on a single execution.
- We will investigate unusual measurements rather than immediately assuming that a runtime is slower.

## 3. Motivation — Impact of Noise on System Tuning

### 3.1 Impact of Noise on Tuner Convergence

- The researchers tested an autotuner with 0%, 5%, and 10% noise.
- With 0% noise, the tuner reached the same noise-free performance in about 40 iterations.
- With 5% noise, it needed about 100 iterations.
- With 10% noise, convergence became even slower.
- The time-to-optimal performance was 2.5x slower with 5% noise and 4.35x slower with 10% noise compared with no noise.

**Key point:** More noise makes an autotuner take more experiments and time to find a good configuration.

### 3.2 Quantifying Cloud Noise

The researchers studied cloud performance for 480 days using:
- 40 microbenchmarks.
- 13 end-to-end application benchmarks.
- 92 performance metrics.
- More than 43,000 short-lived VMs and over 7 million data points.

**Main findings:**
- CPU and disk performance showed relatively low variability.
- Memory, operating system and cache showed higher variability.
- Their reported CoV values were:
  - Memory: 4.92%
  - OS: 9.82%
  - Cache: 14.39%
- Shared resources and interference can affect performance measurements.

**Key point:** Different system resources experience different levels of performance variability.

### 3.3 Burstable vs Non-burstable VMs

- **Burstable VMs:** Use accumulated credits to provide extra performance. When credits run out, performance can drop significantly.
- **Non-burstable VMs:** Do not depend on this burst-credit mechanism.

The researchers observed that burstable VMs could experience more than 50% performance degradation when disk credits were depleted.

Therefore, they used non-burstable VMs for the remaining experiments.

**Key point:** Burst-credit depletion can make performance measurements misleading.

### 3.4 Unstable Configurations

An unstable configuration performs well on some machines but poorly on others.

The researchers:
- Tested 30 tuning runs across 30 identically configured VMs.
- Found that 13 out of 30 transferred configurations were unstable.
- Observed performance degradation of more than 70% in some cases.
- Found CoV values as high as 36.3% for unstable configurations.

**Key point:** A configuration that performs well during tuning may not perform reliably on another machine.

### 3.5 Why Do Unstable Configurations Occur?

- Small performance differences between machines can affect system decisions.
- In PostgreSQL, these differences sometimes caused the query planner to select a much slower execution plan.
- A configuration could therefore appear fast on one machine and slow on another.

**Key point:** Small environmental differences can sometimes cause large performance changes.

### 3.6 Main Takeaways from Motivation

1. Increased noise slows down autotuner convergence.
2. Cloud resources experience different levels of performance variability.
3. Burstable VM credits can cause sudden performance degradation.
4. Unstable configurations may perform poorly when transferred to other machines.
5. Tuning systems must identify unstable configurations and use representative measurements.

### 3.7 Connection to TransitNexus

- Compare PyTorch and ONNX Runtime using repeated benchmark runs.
- Keep the model, input video and machine environment consistent.
- Record mean, standard deviation, p50, p95 and p99 latency.
- Investigate unusually high or low measurements.
- Do not select a runtime based on one unusually fast result.

**Remember:** The best configuration is not just the one that performs fastest once; it should also perform consistently.

---

## 4. Design — How TUNA Improves Autotuning

### Main Idea
TUNA improves autotuning by reducing measurement noise and identifying unstable configurations. It introduces four main components without changing the underlying optimizer or the system being tuned.

### 4.1 Multi-Fidelity Sampling
- Initially test a configuration on one machine.
- If it performs well, promote it and test it on more machines.
- If it performs poorly, discard it early.
- Uses **Successive Halving** to allocate testing resources.

**Meaning:** Spend more testing effort on promising configurations and save time on poor ones.

### 4.2 Unstable Configuration Detection
- Checks performance variation across multiple machines.
- Uses **Relative Range** to measure variation:

  Relative Range = (Maximum - Minimum) / Mean

- TUNA uses a 30% threshold to identify unstable configurations.
- Unstable configurations receive a penalty to discourage the optimizer from selecting them again.

**Meaning:** Identify and avoid configurations with unpredictable performance.

### 4.3 Sampling Noise Modeling
- System noise can affect application performance measurements.
- TUNA collects system metrics, such as CPU and memory usage, using psutil.
- It uses a **Random Forest Regressor** to predict noise-free performance.
- The model is trained using data collected during the current tuning run.
- Unstable configurations bypass this noise-adjustment model.

**Meaning:** Use system information and machine learning to reduce the effect of noisy measurements.

### 4.4 Sample Aggregation
- TUNA must provide one final performance value to the optimizer.
- It uses the **minimum** as its aggregation policy.
- This helps penalize configurations that experience poor performance or outliers.

**Meaning:** Consider the worst observed performance instead of relying only on the average.

### Figure 7 — TUNA Workflow
1. Optimizer suggests a configuration.
2. Multi-Fidelity Scheduler distributes testing across workers.
3. Workers return raw performance measurements.
4. Outlier Detector identifies unstable configurations.
5. Noise Adjuster corrects noisy measurements.
6. Aggregation Policy produces one final performance value.
7. Optimizer is updated with the result.

### Connection to TransitNexus
When comparing PyTorch and ONNX Runtime:
- Repeat measurements under controlled conditions.
- Check latency variation across repeated runs.
- Identify unusual measurements.
- Compare consistency as well as average performance.

**Remember:** TUNA has four key components — Multi-Fidelity Sampling, Unstable Configuration Detection, Sampling Noise Modeling, and Sample Aggregation.

The best configuration should not only be fast but also reliable and consistent.

## 5. Implementation — How TUNA Is Implemented

### 5.1 Implementation Tools

- TUNA is implemented using **Python**.
- **SMAC** is used as the default optimizer.
- **Nautilus** manages machine setup and cleanup during experiments.
- TUNA is evaluated for the same amount of time as traditional single-machine tuning.

### 5.2 Cluster Size

- TUNA uses a fixed group of machines called a **cluster**.
- More machines improve the chances of detecting unstable configurations but increase cost and delays.
- The researchers selected **10 machines** as the maximum sampling budget.
- This provides approximately **95% confidence** of detecting all unstable configurations in their experiments.
- Previous samples are reused when a configuration is tested with a higher budget.
- New samples must run on different machines from the previous tests.

**Figure 9 Meaning:** As the number of machines increases, the probability of detecting unstable configurations also increases. At 10 machines, it reaches approximately 95%.

### 5.3 Example Pipeline

Suppose TUNA tests one configuration:

1. Worker 1 gives **500 TPS**.
2. TUNA schedules two additional tests on different workers.
3. Worker 2 gives **450 TPS**.
4. Worker 3 gives **530 TPS**.
5. Outlier Detector calculates a Relative Range of **16.2%**. Since it is below 30%, the configuration is considered stable.
6. Noise Adjuster corrects the values to **460, 500 and 520 TPS**.
7. Aggregation Policy selects the minimum value: **460 TPS**.
8. The optimizer receives 460 TPS.

**TPS = Transactions Per Second.**

**Note:** During the first iteration, the Noise Adjuster is skipped because it does not yet have training data.

### Key Points to Remember

- **SMAC:** Default optimizer.
- **Nautilus:** Manages machine setup and cleanup.
- **10 machines:** Maximum sampling budget.
- **95% confidence:** Chance of detecting all unstable configurations in the researchers' experiments.
- **30%:** Unstable configuration detection threshold.
- **Minimum aggregation:** Sends the lowest adjusted performance value to the optimizer.

---

## Section 6: Evaluation

### 1. Evaluation objective

The researchers evaluated whether TUNA can:
- Find high-performing application configurations.
- Reduce performance variability.
- Select configurations that remain reliable when deployed on new systems.

The selected configurations were tested on 10 new systems to evaluate their performance after tuning.

### 2. Experimental setup

| Component | Setup |
|---|---|
| Application systems | PostgreSQL, Redis and NGINX |
| Worker nodes | 10 |
| Orchestrator nodes | 1 |
| Virtual machines | Azure D8s_v5 |
| Storage | SSDv2 data disk |
| Optimizer | SMAC |
| Surrogate model | Random Forest |
| Tuning duration | 8 hours |

Three approaches were compared:
1. **TUNA:** Uses distributed sampling and techniques to handle performance noise and unstable configurations.
2. **Traditional sampling:** Evaluates configurations sequentially on a single node without repeated samples.
3. **Default:** Uses the application's original configuration without tuning.

### 3. Evaluation metrics

| Metric | Meaning | Better direction |
|---|---|---|
| Throughput (TPS) | Transactions completed per second | Higher |
| Runtime | Time required to complete a workload | Lower |
| Latency | Time required to respond to a request | Lower |
| P95 latency | 95% of requests complete within this time | Lower |
| Standard deviation | Spread of performance measurements | Lower |

### 4. Main evaluation results

#### 4.1 Generalizability across workloads — Figure 11

PostgreSQL was evaluated using four workloads:

| Workload | TUNA result | Traditional result | Key observation |
|---|---:|---:|---|
| TPC-C | 1,925 TPS | 1,989 TPS | Traditional had slightly higher average throughput, but TUNA was more stable |
| Epinions | 34,957 TPS | 32,189 TPS | TUNA achieved higher throughput |
| TPC-H | 70.3 seconds | 94.5 seconds | TUNA reduced runtime |
| mssales | 33.2 seconds | 62.5 seconds | TUNA substantially reduced runtime |

Important observations:
- TPC-C: TUNA's standard deviation was 69 TPS versus 205.7 TPS for traditional sampling.
- Epinions: Some configurations selected by traditional sampling had high variability despite good training performance.
- TPC-H: TUNA completed the analytical workload faster.
- mssales: TUNA achieved approximately 47% lower runtime and 61.2% lower standard deviation than traditional sampling.

**Learning:** TUNA generalizes across transactional and analytical workloads. It does not always achieve the highest average performance, but it often selects more stable configurations.

#### 4.2 Generalizability across regions — Figure 12

The PostgreSQL TPC-C experiment was repeated in a different Azure region.

| Method | Throughput |
|---|---:|
| TUNA | 2,321 TPS |
| Traditional | 2,239 TPS |

Standard deviation:
- TUNA: 113 TPS
- Traditional: 267.7 TPS

**Learning:** TUNA can maintain better performance consistency across different cloud regions.

#### 4.3 Generalizability across hardware — Figure 13

Researchers tested PostgreSQL TPC-C on bare-metal CloudLab machines instead of Azure virtual machines.

| Method | Throughput |
|---|---:|
| TUNA | 5,756 TPS |
| Traditional | 5,380 TPS |

Traditional sampling had 7.71 times higher standard deviation.

**Learning:** TUNA is not limited to one cloud platform or virtual-machine environment.

#### 4.4 Generalizability across applications — Figures 14 and 15

**Redis — Figure 14**
- Workload: YCSB-C, mainly read operations.
- Metric: P95 latency.
- Some configurations selected through traditional sampling caused Redis crashes because of insufficient memory.
- TUNA avoided selecting the configurations that crashed and reduced variability.

**NGINX — Figure 15**
- Workload: Serving the top 500 Wikipedia pages.
- Metric: P95 latency.
- TUNA achieved 42.6 ms latency versus 46.6 ms for traditional sampling.
- TUNA had 63.3% lower standard deviation.

**Learning:** TUNA can be applied to different application types, including databases and web servers.

#### 4.5 Equal-cost comparisons — Figures 16 and 17

**Figure 16: Equal sample budget**
- Traditional sampling was allowed to use the same number of samples as TUNA.
- TUNA achieved 9.2% higher average performance and 87.8% lower standard deviation in this comparison.

**Figure 17: Naive distributed sampling**
- Naive distributed sampling evaluates configurations across all available nodes.
- TUNA uses multi-fidelity sampling, initially spending less effort on configurations and allocating more resources to promising ones.
- TUNA converged 2.47 times faster in the reported comparison.

**Learning:** Efficient allocation of the measurement budget can help find good configurations faster.

#### 4.6 Component analysis — Figures 18, 19 and 20

**Figure 18: Different optimizer**
- Researchers replaced the usual Random Forest-based optimizer with a Gaussian Process optimizer.
- TUNA achieved 53.1% higher performance and 89.5% lower standard deviation than traditional sampling in the comparison.

**Learning:** TUNA's benefits are not restricted to one optimizer.

**Figure 19: Noise Adjuster**
- Researchers compared TUNA with and without the Noise Adjuster over 100 tuning runs.
- The Noise Adjuster helped TUNA converge 13.3% faster.
- At the illustrated midpoint, relative error was 1.99% with the model versus 4.87% without it.

**Learning:** The Noise Adjuster reduces the influence of platform noise on performance estimates.

**Figure 20: Outlier Detector**
- Researchers compared TUNA with a version without the Outlier Detector.
- TUNA's average throughput was slightly lower: 2,572 TPS versus 2,810 TPS.
- Standard deviation was 54.8 TPS with TUNA versus 550.8 TPS without the detector.
- TUNA achieved approximately 10.1 times lower variability.

**Learning:** The Outlier Detector helps avoid configurations that appear fast but have highly unstable performance.

### 5. Overall findings

1. TUNA was evaluated across different workloads, regions, hardware platforms and applications.
2. It generally improved performance, reduced variability, or achieved both.
3. Its evaluation showed that high average performance alone is not sufficient.
4. The Noise Adjuster helps reduce errors caused by platform noise.
5. The Outlier Detector helps prevent unstable configurations from being selected.
6. Multi-fidelity sampling helps allocate experimental effort efficiently.

### 6. Connection to my TransitNexus benchmark

My benchmark compares PyTorch CPU and ONNX Runtime CPU for TransitNexus inference.

Lessons from TUNA:

- Keep the input data and measurement conditions consistent between runtimes.
- Perform warm-up iterations before collecting timed measurements.
- Record every individual latency measurement.
- Compare mean, median, P95, P99 and standard deviation.
- Monitor hardware and software conditions that may introduce measurement noise.
- Do not select a runtime based only on its lowest or average latency; consider consistency and tail latency too.

**Research takeaway:** A reliable benchmark should measure both performance and variability. The fastest average result is not automatically the most reliable choice.

---

---

## Section 7: Future Work

The researchers identified four areas for improving TUNA.

### 1. Add guardrails to the Noise Adjuster

- Currently, the Noise Adjuster can modify performance scores without a predefined limit.
- Unusual data patterns could cause excessive or unpredictable adjustments.
- Future work could introduce guardrails to limit how much the model changes a score.
- Designing these limits requires knowledge of the system's variability.

**Key point:** Prevent the Noise Adjuster from making excessive or unreliable score adjustments.

### 2. Improve the Outlier Detector

- Currently, the Outlier Detector applies a penalty when variability crosses a threshold.
- An alternative is to apply a penalty based on the relative range of observed performance.
- This approach requires an additional penalty hyperparameter, which the researchers wanted to avoid.

**Key point:** A future detector could consider the degree of performance variation instead of only checking whether a threshold is crossed.

### 3. Learn from previous tuning runs

- The current Noise Adjuster uses data collected only during the current tuning run.
- Researchers suggest transferring data from previous runs to warm-start the model.
- This could help the model become effective sooner.
- Challenges include differences in machines and workloads between previous and current runs.

**Key point:** Reusing knowledge from earlier experiments could improve learning speed, but transferring that knowledge reliably is difficult.

### 4. Support burstable and serverless nodes

- TUNA does not currently address burstable or serverless nodes.
- Burstable VMs have performance credits; when credits are depleted, performance may decrease.
- It is difficult to distinguish configuration instability from performance-credit depletion without platform introspection.
- A suitable configuration should perform well both when credits are available and when they are depleted.

**Key point:** TUNA needs better ways to distinguish configuration problems from platform resource limitations.

### Main limitations and research gaps

1. **Unbounded Noise Adjustments:** The Noise Adjuster has no explicit guardrails, so unusual data patterns could cause unpredictable score adjustments.
2. **Limited Platform Support:** Burstable and serverless environments are not addressed because credit depletion can be difficult to distinguish from configuration instability.
3. **No Cross-Run Learning:** The Noise Adjuster currently uses only current-run data; learning from previous runs remains future work.
4. **Threshold-Based Outlier Penalty:** The current detector uses a threshold-based penalty; a relative-range-based alternative remains unexplored.

---

## Section 8: Conclusion

### 1. Problems identified by the paper

The researchers identified two major problems in cloud system autotuning:

- Ignoring performance variability can make convergence to a good configuration slower and more expensive.
- Configurations that appear good during tuning may become unstable after deployment.

### 2. TUNA's three main mechanisms

1. **Multi-fidelity sampling:** Allocates testing effort efficiently to find good configurations.
2. **Outlier Detector:** Identifies and penalizes configurations with unstable performance.
3. **Noise Adjuster:** Uses component-level metrics to reduce the influence of performance noise during sampling.

### 3. Evaluation scope

The researchers evaluated TUNA across:

- 6 workloads.
- 3 systems.
- 2 deployment regions.
- 2 hardware setups.

### 4. Final research finding

TUNA reduced performance variability and improved the performance of tuned systems across the evaluated environments.

**Overall takeaway:** Selecting a configuration should involve both performance and stability. The highest average performance does not automatically mean the configuration is reliable after deployment.

---

## Connection to TransitNexus — Research Limitations and Scope

My benchmark compares PyTorch CPU and ONNX Runtime CPU using the same TransitNexus model and controlled input data.

Lessons from TUNA:

1. Record performance variability, not just average latency.
2. Keep warm-up, input data and measurement conditions consistent.
3. Report mean, median, P95, P99 and standard deviation.
4. Record the hardware and software environment.
5. Clearly state the tested hardware and runtime conditions.
6. Do not claim that CPU benchmark results automatically generalize to GPUs, other hardware or cloud environments.
7. Preserve unusual measurements and document failed or invalid runs.

**Research takeaway:** A good benchmark should report not only which runtime is faster, but also how consistent and reliable its performance is under the tested conditions.
