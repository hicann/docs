# ScatterPaCache

```c
REG_OP(ScatterPaCache)
    .INPUT(key, "T")
    .INPUT(key_cache, "T")
    .INPUT(slot_mapping, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(compress_lens, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(compress_seq_offset, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(seq_lens, TensorType::IndexNumberType())
    .OUTPUT(key_cache, "T")
    .ATTR(cache_mode, String, "Norm")
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_UINT8, DT_INT16,
                            DT_UINT16, DT_INT32, DT_UINT32, DT_HIFLOAT8, DT_FLOAT8_E5M2,
                            DT_FLOAT8_E4M3FN, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
.OP_END_FACTORY_REG(ScatterPaCache)
```

```c
The dtype of key and key_cache must be same.
When key is a 3D tensor, shape and value limit like:
shape limit:
key:[batch * seqLen, num_head, k_head_size]
key_cache:[num_blocks, block_size, num_head, k_head_size]
slot_mapping:[batch * seqLen]
value limit:
slot_mapping in range [0, num_blocks * block_size - 1]
batch * seqLen <= num_blocks * block_size
value in slot_mapping must be unique
When key is a 4D tensor and compress_seq_offset is not None, shape and value limit like:
shape limit:
key:[batch, seqLen, num_head, k_head_size]
key_cache:[num_blocks, block_size, 1, k_head_size]
slot_mapping:[batch, num_head]
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
compress_lens: [batch * num_head]
seq_lens:[batch]
value limit:
slot_mapping in range [0, num_blocks * block_size - 1]
reduceSum(compress_lens) <= num_blocks * block_size
compress_lens[b][i] < seq_lens[b]
seq_lens[b] <= seqLen
compress_lens[b][i] > 0
value in slot_mapping must be unique
```

## Brief

Update the key to the corresponding cache based on the index. 

## Inputs

Inputs including:
- key: Key values to be updated,A 3D or 4D tensor.
- key_cache: Tensors that need to be updated by key.
- slot_mapping: The offset of each token of key in the cache. Must be one of the following types: int32 or int64.
- compress_lens: Compression amount. Must be one of the following types: int32 or int64.
- compress_seq_offset: Compression starting point for each batch and head. Must be one of the following types: int32 or int64.
- seq_lens: Actual seq_len for each batch. Must be one of the following types: int32 or int64.

## Outputs

- key_cache: Tensors that need to be updated by key.

## Attributes

cache_mode: An optional attribute. Reserved parameter, not effective now. Describing the format of cache. Defaults to "Norm".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 key: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32
- input1 key_cache: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32
- input2 slot_mapping: int32,int64
- input3 compress_lens: int32,int64
- input4 compress_seq_offset: int32,int64
- input5 seq_lens: int32,int64
- output0 key_cache: bfloat16,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,uint8,uint16,uint32


---

[Back to Operator Specifications (Ascend950)](../README.md)
