# ScaleAndTranslate

```c
REG_OP(ScaleAndTranslate)
    .INPUT(images, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
                               DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(size, TensorType({DT_INT32}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(translation, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(kernel_type, String, "lanczos3")
    .ATTR(antialias, Bool, true)
    .OP_END_FACTORY_REG(ScaleAndTranslate)
```

## Brief

Resizes "images" to "size" by scale and translate . 

## Inputs

- images: A `Tensor`. Must be one of the following types: `int8`, `uint8`,
`int16`, `uint16`, `int32`, `int64`, `bfloat16`, `float32`, `float64`.
- size: A `Tensor` of type `int32`.
- scale: A `Tensor` of type `float32`.
- translation: A `Tensor` of type `float32` .

## Outputs

y: A Tensor with type float32 . 

## Attributes

- kernel_type: type is string, default is lanczos3.
- antialias: type is bool, default is true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 size: int32
- input2 scale: float32
- input3 translation: float32
- output0 y: float32

## Third-party framework compatibility

Compatible with TensorFlow ScaleAndTranslate operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
