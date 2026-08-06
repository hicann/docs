# TopKV2

```c
REG_OP(TopKV2)
    .INPUT(x, TensorType::RealNumberType())
    .INPUT(k, TensorType::IndexNumberType())
    .OUTPUT(values, TensorType::RealNumberType())
    .OUTPUT(indices, TensorType::IndexNumberType())
    .ATTR(sorted, Bool, true)
    .ATTR(dim, Int, -1)
    .ATTR(largest, Bool, true)
    .ATTR(indices_dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(TopKV2)
```

## Brief

Finds values and indices of the "k" largest elements for the last
dimension . 

## Inputs

Two inputs, including:
- x: A 1D-8D tensor, with the last dimension at least "k".
Supported type: float16, float32, int16, int8, uint8, int32, int64, bfloat16, uint32, uint16, uint64.
Supported format: ND.
- k: A 0D Tensor. Supported type: int32, int64.
Supported format: ND.
Number of top elements to look for along the last dimension (along each row
for matrices) . 

## Outputs

- values: A Tensor, specifying the sorted data. Has the same type and format as
"input".
- indices: A Tensor. Indices of values in x. Dtype must be "int32" or "int64". Supported format: ND .
@see TopK()

## Attributes

- sorted: An optional bool. Defaults to "True".
If "True", the returned "k" elements are themselves sorted.
If "False", the returned "k" elements are not sorted.
- dim: An optional int. Defaults to -1. For reserved use.
- largest: An optional bool, controls whether to return largest or smallest elements. Defaults to true.
If "True", the "k" largest elements are returned in descending order.
If "False", the "k" smallest elements are returned in ascending order. 
- indices_dtype: An optional attribute indicates the sort result of indices' dtype, either "DT_INT32(3)" or "DT_INT64(9)". Defaults to "DT_INT32(3)".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 k: int32
- output0 values: bfloat16,float16,float32
- output1 indices: int32

## Third-party framework compatibility

- Compatible with the TensorFlow operator TopKV2.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
