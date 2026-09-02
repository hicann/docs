# MatmulLayerNormReduceFusionPass

## 融合模式

将满足如下Pattern的结构融合成MatmulLayerNormReduce算子加LayerNormUpdate算子。

![](../figures/MatmulLayerNormReduceFusionPass_1.png)

或

![](../figures/MatmulLayerNormReduceFusionPass_2.png)

## 使用约束

仅在SDXL网络中生效

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->
