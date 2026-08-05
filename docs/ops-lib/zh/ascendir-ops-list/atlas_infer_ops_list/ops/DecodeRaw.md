# DecodeRaw

```c
REG_OP(DecodeRaw)
    .INPUT(bytes, TensorType({DT_STRING}))
    .OUTPUT(output, TensorType({DT_BOOL,DT_FLOAT16,DT_DOUBLE,DT_FLOAT,
                                    DT_INT64,DT_INT32,DT_INT8,DT_UINT8,DT_INT16,
                                    DT_UINT16,DT_COMPLEX64,DT_COMPLEX128}))
    .ATTR(out_type, Type, DT_FLOAT)
    .ATTR(little_endian, Bool, true)
    .OP_END_FACTORY_REG(DecodeRaw)
```

## Brief

Decodes raw file into tensor. 

## Inputs

bytes: A Tensor of type string.

## Outputs

Output: A Tensor.

## Attributes

- little_endian: An optional bool, default is true.
- out_type: An optional attribute, that indicates the output type. Defaults to float.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 bytes: string
- output0 output: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
