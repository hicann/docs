# BNInfer

```c
REG_OP(BNInfer)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(offset, TensorType({DT_FLOAT}))
    .INPUT(mean, TensorType({DT_FLOAT}))
    .INPUT(variance, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(epsilon, Float)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(BNInfer)
```

## Brief

Performs batch normalization for inference .

## Inputs

Five inputs, including:
- x: A 4D tensor of type float16 or float32 or bfloat16, with format NHWC or NCHW.
- scale: A 1D tensor of type float32, for the scaling factor, the shape is same as dim C of input x.
- offset: A 1D tensor of type float32, for the scaling offset, the shape is same as dim C of input x.
- mean: A 1D tensor of type float32, for the mean, the shape is same as dim C of input x.
- variance: A 1D tensor of type float32, for the variance, the shape is same as dim C of input x.

## Outputs

y: A 4D tensor of type float16 or float32 or bfloat16 for the normalized "x", with format NHWC or NCHW. 

## Attributes

epsilon: An optional float32, specifying the small value added to variance to
avoid dividing by zero. Defaults to "0.0001" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 scale: float32
- input2 offset: float32
- input3 mean: float32
- input4 variance: float32
- output0 y: float16,float32

## Attention Constraints

For Atlas 200/300/500 Inference Product, the result accuracy fails to reach 1/1000 due to the
square root instruction.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
