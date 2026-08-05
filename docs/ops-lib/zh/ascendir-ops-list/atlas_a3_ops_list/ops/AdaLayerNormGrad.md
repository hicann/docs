# AdaLayerNormGrad

```c
REG_OP(AdaLayerNormGrad)
    .INPUT(dy, "T1")
    .INPUT(x, "T1")
    .INPUT(mean, "T2")
    .INPUT(rstd, "T2")
    .INPUT(scale, "T1")
    .INPUT(ln_res, "T1")
    .OUTPUT(dx, "T1")
    .OUTPUT(dshift, "T2")
    .OUTPUT(dscale, "T2")
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T2, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(AdaLayerNormGrad)
```

## Brief

AdaLayerNormGrad operator interface implementation
 calculating: dy, x, mean, rstd, scale, ln_res
 pd_xl = dy * (1 + scale)
 pd_var = np.sum(((-0.5)*pd_xl*(x - data_mean)
          np.power(rstd, 3)),
          reduce_axis, keepdims=True)
 pd_mean = np.sum(((-1.0)*pd_xl*rstd), reduce_axis, keepdims=True)
           + pd_var*(1.0/m)
           np.sum(((-2.0)*(x - data_mean)), reduce_axis, keepdims=True)
 dx = pd_xl*rstd +
        pd_var*(2.0/m)*(x - data_mean) + pd_mean*(1.0/m)
 dscale = np.sum(dy * ln_res, param_axis, keepdims=True)
 dshift = np.sum(dy, param_axis, keepdims=True) 

## Inputs

Six inputs, including:
- dy: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- x: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- mean: A Tensor. Must be one of the following types: float32.
- rstd: A Tensor. Must be one of the following types: float32.
- scale: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- ln_res: A Tensor. Must be one of the following types: float16, float32, bfloat16.

## Outputs

Three outputs, including:
- dx: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- dshift: A Tensor. Must be one of the following types: float32.
- dscale: A Tensor. Must be one of the following types: float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 rstd: float32
- input3 mean: float32
- input4 scale: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
