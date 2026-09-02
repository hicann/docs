# TbeElemwiseQuantFusionPass

## 融合模式

该融合将Elemwise/Broadcast类算子和Quant算子进行UB融合。

![](../figures/TbeElemwiseQuantFusionPass_01.png)

## 使用约束

- Elemwise/Broadcast算子类型不能是Eltwise。
- Elemwise/Broadcast算子必须是双输入
- 不支持动态shape场景。
