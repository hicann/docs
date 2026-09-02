# InterleaveRope2RotaryPositionEmbeddingFusionPass

## 融合模式

完成如下结构的融合，把算子InterleaveRope融合成算子RotaryPositionEmbedding。

![](../figures/InterleaveRope2RotaryPositionEmbeddingFusionPass_1.png)

## 使用约束

不建议关闭，如果关闭，会导致InterleaveRope Ascend IR功能不可用。

## 支持的型号

<!-- npu="950" id1 -->
Ascend 950PR/Ascend 950DT
<!-- end id1 -->
