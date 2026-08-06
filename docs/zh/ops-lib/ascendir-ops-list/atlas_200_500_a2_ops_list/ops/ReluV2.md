# ReluV2

```c
REG_OP(ReluV2)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT8, DT_INT32, DT_INT16, DT_INT64, DT_UINT8, DT_UINT16, DT_QINT8, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT8, DT_INT32, DT_INT16, DT_INT64, DT_UINT8, DT_UINT16, DT_QINT8, DT_BF16}))
    .OUTPUT(mask, TensorType({DT_UINT8, DT_UINT1}))
    .OP_END_FACTORY_REG(ReluV2)
```

## Brief

Computes rectified linear: "max(x, 0)".

## Inputs

x: A tensor. Must be one of the following types: float32, float16, double, int8, int32, int16, int64, uint8, uint16, qint8, bfloat16.
In Ascend 950 AI Processor, support ND format. Others support 4D, format must be one of [NHWC, NCHW, HWCN].

## Outputs

- y: A tensor with the same dtype and shape as the "x".
- mask: A tensor of value "1" (for x > 0) or "0" (for x <= 0). Type is uint8 or uint1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
- output1 mask: uint1

## Attention Constraints

The last dimension of "x" must be divisible by 8.

## Third-party framework compatibility

Incompatible with TensorFlow or Caffe.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
