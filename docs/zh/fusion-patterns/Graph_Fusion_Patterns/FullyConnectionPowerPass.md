# FullyConnectionPowerPass

## 融合模式

该融合规则将FullyConnection+Power算子融合为FullyConnectionPower算子。

![](../figures/FullyConnectionPowerPass_1.png)

融合成

![](../figures/FullyConnectionPowerPass_2.png)

## 使用约束

- FC的weight不能少于2个。
- FC的输入数据类型不能是int8、uint8类型
