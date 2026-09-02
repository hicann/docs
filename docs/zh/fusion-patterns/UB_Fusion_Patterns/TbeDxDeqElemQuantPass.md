# TbeDxDeqElemQuantPass

## 融合模式

该融合将满足DX+AscendDequant + ElementWise + AscendQuant（可选）进行UB融合。

![](../figures/TbeDxDeqElemQuantPass_1.png)

## 使用约束

- ElementWise支持Relu、LeakyRelu和Prelu。
- DX支持Conv2DBackpropInputD、Conv2DTransposeD和Deconvolution。
- 当AscendQuant存在时，还支持ElementWise和AscendQuant双输出。
- 不支持动态场景
- 该UB融合适用于DX类的量化场景

## 支持的型号

Atlas 推理系列产品

Atlas 200I/500 A2 推理产品

Atlas 训练系列产品
