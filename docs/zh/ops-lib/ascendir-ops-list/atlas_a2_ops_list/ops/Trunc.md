# Trunc

```c
REG_OP(Trunc)
    .INPUT(input_x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8}))
    .OUTPUT(output_y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8}))
    .OP_END_FACTORY_REG(Trunc)
```

## Brief

Returns a new tensor with the truncated integer values of the elements of input.

## Inputs

One inputs, including:
input_x: A tensor. Must be one of the following types: float16, bfloat16, float32, int8, uint8, int32. 

## Outputs

output_y: A tensor with the same type and shape of input_x 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: bfloat16,float16,float32,int8,int32,uint8
- output0 output_y: bfloat16,float16,float32,int8,int32,uint8

## Third-party framework compatibility

Compatible with the Pytorch operator Trunc. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
