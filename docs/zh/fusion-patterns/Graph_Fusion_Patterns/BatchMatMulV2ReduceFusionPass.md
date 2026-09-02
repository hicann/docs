# BatchMatMulV2ReduceFusionPass

## 融合模式

该融合规则将BatchMatMulV2+ReduceSumD算子融合为BatchMatMulV2算子。

模式一：

![](../figures/BatchMatMulV2ReduceFusionPass_1.png)融合成![](../figures/BatchMatMulV2ReduceFusionPass_2.png)

模式二：

![](../figures/BatchMatMulV2ReduceFusionPass_3.png)融合成![](../figures/BatchMatMulV2ReduceFusionPass_2.png)

## 使用约束

- BatchMatMulV2左右矩阵均为3维，且batch轴\>1。
- BatchMatMulV2输入的数据类型仅支持float32、float16、bfloat16。
- 图融合中各个节点都为静态节点。
- 构造图必须为两种情况中的一种：BatchMatMulV2--\>Cast32--\>ReduceSumD--\>Output或者是BatchMatMulV2--\>ReduceSumD--\>Output。
- BatchMatMulV2后节点若为Cast32，输出数据类型为float16，Cast输出数据类型为float32。
- BatchMatMulV2输入节点必须为两个，输出节点数只能为1。
