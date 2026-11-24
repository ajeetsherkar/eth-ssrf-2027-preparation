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
