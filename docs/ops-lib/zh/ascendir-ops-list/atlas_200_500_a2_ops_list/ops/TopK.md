# TopK

```c
REG_OP(TopK)
    .INPUT(x, TensorType::RealNumberType())
    .INPUT(k, TensorType({DT_INT32}))
    .OUTPUT(values, TensorType::RealNumberType())
    .OUTPUT(indices, TensorType({DT_INT32}))
    .ATTR(sorted, Bool, true)
    .ATTR(largest, Bool, true)
    .ATTR(dim, Int, -1)
    .OP_END_FACTORY_REG(TopK)
```

## Brief

Finds the k largest or smallest values and indices along a dimension.

## Inputs

x: A Tensor of type float16/float/double/int8/int16/int32/int64/uint8/uint16/uint32/uint64/bfloat16. 
k: A Tensor of type int32, specifying the number of top elements.

## Outputs

values: A Tensor of same type as x, containing the k largest/smallest values.
indices: A Tensor of type int32, containing the indices of the k largest/smallest values.

## Attributes

dim: An optional int, specifying the dimension along which to perform topk. Default: -1.
largest: An optional bool, specifying whether to select largest or smallest values. Default: true.
sorted: An optional bool, specifying whether to sort the output. Default: true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 k: int32
- output0 values: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output1 indices: int32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
