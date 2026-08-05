# Bitcast

```c
REG_OP(Bitcast)
    .INPUT(x, TensorType({DT_BOOL,       DT_FLOAT16, DT_FLOAT,  DT_INT4,   DT_INT8,    DT_INT32,  DT_UINT32,
                          DT_UINT8,      DT_INT64,   DT_UINT64, DT_INT16,  DT_UINT16,  DT_DOUBLE, DT_COMPLEX64,
                          DT_COMPLEX128, DT_QINT8,   DT_QUINT8, DT_QINT16, DT_QUINT16, DT_QINT32}))
    .OUTPUT(y, TensorType({DT_BOOL,       DT_FLOAT16, DT_FLOAT,  DT_INT4,   DT_INT8,    DT_INT32,  DT_UINT32,
                           DT_UINT8,      DT_INT64,   DT_UINT64, DT_INT16,  DT_UINT16,  DT_DOUBLE, DT_COMPLEX64,
                           DT_COMPLEX128, DT_QINT8,   DT_QUINT8, DT_QINT16, DT_QUINT16, DT_QINT32}))
    .REQUIRED_ATTR(type, Type)
    .ATTR(keep_dim, Bool, false)
    .OP_END_FACTORY_REG(Bitcast)
```

## Brief

This operation convert output dataType and shape.

## Inputs

The input handle must have the resource type. Inputs include:
x:A list of Tensor objects. One or more tensors from which
the enqueued tensors should be taken . 

## Outputs

y:A list of Tensor objects. One or more tensors from which
the enqueued tensors should be taken . 

## Attributes

type: An optional ge::DataType. It refers to the target data type of outputs . 
keepdim: If True, output dims equal intput dims. otherwise output dims can append. default value is false.  

## Third-party framework compatibility

Compatible with tensorflow QueueIsClosed operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
