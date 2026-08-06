# MultiAddRmsNormDynamicQuant

```c
REG_OP(MultiAddRmsNormDynamicQuant)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scale1, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scale2, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y1, TensorType({DT_INT8}))
    .OUTPUT(y2, TensorType({DT_INT8}))
    .OUTPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(scale1, TensorType({DT_FLOAT}))
    .OUTPUT(scale2, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-6)
    .OP_END_FACTORY_REG(MultiAddRmsNormDynamicQuant)
```

## Brief

Fused Operator of 0~4 Add, 1 RmsNorm and 1 DynamicQuant.
Calculating input: x1, x2, gamma, smooth_scale1, smooth_scale2 
Calculating process: 
 x = sum(x1) + x2 
 rstd = np.rsqrt(np.mean(np.power(x, 2), reduce_axis, keepdims=True) + epsilon)) 
 rmsnorm_out = x * rstd * gamma 
 if smooth_scales1 exist: 
   scale1 = row_max(abs(rmsnorm_out * smooth_scale1)) / 127 
 if smooth_scales1 not exist: 
   scale1 = row_max(abs(rmsnorm_out)) / 127 
 y1 = round(rmsnorm_out / scale1) 
 if smooth_scales2 exist: 
   scale2 = row_max(abs(rmsnorm_out * smooth_scale2)) / 127 
   y2 = round(rmsnorm_out / scale2) 
 if smooth_scales2 not exist:  
   not calculate scale2 and y2. 
 Only for experimental use. 

## Inputs

- x1: A tensor list. Each item of x1 is for the add operation, supports length 1 to 5.
        Support dtype: float16/bfloat16, support format: ND.
- x2: A tensor. Input x2 for the add operation.
        Support dtype: float16/bfloat16, support format: ND.
- gamma: A tensor. Describing the weight of the rmsnorm operation.
           Support dtype: float16/bfloat16, support format: ND.
- smooth_scale1: A tensor. Describing the weight of the first dynamic quantization.
             Support dtype: float16/bfloat16, support format: ND.
- smooth_scale2: An optional input tensor. Describing the weight of the secend dynamic quantization.
             Support dtype: float16/bfloat16, support format: ND.

## Outputs

- y1: A tensor. Describing the output of the first dynamic quantization.
                  Support dtype: int8, support format: ND.
- y2: A tensor. Describing the output of the second dynamic quantization.
                  Support dtype: int8, support format: ND.
- x: A tensor. Describing the output of the x1+x2 add operation.
                 Support dtype: float16/bfloat16, support format: ND.
- y: A tensor. Describing the output of the rmsNorm operation.
                 Support dtype: float16/bfloat16, support format: ND.
- scale1: A tensor. Describing of the factor for the first dynamic quantization.
                 Support dtype: float32, support format: ND.
- scale2: A tensor. Describing of the factor for the second dynamic quantization.
                 Support dtype: float32, support format: ND.

## Attributes

epsilon: An optional attribute. Describing the epsilon of the rmsnorm operation.
         The type is float. Defaults to 1e-6.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16
- input1 x2: bfloat16,float16
- input2 gamma: bfloat16,float16
- input3 smooth_scale1: bfloat16,float16
- input4 smooth_scale2: bfloat16,float16
- output0 y1: int8
- output1 y2: int8
- output2 x: bfloat16,float16
- output3 y: bfloat16,float16
- output4 scale1: float32
- output5 scale2: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
