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
