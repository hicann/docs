# SoftShrinkGrad

```c
REG_OP(SoftShrinkGrad)
     .INPUT(input_grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
     .INPUT(input_x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
     .OUTPUT(output_y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
     .ATTR(lambd, Float, 0.5)
     .OP_END_FACTORY_REG(SoftShrinkGrad)
```

## Brief

Calculate the reversed outputs of the function "soft_shrink".

## Inputs

Two inputs, including:
- input_grad: A tensor. The shape should be within the range of 0D to 8D. Must be one of the following types:
    float16, float32, bfloat16. 
- input_x: A tensor of the same dtype and shape as "input_grad". The shape should be within the range of 0D to 8D.

## Outputs

output_y: A Tensor of the same dtype and shape as "input_grad". The shape should be within the range of 0D to 8D. 

## Attributes

lambd: An optional float. Defaults to 0.5. lambd should be greater or equal to 0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_grad: float16,float32
- input1 input_x: float16,float32
- output0 output_y: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator SoftShrinkGrad. 


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
