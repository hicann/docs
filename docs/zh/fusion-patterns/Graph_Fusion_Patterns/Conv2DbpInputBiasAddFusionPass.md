# Conv2DbpInputBiasAddFusionPass

## 融合模式

将Conv2DBackpropInput算子和BiasAdd算子融合为Conv2DTransposeD算子。

![](../figures/Conv2DbpInputBiasAddFusionPass_1.png)

融合为

![](../figures/Conv2DbpInputBiasAddFusionPass_2.png)

## 使用约束

无
