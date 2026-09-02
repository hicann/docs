# TbeConv2dAddRelu6MulMulFusionPass

## 融合模式

支持以下两种融合模式

将Conv2D/DepthwiseConv2D  + Add  + Relu6  + Mul + Mul融合成一个算子。

![](../figures/TbeConv2dAddRelu6MulMulFusionPass_1.png)

将Conv2D/DepthwiseConv2D + Dequant+ Add  + Relu6  +Mul +Mul +Quant融合成一个算子。

![](../figures/TbeConv2dAddRelu6MulMulFusionPass_2.png)

## 使用约束

无。

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
