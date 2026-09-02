# PadFusionPass 

## 融合模式

该融合将符合图融合pattern的Pad算子，在输入paddings为const节点时，将图中的Pad算子改为PadD算子，并将输入转换为属性。

![](../figures/PadFusionPass_1.png)

## 使用约束

x数据类型不在\{float16,float,int32\}的范围内时，不进行图融合操作。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
