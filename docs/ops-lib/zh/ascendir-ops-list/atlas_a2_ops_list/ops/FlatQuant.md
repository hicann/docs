# FlatQuant

```c
REG_OP(FlatQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(kronecker_p1, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(kronecker_p2, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(out, TensorType({DT_INT4, DT_FLOAT4_E2M1}))
    .OUTPUT(quant_scale, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
    .ATTR(clip_ratio, Float, 1)
    .ATTR(dst_dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(FlatQuant)
```

## Brief

Flatness matters for LLM quantization. 

## Inputs

- x: A tensor. The original data input. 3-D with shape [K, M, N]. Must be one of the following types:
float16, bfloat16. The format support ND.
- kronecker_p1: A tensor. Input calculation matrix 1. 2-D with shape [M, M]. The value of M is same as input "x".
Must be one of the following types: float16, bfloat16. Has the same type as input "x".
The format support ND.
- kronecker_p2: A tensor. Input calculation matrix 2. 2-D with shape [N, N]. The value of N is same as input "x".
Must be one of the following types: float16, bfloat16. Has the same type as input "x".
The format support ND. 

## Outputs

- out: A 3-D tensor of type int4. Output result data. Shape is same as input "x". The format support ND.
- quant_scale: A tensor of type float32. Output quantization factor. 1-D with shape [K].
The value of K is same as input "x". The format support ND. 

## Attributes

clip_ratio: An optional float. Used to control the quantization cropping ratio. Defaults to 1. 
dst_dtype: An optional int. Used to control the quantization dst_type. Defaults to DT_INT32, which is 3. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 kronecker_p1: bfloat16,float16
- input2 kronecker_p2: bfloat16,float16
- output0 out: int4
- output1 quant_scale: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
