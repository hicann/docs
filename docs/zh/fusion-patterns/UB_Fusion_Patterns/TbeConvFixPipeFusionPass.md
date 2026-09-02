# TbeConvFixPipeFusionPass 

## 融合模式

将conv2d与[FIXPIPEFUSIONPASS](../Graph_Fusion_Patterns/FIXPIPEFUSIONPASS.md)中生成的fixpipe节点、elemwise类算子（可选）和quant算子（可选）进行UB融合。

![](../figures/TbeConvFixPipeFusionPass_1.png)

## 使用约束

无

## 支持的型号

<!-- npu="310b" id1 -->
Atlas 200I/500 A2 推理产品
<!-- end id1 -->

<!-- npu="910b" id2 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id2 -->

<!-- npu="A3" id3 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id3 -->
