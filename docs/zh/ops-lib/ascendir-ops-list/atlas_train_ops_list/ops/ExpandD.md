# ExpandD

```c
REG_OP(ExpandD)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8, DT_BOOL}))
    .REQUIRED_ATTR(shape, ListInt)
    .OP_END_FACTORY_REG(ExpandD)
```

## Brief

Expand the input tensor to a compatible shape. 

## Inputs

One inputs, including:
x: A Tensor. Must be one of the following types:
    float16, float32, int32, int8, uint8, bool. 

## Outputs

y: A Tensor. Has the same type as "x", and the shape specified by input and attr shape 

## Attributes

shape: A required listInt to specify the shape that the input tensor expanded to. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int32,uint8
- output0 y: bool,float16,float32,int8,int32,uint8

## Attention Constraints

The operator will not be enhanced in the future.

## Third-party framework compatibility

Compatible with the ONNX operator Expand.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
