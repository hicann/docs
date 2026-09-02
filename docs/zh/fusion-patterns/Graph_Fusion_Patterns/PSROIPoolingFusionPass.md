# PSROIPoolingFusionPass

## 融合模式

当PSROIPooling前驱是Conv2D时，在Conv2D的Filter和Bias的输出插入SwapCo算子；如果PSROIPooling前驱不是Conv2D，则在PSROIPooling输入插入SwapCi算子。

![](../figures/PSROIPoolingFusionPass_1.png)

融合成

![](../figures/PSROIPoolingFusionPass_2.png)

或

![](../figures/PSROIPoolingFusionPass_3.png)

融合成

![](../figures/PSROIPoolingFusionPass_4.png)

## 使用约束

PSROIPooling的前驱节点必须接在input0，同时input1的rois参数输入不能缺失。
