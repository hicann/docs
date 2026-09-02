# FixPipeAbilityProcessPass

## 融合模式

该融合规则给fixpipe节点打上“support\_fixpipe\_ability”属性。属性值为枚举类型，含义如下。

- 1：Conv2D、DepthwiseConv2D算子在输出数量为2时，支持fixpipe双输出
- 2：Conv2DBackpropFilterD和DepthwiseConv2DBackpropFilterD使用atomic write
- 3：不支持fixpipe处理

## 使用约束

该融合规则不可关闭。

该Pass的有效性依赖于运行的产品是否支持相应算子类型，具体信息请参考《算子库》中的“[Ascend IR算子规格说明](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/latest/API/aolapi/operatorlist_00094.html)”章节。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="950" id2 -->
Ascend 950PR/Ascend 950DT
<!-- end id2 -->
