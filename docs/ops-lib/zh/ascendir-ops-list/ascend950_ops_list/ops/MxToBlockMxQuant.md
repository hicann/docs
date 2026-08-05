# MxToBlockMxQuant

```c
REG_OP(MxToBlockMxQuant)
    .INPUT(x, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .INPUT(mxscale, TensorType({DT_FLOAT8_E8M0}))
    .OUTPUT(y, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .OUTPUT(scale1, TensorType({DT_FLOAT8_E8M0}))
    .OUTPUT(scale2, TensorType({DT_FLOAT8_E8M0}))
    .ATTR(dst_type, Int, DT_FLOAT8_E4M3FN)
    .OP_END_FACTORY_REG(MxToBlockMxQuant)
```

## Brief

Convert FP4-MX format data into FP8 block-quantized format. 

## Inputs

- x: A tensor of type FLOAT4_E2M1 or FLOAT4_E1M2, specifying the input.
The shape only supports 2-3 dimensions.
- mxscale: A tensor of type FLOAT8_E8M0. Shape needs to meet the following conditions:
The shape only supports 3-4 dimensions.
- mxscale.shape[-2] = (Ceil(x.shape[axis] / 32) + 2 - 1) / 2.
- mxscale.shape[-1] = 2.
- Other dimensions maintain the same shape as x.

## Outputs

- y: An output tensor of type FLOAT8_E5M2 or FLOAT8_E4M3FN. It has the same shape as input x.
- scale1: An output tensor of type FLOAT8_E8M0. Shape needs to meet the following conditions:
- It has the same shape as input mxscale.
- scale2: An output tensor of type DT_FLOAT8_E8M0. Shape needs to meet the following conditions:
- rank(scale2) = rank(x) + 1.
- scale2.shape[-3] = ((Ceil(x.shape[-2] / 32) + 2 - 1) / 2) * 2 / 2.
- scale2.shape[-2] = x.shape[-1].
- scale2.shape[-1] = 2.
- Other dimensions match input x.
- scale2 tensor is padded with zeros to ensure its size along the quantized axis is even.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float4_e1m2,float4_e2m1
- input1 mxscale: float8_e8m0
- output0 y: float8_e4m3fn,float8_e5m2
- output1 scale1: float8_e8m0
- output2 scale2: float8_e8m0

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, Onnx, Tensorflow or PyTorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
