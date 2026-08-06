# Dot

```c
REG_OP(Dot)
    .INPUT(input_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_UINT8, DT_INT8, DT_INT32}))
    .INPUT(input_y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_UINT8, DT_INT8, DT_INT32}))
    .OUTPUT(output, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_UINT8, DT_INT8, DT_INT32}))
    .OP_END_FACTORY_REG(Dot)
```

## Brief

Computes the dot product (inner product) of two tensors. This function does not broadcast.

## Inputs

Two inputs, including:
- input_x: A ND Tensor. the first tensor must be 1d. Must be one of the following types:
float32, float16, bfloat16, uint8, int8, int32. 
- input_y: A ND Tensor. the second tensor must be 1d. Must be one of the following types:
float32, float16, bfloat16, uint8, int8, int32. 

## Outputs

output: A ND Tensor. Result of the two inputs, must be 1d. A ND Tensor of the same dtype as input_x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: bfloat16,float16,float32,int8,int32,uint8
- input1 input_y: bfloat16,float16,float32,int8,int32,uint8
- output0 output: bfloat16,float16,float32,int8,int32,uint8

## Third-party framework compatibility

Compatible with the PyTorch dot operator. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
