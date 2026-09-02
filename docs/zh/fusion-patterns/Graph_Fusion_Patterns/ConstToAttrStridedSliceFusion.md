# ConstToAttrStridedSliceFusion

## 融合模式

将StridedSlice算子融合成StridedSliceD算子，并将StridedSlice算子的Const节点输入begin、end、strides，转变成StridedSliceD算子的属性。

![](../figures/ConstToAttrStridedSliceFusion_1.png)

## 使用约束

- 当场景是动态shape且对应平台上支持StridedSlice算子时，该融合规则不生效。
- 当输出shape中存在0时，该融合规则不生效。
- 当StridedSlice算子的begin、end、strides输入不是Const节点时，该融合规则不生效。
- 当StridedSliceD算子在对应平台上不支持时，该融合规则不生效。
- 当strides的尾轴小于1时，该融合规则不生效。
- 当属性new\_axis\_mask、shrink\_axis\_mask、begin\_mask、end\_mask、ellipsis\_mask存在缺失，该融合规则不生效。
- 当属性中，begin\_mask为0且其余属性均不为0时，该融合规则不生效。
- 数据类型不在融合后算子的支持范围内，该融合规则不生效。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
