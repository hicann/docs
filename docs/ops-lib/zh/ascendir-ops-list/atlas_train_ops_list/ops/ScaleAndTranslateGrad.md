# ScaleAndTranslateGrad

```c
REG_OP(ScaleAndTranslateGrad)
    .INPUT(grads, TensorType({DT_FLOAT}))
    .INPUT(original_image, TensorType({DT_FLOAT}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(translation, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(kernel_type, String, "lanczos3")
    .ATTR(antialias, Bool, true)
    .OP_END_FACTORY_REG(ScaleAndTranslateGrad)
```

## Brief

Computes the gradient by scale and translate . 

## Inputs

- grads: A `Tensor`. Must be one of the following types: `float32`.
- original_image: A `Tensor`. Must have the same type as `grads`.
- scale: A `Tensor` of type `float32`.
- translation: A `Tensor` of type `float32` .

## Outputs

y: A `Tensor`. Has the same type as `grads` . 

## Attributes

- kernel_type: type is string, default is lanczos3.
- antialias: type is bool, default is true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 grads: float32
- input1 original_image: float32
- input2 scale: float32
- input3 translation: float32
- output0 y: float32

## Third-party framework compatibility

Compatible with TensorFlow ScaleAndTranslateGrad operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
