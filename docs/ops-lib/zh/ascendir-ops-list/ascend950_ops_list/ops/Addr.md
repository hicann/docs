# Addr

```c
REG_OP(Addr)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_BOOL}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_BOOL}))
    .INPUT(x3, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_BOOL}))
    .INPUT(beta, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_BOOL}))
    .INPUT(alpha, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_BOOL}))
    .OP_END_FACTORY_REG(Addr)
```

## Brief

Add x1 and the outer product of x2 and x3.

## Inputs

- x1: A 2D tensor with data type float32, float16, bfloat16, int8, uint8, bool, which can be broadcasted.
Shape after broadcasting must be same with the outer product of x2 and x3.
Supported format list ["ND"].
- x2: A 1D tensor with data type float32, float16, bfloat16, int8, uint8, bool. Supported format list ["ND"].
- x3: A 1D tensor with data type float32, float16, bfloat16, int8, uint8, bool. Supported format list ["ND"].
- beta: A tensor of data type float32, float16, bfloat16, int8, uint8, bool with only one data.
Supported format list ["ND"].
- alpha: A tensor of data type float32, float16, bfloat16, int8, uint8, bool with only one data.
Supported format list ["ND"].

## Outputs

y:  A 2D tensor.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,bool,float16,float32,int8,uint8
- input1 x2: bfloat16,bool,float16,float32,int8,uint8
- input2 x3: bfloat16,bool,float16,float32,int8,uint8
- input3 beta: bfloat16,bool,float16,float32,int8,uint8
- input4 alpha: bfloat16,bool,float16,float32,int8,uint8
- output0 y: bfloat16,bool,float16,float32,int8,uint8

## Third-party framework compatibility

Compatible with the ONNX operator ConstantOfShape.


---

[Back to Operator Specifications (Ascend950)](../README.md)
