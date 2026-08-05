# SplitV

```c
REG_OP(SplitV)
    .INPUT(x, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT16,
                          DT_INT32, DT_INT64, DT_INT8, DT_QINT16, DT_QINT32, DT_QINT8,
                          DT_QUINT16, DT_QUINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8,
                          DT_BF16, DT_BOOL, DT_STRING}))
    .INPUT(size_splits, TensorType::IndexNumberType())
    .INPUT(split_dim, TensorType({DT_INT32, DT_INT64}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT16,
                                   DT_INT32, DT_INT64, DT_INT8, DT_QINT16, DT_QINT32, DT_QINT8,
                                   DT_QUINT16, DT_QUINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8,
                                   DT_BF16, DT_BOOL, DT_STRING}))
    .REQUIRED_ATTR(num_split, Int)
    .OP_END_FACTORY_REG(SplitV)
```

## Brief

Splits a tensor along dimension "split_dim" into "num_split"
smaller tensors according to "size_splits" .

## Inputs

Three inputs, including:
- x: An ND Tensor.
Must be one of the types:float16, float32, double, int64, int32, uint8,
uint16, uint32, uint64, int8, int16, bool, complex64, complex128, qint8,
quint8, qint16, quint16, qint32, string, bfloat16.
- size_splits: Must be one of the IndexNumberType:int32, int64.
Specifies a list containing the sizes of each output tensor along the split dimension.
The elements in "size_splits" sum to the size of dimension "split_dim".
- split_dim: Must be the following type:int32, int64. Specifies the
dimension along which to split. Must be in the range [-len(x.shape), len(x.shape)) . 

## Outputs

- y:  Dynamic output.A list of output tensors.
Has the same type and format as "x" . 

## Attributes

- num_split: A required int includes all types of int. Specifies the number of output tensors.
No default value . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- input1 size_splits: int32,int64
- input2 split_dim: int32,int64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
### AI CPU
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- input1 size_splits: int32,int64
- input2 split_dim: int32

## Attention Constraints

- Each element in "size_splits" is greater than or equal to 1.
- The length of "size_splits" is equal to the value of "num_split".
- The elements in "size_splits" sum to the size of dimension "split_dim" .

## Third-party framework compatibility

Compatible with the TensorFlow operator SplitV.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
