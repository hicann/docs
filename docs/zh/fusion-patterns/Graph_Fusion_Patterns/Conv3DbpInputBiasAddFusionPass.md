# Conv3DbpInputBiasAddFusionPass

## 融合模式

该融合规则将Conv3DBackpropInput+BiasAdd算子融合为Conv3DTransposeD算子，BiasAdd输入作为Conv3DTransposeD的输入bias。

![](../figures/Conv3DbpInputBiasAddFusionPass_1.png)

## 使用约束

Conv3DTransposeD算子输出的格式为FLOAT16类型。
