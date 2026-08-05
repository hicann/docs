# SoftMarginLoss

```c
REG_OP(SoftMarginLoss)
    .INPUT(input_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(input_y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .OUTPUT(output_z, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(SoftMarginLoss)
```

## Brief

Calculate the loss. Creates a criterion that optimizes a two-class classification
logistic loss between input_x and input_y (containing 1 or -1).

## Inputs

Tow inputs, including:
- input_x: A tensor. Must be one of the following types:
    float16, float32, bfloat16. 
- input_y: A tensor. Must be one of the following types:
    float16, float32, bfloat16. 

## Outputs

output_z: while reduction == "none", A Tensor with the same type and shape of input_x's. 
         while reduction == "sum" or "mean", A Tensor with the same type of input_x , shape of which is (1,)

## Attributes

reduction: An optional string. Defaults to "mean". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: float16,float32
- input1 input_y: float16,float32
- output0 output_z: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator SoftMarginLoss. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
