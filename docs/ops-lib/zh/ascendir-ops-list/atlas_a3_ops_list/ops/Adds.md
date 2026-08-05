# Adds

```c
REG_OP(Adds)
     .INPUT(x, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_INT64}))
     .OUTPUT(y, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_INT64}))
     .REQUIRED_ATTR(value,Float)
     .OP_END_FACTORY_REG(Adds)
```

## Brief

Add tensor with value.

## Inputs

One input, including: 
x: A ND Tensor. Must be one of the following types:int32,int16, float16, float32, bfloat16,int64. 

## Outputs

y: A ND Tensor. Has the same dtype and shape as "x1". 

## Attributes

value: A scale. Must be float. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int16,int32,int64
- output0 y: bfloat16,float16,float32,int16,int32,int64

## Attention Constraints

For parameters of the float32 type, there is no precision loss. For INT32 and INT64 parameters,
precision loss occurs when the parameter value exceeds 2^24. it is recommended to use Add.

## Third-party framework compatibility

Compatible with the PyTorch operator adds.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
