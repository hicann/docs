# IndexByTensorStaticFusionPass

## 融合模式

在PyTorch图模式场景中，静态shape时，将IndexByTensor转换为Index算子，用于保证图下沉不被破坏。

![](../figures/IndexByTensorStaticFusionPass_1.png)

## 使用约束

仅支持静态shape。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->

<!-- npu="950" id3 -->
Ascend 950PR/Ascend 950DT
<!-- end id3 -->
