# AntiMxQuant

```c
REG_OP(AntiMxQuant)
    .INPUT(x, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(mxscale, TensorType({DT_FLOAT8_E8M0}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .ATTR(axis, Int, -1)
    .ATTR(dst_type, Int, DT_BF16)
    .OP_END_FACTORY_REG(AntiMxQuant)
```

## Brief

Dequantize the quantized FLOAT4/FLOAT8 input into FLOAT16/BFLOAT16/FLOAT32 format. 

## Inputs

- x: A tensor of type FLOAT4_E2M1/FLOAT4_E1M2 or FLOAT8_E5M2/FLOAT8_E4M3FN, specifying the input.
The shape only supports 1-7 dimensions.
- mxscale: A tensor of type FLOAT8_E8M0, specifying the quantization coefficient.
The shape only supports 2-8 dimensions.
- mxscale.shape[axis - 1] = Even(Ceil(x.shape[axis], 32)).
- mxscale.shape[-1] = 2.
- Other dimensions maintain the same shape as x.

## Outputs

- y: An output tensor of type FLOAT16, BFLOAT16 or FLOAT32. It has the same shape as input x.

## Attributes

- axis: An optional int, specifying the dequantization axis.
Defaults to -1.
- dst_type: An optional int, specifying the dtype of output y. Target data type enum value:
- 0: DT_FLOAT32
- 1: DT_FLOAT16
- 27: DT_BF16
Defaults to BFLOAT16.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- input1 mxscale: float8_e8m0
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, Onnx, Tensorflow or Pytorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
