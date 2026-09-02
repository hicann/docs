# CastReluCastFusionPass

## 融合模式

该融合规则将Cast+Relu+Cast算子融合为Relu算子，即消除Relu前后的Cast算子。

![](../figures/CastReluCastFusionPass_1.png)

## 使用约束

Relu本身的数据类型是fp32，前Cast的输入数据类型必须与后Cast的输出数据类型相同，比如fp16转fp32和fp32转fp16。
