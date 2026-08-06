# MapIndex

```c
REG_OP(MapIndex)
    .INPUT(x, TensorType({DT_INT32}))
    .INPUT(data_seq, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(level_index, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .ATTR(transpose, Bool, false)
    .OP_END_FACTORY_REG(MapIndex)
```

## Brief

Returns index of shape in the map.

## Inputs

Three inputs, including:
- x: One dimensional tensor of type int32, specifying queried shape,
Format support ND, the max dim is 400 (128 on Lhisi(Hi3796CV300CS, SD3403), 24000 on Ascend 950 AI Processor).
- data_seq: One dimensional tensor of type int32,
Format support ND, specifying the mapped table is queried.
The length of data_seq must be multiple of the length of x, and the length of data_seq / x <= 100 (256 on Ascend 950 AI Processor).
- level_index: One dimensional tensor of type int32, the length of level_index must be equal to the length of data_seq divided by the length of x.
Format support ND, specifying secondary index. 

## Outputs

y: A scalar of type int32, specifying index of shape in the map.

## Attributes

- transpose: An optional bool. specifying the input is transposed on A3 or A5, A3 is true, A5 is false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int32
- input1 data_seq: int32
- input2 level_index: int32
- output0 y: int32
### AI CPU
- input0 x: int32
- input1 data_seq: int32
- output0 y: int32

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
