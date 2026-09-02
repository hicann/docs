# GeGluV2FusionPass

## 融合模式

完成如下结构的融合，把小算子\(SplitVD + Gelu + Mul\)融合成大算子GeGluV2。

![](../figures/GeGluV2FusionPass_1.png)

## 使用约束

仅支持SplitVD节点切分轴大于512的场景。

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->

<!-- npu="910b" id3 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品中的Ascend_xxx_B
<!-- end id3 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->
