# ASplitConv2dConcatPass

## 融合模式

将Split/SplitV + Conv2D \*N + Concat/ConcatV2融合成一个组卷积，简化图结构。

![](../figures/ASplitConv2dConcatPass_1.png)

## 使用约束

- 每个Conv2D的输入个数必须相同，且大于等于2个。
- 每个Conv2D的filter的shape和format要相同（只支持HWCN或NCHW）。
- 每个Conv2D只能单输出。
- Conv2D的filter和bias必须是类型\{"Const", "Constant", "QuantBiasOptimization", "QuantWeightRollBack", "QuantBiasRollBack", "AscendWeightQuant"\}中的一个。
- Split/SplitV节点和Concat/ConcatV2节点的另一路输入必须是const类型，且Split/SplitV节点的输出个数和Concat/ConcatV2的输入个数必须相同。
- Split/SplitV节点的切分轴和Concat/ConcatV2节点的组合轴必须都为channel方向。
  <!-- npu="910,310p,310b" id1 -->
- Conv2D输入的类型只支持：float、float16、int8和int32，且不支持Conv2D动态输入。该约束适用的型号如下：
  <!-- npu="310p" id2 -->
  - Atlas 推理系列产品
  <!-- end id2 -->
  <!-- npu="310b" id3 -->
  - Atlas 200I/500 A2 推理产品
  <!-- end id3 -->
  <!-- npu="910" id4 -->
  - Atlas 训练系列产品
  <!-- end id4 -->
  <!-- end id1 -->

  <!-- npu="950" id5 -->
- Conv2D输入的类型只支持：float、float16、int8。该约束适用的型号如下：
  - Ascend 950PR/Ascend 950DT
  <!-- end id5 -->

## 支持的型号

<!-- npu="310p" id6 -->
Atlas 推理系列产品
<!-- end id6 -->

<!-- npu="310b" id7 -->
Atlas 200I/500 A2 推理产品
<!-- end id7 -->

<!-- npu="910" id8 -->
Atlas 训练系列产品
<!-- end id8 -->

<!-- npu="950" id9 -->
Ascend 950PR/Ascend 950DT
<!-- end id9 -->
