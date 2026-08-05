# BNInference

```c
REG_OP(BNInference)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(mean, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(variance, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(momentum, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(scale, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(epsilon, Float,1e-5f)
    .ATTR(use_global_stats, Bool,true)
    .ATTR(mode, Int,1)
    .OP_END_FACTORY_REG(BNInference)
```

## Brief

Performs batch normalization .

## Inputs

- x: A 4D or 5D Tensor of type float16 or float32 or bfloat16, with format NHWC or NCHW.
- mean: A 1D Tensor of type float32 or float16 or bfloat16, the shape is same as dim C of input x.
Specifies the mean used for inference.
- variance: A 1D Tensor of type float32 or float16 or bfloat16, the shape is same as dim C of input x.
Specifies the variance used for inference.
- momentum: A 1D Tensor of type float32 or float16 or bfloat16, the shape is same as dim C of input x.
represents the mean and the variance's scale factor
- scale: An optional 1D tensor of type float16 or float32 or bfloat16, the shape is same as dim C of input x.
- offset: An optional 1D tensor of type float16 or float32 or bfloat16, the shape is same as dim C of input x.

## Outputs

- y: A 4D or 5D Tensor of type float16 or float32 or bfloat16 for the normalized "x"

## Attributes

- epsilon: An optional float32, specifying the small value added to variance to avoid dividing by zero.
Defaults to "0.00001".
- use_global_stats: An optional bool, mean inference mode, only can be "True".
- mode: An optional int, defaults to "1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 mean: float16,float32
- input2 variance: float16,float32
- input3 momentum: float16,float32
- input4 scale: float16,float32
- input5 offset: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
