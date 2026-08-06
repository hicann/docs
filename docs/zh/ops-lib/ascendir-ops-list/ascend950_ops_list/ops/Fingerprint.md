# Fingerprint

```c
REG_OP(Fingerprint)
    .INPUT(data, TensorType({DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16, \
              DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .INPUT(method, TensorType({DT_STRING}))
    .OUTPUT(y, TensorType({DT_UINT8}))
    .OP_END_FACTORY_REG(Fingerprint)
```

## Brief

Generates fingerprint values. 

## Inputs

- data: Must have rank 1 or higher.
- method: Fingerprint method used by this op. Currently available method is
`farmhash::fingerprint64`. 

## Outputs

y: A two-dimensional `Tensor` of type `tf.uint8`. The first dimension equals to
`data`'s first dimension, and the second dimension size depends on the
fingerprint algorithm. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 data: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 method: string
- output0 y: uint8

## Third-party framework compatibility

Compatible with TensorFlow Fingerprint operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
