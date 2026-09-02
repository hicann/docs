# ReshapeTransposeFusionPass

## 融合模式

该融合将符合图融合pattern的Reshape+TransposeD算子改为ConfusionTransposeD算子。

![](../figures/ReshapeTransposeFusionPass_1.png)

## 使用约束

对于reshape节点的限制：

- reshape输入是动态shape, 不融合。
- reshape输入维度是1维，且是动态shape不融合。
- reshape输入维度是1维，且shape不能整除16不融合。
- reshape输入维度大于等于2维时，后两维如果有一维是动态shape不融合。
- reshape输入维度大于等于2维时，后两维如果有一维不能整除16不融合。
- reshape输入是空tensor，不融合。

对于TransposeD的限制：

- TransposeD输入的数据类型仅支持float16、float32、int8、int16、int32、int64、uint8、uint16、uint32和uint64。
- TransposeD输入的最大尺寸不能超过8维，形状需与输出一致。

- TransposeD输出是动态shape, 不融合。
- TransposeD输出维度是1维，且是动态shape不融合。
- TransposeD输出维度是1维，且shape不能整除16不融合。
- TransposeD输出维度大于等于2维时，后两维如果有一维是动态shape不融合。
- TransposeD输出维度大于等于2维时，后两维如果有一维不能整除16不融合。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
