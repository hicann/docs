# ScatterPaKvCache

```c
REG_OP(ScatterPaKvCache)
    .INPUT(key, "T")
    .INPUT(key_cache, "T")
    .INPUT(slot_mapping, TensorType::IndexNumberType())
    .INPUT(value, "T")
    .INPUT(value_cache, "T")
    .OPTIONAL_INPUT(compress_lens, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(compress_seq_offset, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(seq_lens, TensorType::IndexNumberType())
    .OUTPUT(key_cache, "T")
    .OUTPUT(value_cache, "T")
    .ATTR(cache_mode, String, "Norm")
    .ATTR(scatter_mode, String, "None")
    .ATTR(strides, ListInt, {1,1})
    .ATTR(offsets, ListInt, {0,0})
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_UINT8, DT_INT16,
                            DT_UINT16, DT_INT32, DT_UINT32, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
.OP_END_FACTORY_REG(ScatterPaKvCache)
```

```c
When cache_mode is "Norm" or None, the dtype of key, value, key_cache and value_cache dtype must be same.
When key is a 3D tensor, shape and value limit like:
shape limit:
key:[batch * seqLen, num_head, k_head_size]
key_cache:[num_blocks, block_size, num_head, k_head_size]
slot_mapping:[batch * seqLen]
value:[batch * seqLen, num_head, v_head_size]
value_cache:[num_blocks, block_size, num_head, v_head_size]
value limit:
slot_mapping in range [0, num_blocks * block_size - 1]
batch * seqLen <= num_blocks * block_size
value in slot_mapping must be unique
When key is a 4D tensor and compress_seq_offset is not None, shape and value limit like:
shape limit:
key:[batch, seqLen, num_head, k_head_size]
key_cache:[num_blocks, block_size, 1, k_head_size]
slot_mapping:[batch, num_head]
value:[batch, seqLen, num_head, v_head_size]
value_cache:[num_blocks, block_size, 1, v_head_size]
compress_lens: [batch, num_head]
compress_seq_offset:[batch*num_head]
seq_lens:[batch]
value limit:
slot_mapping in range [0, num_blocks * block_size - 1]
reduceSum(seqLen - compress_lens + 1) <= num_blocks * block_size
compress_lens[b][i] + compress_seq_offset[b*i] < seq_lens[b]
seq_lens[b] < seqLen
0 < compress_lens[b][i] <= seq_lens[b] - compress_seq_offset[b*i]
0 <= compress_seq_offset[b*i] < seq_lens[b] - compress_seq_offset[b*i]
value in slot_mapping must be unique
When key is a 4D tensor and compress_seq_offset is None, shape and value limit like:
shape limit:
key:[batch, seqLen, num_head, k_head_size]
key_cache:[num_blocks, block_size, 1, k_head_size]
slot_mapping:[batch, num_head]
value:[batch, seqLen, num_head, v_head_size]
value_cache:[num_blocks, block_size, 1, v_head_size]
compress_lens: [batch * num_head]
seq_lens:[batch]
value limit:
slot_mapping in range [0, num_blocks * block_size - 1]
reduceSum(compress_lens) <= num_blocks * block_size
compress_lens[b][i] < seq_lens[b]
seq_lens[b] <= seqLen
compress_lens[b][i] > 0
value in slot_mapping must be unique
When cache_mode is "PA_NZ", the dtype of key and key_cache, value and value_cache dtype must be same, shape and value limit like:
shape limit:
key:[batch * seqLen, num_head, k_head_size]
key_cache:[num_blocks, num_head * k_head_size / last_dim_k, block_size, last_dim_k]
slot_mapping:[batch * seqLen]
value:[batch * seqLen, num_head, v_head_size]
value_cache:[num_blocks, num_head * v_head_size / last_dim_v, block_size, last_dim_v]
value limit:
slot_mapping in range [0, num_blocks * block_size - 1]
batch * seqLen <= num_blocks * block_size
value in slot_mapping must be unique
```

## Brief

Update the key and value to the corresponding cache based on the index. 

## Inputs

Inputs including:
- key: Key values to be updated,A 3D or 4D tensor.
- key_cache: Tensors that need to be updated by key.
- slot_mapping: The offset of each token, key, or value in the cache. Must be one of the following types: int32 or int64.
- value: Key values to be updated.
- value_cache: Tensors that need to be updated by value.
- compress_lens: Compression amount. Must be one of the following types: int32 or int64.
- compress_seq_offset: Compression starting point for each batch and head. Must be one of the following types: int32 or int64.
- seq_lens: Actual seq_len for each batch. Must be one of the following types: int32 or int64.

## Outputs

- key_cache: Tensors that need to be updated by key.
- value_cache: Tensors that need to be updated by value.

## Attributes

- cache_mode: An optional attribute. Describing the format of cache. Defaults to "Norm".
This attribute field is only applicable to the Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component 
and Atlas A3 Training Series Product/Atlas A3 Inference Series Product; other products can only take the default value.
- If "PA_NZ"(Paged Attention NZ Format), the format of key_cache and value_cache is NZ.
- If "Norm" or None, the format of key_cache and value_cache is ND.
- scatter_mode: An optional attribute. Describing the format of cache. Defaults to "None".
This attribute field is only applicable to the Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component 
and Atlas A3 Training Series Product/Atlas A3 Inference Series Product; other products can only take the default value.
- If "Alibi", key and value will compress by alibi mode.
- If "Rope", key and value will compress by Rope mode.
- If "Omni", key and value will compress by Omni mode.
- If "Nct", key and value will be uncontiguous.
- If "None" or None, key and value will update normally.
- strides: An optional attribute. A list of 2 integers. The stride of the key and value, its' shape is [stride_k, stride_v].
This attribute field is only applicable to the Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component 
and Atlas A3 Training Series Product/Atlas A3 Inference Series Product; other products can only take the default value.
- offsets: An optional attribute. A list of 2 integers. The offsets of the key and value, its' shape is [offset_k, offset_v].
This attribute field is only applicable to the Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component 
and Atlas A3 Training Series Product/Atlas A3 Inference Series Product; other products can only take the default value.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 key: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32
- input1 key_cache: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32
- input2 slot_mapping: int32,int64
- input3 value: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32
- input4 value_cache: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32
- input5 compress_lens: int32,int64
- input6 compress_seq_offset: int32,int64
- input7 seq_lens: int32,int64
- output0 key_cache: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32
- output1 value_cache: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32


---

[Back to Operator Specifications (Ascend950)](../README.md)
