# Shrink

```c
REG_OP(Shrink)
    .INPUT(input_x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(output_y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(lambd, Float, 0.5)
    .ATTR(bias, Float, 0.0)
    .OP_END_FACTORY_REG(Shrink)
```

## Brief

Calculate the shrink function.

## Inputs

One inputs, including:
- input_x: A tensor. Must be one of the following types:
    float16, float32. 

## Outputs

y: A Tensor with the same dtype and shape of input_x's. 

## Attributes

- lambd: An optional float. Defaults to 0.5.
- bias: An optional float. Defaults to 0.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: float16,float32
- output0 output_y: float16,float32

## Third-party framework compatibility

Compatible with the ONNX operator Shrink. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
