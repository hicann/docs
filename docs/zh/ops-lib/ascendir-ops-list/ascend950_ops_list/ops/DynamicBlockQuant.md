# DynamicBlockQuant

```c
REG_OP(DynamicBlockQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(scale, TensorType({DT_FLOAT}))
    .ATTR(min_scale, Float, 0.0)
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, DT_FLOAT8_E5M2)
    .ATTR(row_block_size, Int, 1)
    .ATTR(col_block_size, Int, 128)
    .ATTR(dst_type_max, Float, 0.0)
    .OP_END_FACTORY_REG(DynamicBlockQuant)
```

## Brief

Online quantizes the input tensor per block.

## Inputs

- x: A tensor of type float16, bfloat16 or float32. Shape must be 2-dimensional or 3-dimensional.

## Outputs

- y: Quantized tensor with same shape as input x. Data type depends on dst_type.
- scale: Scale tensor of type float. Shape is [ceil(x.rows/row_block_size), ceil(x.cols/col_block_size)] or [B,
ceil(x.rows/row_block_size), ceil(x.cols/col_block_size)].

## Attributes

- min_scale: (Optional) Minimum scale value for quantization. Must be a positive float.
  Defaults to 0.0.
- round_mode: (Optional) Quantization rounding mode. Valid values:
  - "rint": Supported for FLOAT8_E5M2/FLOAT8_E4M3FN
  - "round": Supported for HIFLOAT8 only
  Defaults to "rint".
- dst_type: (Optional) Target data type enum value:
  - 2: INT8
  - 34: HIFLOAT8
  - 35: FLOAT8_E5M2
  - 36: FLOAT8_E4M3FN
  Defaults to 35 (FLOAT8_E5M2).
- row_block_size: (Optional) Number of elements per block in -2 dimension.
Only support 1, 128, 256, 512. Defaults to 1.
- col_block_size: (Optional) Number of elements per block in -1 dimension.
Only support 64, 128, 192, 256. Defaults to 128.
- dst_type_max: (Optional) Maximum Value of the target data type.
Only effective when dst_type is 34(HIFLOAT8), supporting values 0.0, 15.0, 56.0, 224.0, 32768.0. Defaults to 0.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: float8_e4m3fn,float8_e5m2,hifloat8,int8
- output1 scale: float32

## Third-party framework compatibility

Custom operator with no direct mapping in Caffe/ONNX/TensorFlow/PyTorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
