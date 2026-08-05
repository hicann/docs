# ParallelConcat

```c
REG_OP(ParallelConcat)
    .DYNAMIC_INPUT(values, TensorType({DT_FLOAT,DT_FLOAT16,DT_INT8,DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_UINT32,DT_UINT64}))
    .OUTPUT(output_data, TensorType({DT_FLOAT,DT_FLOAT16,DT_INT8,DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_UINT32,DT_UINT64}))
    .REQUIRED_ATTR(shape, ListInt)
    .REQUIRED_ATTR(N, Int)
    .OP_END_FACTORY_REG(ParallelConcat)
```

## Brief

Concatenates a list of N tensors along the first dimension.

## Inputs

One input, including:
values: A list of Tensors. Must be one of the following types: int8, int16,
int32, int64, uint8, uint16, uint32, uint64, float16, float32.
Tensors to be concatenated. All must have size 1 in the first dimension
and same shape. It's a dynamic input.

## Outputs

output_data: The concatenated tensor with same type as "values".

## Attributes

- shape: A required list of ints.
- N: A required int. The numble of dynamic_input "values" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 values: bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 output_data: bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ParallelConcat.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
