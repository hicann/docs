# MatmulReshapeFusionPass

## 融合模式

该融合规则在Matmul N轴等于1时，会对第二个输入增加Reshape节点。

![](../figures/MatmulReshapeFusionPass_1.png)

## 使用约束

- 该规则默认关闭，可参考[如何关闭/开启融合规则](../Introduction.md)自行开启。
- 仅支持静态shape场景。
- 支持数据类型：BFLOAT16、FLOAT16、FLOAT32。
- x1的输入为\[M, K\]，x2的输入未转置，N=1在轴的末尾，输入为\[K, 1\]。
- 数据类型为BFLOAT16或FLOAT16，K<27392时，该融合规则生效。
- 数据类型为BFLOAT16或FLOAT16，K\>=8，K<=64且M\>=8192时，该融合规则不生效。
- 数据类型为BFLOAT16或FLOAT16，K\>12800且M\>16384时，该融合规则不生效。
- 数据类型为FLOAT32，K\>=8，K<=64，M\>=8192且M<=32768时，该融合规则不生效。
- 数据类型为FLOAT32，M=9或K=23697，27167时，该融合规则不生效。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->

<!-- npu="950" id3 -->
Ascend 950PR/Ascend 950DT
<!-- end id3 -->
