# SoftShrink

```c
REG_OP(SoftShrink)
     .INPUT(input_x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
     .OUTPUT(output_y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
     .ATTR(lambd, Float, 0.5)
     .OP_END_FACTORY_REG(SoftShrink)
```

## Brief

Calculate the soft shrinkage function.

## Inputs

One inputs, including:
input_x: A tensor. Must be one of the following types:
    float16, float32, bfloat16. 

## Outputs

output_y: A Tensor with the same dtype and shape of input_x's. 

## Attributes

lambd: An optional float. Defaults to 0.5. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: bfloat16,float16,float32
- output0 output_y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator Softshrink. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
