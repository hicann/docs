# TbeConv2DAddMulQuantPass

## 融合模式

将Conv2D + Dequant + Add + Quant进行UB融合。

![](../figures/TbeConv2DAddMulQuantPass_1.png)

## 使用约束

当Add算子另外两路输出节点为MaxPoolV3类型时，不支持融合。

当Add算子转换为Fixpipe算子时，不支持融合。

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
