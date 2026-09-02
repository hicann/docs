# QuantBatchMatmulV3TransposeFusionPass

## 融合模式

将算子QuantBatchMatmulV3的输入x1/x2所连接的Transpose/TransposeD算子节点融合，将其信息分别转化到QuantBatchMatmulV3的两个属性transpose\_x1和transpose\_x2中。

其中，x1和x2相互独立，只要其中一路出现Transpose节点，就可触发该融合。

![](../figures/QuantBatchMatmulV3TransposeFusionPass_1.png)

## 使用约束

无

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->

<!-- npu="950" id3 -->
Ascend 950PR/Ascend 950DT
<!-- end id3 -->
