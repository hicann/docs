# SilentCheckV3

```c
REG_OP(SilentCheckV3)
    .INPUT(val, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(max, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(avg, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(input_grad, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(step, TensorType({DT_INT64}))
    .INPUT(dst_size, TensorType({DT_INT64}))
    .INPUT(dst_stride, TensorType({DT_INT64}))
    .INPUT(dst_offset, TensorType({DT_INT64}))
    .OUTPUT(avg, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .OUTPUT(input_grad, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .OUTPUT(step, TensorType({DT_INT64}))
    .OUTPUT(result, TensorType({DT_INT32}))
    .ATTR(c_thresh_l1, Float, 1000000)
    .ATTR(c_thresh_l2, Float, 10000)
    .ATTR(beta1, Float, 0.99)
    .ATTR(npu_asd_detect, Int, 1)
    .OP_END_FACTORY_REG(SilentCheckV3)
```

## Brief

silentcheckV3. Detect npu silent-fault, return 0/1/2 as result represent normal/L1-error/L2-warn

## Inputs

- val: A Tensor, dtype is float16 bfloat16 or float32. Must be shape of [0].
- max: A Tensor, dtype is float16 bfloat16 or float32. Must be shape of [0].
- avg: A Tensor, dtype is float16 bfloat16 or float32. Must be shape of [0].
- input_grad: A Tensor, dtype is float16 bfloat16 or float32.
- step: A Tensor, dtype is int64. Must be shape of [1].
- dst_size: A Tensor, dtype is int64.
- dst_stride: A Tensor, dtype is int64.
- dst_offset: A Tensor, dtype is int64.

## Outputs

- avg: A ref tensor, dtype is float16 bfloat16 or float32.
- input_grad: A ref tensor, dtype is float16 bfloat16 or float32.
- step: A ref tensor, dtype is int64.
- result: A tensor, dtype is int32.

## Attributes

- c_thresh_l1: An optional float
- c_thresh_l2: An optional float
- beta1: An optional float
- npu_asd_detect: An optional int

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 val: bfloat16,float16,float32
- input1 max: bfloat16,float16,float32
- input2 avg: bfloat16,float16,float32
- input3 input_grad: bfloat16,float16,float32
- input4 step: int64
- input5 dst_size: int64
- input6 dst_stride: int64
- input7 dst_offset: int64
- output0 avg: bfloat16,float16,float32
- output1 input_grad: bfloat16,float16,float32
- output2 step: int64
- output3 result: int32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
