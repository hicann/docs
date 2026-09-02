# MatmulTransdataFusionPass

## 融合模式

该融合规则通过等价替换将图中的Transdata算子从2个减少为1个。

![](../figures/MatmulTransdataFusionPass_1.png)

融合成

![](../figures/MatmulTransdataFusionPass_2.png)

或在没有Cast算子的场景

![](../figures/MatmulTransdataFusionPass_3.png)

融合成

![](../figures/MatmulTransdataFusionPass_4.png)

## 使用约束

无
