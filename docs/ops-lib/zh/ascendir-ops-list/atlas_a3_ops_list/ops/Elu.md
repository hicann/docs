# Elu

```c
REG_OP(Elu)
    .INPUT(x, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
    .ATTR(alpha, Float, 1.0)
    .ATTR(scale, Float, 1.0)
    .ATTR(input_scale, Float, 1.0)
    .OP_END_FACTORY_REG(Elu)
```

## Brief

Activation function fused from sigmoid and ReLU, with soft saturation
on the left and no saturation on the right .

## Inputs

x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types: bfloat16, float16, float32.

## Outputs

y: A bfloat16, float16, float32, for the normalized result.
Has the same type, shape and format as input x.

## Attributes

- alpha: An optional float32. Defines at which negative value the ELU saturates. Defaults to "1.0".
- scale: An optional float32. Input data scaling factor. Defaults to "1.0".
- input_scale: An optional float32. Negative data scaling factor. Defaults to "1.0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: bfloat16,double,float16,float32
- output0 y: bfloat16,double,float16,float32

## Third-party framework compatibility

- Compatible with Tensorflow's Elu operator
- Compatible with Caffe's ELULayer operator
- Compatible with Pytorch's elu Opeartor


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
