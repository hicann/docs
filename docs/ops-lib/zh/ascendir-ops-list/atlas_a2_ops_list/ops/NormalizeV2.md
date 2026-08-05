# NormalizeV2

```c
REG_OP(NormalizeV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(mean, TensorType({DT_FLOAT}))
    .INPUT(variance, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(NormalizeV2)
```

## Brief

NormalizeV2 

## Inputs

- x: A 4-D Tensor. Must be one of the following types: uint8, float16,
       float. Must set the format, supported format list ["NCHW, NHWC"].
- mean: A 4-D float tensor. value of "C(channel)" is same to x
- variance: A 4-D float tensor. value of "C(channel)" is same to x

## Outputs

- y: A 4-D Tensor. Must be one of the following types: float16, float.
       Must set the format, supported format list ["NCHW, NHWC"]. 

## Attributes

- dtype: An Type attr, support type list [DT_FLOAT16, DT_FLOAT].
           Defaults to DT_FLOAT. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input0 x: float16,float32
- input1 mean: float32
- input2 variance: float32
- output0 y: float16,float32

## Attention Constraints

This operator will be deprecated in the future.

## Third-party framework compatibility

Compatible with pytorch normalize operator. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
