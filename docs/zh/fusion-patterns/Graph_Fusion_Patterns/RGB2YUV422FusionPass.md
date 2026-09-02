# RGB2YUV422FusionPass

## 融合模式

由于RGB2YUV422算子和该算子中的load\_image支持形态不一致，所以新增融合规则，将RGB2YUV422拆分成两个算子：Aipp+YUV4442YUV422。

![](../figures/RGB2YUV422FusionPass_1.png)

## 使用约束

- RGB2YUV422输入shape是三维，且最后维必须等于3。
- RGB2YUV422的输入Reshape为NHWC格式之后必须保证HW小于等于4096。
- RGB2YUV422的输入shape的前两维取值范围是\[2, 4096\]。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->
