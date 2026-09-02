# TbeMultiOutputFusionPass

## 融合模式

该融合将满足如下Pattern关系的子图中ElemWise对应节点进行UB融合。

括号内数字表示ElemWise节点个数的取值范围，head表示以当前节点为匹配的首节点。

![](../figures/TbeMultiOutputFusionPass_1.png)

或者

![](../figures/TbeMultiOutputFusionPass_2.png)

## 使用约束

无
