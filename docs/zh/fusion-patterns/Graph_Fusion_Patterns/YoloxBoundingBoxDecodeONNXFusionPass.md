# YoloxBoundingBoxDecodeONNXFusionPass

## 融合模式

该融合规则将StridedSliceD/Mul/Exp/GatherV2/Add/Muls/Sub/Unsqueeze/ConcatD算子融合为YoloxBoundingBoxDecode算子，提高计算性能。

![](../figures/YoloxBoundingBoxDecodeONNXFusionPass_1.png)

融合成

![](../figures/YoloxBoundingBoxDecodeONNXFusionPass_2.png)

## 使用约束

无

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->
