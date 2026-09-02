# TbeConv2DBackpropElemwiseFusionPass

## 融合模式

该融合将满足DX+ElementWise+ElementWise1（可选）进行UB融合。

![](../figures/TbeConv2DBackpropElemwiseFusionPass_1.png)

## 使用约束

- 仅ElementWise存在时，支持ReluGradV2；当ElementWise1存在时，ElementWise支持AddN和Add，ElementWise1支持ReluGradV2。
- DX支持Conv2DBackpropInputD、Conv2DTransposeD和Deconvolution。
- DX仅支持非FP32类型。
- 该UB融合适用于DX类的非量化场景。
