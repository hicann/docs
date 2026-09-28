# FusedInferAttentionScoreQuantFusionPass

## Description

Fuses FusedInferAttentionScore+AscendQuant into the FusedInferAttentionScore operator in quantization use cases. The `scale` and `offset` parameters of `quant` are converted into the input parameters `quant_scale2` and `quant_offset2` of FIA.

![](../figures/FusedInferAttentionScoreQuantFusionPass_1.png)

## Constraints

- FusedInferAttentionScore supports only fp16 output.
- AscendQuant supports only fp16 input and int8 output.
- `quant_scale2` and `quant_offset2` of the FusedInferAttentionScore operator must be empty.

## Applicable Products

<!-- npu="910b" id1 -->
Atlas A2 training products/Atlas A2 inference products
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 training products/Atlas A3 inference products
<!-- end id2 -->
