# ViewCopy

```c
REG_OP(ViewCopy)
    .INPUT(dst, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(dst_size, TensorType::IndexNumberType())
    .INPUT(dst_stride, TensorType::IndexNumberType())
    .INPUT(dst_storage_offset, TensorType::IndexNumberType())
    .INPUT(src, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(src_size, TensorType::IndexNumberType())
    .INPUT(src_stride, TensorType::IndexNumberType())
    .INPUT(src_storage_offset, TensorType::IndexNumberType())
    .OUTPUT(dst, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .OP_END_FACTORY_REG(ViewCopy)
```

## Brief

Copy the src tensor to the dst tensor according the special parameter.
The function of ViewCopy operator is to copy the non-contiguous src tensor to the non-contiguous dst tensor, each defined respectively
by a quadruple of parameters: (src, src_storage_offset, src_stride, src_size) and (dst, dst_storage_offset, dst_stride, dst_size)
which both correspond to the term (tensor, storage_offset, view_stride, view_shape) and of course must satisfy the constraints regarding view_shape,
view_stride, and storage_offset for a valid tensor, details are as follows:
- The length of view_shape must equal the length of view_stride: len(view_shape) == len(view_stride).
- Each element in the tensor view_stride is non-negative.
- The storage_offset must be non-negative and not exceed the bounds of the tensor's size.
- All memory accesses must be legal; any element addressed by the view_shape and view_stride parameters must lie within the valid range of
the original tensor, in other words, for each axis i of view_stride, storage_offset + (view_shape[i] -1 ) * view_stride[i] <= total element num of tensor.

## Inputs

Eight inputs, including:
- dst: A tensor. Must be one of the following types:
float32, float16, bfloat16, int8, uint8, int16, uint16,
int32, uint32, int64, uint64, bool, hifloat8,
float8_e5m2, float8_e4m3fn.
- dst_size: A tensor, the view shape of dst tensor. Must be one of the following types: int32, int64, not negative.
- dst_stride: A tensor, the view stride of dst tensor. Must be one of the following types: int32, int64, not negative.
- dst_storage_offset: A tensor representing the storage offset of dst tensor. Must be one of the following types: int32, int64, not negative and can't out range of dst tensor.
- src: A tensor. Must be one of the following types:
float32, float16, bfloat16, int8, uint8, int16, uint16,
int32, uint32, int64, uint64, bool, hifloat8, float8_e5m2, float8_e4m3fn.
- src_size: A tensor, the view shape of src tensor. Must be one of the following types: int32, int64, not negative.
- src_stride: A tensor, the view stride of src tensor. Must be one of the following types: int32, int64, not negative.
- src_storage_offset: A tensor representing the storage offset of src tensor. Must be one of the following types:
int32, int64, not negative and can't out range of src tensor.

## Outputs

dst: An ref tensor. Must be one of the following types:
float32, float16, bfloat16, int8, uint8, int16, uint16,
int32, uint32, int64, uint64, bool, hifloat8, float8_e5m2, float8_e4m3fn.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dst: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 dst_size: int32,int64
- input2 dst_stride: int32,int64
- input3 dst_storage_offset: int32,int64
- input4 src: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input5 src_size: int32,int64
- input6 src_stride: int32,int64
- input7 src_storage_offset: int32,int64
- output0 dst: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 dst: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 dst_size: int32,int64
- input2 dst_stride: int32,int64
- input3 dst_storage_offset: int32,int64
- input4 src: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input5 src_size: int32,int64
- input6 src_stride: int32,int64
- input7 src_storage_offset: int32,int64
- output0 dst: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Attention Constraints

- dst_size and src_size must have same shape. For example: {'dst_size': (1, 199, 53, 3), 'src_size': (1, 199, 53, 3)}, for each axis i, dst_size[i] and src_size[i] is equal.
- The dst_size and dst_stride must have same dimension size. For example: {'dst_size': (192, 1, 16, 4), 'dst_stride': (80, 80, 5, 1)}, dst_size and dst_stride both have the same dimension size 4.
- The src_size and src_stride must have same dimension size. For example: {'src_size': (991, 1, 149), 'src_stride': (149, 149, 1)}, src_size and src_stride both have the same dimension size 3.
- For each axis i of dst_stride, the result: dst_storage_offset + (dst_size[i] - 1) * dst_stride[i] should less equal than dst tensor size.
- For each axis i of src_stride, the result: src_storage_offset + (src_size[i] - 1) * src_stride[i] should less equal than src tensor size.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
