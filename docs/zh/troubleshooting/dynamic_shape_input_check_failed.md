# 动态shape模型输入大小校验失败

## 问题现象描述

动态shape模型输入大小校验失败，plog日志信息中包含以下关键信息：tensor size mismatches. expected: ..., but given ...

```bash
17480:[ERROR] GE(187626,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [execution_engine.cc:450]191154 ValidInputTensor:ErrorNo: 1343225860(Internal errors) [EXEC][EXEC][Check][Size] for [PartitionedCall_14(PartitionedCall)] Input[40]:tensor size mismatches.expected: 768032, but given 32.
```

## 可能原因

动态shape场景每个node都会在执行时对shape进行推导，该故障现象可能为算子的shape校验不合法。

## 解决措施

针对分析的故障可能原因，应根据模型中的连接关系，对shape的来源进行排查，找出不合理的shape推导。

开启DEBUG级别的日志，再次运行应用后，可搜索执行plog日志查看关键词：

"before\_infershape when running"：显示算子shape推导前的输入、输出shape等信息。

"after\_infershape when running"：显示算子shape推导后的输入、输出shape等信息。

从报错节点的输入、输出shape开始进行排查， 检查当前节点shape推导结果是否正确（即判定根据输入shape推出的输出shape是否符合预期）， 如果是输入shape存在问题，则按照相同方法继续排查输入节点的shape推导。

![](figures/image_0000001927835337.png)

>**说明：** 
>执行export ASCEND\_GLOBAL\_LOG\_LEVEL=0命令开启DEBUG日志，调试完成后，再执行export ASCEND\_GLOBAL\_LOG\_LEVEL=3命令将日志级别设置成ERROR，关于日志级别的详细说明请参见[《日志参考》](https://hiascend.com/document/redirect/CannCommunitylogref)。
