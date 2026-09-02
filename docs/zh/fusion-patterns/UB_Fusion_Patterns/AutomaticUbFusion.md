# AutomaticUbFusion

## 融合模式

经过其他UB融合之后，将未参与UB融合且相连的Elemwise类算子进行UB融合。该融合优先级最低。

![](../figures/AutomaticUbFusion_1.png)

## 使用约束

- 最多融合29个Elemwise类算子。
- 已经被其他UB融合规则匹配的算子不参与融合。
- 输入数量超过6个的AddN算子不参与融合。
