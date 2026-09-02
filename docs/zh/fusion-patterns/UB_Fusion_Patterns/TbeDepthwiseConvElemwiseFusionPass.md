# TbeDepthwiseConvElemwiseFusionPass

## 融合模式

将满足如下Pattern关系的Elemwise+DepthwiseConvolution进行UB融合。

![](../figures/TbeDepthwiseConvElemwiseFusionPass_1.png)

## 使用约束

- ElementWise类型只支持LeakyRelu，系数为0。
- DepthwiseConvolution类型只支持DepthwiseConv2D。

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->

<!-- npu="910" id2 -->
Atlas 训练系列产品
<!-- end id2 -->
