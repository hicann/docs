# Expand

```c
REG_OP(Expand)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32,DT_INT64, DT_INT8, DT_UINT8, DT_BOOL, DT_BF16}))
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32,DT_INT64, DT_INT8, DT_UINT8, DT_BOOL, DT_BF16}))
    .OP_END_FACTORY_REG(Expand)
```

## Brief

Expand the input tensor to a compatible shape. 

## Inputs

One inputs, including:
- x: A Tensor. Must be one of the following types:
    float16, float32, int32, int64, int8, uint8, bool, bfloat16. 
- shape: A Tensor to specify the shape that the input tensor expanded to.

## Outputs

y: A Tensor. Has the same type as "x", and the shape specified by input and attr shape 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int32,int64,uint8
- input1 shape: int32,int64
- output0 y: bool,float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 x: float16,float32,int8,int32,int64,uint8
- input1 shape: int32,int64
- output0 y: float16,float32,int8,int32,int64,uint8

## Attention Constraints

- The dim numbers of shape cannot be more than one.
- The inputs cannot be empty tensor.

## Third-party framework compatibility

Compatible with the ONNX operator Expand.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
