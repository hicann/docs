# LayerNormSpecialFourGradsTrainingFusionPass

## 融合模式

和LayerNormSpecialTrainingFusionPass类似，该融合规则将Mean/SquaredDifference/Add/Rsqrt/RsqrtGrad/Mul/Sub/AddN算子融合成一个LayerNorm算子和两个LayerNormGrad算子，提高计算性能。有差异的是该融合pass会匹配四个反向的pattern，并将其中两个scope名称和正向LayerNorm一致的反向LayerNorm结构融合成LayerNormGrad算子。如下图所示：

![](../figures/LayerNormSpecialFourGradsTrainingFusionPass_01.png)

## 使用约束

无
