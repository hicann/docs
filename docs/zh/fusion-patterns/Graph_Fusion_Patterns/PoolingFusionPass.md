# PoolingFusionPass

## 融合模式

![](../figures/PoolingFusionPass_1.png)

融合成

![](../figures/PoolingFusionPass_2.png)

## 使用约束

- 不支持动态shape。
- 静态融合数据类型仅支持float16和int8。
- 在AVG Pooling下融合规则生效，如果网络模型中涉及AVG Pooling int8量化情况，即prototxt文件中pooling属性参数pool为AVG时，该融合规则必须打开。
