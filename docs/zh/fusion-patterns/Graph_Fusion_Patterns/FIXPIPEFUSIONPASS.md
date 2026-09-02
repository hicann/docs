# FIXPIPEFUSIONPASS

## 融合模式

在拥有FIXPIPE相关硬件上，当cube算子包含[FixPipeAbilityProcessPass](FixPipeAbilityProcessPass.md)配置的“support\_fixpipe\_ability”属性时，会按照图中顺序依次匹配convert、activation和transform单元，当三个单元中至少存在一个单元时（不存在的单元则跳过），会将匹配到的算子融合为FIXPIPE算子。

- convert unit：格式转换单元，通常为quant类算子或者cast算子。
- activation unit：激活单元，通常为relu算子。
- transform unit：nd转换为nz的格式转换单元，通常为transdata算子。

![](../figures/FIXPIPEFUSIONPASS_1.png)

## 使用约束

- 仅支持静态网络。
- 该融合规则不能关闭。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
