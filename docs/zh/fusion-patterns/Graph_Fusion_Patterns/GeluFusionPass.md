# GeluFusionPass

## 融合模式

该融合规则将Pow、Mul、Add、Tanh等小算子融合为Gelu算子。

计算公式：

![](../figures/GeluFusionPass_1.png)

- 场景一：

    ![](../figures/GeluFusionPass_2.png)
    
    融合为
    
    ![](../figures/GeluFusionPass_3.png)

- 场景二：

    ![场景二_1](../figures/GeluFusionPass_4.png)
    
    融合为
    
    ![](../figures/GeluFusionPass_5.png)

- 场景三：

    ![](../figures/GeluFusionPass_6.png)
    
    融合为
    
    ![](../figures/GeluFusionPass_7.png)

- 场景四：

    ![](../figures/GeluFusionPass_8.png)
    
    融合为
    
    ![](../figures/GeluFusionPass_9.png)

- 场景五：

    ![](../figures/GeluFusionPass_10.png)
    
    融合为
    
    ![](../figures/GeluFusionPass_11.png)

- 场景六：

    ![](../figures/GeluFusionPass_12.png)
    
    融合为
    
    ![](../figures/GeluFusionPass_13.png)

- 场景七：

 ![](../figures/GeluFusionPass_14.png)
 
 融合为
 
 ![](../figures/GeluFusionPass_15.png)

- 场景八：

![](../figures/GeluFusionPass_16.png)

融合为

![](../figures/GeluFusionPass_17.png)

## 使用约束

- 不支持动态shape场景。
<!-- npu="910b" id2 -->
- 数据类型限制：
  - Atlas A2 训练系列产品/Atlas A2 推理系列产品：数据类型支持FLOAT32、FLOAT16、BFLOAT16。
<!-- end id2 -->

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
