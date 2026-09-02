# ConvWeightCompressFusionPass

## 融合模式

对于Cube类运算算子，通过插入压缩算子将Filter进行压缩，或通过插入四选二结构化稀疏算子进行稀疏。该Pass根据用户配置的参数执行压缩或者四选二结构化稀疏。

Cube类算子支持Conv2D、FullyConnection、MatMulV2。

![](../figures/ConvWeightCompressFusionPass_1.png)

融合成

![](../figures/ConvWeightCompressFusionPass_2.png)

## 使用约束

首节点（Conv2D/FullyConnection/MatMulV2）需要满足如下条件。

- 索引为0的输入的dtype必须是int8或者uint8。
- 需要支持AICore。
- 不支持groups大于1 。
- 需要支持权重压缩或四选二结构化稀疏。

## 支持的型号

该Pass的有效性依赖于目标平台是否支持相应算子类型，具体信息请参考《算子库》中的“[Ascend IR算子规格说明](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/latest/API/aolapi/operatorlist_00094.html)”章节。
