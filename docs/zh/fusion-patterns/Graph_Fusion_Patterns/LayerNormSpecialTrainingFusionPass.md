# LayerNormSpecialTrainingFusionPass

## 融合模式

该融合规则将Mean/SquaredDifference/Add/Rsqrt/RsqrtGrad/Mul/Sub/AddN算子融合成一个LayerNorm算子和两个LayerNormGrad算子，提高计算性能。如下图所示。

![](../figures/LayerNormSpecialTrainingFusionPass_01.png)

## 使用约束

无
