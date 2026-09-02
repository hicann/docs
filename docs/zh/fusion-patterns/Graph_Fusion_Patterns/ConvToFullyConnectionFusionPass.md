# ConvToFullyConnectionFusionPass

## 融合模式

该融合规则将Conv卷积算子融合为FullyConnection算子，提高计算性能：

![](../figures/ConvToFullyConnectionFusionPass_1.png)融合成![](../figures/ConvToFullyConnectionFusionPass_2.png)

## 使用约束

- 不支持动态shape场景。
- 不支持int4、int8数据类型。
<!-- npu="910b" id1 -->
- Atlas A2 训练系列产品/Atlas A2 推理系列产品场景下，float32数据类型不支持filter的N轴非16对齐的场景。
<!-- end id1 -->
- conv2d输出节点数量只允许为1，输入input大小与filter大小HWC轴必须相等，group属性必须等于1，pad属性必须为\[0,0,0,0\]。
- 不支持conv2d算子后接quant或requant算子。
- 不支持conv2d算子后接dequant+sigmoid算子级联。

## 支持的型号

<!-- npu="310b" id2 -->
Atlas 200I/500 A2 推理产品
<!-- end id2 -->

<!-- npu="310p" id3 -->
Atlas 推理系列产品
<!-- end id3 -->

<!-- npu="910" id4 -->
Atlas 训练系列产品
<!-- end id4 -->

<!-- npu="910b" id5 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id5 -->

<!-- npu="A3" id6 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id6 -->
