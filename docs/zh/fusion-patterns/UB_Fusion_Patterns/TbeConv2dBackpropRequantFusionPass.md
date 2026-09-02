# TbeConv2dBackpropRequantFusionPass

## 融合模式

该融合将满足DX+AscendRequant+StridedWrite（可选）进行UB融合。

![](../figures/TbeConv2dBackpropRequantFusionPass_1.png)

## 使用约束

DX支持Conv2DBackpropInputD、Conv2DTransposeD和Deconvolution。

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->

<!-- npu="310b" id2 -->
Atlas 200I/500 A2 推理产品
<!-- end id2 -->

<!-- npu="910" id3 -->
Atlas 训练系列产品
<!-- end id3 -->
