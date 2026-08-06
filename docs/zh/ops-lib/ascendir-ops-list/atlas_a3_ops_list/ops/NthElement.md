# NthElement

```c
REG_OP(NthElement)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
                          DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .INPUT(n, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
                          DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .ATTR(reverse, Bool, false)
    .OP_END_FACTORY_REG(NthElement)
```

## Brief

Finds values of the n-th order statistic for the last dimension .

## Inputs

Inputs include:
- x: A Tensor. Must be one of the following types: float32, double, int32, uint8,
int16, int8, int64, bfloat16, uint16, float16, uint32, uint64.
- n: A Tensor of type int32. 0-D .

## Outputs

y: A Tensor. Has the same type as x . 

## Attributes

reverse: An optional bool. Defaults to False . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 n: int32
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Attention Constraints

The implementation for NthElement on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow NthElement operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
