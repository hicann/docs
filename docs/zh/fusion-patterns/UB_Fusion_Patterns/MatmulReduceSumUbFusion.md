# MatmulReduceSumUbFusion

## 融合模式

该融合将满足如下Pattern关系的子图中BatchMatMul和ReduceSum进行UB融合。

![](../figures/MatmulReduceSumFusionPass.png)

## 使用约束

- BatchMatMul的输入都有且都不为1，输出为1维。
- ReduceSum的输出为float32类型，keep\_dim为false。
- BatchMatMul类型支持BatchMatMul和BatchMatMulV2。
- BatchMatMul输入数据shape不超过三维，且三维时输入数据的第0维不能是1且不能超过uint16\_t的最大值。

## 支持的型号

<!-- npu="310b" id1 -->
Atlas 200I/500 A2 推理产品
<!-- end id1 -->

<!-- npu="310p" id2 -->
Atlas 推理系列产品
<!-- end id2 -->

<!-- npu="910" id3 -->
Atlas 训练系列产品
<!-- end id3 -->
