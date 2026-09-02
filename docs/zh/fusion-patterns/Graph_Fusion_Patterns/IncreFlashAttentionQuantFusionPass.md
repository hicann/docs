# IncreFlashAttentionQuantFusionPass

## 融合模式

量化场景，将IncreFlashAttention+AscendQuant融合为IncreFlashAttention算子，quant的scale和offset转化为ifa的quant\_scale2和quant\_offset2入参。

![](../figures/IncreFlashAttentionQuantFusionPass_1.png)

## 使用约束

- 仅支持IncreFlashAttention输出为fp16。
- 仅支持AscendQuant的输入为fp16，输出为int8。
- IncreFlashAttention算子的quant\_scale2和quant\_offset2必须为空。
- IncreFlashAttention算子必须为单输出。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->
