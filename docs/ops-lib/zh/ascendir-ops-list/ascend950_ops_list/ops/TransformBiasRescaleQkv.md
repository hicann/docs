# TransformBiasRescaleQkv

```c
REG_OP(TransformBiasRescaleQkv)
.INPUT(qkv, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
.INPUT(qkv_bias, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
.OUTPUT(q, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
.OUTPUT(k, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
.OUTPUT(v, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
.REQUIRED_ATTR (num_heads, Int)
.OP_END_FACTORY_REG(TransformBiasRescaleQkv)
```

## Brief

In Multi-Head Attention(MHA) computation, bias and rescale qkv tensor.

## Inputs

- qkv:  A 3D tensor. Type is:BFloat16, Float16 or Float32. Format support
ND. shape is (batch, token, 3 * num_heads * dim_per_head).
- qkv_bias: A 1D tensor. Type is:BFloat16, Float16 or Float32. Format support
ND. shape is (3 * num_heads * dim_per_head).

## Outputs

- q: A 4D tensor.Type is:BFloat16, Float16 or Float32. Format support
ND. shape is (batch, num_heads,token, dim_per_head).
- k: A 4D tensor.Type is:BFloat16, Float16 or Float32. Format support
ND. shape is (batch, num_heads,token, dim_per_head).
- v: A 4D tensor.Type is:BFloat16, Float16 or Float32. Format support
ND. shape is (batch, num_heads,token, dim_per_head).

## Attributes

num_heads: head nums. Type is Int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 qkv: bfloat16,float16,float32
- input1 qkv_bias: bfloat16,float16,float32
- output0 q: bfloat16,float16,float32
- output1 k: bfloat16,float16,float32
- output2 v: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
