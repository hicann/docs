# ZBNupdateReluV2Conv2DBNreducePass

## 融合模式

该融合规则将BNTrainingUpdate+ReluV2+Conv2D+BNTrainingReduce四个算子融合成一个Conv2D算子，提高性能。

![](../figures/ZBNupdateReluV2Conv2DBNreducePass_1.png)

## 使用约束

不支持Conv2D节点带bias场景。

## 支持的型号

<!-- npu="910" id1 -->
Atlas 训练系列产品
<!-- end id1 -->
