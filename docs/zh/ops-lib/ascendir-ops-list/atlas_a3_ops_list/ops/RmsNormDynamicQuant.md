# RmsNormDynamicQuant

```c
REG_OP(RmsNormDynamicQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scales, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_INT8}))
    .OUTPUT(scale, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-6)
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(RmsNormDynamicQuant)
```

## Brief

Fused Operator of RmsNorm and DynamicQuant.
Calculating input: x, gamma, smooth_scales 
Calculating process: 
 rstd = np.rsqrt(np.mean(np.power(x, 2), reduce_axis, keepdims=True) + epsilon)) 
 rmsnorm_out = x * rstd * gamma 
 if smooth_scales exist: 
   input = rmsnorm_out * smooth_scales 
   scale = row_max(abs(input)) / max_val 
 if smooth_scales not exist: 
   scale = row_max(abs(rmsnorm_out)) / max_val 
 y = round(input / scale) 

## Inputs

- x: A tensor. Input x for the operation.
        Support dtype: float16/bfloat16, support format: ND.
- gamma: A tensor. Describing the weight of the rmsnorm operation.
           Support dtype: float16/bfloat16, support format: ND.
- smooth_scales: An optional input tensor. Describing the weight of dynamic quantization.
             Support dtype: float16/bfloat16, support format: ND.
- beta: An optional input tensor. Describing the offset value of rmsnorm operation.
             Support dtype: float16/bfloat16, support format: ND. Has the same dtype and shape as "gamma".

## Outputs

- y: A tensor. Describing the output of dynamic quantization.
                  Support dtype: int8, support format: ND.
- scale: A tensor. Describing of the factor for dynamic quantization.
                 Support dtype: float32, support format: ND.

## Attributes

- epsilon: An optional attribute. Describing the epsilon of the rmsnorm operation.
         The type is float. Defaults to 1e-6.
- dst_type: An optional int32. Output y data type enum value. Support DT_INT8.
              Defaults to DT_INT8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 gamma: bfloat16,float16
- input2 smooth_scales: bfloat16,float16
- input3 beta: bfloat16,float16
- output0 y: int8
- output1 scale: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
