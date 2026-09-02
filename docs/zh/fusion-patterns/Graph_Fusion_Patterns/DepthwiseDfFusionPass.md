# DepthwiseDfFusionPass

## 融合模式

该融合规则为DepthwiseConv2DbackpropInput卷积算子添加TransposeD算子，提高计算性能。

![](../figures/DepthwiseDfFusionPass_1.png)融合为

![](../figures/DepthwiseDfFusionPass_2.png)

## 使用约束

该融合只在filter为NCHW时生效。
