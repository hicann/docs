# TbeConvBnreduceFusionPass

## 融合模式

该融合将满足如下Pattern关系的子图中Convolution + bn\_reduce对应节点进行UB融合。

![](../figures/TbeConvBnreduceFusionPass_1.png)

或者

![](../figures/TbeConvBnreduceFusionPass_2.png)

## 使用约束

卷积的输入输出数据类型仅支持fp16。

若给出最小Tiling，L1仍无法容纳FeatureMap，则放弃融合。

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

<!-- npu="910b" id4 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id4 -->

<!-- npu="A3" id5 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id5 -->
