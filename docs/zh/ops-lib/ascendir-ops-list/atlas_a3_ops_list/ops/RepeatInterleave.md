# RepeatInterleave

```c
REG_OP(RepeatInterleave)
    .INPUT(x, TensorType::BasicType())
    .INPUT(repeats, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType::BasicType())
    .ATTR(axis, Int, 1000)
    .OP_END_FACTORY_REG(RepeatInterleave)
```

## Brief

Repeat elements of input with copies of data along a specified dimension.

## Inputs

Two inputs:
- x: A Tensor with ND format. Support float, float16, bfloat16, int8, int16, int32, int64,
uint8, uint16, uint32, uint64, bool.
- repeats: A Tensor with 0-D / 1-D or a Scalar. Support int32, int64.

## Outputs

y: A Tensor, which is the same dtype as x.

## Attributes

axis: An optional int32, specifying the axis to repeat. Defaults to 1000.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 repeats: int32,int64
- output0 y: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- When "repeats" is 1-D tensor, the size of "repeats" must be 1 or x.size()[axis].
- "axis" must be within the rank of the input tensor.

## Third-party framework compatibility

Compatible with the PyTorch operator RepeatInterleave.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
