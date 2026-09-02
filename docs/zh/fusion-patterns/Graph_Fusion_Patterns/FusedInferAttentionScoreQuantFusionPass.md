# FusedInferAttentionScoreQuantFusionPass

## 融合模式

量化场景，将FusedInferAttentionScore+AscendQuant融合为FusedInferAttentionScore算子，quant的scale和offset转化为FIA接口的quant\_scale2和quant\_offset2入参。

![](../figures/FusedInferAttentionScoreQuantFusionPass_1.png)

## 使用约束

- 仅支持FusedInferAttentionScore为fp16输出。
- 仅支持AscendQuant为fp16输入int8输出。
- FusedInferAttentionScore算子的quant\_scale2和quant\_offset2必须为空。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->
