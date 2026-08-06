# RmsNormQuantV3

```c
REG_OP(RmsNormQuantV3)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(scales1, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(scales2, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(zero_points1, TensorType({DT_INT32, DT_INT8, DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(zero_points2, TensorType({DT_INT32, DT_INT8, DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y1, TensorType({DT_INT8, DT_INT4, DT_HIFLOAT8, DT_FP8_E5M2, DT_FP8_E4M3FN}))
    .OUTPUT(y2, TensorType({DT_INT8, DT_INT4, DT_HIFLOAT8, DT_FP8_E5M2, DT_FP8_E4M3FN}))
    .OUTPUT(rstd, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-6f)
    .ATTR(div_mode, Bool, true)
    .ATTR(dst_type, Int, DT_INT8)
    .ATTR(output_rstd, Bool, false)
    .OP_END_FACTORY_REG(RmsNormQuantV3)
```

## Brief

RmsNormQuantV3 operator interface implementation.
Extends RmsNormQuantV2 with optional rstd output.
Calculating input: x, gamma, scales1, scales2, zero_points1, zero_points2 
Calculating process: 
 rstd = np.rsqrt(np.mean(np.power(x, 2), reduce_axis, keepdims=True) + epsilon)) 
 rmsnorm_out = x * rstd * gamma 
 if div_mode is true: 
   y1 = round(rmsnorm_out / scales1 + zero_points1) 
   y2 = round(rmsnorm_out / scales2 + zero_points2) 
 if div_mode is false: 
   y1 = round(rmsnorm_out * scales1 + zero_points1) 
   y2 = round(rmsnorm_out * scales2 + zero_points2) 

## Inputs

- x: A tensor. Support dtype: float32/float16/bfloat16, support format: ND.
       The shape supports at least 1 dimension, and at most 8 dimensions.
- gamma: A tensor. Describing the weight of the rmsnorm operation.
           Support dtype: float32/float16/bfloat16, support format: ND.
           The shape supports at least 1 dimension, and at most 8 dimensions.
- scales1: A tensor. Describing the weight of the first quant operation.
             Support dtype: float32/float16/bfloat16, support format: ND.
             The shape supports at least 1 dimension, and at most 8 dimensions.
- scales2: An optional input tensor. Describing the weight of the secend quant operation.
             Support dtype: float32/float16/bfloat16, support format: ND.
             The shape supports at least 1 dimension, and at most 8 dimensions.
- zero_points1: An optional input tensor. Describing the bias of the first quant operation.
                  Support dtype: int32/int8/float32/float16/bfloat16, support format: ND.
                  The shape supports at least 1 dimension, and at most 8 dimensions.
- zero_points2: An optional input tensor. Describing the bias of the secend quant operation.
                  Support dtype: int32/int8/float32/float16/bfloat16, support format: ND.
                  The shape supports at least 1 dimension, and at most 8 dimensions.
- beta: An optional input tensor. Describing the bias of the rmsnorm operation.
          Support dtype: float32/float16/bfloat16, support format: ND.
          The shape supports at least 1 dimension, and at most 8 dimensions.

## Outputs

- y1: A tensor. Describing the output of the first quant operation.
                  Support dtype: int8/int4/hifloat8/float8e5m2/float8e4m3fn, support format: ND.
                  The shape supports at least 1 dimension, and at most 8 dimensions.
- y2: A tensor. Describing the output of the second quant operation.
                  Support dtype: int8/int4/hifloat8/float8e5m2/float8e4m3fn, support format: ND.
                  The shape supports at least 1 dimension, and at most 8 dimensions.
- rstd: A tensor. Describing the output of the reciprocal of standard deviation from RMS normalization.
                    Support dtype: float32, support format: ND.
                    The shape supports at least 1 dimension, and at most 8 dimensions.

## Attributes

- epsilon: An optional attribute. Describing the epsilon of the rmsnorm operation.
             The type is float. Defaults to 1e-6.
- div_mode: An optional attribute. When div_mode is true, the quant opertaion uses division, otherwise, uses multiplication.
              The type is bool. Defaults to true.
- dst_type: An optional attribute. Output y data type enum value. Support DT_INT8, DT_INT4, DT_HIFLOAT8, DT_FP8_E5M2,
              DT_FP8_E4M3FN. Defaults to DT_INT8.
- output_rstd: An optional attribute. Whether to output rstd. The type is bool. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 gamma: bfloat16,float16,float32
- input2 scales1: bfloat16,float16,float32
- input3 scales2: bfloat16,float16,float32
- input4 zero_points1: bfloat16,float16,float32,int8,int32
- input5 zero_points2: bfloat16,float16,float32,int8,int32
- input6 beta: bfloat16,float16,float32
- output0 y1: float8_e4m3fn,float8_e5m2,hifloat8,int4,int8
- output1 y2: float8_e4m3fn,float8_e5m2,hifloat8,int4,int8
- output2 rstd: float32

## Attention Constraints

- When x dtype is FLOAT32, scales1/scales2 and zero_points1/zero_points2 must also be FLOAT32.
- When x dtype is FLOAT16 or BFLOAT16 and scales1/scales2 dtype is FLOAT32,
    zero_points1/zero_points2 dtype must be FLOAT32 or INT32.
- When x dtype is FLOAT16 or BFLOAT16 and scales1/scales2 dtype is not FLOAT32,
    scales1/scales2 dtype must match x dtype, and zero_points1/zero_points2 dtype must match x dtype or be INT8.
- When y dtype is INT4, the last dimension of x, gamma, and beta must be even.
- zero_points2 can only be provided when scales2 is present.


---

[Back to Operator Specifications (Ascend950)](../README.md)
