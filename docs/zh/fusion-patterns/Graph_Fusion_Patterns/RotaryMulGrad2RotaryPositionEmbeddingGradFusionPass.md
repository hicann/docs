# RotaryMulGrad2RotaryPositionEmbeddingGradFusionPass

## 融合模式

完成如下结构的融合，把算子RotaryMulGrad融合成算子RotaryPositionEmbeddingGrad。

- needBackward == true

  ![](../figures/RotaryMulGrad2RotaryPositionEmbeddingGradFusionPass_1.png)

- needBackward == false

  ![](../figures/RotaryMulGrad2RotaryPositionEmbeddingGradFusionPass_2.png)

## 使用约束

不建议关闭，如果关闭，会导致RotaryMulGrad Ascend IR功能不可用。

## 支持的型号

<!-- npu="950" id1 -->
Ascend 950PR/Ascend 950DT
<!-- end id1 -->