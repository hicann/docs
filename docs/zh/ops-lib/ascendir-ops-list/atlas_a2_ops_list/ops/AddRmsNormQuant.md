# AddRmsNormQuant

```c
REG_OP(AddRmsNormQuant)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(scales1, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(scales2, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(zero_points1, TensorType({DT_INT32, DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(zero_points2, TensorType({DT_INT32, DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y1, TensorType({DT_INT8, DT_HIFLOAT8, DT_FP8_E5M2, DT_FP8_E4M3FN}))
    .OUTPUT(y2, TensorType({DT_INT8, DT_HIFLOAT8, DT_FP8_E5M2, DT_FP8_E4M3FN}))
    .OUTPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(axis, Int, -1)
    .ATTR(epsilon, Float, 1e-6f)
    .ATTR(div_mode, Bool, true)
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(AddRmsNormQuant)
```

## Brief

AddRmsNormQuant operator interface implementation.
Calculating input: x1, x2, gamma, scales1, scales2, zero_points1, zero_points2 
Calculating process: 
 x = x1 + x2 
 rstd = np.rsqrt(np.mean(np.power(x, 2), reduce_axis, keepdims=True) + epsilon)) 
 rmsnorm_out = x * rstd * gamma 
 if div_mode is true: 
   y1 = round(rmsnorm_out / scales1 + zero_points1) 
   y2 = round(rmsnorm_out / scales2 + zero_points2) 
 if div_mode is false: 
   y1 = round(rmsnorm_out * scales1 + zero_points1) 
   y2 = round(rmsnorm_out * scales2 + zero_points2) 

## Inputs

- x1: A tensor. Input x1 for the add operation.
        Support dtype: float32/float16/bfloat16, support format: ND.
- x2: A tensor. Input x2 for the add operation.
        Support dtype: float32/float16/bfloat16, support format: ND.
- gamma: A tensor. Describing the weight of the rmsnorm operation.
           Support dtype: float32/float16/bfloat16, support format: ND.
- scales1: A tensor. Describing the weight of the first quant operation.
             Support dtype: float32/float16/bfloat16, support format: ND.
- scales2: An optional input tensor. Describing the weight of the secend quant operation.
             Support dtype: float32/float16/bfloat16, support format: ND.
- zero_points1: An optional input tensor. Describing the bias of the first quant operation.
                  Support dtype: int32/float32/float16/bfloat16, support format: ND.
- zero_points2: An optional input tensor. Describing the bias of the secend quant operation.
                  Support dtype: int32/float32/float16/bfloat16, support format: ND.
- beta: An optional input tensor. Describing the bias of the rmsnorm operation.
                  Support dtype: int32/float32/float16/bfloat16, support format: ND.

## Outputs

- y1: A tensor. Describing the output of the first quant operation.
                  Support dtype: int8/hifloat8/float8e5m2/float8e4m3fn, support format: ND.
- y2: A tensor. Describing the output of the second quant operation.
                  Support dtype: int8/hifloat8/float8e5m2/float8e4m3fn, support format: ND.
- x: A tensor. Describing the output of the x1+x2 add operation.
                 Support dtype: float32/float16/bfloat16, support format: ND.

## Attributes

- axis: An optional attribute. Describing the axis of the quant operation, does not take effect now.
          The type is int. Defaults to -1.
- epsilon: An optional attribute. Describing the epsilon of the rmsnorm operation.
             The type is float. Defaults to 1e-6.
- div_mode: An optional attribute. When div_mode is true, the quant opertaion uses division, otherwise, uses multiplication.
              The type is bool. Defaults to true.
- dst_type: An optional int32. Output y data type enum value. Support DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E5M2,
              DT_FLOAT8_E4M3FN. Defaults to DT_INT8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16
- input1 x2: bfloat16,float16
- input2 gamma: bfloat16,float16
- input3 scales1: bfloat16,float32
- input4 scales2: bfloat16,float32
- input5 zero_points1: bfloat16,int32
- input6 zero_points2: bfloat16,int32
- input7 beta: bfloat16,float16
- output0 y1: int8
- output1 y2: int8
- output2 x: bfloat16,float16


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
