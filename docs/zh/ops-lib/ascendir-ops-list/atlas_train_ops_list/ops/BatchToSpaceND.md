# BatchToSpaceND

```c
REG_OP(BatchToSpaceND)
    .INPUT(x, TensorType({BasicType(), DT_BOOL}))
    .INPUT(block_shape, TensorType::IndexNumberType())
    .INPUT(crops, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL}))
    .OP_END_FACTORY_REG(BatchToSpaceND)
```

## Brief

Permutes data from batch into blocks of spatial data and then prunes them.
The values from the batch dimension are moved in spatial blocks to the height and width dimensions.
And then prunes the height and width dimensions.

## Inputs

- x: A ND tensor, must be one of the following types:
float16, float32, double, int64, int32, uint8, uint16, uint32, uint64, int8,
int16, complex64, complex128, qint8, quint8, qint16, quint16, qint32, bfloat16.
- block_shape: A 1D tensor with shape [M], support int32 or int64.
- crops: A 2D tensor with shape [M, 2], support int32 or int64.

## Outputs

y: A ND tensor, the same type as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 block_shape: int32,int64
- input2 crops: int32,int64
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 block_shape: int32,int64
- input2 crops: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Attention Constraints

If N is 4 and M is 2: 
The size of the first dimension of input "x" must be divisible by the product of all elements in block_shape. 
"y" is a 4D shape [batch, height, width, depth], batch = x.shape[0] / (block_shape[0] * block_shape[1]),
depth = x.shape[3], height = height_pad - crop_top - crop_bottom, width = width_pad - crop_left - crop_right
where height_pad = x.shape[1] * block_shape[0], width_pad = x.shape[2] * block_shape[1],
crop_top = crops[0][0], crop_bottom = crops[0][1], crop_left = crops[1][0], crop_right = crops[1][1]

## Third-party framework compatibility

Compatible with the TensorFlow operator BatchToSpaceND.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
