# GroupedDynamicBlockQuant

```c
REG_OP(GroupedDynamicBlockQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(group_list, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_HIFLOAT8, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(scale, TensorType({DT_FLOAT}))
    .ATTR(min_scale, Float, 0.0)
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, DT_FLOAT8_E5M2)
    .ATTR(row_block_size, Int, 1)
    .ATTR(col_block_size, Int, 128)
    .ATTR(group_list_type, Int, 0)
    .ATTR(dst_type_max, Float, 0.0)
    .OP_END_FACTORY_REG(GroupedDynamicBlockQuant)
```

## Brief

Online quantizes the input tensor per block & per group.

## Inputs

- x: A tensor of type Float16 or Bfloat16. Shape must be 2-dimensional or 3-dimensional.
- group_list: A tensor of type Int32. Shape must be 1-dimensional. Indicate the size or offset of each group on the
-2 axis of x.

## Outputs

- y: A tensor of type Fp8/HiF8. Quantized tensor with same shape as input x. Data type depends on dst_type.
- scale: A tensor of type float. Shape is [x.rows/row_block_size + group_num, ceil(x.cols/col_block_size)] or [B,
x.rows/row_block_size + group_num, ceil(x.cols/col_block_size)].

## Attributes

- min_scale: An Optional Float. Minimum scale value for quantization. Must be a non-negative float.
  Defaults to 0.0.
- round_mode: An Optional String. Quantization rounding mode. Valid values:
  - "rint": Supported for FLOAT8_E5M2/FLOAT8_E4M3FN
  - "round": Supported for HIFLOAT8 only
  - "hybrid": Supported for HIFLOAT8 only
  Defaults to "rint".
- dst_type: An Optional Int. Target data type enum value:
  - 34: HIFLOAT8
  - 35: FLOAT8_E5M2
  - 36: FLOAT8_E4M3FN
  Defaults to 35 (FLOAT8_E5M2).
- row_block_size: An Optional Int. Number of elements per block in -2 dimension.
  Defaults to 1.
- col_block_size: An Optional Int. Number of elements per block in -1 dimension.
  Defaults to 128.
- group_list_type: An Optional Int. Indicate the meaning of group_list.
  Defaults to 0.
- dst_type_max: An Optional Float. Maximum Value of the target data type.
  Only effective when dst_type is 34(HIFLOAT8), supporting values range 0 ~ 32768.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 group_list: int32
- output0 y: float8_e4m3fn,float8_e5m2,hifloat8
- output1 scale: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
