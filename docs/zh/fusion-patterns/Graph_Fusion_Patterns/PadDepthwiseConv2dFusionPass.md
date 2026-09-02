# PadDepthwiseConv2dFusionPass

## 融合模式

该融合规则将PadD+DepthwiseConv2D算子融合为DepthwiseConv2D算子。

![](../figures/PadDepthwiseConv2dFusionPass_1.png)

融合成

![](../figures/PadDepthwiseConv2dFusionPass_2.png)

## 使用约束

- 不支持动态shape。
- 不支持PadD算子连接多个DepthwiseConv2D结构。
- 融合前DepthwiseConv2D需要有padding属性，且必须为VALID。
- PadD算子只支持在DepthwiseConv2D的H/W维度补pad，融合后的pad大小要在\[0, 255\]区间内，融合后的pad\_top和pad\_bottom均小于kernel\_h。

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

<!-- npu="910b" id4 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id4 -->

<!-- npu="A3" id5 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id5 -->

<!-- npu="950" id7 -->
Ascend 950PR/Ascend 950DT
<!-- end id7 -->
