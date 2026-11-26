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
