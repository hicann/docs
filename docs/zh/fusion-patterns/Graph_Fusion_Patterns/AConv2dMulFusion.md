# AConv2dMulFusion

## 融合模式

该融合将Conv2d+mul或Conv3d+mul融合为一个融合算子Conv。

![](../figures/AConv2dMulFusion_1.png)融合为

![](../figures/AConv2dMulFusion_2.png)

## 使用约束

- conv节点可以是Conv2D，也可以是Conv3D。
- data输入为动态时，支持融合。
- filter、bias和mul的另一路，三个输入均为const时，支持融合。
- 当conv节点是Conv3D时，仅支持data输入的format为NDHWC格式，此时mul算子的const mul输入为1维输入，且该维度等于Conv3D算子输出的C维度时，才会进行融合。
- 当conv节点是Conv3D时，仅支持data输入的format为NDHWC格式，此时mul算子的const mul输入也为NDHWC格式，且NDHW维度均为1，只有C维度等于Conv3D算子输出的C维度时，才会进行融合。

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->

<!-- npu="310b" id2 -->
Atlas 200I/500 A2 推理产品
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

<!-- npu="950" id7 -->
Ascend 950PR/Ascend 950DT
<!-- end id7 -->
