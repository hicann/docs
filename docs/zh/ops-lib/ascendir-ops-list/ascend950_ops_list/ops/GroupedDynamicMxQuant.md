# GroupedDynamicMxQuant

```c
REG_OP(GroupedDynamicMxQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(group_index, TensorType({DT_Int32}))
    .OUTPUT(y, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(mxscale, TensorType({DT_FLOAT8_E8M0}))
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, DT_FLOAT8_E5M2)
    .ATTR(blocksize, Int, 32)
    .ATTR(scale_alg, Int, 0)
    .ATTR(dst_type_max, Float, 0.0)
    .OP_END_FACTORY_REG(GroupedDynamicMxQuant)
```

## Brief

Quantizes the input to mxfp8 group-wisely, according to group_index. 

## Inputs

- x: A tensor of type float16 or bfloat16, specifying the input.
The shape only supports 2 dimensions.
- group_index: A tensor of type int32, specifying the index of groups.
The shape only supports 1 dimension.

## Outputs

- y: An output tensor of type FLOAT4_E2M1/FLOAT4_E1M2 or FLOAT8_E4M3FN/FLOAT8_E5M2. It has the same shape and rank
as input x.
- mxscale: An output tensor of type FLOAT8_E8M0, the shape only supports 3 dimensions.
- mxscale.shape[0] = x.shape[0] / (blocksize * 2) + group_index.shape[0].
- mxscale.shape[1] = x.shape[1].
- mxscale.shape[2] = 2.

## Attributes

- round_mode: An optional string, specifying the quantization rounding mode.
Support "rint"/"round"/"floor". For FLOAT8, only support "rint". For Float4, support "rint"/"round"/"floor".
Defaults to "rint".
- dst_type: An optional int, specifying the dtype of output y. Target data type enum value:
- 35: DT_FLOAT8_E5M2
- 36: DT_FLOAT8_E4M3FN
- 40: DT_FLOAT4_E2M1
- 41: DT_FLOAT4_E1M2
Defaults to DT_FLOAT8_E5M2.
- blocksize: An optional int, specifying the block size of quantization.
Defaults and only supports 32.
- scale_alg: An Optional Int. The algorithm for the scale in quantization.
Support MxFP4/MxFP8(OCP Microscaling Formats(Mx) Specification, count 0) or MxFP8(nvidia-cuBLAS, count 1) or
MxFP4(Dynamic Dtype Range, count 2).
Defaults to 0.
- dst_type_max: An Optional Float. Max_dtype takes the maximum value of the quant_data_type, or the provided value.
Only support in FLOAT4 mode, with a valid range of 0.0/6.0 to 12.0(FLOAT4_E2M1) or 0.0/1.75 to 3.5(FLOAT4_E1M2).
Defaults to 0.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 group_index: int32
- output0 y: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output1 mxscale: float8_e8m0

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, Onnx, Tensorflow or Pytorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
