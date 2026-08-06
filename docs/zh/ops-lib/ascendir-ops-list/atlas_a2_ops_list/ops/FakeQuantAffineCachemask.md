# FakeQuantAffineCachemask

```c
REG_OP(FakeQuantAffineCachemask)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(scale, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(zero_point, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(mask, TensorType({DT_BOOL}))
    .REQUIRED_ATTR(axis, Int)
    .REQUIRED_ATTR(quant_min, Int)
    .REQUIRED_ATTR(quant_max, Int)
    .OP_END_FACTORY_REG(FakeQuantAffineCachemask)
```

## Brief

Fake-quantize the data of 'x' tensor with scale, zero_point, quant_min and quant_max. 

## Inputs

Three inputs, including:
- x: A Tensor. Must be one of the following types: float16, float32.
- scale: A Tensor of type float32 or float16. Has the same type and format as "x".
- zero_point: A Tensor of type int32, float16 or float32.

## Outputs

y: A Tensor of type float32 or float16.
mask: A Tensor of type bool. 

## Attributes

- axis: An required attribute of type int64.
- quant_min: An required attribute of type int64.
- quant_max: An required attribute of type int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 scale: float16,float32
- input2 zero_point: float16,float32,int32
- output0 y: float16,float32
- output1 mask: bool

## Third-party framework compatibility

Compatible with Pytorch operator FakeQuantAffineCachemask.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
