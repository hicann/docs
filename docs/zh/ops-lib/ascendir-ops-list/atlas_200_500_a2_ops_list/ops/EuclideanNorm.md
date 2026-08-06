# EuclideanNorm

```c
REG_OP(EuclideanNorm)
    .INPUT(x, TensorType::NumberType())
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(keep_dims, Bool, false)
    .OP_END_FACTORY_REG(EuclideanNorm)
```

## Brief

Computes the Euclidean norm along the given axes:
       y = sqrt( sum( x^2 ) along axes )

## Inputs

Two inputs, including:
- x: A ND tensor of type NumberType.
Must be one of the following types: float32, float64, int32, uint8, int16,
int8, complex64, int64, qint8, quint8, qint32, bfloat16, uint16, complex128, float16, uint32, uint64.
- axes: An IndexNumberType tensor (int32/int64), 1-D, listing the axes to reduce.

## Outputs

y: A tensor with the same dtype as x. Output shape is derived from x's shape,
   axes, and keep_dims.

## Attributes

keep_dims: Optional bool, default false. If true, the reduced axes are
           retained as size-1 dimensions in the output.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- input1 axes: int32,int64
- output0 y: float16,float32,int32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 axes: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator tf.math.reduce_euclidean_norm.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
