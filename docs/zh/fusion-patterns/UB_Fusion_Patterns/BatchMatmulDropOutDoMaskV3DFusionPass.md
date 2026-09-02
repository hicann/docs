# BatchMatmulDropOutDoMaskV3DFusionPass

## 融合模式

该融合将满足如下Pattern关系的子图中BatchMatMul和DropOutDoMaskV3D/Add进行UB融合。

![](../figures/BatchMatmulDropOutDoMaskV3DFusionPass_1.png)

## 使用约束

- 不支持动态shape场景。
- BatchMatMul支持BatchMatMul和BatchMatMulV2。

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
