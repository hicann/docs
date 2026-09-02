# Conv2DSqueezeBiasaddFusionPass

## 融合模式

该融合将conv2D+squeeze+biasadd转换成conv2D+biasadd+squeeze的结构。

![](../figures/Conv2DSqueezeBiasaddFusionPass_1.png)融合为

![](../figures/Conv2DSqueezeBiasaddFusionPass_2.png)

## 使用约束

- biasadd节点的另一路输入data的维度必须是1，否则报错。
- biasadd节点的另一路输入data，如果来自Variable节点，则不融合。
- biasadd节点两路输入需要满足都是静态shape，否则不融合。
- biasadd节点的第二路输入维度需要满足为1，否则不融合。
- 训练场景下不融合。

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->

<!-- npu="310b" id2 -->
Atlas 200I/500 A2 推理产品
<!-- end id2 -->

<!-- npu="910" id3 -->
Atlas 训练系列产品
<!-- end id3 -->

<!-- npu="910b" id4 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id4 -->

<!-- npu="A3" id5 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id5 -->

<!-- npu="950" id7 -->
Ascend 950PR/Ascend 950DT
<!-- end id7 -->
