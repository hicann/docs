# DynamicQuantUpdateScatterV2

```c
REG_OP(DynamicQuantUpdateScatterV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(indices, TensorType({DT_INT32}))
    .INPUT(var, TensorType({DT_INT4}))
    .INPUT(var_scale, TensorType({DT_FLOAT}))
    .INPUT(var_offset, TensorType({DT_FLOAT}))
    .OUTPUT(var, TensorType({DT_INT4}))
    .OUTPUT(var_scale, TensorType({DT_FLOAT}))
    .OUTPUT(var_offset, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(DynamicQuantUpdateScatterV2)
```

## Brief

Multiplies dynamic asymmetric quantize and sparse updates into a variable reference.

## Inputs

Five inputs, including:
- x: A tensor which layout need to be setted BSH. Shape is (B, 1, H).
The type support float16, bfloat16, format support ND.
- indices: A 1D tensor with shape (B). Indices of scatter. The type support int32, format support ND.
- var: A tensor with shape (B, S, 1, H). Target tensor to which the quantization results are scattered.
The type support int4, format support ND.
- var_scale: A tensor with shape (B, S). Target tensor to which the quantization scales are scattered.
The type support float32, format support ND.
- var_offset: A tensor with shape (B, S). Target tensor to which the quantization offsets are scattered.
The type support float32, format support ND.

## Outputs

- var: A tensor with shape (B, S, H). Result tensor after an in-place scatter.
The type support int4, format support ND.
- var_scale: A tensor with shape (1, B, S). Result tensor after an in-place scatter.
The type support float32, format support ND.
- var_offset: A tensor with shape (1, B, S). Result tensor after an in-place scatter.
The type support float32, format support ND.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 indices: int32
- input2 var: int4
- input3 var_scale: float32
- input4 var_offset: float32
- output0 var: int4
- output1 var_scale: float32
- output2 var_offset: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
