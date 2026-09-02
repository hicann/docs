# TransposedUpdateFusionPass

## 融合模式

该融合将符合图融合pattern的TransposeD算子，当算子中的check\_supported函数返回True时，将图中的TransposeD算子改为Transpose算子。

![](../figures/TransposedUpdateFusionPass_1.png)

## 使用约束

- 调用check\_supported返回True时，进行融合。
- 该融合不可关闭。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
