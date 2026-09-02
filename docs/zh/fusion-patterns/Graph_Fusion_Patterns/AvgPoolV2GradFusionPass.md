# AvgPoolV2GradFusionPass

该融合规则将AvgPoolV2Grad算子融合为AvgPoolV2GradD算子。

![](../figures/AvgPoolV2GradFusionPass_1.png)

## 使用约束

AvgPoolV2Grad的输入ori\_input\_shape必须是const节点或者带value值的data节点。
