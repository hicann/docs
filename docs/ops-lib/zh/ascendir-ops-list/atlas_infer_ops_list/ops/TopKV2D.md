# TopKV2D

```c
REG_OP(TopKV2D)
    .INPUT(x, TensorType::RealNumberType())
    .INPUT(k, TensorType({DT_INT32}))
    .INPUT(assist_seq, TensorType({DT_FLOAT16}))
    .OUTPUT(values, TensorType::RealNumberType())
    .OUTPUT(indices, TensorType({DT_INT32}))
    .ATTR(sorted, Bool, true)
    .ATTR(dim, Int, -1)
    .ATTR(largest, Bool, true)
    .OP_END_FACTORY_REG(TopKV2D)
```

## Brief

Finds the k largest or smallest values and indices along a dimension.

## Inputs

Three inputs, including:
- x: A Tensor of type float16/float/double/int8/int16/int32/int64/uint8/uint16/uint32/uint64.
- k: A Tensor of type int32, specifying the number of top elements.
- assist_seq: A Tensor of type float16, assisting in sequence computation.

## Outputs

- values: A Tensor of same type as x, containing the k largest/smallest values.
- indices: A Tensor of type int32, containing the indices of the k largest/smallest values.

## Attributes

- sorted: An optional bool, specifying whether to sort the output. Default: true.
- dim: An optional int, specifying the dimension along which to perform topk. Default: -1.
- largest: An optional bool, specifying whether to select largest or smallest values. Default: true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float16
- input1 k: int32
- input2 assist_seq: float16
- output0 values: float16
- output1 indices: int32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
