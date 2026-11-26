# Decoding Speculative Decoding — S2 Paper Notes

**Paper:** Decoding Speculative Decoding
**Authors:** Minghao Yan, Saurabh Agarwal, Shivaram Venkataraman
**Venue:** NAACL 2025
**Official paper:** https://aclanthology.org/2025.naacl-long.328.pdf

## 1. Problem in my own words

Autoregressive LLM inference generates tokens sequentially, one at a time.
This leads to poor hardware utilization and low generation throughput.
Speculative decoding uses a smaller draft model to propose multiple tokens
and a larger target model to verify those tokens in parallel.
However, the draft model itself can become a latency bottleneck.
The research problem is how to design draft models that maximize throughput.

## 2. Explanation for a classmate

A large neural network normally predicts one token at a time, waiting for
each prediction before generating the next. This makes text generation
slow. Speculative decoding uses a smaller model to propose several tokens
in advance. The larger model checks these proposals together and accepts
the matching tokens. This can speed up generation while preserving output
quality, provided the smaller model is fast enough.

## 3. Five-line problem note

1. Autoregressive decoding generates one token at a time.
2. Sequential generation causes poor hardware utilization and low throughput.
3. Speculative decoding uses a smaller draft model to propose multiple tokens.
4. The target model verifies draft tokens in parallel.
5. Draft-model latency is a key bottleneck that must be reduced.

## 4. Two questions I still have

1. How does the target model verify multiple draft tokens in parallel while
   preserving the original model's output distribution?
2. Why can a wider and shallower draft model be faster than a deeper model
   with a similar number of parameters?

## 5. Key terms

- Autoregressive decoding: Generating tokens sequentially.
- Draft model: Smaller model that proposes candidate tokens.
- Target model: Main LLM that verifies proposed tokens.
- Throughput: Number of generated tokens per second.
- TAR: Tokens accepted per speculative decoding iteration.

## 6. Reading scope

This note covers the abstract and introduction only.
Detailed experimental findings and draft-model design are for later reading.

---

# Detailed Paper Study

## Section 1: Abstract — Easy Explanation

### 1. What is Speculative Decoding?

Speculative Decoding is a technique used to speed up inference
(generating predictions or responses) in Large Language Models (LLMs)
without sacrificing the target model's output quality.

Normally, autoregressive LLMs generate tokens one at a time.
Speculative decoding tries to make this process faster by using
a smaller draft model and a larger target model.

### 2. How does Speculative Decoding work?

Two models are involved:

- **Draft Model:** A smaller, faster model that proposes multiple
  speculative tokens.
- **Target Model:** The larger original LLM that verifies the
  proposed tokens.

Basic workflow:

1. The draft model generates several candidate tokens.
2. The target model verifies the proposed tokens together.
3. Matching tokens are accepted.
4. Incorrect proposals are rejected or corrected.
5. The process continues from the resulting sequence.

The target model remains responsible for maintaining its original
output distribution. Speculative decoding aims to accelerate
generation without changing the target model's output quality.

### 3. Why is the choice of Draft Model important?

The speedup provided by speculative decoding heavily depends on
the choice of the draft model.

A good draft model should:

- Generate speculative tokens quickly.
- Propose tokens that the target model is likely to accept.
- Avoid becoming a latency bottleneck.

Example:

- Draft Model A generates proposals in 5 ms.
- Draft Model B generates proposals in 30 ms.

Even if Model B has better language-modelling capability,
its higher latency may reduce the overall speedup.

The goal is to balance draft-model speed and useful predictions.

### 4. Experiments conducted by the researchers

The authors performed more than 350 experiments using:

- LLaMA-65B
- OPT-66B

Here, B means billion parameters.

The objective was to investigate the factors that affect the
performance gains of speculative decoding.

### 5. Main research findings

**Finding 1: Draft-model latency is important.**

The performance of speculative decoding depends heavily on
the latency of the draft model.

If the draft model takes too long to generate candidate tokens,
it can become a bottleneck and reduce the overall speedup.

**Finding 2: Language-modelling capability does not guarantee
better speculative-decoding performance.**

A draft model may perform well on normal language-modelling tasks,
but that does not necessarily mean it will perform well in
speculative decoding.

Other important factors include:

- Draft-model generation latency.
- Number of proposed tokens accepted by the target model.
- Overall verification and generation latency.

**Key distinction:**

Prediction quality is not the same as speculative-decoding performance.

A more accurate draft model is not automatically a faster draft model.

### 6. Proposed solution

The researchers explored a new design space for draft models
and designed hardware-efficient draft models specifically for
speculative decoding.

The focus is to design models that execute efficiently on hardware,
such as GPUs, while reducing draft-generation latency.

The important idea is to design a draft model for the actual
requirements of speculative decoding instead of selecting one
only because it performs well on normal language-modelling tasks.

### 7. Reported results

The authors report that their newly designed draft model provides
111% higher throughput than existing draft models.

**Throughput:** The number of tokens generated per unit of time.

Illustrative calculation:

If an existing approach generates 100 tokens per second,
a 111% increase would result in:

100 + (100 x 1.11) = 211 tokens per second.

This is an illustration of the percentage increase, not an
independently measured result from this paper.

The authors also report that their approach generalizes to:

- LLaMA 1
- LLaMA 2
- LLaMA 3.1
- Supervised fine-tuned (SFT) models

### 8. Abstract — Research Story

1. **Problem:** Autoregressive LLM generation is slow.
2. **Existing technique:** Speculative decoding uses a small draft
   model and a large target model.
3. **Research gap:** Choosing a suitable draft model is difficult.
   Better language-modelling capability does not guarantee better
   speculative-decoding performance.
4. **Research approach:** The authors performed more than 350
   experiments and investigated draft-model latency and performance.
5. **Proposed solution:** They designed hardware-efficient draft models.
6. **Result:** The abstract reports 111% higher throughput compared
   with existing draft models.

### 9. Important Technical Terms

| Term | Meaning |
|---|---|
| Inference | Using a trained model to generate predictions or responses |
| Autoregressive decoding | Generating tokens sequentially, one at a time |
| Draft model | Smaller model that proposes candidate tokens |
| Target model | Main LLM that verifies proposed tokens |
| Speculative tokens | Candidate tokens proposed by the draft model |
| Latency | Time required to perform an operation |
| Throughput | Number of tokens generated per unit of time |
| Hardware efficiency | How efficiently a model uses hardware resources |
| SFT | Supervised Fine-Tuning |

### 10. Abstract Knowledge Check

**Score: 5/5**

All five knowledge-check questions were answered correctly.

Key concepts understood:

- Purpose of speculative decoding.
- Responsibility of the draft model.
- Importance of draft-model latency.
- Meaning of throughput.
- Reported 111% throughput improvement.

### 11. Final Takeaway

The central message of this paper is that a good draft model
for speculative decoding should not be selected only by its
language-modelling accuracy.

Its latency, hardware efficiency, and ability to generate
acceptable speculative tokens are also important.

The authors use this insight to explore and design
hardware-efficient draft models that improve LLM inference throughput.

**Reading progress:** Abstract studied and understood.
**Next:** Study the Introduction paragraph by paragraph.


---

# Section 2: Introduction — Easy Explanation

## 1. Why is LLM inference slow?

Large Language Models (LLMs) use autoregressive decoding
to generate text.

- The model generates one token at a time.
- Each new token depends on the previously generated tokens.
- Generation continues until the response is complete.

**Problem:** Sequential token generation is hardware-inefficient.
It can lead to poor GPU resource utilization and low inference throughput.

## 2. How does Speculative Decoding help?

Speculative decoding uses two models:

- **Draft model:** A significantly smaller LLM that generates
  multiple candidate tokens.
- **Target model:** The larger original LLM that verifies
  the candidate tokens.

### Workflow

1. The prompt is processed by the target LLM (prefill).
2. The draft model generates multiple candidate tokens.
3. The target LLM verifies the proposed tokens together.
4. Matching tokens are accepted; incorrect proposals are rejected
   or corrected.
5. The process repeats until generation is complete.

This converts sequential generation on the target model into
a more hardware-friendly batched operation.

**Important:** Speculative decoding preserves the target model's
output distribution while aiming to increase throughput.

## 3. Experiments conducted

The researchers performed more than 350 experiments.
Their contribution statement specifies more than 352 experiments.

Models used:

**Target models:**
- LLaMA-65B
- OPT-66B
- Fine-tuned chat models such as Vicuna-33B

**Draft models:**
- Models from the LLaMA and OPT families.
- Draft models ranged from approximately 5x to 528x fewer
  parameters than their target models.

**Objective:** Identify the factors that determine the throughput
improvement provided by speculative decoding.

**Main finding:** Draft-model latency is a key bottleneck.

## 4. Two important research observations

### Observation 1: Model depth affects latency

The researchers observed that draft-model latency is affected
by model depth.

Even when two models have the same number of parameters,
a deeper model can have higher latency because more sequential
computation is required.

**Remember:** Greater model depth can increase draft-generation latency.

### Observation 2: Language-modelling accuracy does not guarantee
better speculative-decoding performance

A draft model with higher accuracy on normal language-modelling
tasks can achieve a similar Tokens Accepted per iteration (TAR)
to a model with lower language-modelling accuracy.

Therefore, selecting a draft model only by its language-modelling
accuracy can lead to suboptimal speculative-decoding performance.

**Key distinction:**

Language-modelling accuracy is not the same as
speculative-decoding performance.

## 5. Proposed solution: Trade depth for width

Based on these observations, the researchers propose redesigning
draft models by trading increased depth for width while retaining
approximately the same parameter count.

- Reduce model depth.
- Increase model width.
- Improve hardware efficiency.
- Reduce draft-model latency.
- Improve speculative-decoding throughput.

The paper reports that these redesigned draft models can improve
inference throughput by over 60% in the discussed experiments.

The researchers also explore pruning methods such as
Sheared-LLaMA to create smaller draft models with suitable
configurations across OPT, LLaMA and LLaMA-3.1 model families.

## 6. Main contributions of the paper

### Contribution 1: Comprehensive benchmarking

The authors report more than 352 experiments involving
LLAMA-65B and OPT-66B, studying the factors that matter when
selecting and designing draft models.

### Contribution 2: Systematic draft-model redesign

They demonstrate that selecting draft models using only
language-modelling accuracy can lead to suboptimal choices.

Their redesign improves speculative-decoding throughput
by up to 111%.

### Contribution 3: KV-cache reduction

Their design reduces KV-cache requirements by 37%.

This reduction can enable larger batch sizes and improve
serving efficiency.

They also report outperforming self-speculative decoding
in several experimental setups.

## 7. Figure 1: Normal LLM inference vs Speculative Decoding

**Normal LLM inference:**
- The prompt is processed first (prefill).
- The target LLM generates tokens sequentially:
  x1, x2, x3, x4.
- Each next token depends on the previous generation.

**Speculative decoding:**
- The prompt is processed first.
- The draft model proposes multiple tokens.
- The target LLM verifies the proposed tokens together.
- Some or all proposed tokens can be accepted.
- The next speculative iteration begins from the accepted sequence.

### Understanding TAR

TAR means Tokens Accepted per speculative decoding iteration.

The paper defines it as:

TAR = (sum of accepted tokens across all iterations) / (number of iterations)

Formula:

TAR = (k1 + k2 + ... + km) / m

Where:
- ki = Number of tokens accepted in iteration i.
- m = Total number of speculative decoding iterations.

**Example:**

Suppose three iterations accept 3, 4 and 2 tokens.

TAR = (3 + 4 + 2) / 3 = 3

Therefore, the average number of accepted tokens per iteration is 3.

## 8. Important technical terms

| Term | Meaning |
|---|---|
| Autoregressive decoding | Generating tokens sequentially |
| Prefill | Processing the input prompt and preparing KV-cache |
| Draft model | Smaller model that proposes candidate tokens |
| Target model | Main LLM that verifies candidate tokens |
| Latency | Time required to perform an operation |
| Throughput | Tokens generated per unit of time |
| Model depth | Number of sequential layers in a model |
| Model width | Size of the model's layers or hidden representations |
| TAR | Average tokens accepted per speculative iteration |
| KV-cache | Stores previously computed key and value information |
| Batch size | Number of inputs processed together |
| Pruning | Removing selected model parameters or structures |
| Self-speculative decoding | Speculative decoding using parts or versions of the same model |

## 9. Introduction — Research Story

1. **Problem:** Autoregressive decoding is sequential and
   hardware-inefficient.
2. **Existing solution:** Speculative decoding uses draft and
   target models to accelerate generation.
3. **Research gap:** Draft-model latency limits performance,
   and language-modelling accuracy alone is not a good selection criterion.
4. **Observations:** Model depth affects latency, and higher
   language-modelling accuracy does not guarantee better TAR.
5. **Proposed solution:** Design wider and shallower,
   hardware-efficient draft models.
6. **Results:** Up to 111% higher throughput and 37% lower
   KV-cache requirements, as reported by the authors.

## 10. Five key takeaways

1. Autoregressive decoding generates one token at a time.
2. Speculative decoding uses a draft model and a target model.
3. Draft-model latency is a major performance bottleneck.
4. Deeper draft models can have higher latency, even with
   similar parameter counts.
5. Wider and shallower draft models can improve hardware efficiency
   and speculative-decoding throughput.

**Reading progress:** Abstract and Introduction studied.

**Next:** Study Section 2 — Background and Motivation.

