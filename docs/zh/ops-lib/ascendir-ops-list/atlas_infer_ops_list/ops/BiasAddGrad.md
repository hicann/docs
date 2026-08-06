# BiasAddGrad

```c
REG_OP(BiasAddGrad)
    .INPUT(x, TensorType::NumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(BiasAddGrad)
```

## Brief

Performs the the backward operation for "BiasAdd" on the "bias" tensor.
       It accumulates all the values from out_backprop into the feature
       dimension. For NHWC data format, the feature dimension is the last.
       For NCHW data format, the feature dimension is the third-to-last .

## Inputs

x: A Tensor of type NumberType . 

## Outputs

y: A Tensor.Has the same type as "x" . 

## Attributes

data_format: A required attr. Data format. Defaults to "NHWC" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator BiasAddGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
