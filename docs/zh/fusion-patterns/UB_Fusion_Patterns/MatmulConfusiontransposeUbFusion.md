# MatmulConfusiontransposeUbFusion

## 融合模式

该融合将满足如下Pattern关系的子图中MatMul和ConfusionTransposeD进行UB融合。

![](../figures/MatmulConfusiontransposeUbFusion_1.png)

## 使用约束

不支持动态shape场景
