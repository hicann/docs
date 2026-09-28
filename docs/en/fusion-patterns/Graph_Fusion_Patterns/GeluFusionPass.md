# GeluFusionPass

## Description

Fuses small operators, such as Pow, Mul, Add, and Tanh, into the Gelu operator.

The formula is as follows:

![](../figures/GeluFusionPass_1.png)

- Scenario 1:

    ![](../figures/GeluFusionPass_2.png)
    
    After:
    
    ![](../figures/GeluFusionPass_3.png)

- Scenario 2:

    ![Scenario 2_1](../figures/GeluFusionPass_4.png)
    
    After:
    
    ![](../figures/GeluFusionPass_5.png)

- Scenario 3:

    ![](../figures/GeluFusionPass_6.png)
    
    After:
    
    ![](../figures/GeluFusionPass_7.png)

- Scenario 4:

    ![](../figures/GeluFusionPass_8.png)
    
    After:
    
    ![](../figures/GeluFusionPass_9.png)

- Scenario 5:

    ![](../figures/GeluFusionPass_10.png)
    
    After:
    
    ![](../figures/GeluFusionPass_11.png)

- Scenario 6:

    ![](../figures/GeluFusionPass_12.png)
    
    After:
    
    ![](../figures/GeluFusionPass_13.png)

- Scenario 7:

 ![](../figures/GeluFusionPass_14.png)
 
 After:
 
 ![](../figures/GeluFusionPass_15.png)

- Scenario 8:

![](../figures/GeluFusionPass_16.png)

After:

![](../figures/GeluFusionPass_17.png)

## Constraints

- Dynamic shapes are not supported.
<!-- npu="910b" id2 -->
- Data type constraints:
  - Atlas A2 training products/Atlas A2 inference products: The data type can be FLOAT32, FLOAT16, or BFLOAT16.
<!-- end id2 -->

## Applicable Products

<!-- npu="910b" id1 -->
Atlas A2 training products/Atlas A2 inference products
<!-- end id1 -->
