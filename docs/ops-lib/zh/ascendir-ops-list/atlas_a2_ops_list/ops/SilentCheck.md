# SilentCheck

```c
REG_OP(SilentCheck)
    .INPUT(val, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(input_grad, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(pre_val, TensorType({DT_FLOAT32}))
    .INPUT(min_val, TensorType({DT_FLOAT32}))
    .INPUT(max_val, TensorType({DT_FLOAT32}))
    .INPUT(val_counter, TensorType({DT_INT32}))
    .OUTPUT(input_grad, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BFLOAT16}))
    .OUTPUT(pre_val, TensorType({DT_FLOAT32}))
    .OUTPUT(min_val, TensorType({DT_FLOAT32}))
    .OUTPUT(max_val, TensorType({DT_FLOAT32}))
    .OUTPUT(result, TensorType({DT_INT32}))
    .ATTR(c_min_steps, Int, 7)
    .ATTR(c_thresh_l1, Float, 1000000)
    .ATTR(c_coeff_l1, Float, 100000)
    .ATTR(c_thresh_l2, Float, 10000)
    .ATTR(c_coeff_l2, Float, 5000)
    .OP_END_FACTORY_REG(SilentCheck)
```

## Brief

silentcheck.

## Inputs

- val: A Tensor, dtype is float16 bfloat16 or float32.
- input_grad: A Tensor, dtype is float16 bfloat16 or float32.
- pre_val: A Tensor, dtype is float32.
- min_val: A Tensor, dtype is float32.
- max_val: A Tensor, dtype is float32.
- val_counter: A Tensor, dtype is int32.

## Outputs

- pre_val: A ref tensor, dtype is float32.
- min_val: A ref tensor, dtype is float32.
- max_val: A ref tensor, dtype is float32.
- input_grad: A ref tensor, dtype is float16 bfloat16 or float32.
- result: A tensor, dtype is int32.

## Attributes

- c_min_steps: An optional int
- c_thresh_l1: An optional float
- c_coeff_l1: An optional float
- c_thresh_l2: An optional float
- c_coeff_l2: An optional float

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 val: bfloat16,float16,float32
- input1 input_grad: bfloat16,float16,float32
- input2 pre_val: float32
- input3 min_val: float32
- input4 max_val: float32
- input5 val_counter: int32
- output0 input_grad: bfloat16,float16,float32
- output1 pre_val: float32
- output2 min_val: float32
- output3 max_val: float32
- output4 result: int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
