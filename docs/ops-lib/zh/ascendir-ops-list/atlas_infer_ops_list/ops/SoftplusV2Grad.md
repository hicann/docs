# SoftplusV2Grad

```c
REG_OP(SoftplusV2Grad)
    .INPUT(input_gradients, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(input_features, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .OUTPUT(output_backprops, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .ATTR(beta, Float, 1.0)
    .ATTR(threshold, Float, 20.0)
    .OP_END_FACTORY_REG(SoftplusV2Grad)
```

## Brief

Calculates the reversed outputs of the function "softplus_v2".

## Inputs

Two inputs, including:
- input_gradients: A mutable tensor, which supports 1D-8D defaultly. Format support ND.
Must be one of the following types: float16, float32, bfloat16.
- input_features: A mutable tensor of the same type, shape and format as "input_gradients".

## Outputs

output_backprops: A mutable tensor of the same type, shape and format as "input_gradients".

## Attributes

- beta: An optional float. Defaults to "1.0".
Control the steepness of the beta function.
- threshold: An optional float. Defaults to "20.0".
Define a function to switch the threshold from nonlinear to linear.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_gradients: float16,float32
- input1 input_features: float16,float32
- output0 output_backprops: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator SoftplusGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
