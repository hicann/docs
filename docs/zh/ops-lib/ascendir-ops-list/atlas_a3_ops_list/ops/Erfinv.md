# Erfinv

```c
REG_OP(Erfinv)
    .INPUT(input_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(output_y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(Erfinv)
```

## Brief

Computes the inverse error function of each element of input.

## Inputs

One inputs, including:
input_x: A tensor. Must be one of the following types:
    float16, float32, bfloat16. 

## Outputs

output_y: A ND Tensor with the same dtype and shape of input_x's. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: bfloat16,float16,float32
- output0 output_y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the PyTorch operator Erfinv. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
