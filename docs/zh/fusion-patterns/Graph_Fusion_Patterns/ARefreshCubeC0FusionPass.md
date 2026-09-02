# ARefreshCubeC0FusionPass

## 融合模式

修正cube类算子的输入输出是重型格式（私有格式）的c0值。

## 使用约束

- cube类算子，包括AvgPool、AvgPoolV2、BatchMatMulV2、Conv2D、Conv2DTransposeD、Conv3D、Deconvolution、DepthwiseConv2D、FullyConnection、MatMulV2、MaxPool、Pooling、QuantBatchMatmulV3等算子。
- 转换前的输入输出data type均为float。
- 该融合规则不可关闭。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
