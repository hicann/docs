# BiasAdd

```c
REG_OP(BiasAdd)
    .INPUT(x, TensorType::NumberType())
    .INPUT(bias, TensorType::NumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(BiasAdd)
```

## Brief

Adds 'bias' to 'x'. Support broadcasting operations.

## Inputs

Two inputs, including:
- x: A ND tensor of type NumberType, format list [ND, NCHW, NHWC, NCDHW, NDHWC].
Must be one of the following types: float32, float64, int32, uint8, int16,
int8, complex64, int64, qint8, quint8, qint32, bfloat16, uint16, complex128, float16, uint32, uint64.
- bias: A 1D tensor with size the C dimension of x:
when x format is NCHW or NCDHW, C dimension is x.shape[1]. 
When x format is NHWC or NDHWC, C dimension is x.shape[-1]. 
when x format is ND and data_format is in [NCHW, NCDHW], C dimension is x.shape[1]. 
when x format is ND and data_format is in [NHWC, NDHWC], C dimension is x.shape[-1]. 

## Outputs

y: A ND tensor with same type and shape and format as "x". 

## Attributes

data_format: An optional string. Defaults to "NHWC". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 bias: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator BiasAdd.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
