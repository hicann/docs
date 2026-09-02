# MatMulFastgelugradUbFusion

## 融合模式

该融合将满足如下Pattern关系的子图中MatMul/GEMM和Elemwise进行UB融合。

![](../figures/MatMulFastgelugradUbFusion_1.png)

## 使用约束

不支持动态shape场景
