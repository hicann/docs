# IFMR

```c
REG_OP(IFMR)
  .INPUT(data, TensorType({DT_FLOAT16, DT_FLOAT}))
  .INPUT(data_min, TensorType({DT_FLOAT16, DT_FLOAT}))
  .INPUT(data_max, TensorType({DT_FLOAT16, DT_FLOAT}))
  .INPUT(cumsum, TensorType({DT_INT32}))
  .OUTPUT(scale, TensorType({DT_FLOAT}))
  .OUTPUT(offset, TensorType({DT_FLOAT}))
  .REQUIRED_ATTR(min_percentile, Float)
  .REQUIRED_ATTR(max_percentile, Float)
  .REQUIRED_ATTR(search_range, ListFloat)
  .REQUIRED_ATTR(search_step, Float)
  .REQUIRED_ATTR(with_offset, Bool)
  .ATTR(quant_bits, Int, 8)
  .OP_END_FACTORY_REG(IFMR)
```

## Brief

IFMR(Input Feature Map Reconstruction).

## Inputs

- data: A Tensor of feature map.
- data_min: A Tensor of min value of feature map.
- data_max: A Tensor of max value of feature map.
- cumsum: A Tensor of cumsum bin of data .

## Outputs

- scale: optimal scale.
- offset: optimal offset .

## Attributes

- min_percentile: min init percentile.
- max_percentile: max init percentile.
- search_range: search range.
- search_step: step size of searching.
- with_offset: whether using offset .
- quant_bits: bits of quant, an optional attr, default value is 8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 data: float16,float32
- input1 data_min: float16,float32
- input2 data_max: float16,float32
- input3 cumsum: int32
- output0 scale: float32
- output1 offset: float32

## Third-party framework compatibility

Compatible with mindspore


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
