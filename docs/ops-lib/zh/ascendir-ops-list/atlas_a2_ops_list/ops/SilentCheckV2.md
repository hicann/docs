# SilentCheckV2

```c
REG_OP(SilentCheckV2)
    .INPUT(val, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(input_grad, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(sfda, TensorType({DT_FLOAT32}))
    .INPUT(step, TensorType({DT_INT64}))
    .OUTPUT(input_grad, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .OUTPUT(sfda, TensorType({DT_FLOAT32}))
    .OUTPUT(step, TensorType({DT_INT64}))
    .OUTPUT(result, TensorType({DT_INT32}))
    .ATTR(c_min_steps, Int, 7)
    .ATTR(c_thresh_l1, Float, 1000000)
    .ATTR(c_coeff_l1, Float, 100000)
    .ATTR(c_thresh_l2, Float, 10000)
    .ATTR(c_coeff_l2, Float, 5000)
    .ATTR(npu_asd_detect, Int, 1)
    .OP_END_FACTORY_REG(SilentCheckV2)
```

## Brief

silentcheckV2. Detect npu silent-fault, return 0/1/2 as result represent normal/L1-error/L2-warn

## Inputs

- val: A Tensor, dtype is float16 bfloat16 or float32.
- input_grad: A Tensor, dtype is float16 bfloat16 or float32.
- sfda: A Tensor, dtype is float32. Must be shape of [3], represent: [pre_val, min_val, max_val]
- step: A Tensor, dtype is int64. Must be shape of [1].

## Outputs

- input_grad: A ref tensor, dtype is float16 bfloat16 or float32.
- sfda: A ref tensor, dtype is float32.
- step: A ref tensor, dtype is int64.
- result: A tensor, dtype is int32.

## Attributes

- c_min_steps: An optional int
- c_thresh_l1: An optional float
- c_coeff_l1: An optional float
- c_thresh_l2: An optional float
- c_coeff_l2: An optional float
- npu_asd_detect: An optional int

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 val: bfloat16,float16,float32
- input1 input_grad: bfloat16,float16,float32
- input2 sfda: float32
- input3 step: int64
- output0 input_grad: bfloat16,float16,float32
- output1 sfda: float32
- output2 step: int64
- output3 result: int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
