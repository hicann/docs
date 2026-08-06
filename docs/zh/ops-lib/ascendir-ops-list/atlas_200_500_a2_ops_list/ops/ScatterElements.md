# ScatterElements

```c
REG_OP(ScatterElements)
    .INPUT(data, TensorType({NumberType(),DT_FLOAT8_E5M2,DT_FLOAT8_E4M3FN,DT_FLOAT8_E8M0}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({NumberType(),DT_FLOAT8_E5M2,DT_FLOAT8_E4M3FN,DT_FLOAT8_E8M0}))
    .OUTPUT(y, TensorType({NumberType(),DT_FLOAT8_E5M2,DT_FLOAT8_E4M3FN,DT_FLOAT8_E8M0}))
    .ATTR(axis, Int, 0)
    .ATTR(reduction, String, "none")
    .OP_END_FACTORY_REG(ScatterElements)
```

## Brief

Uses "updates" to update tensor "data" by "indices". 

## Inputs

Three inputs, including:
- data: A ND Tensor .
Must be one of the following types: complex128, complex64, double, float32, float16, int16, int32, int64, int8,
qint32, qint8, quint8, uint16, uint32, uint64, uint8, bfloat16, complex32.
- indices: An ND Tensor of type int32 or int64, its value shoule be less than the numbers of elements in the
data target axis.
- updates: An Tensor. Same shape as indices. format:NCHW, NHWC .
Must be one of the following types: complex128, complex64, double, float32, float16, int16, int32, int64, int8,
qint32, qint8, quint8, uint16, uint32, uint64, uint8, bfloat16, complex32.

## Outputs

y: A Tensor. Has the same type and format as input "data" . 

## Attributes

- axis: An optional int. Defaults to 0.
- reduction: An optional string. Defaults to string "none" and can be
"add" or "mul". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 data: float16,float32,int8,int32,uint8
- input1 indices: int32,int64
- input2 updates: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
### AI CPU
- input0 data: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- input2 updates: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component and
Atlas A3 Training Series Product/Atlas A3 Inference Series Product,
you are advised to replace ScatterElements with ScatterElementsV2(When there are duplicate indexes, ScatterElementsV2 provides higher precision). 

## Third-party framework compatibility

Compatible with the ONNX operator ScatterElements.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
