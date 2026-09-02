# ConvClipByValueFusionPass

## 融合模式

支持以下融合模式

将Conv2D + Elemwise（ClipByValue类型）算子融合成一个融合算子。

![](../figures/ConvClipByValueFusionPass_1.png)

## 使用约束

- Elemwise个数为1-3个，第一个Elemwise算子必须是ClipByValue类型，后两个Elemwise算子类型为Relu或Add。
- Conv2D算子的output channel需为16的整数倍大小。

## 支持的型号

<!-- npu="310b" id1 -->
Atlas 200I/500 A2 推理产品
<!-- end id1 -->

<!-- npu="310p" id2 -->
Atlas 推理系列产品
<!-- end id2 -->

<!-- npu="910" id3 -->
Atlas 训练系列产品
<!-- end id3 -->
