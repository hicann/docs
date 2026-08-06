# GatherPaKvCache

```c
REG_OP(GatherPaKvCache)
    .INPUT(key_cache, "T")
    .INPUT(value_cache, "T")
    .INPUT(block_tables, TensorType::IndexNumberType())
    .INPUT(seq_lens, TensorType::IndexNumberType())
    .INPUT(key, "T")
    .INPUT(value, "T")
    .OPTIONAL_INPUT(seq_offset, TensorType::IndexNumberType())
    .OUTPUT(key, "T")
    .OUTPUT(value, "T")
    .ATTR(cache_mode, String, "Norm")
    .ATTR(is_seq_lens_cumsum, Bool, true)
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_UINT8, DT_INT16,
                            DT_UINT16, DT_INT32, DT_UINT32, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
.OP_END_FACTORY_REG(GatherPaKvCache)
```

```c
 - key_cache/value_cache/key/value share the same data type.
 - block_tables/seq_lens/seq_offset share the same data type.

Shape constraints in "Norm" mode:
  key_cache:     [num_blocks, block_size, num_heads, head_size_k]
  value_cache:   [num_blocks, block_size, num_heads, head_size_v]
  block_tables:  [batch, block_indices]
  seq_lens:      [batch] (if is_seq_lens_cumsum=false) or [batch + 1] (if is_seq_lens_cumsum=true)
  key:           [num_tokens, num_heads, head_size_k]
  value:         [num_tokens, num_heads, head_size_v]
  seq_offset:    [batch] (optional)

Shape constraints in "PA_NZ" mode:
  key_cache:     [num_blocks, (num_heads * head_size_k) / elenum_aligned, block_size, elenum_aligned]
  value_cache:   [num_blocks, (num_heads * head_size_v) / elenum_aligned, block_size, elenum_aligned]
  block_tables:  [batch, block_indices]
  seq_lens:      [batch] or [batch + 1]
  key:           [num_tokens, num_heads * head_size_k]
  value:         [num_tokens, num_heads * head_size_v]
  seq_offset:    [batch] (optional)

Special note for PA_NZ mode: enum_aligned has 3 possible values, which depend on the bit-width of key_cache/value_cache data type.
      b8  (8 bits = 1 byte): elenum_aligned = 32
      b16 (16 bits = 2 bytes): elenum_aligned = 16
      b32 (32 bits = 4 bytes): elenum_aligned = 8

block_tables constraints: All elements in block_tables must be in range [0, num_blocks).
seq_lens constraints: All elements in seq_lens must be ≥ 0.

```

## Brief

Gather the key and value from the corresponding cache based on the block tables and sequence lengths. 
       This operation is typically used in Paged Attention (PA) to retrieve cached key-value pairs for variable-length sequences. 

## Inputs

Inputs including:
- key_cache: Key cache tensor. The format and the shape depends on cache_mode.
  - The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
    and Atlas A3 Training Series Product/Atlas A3 Inference Series Product: The format is ND.
  - Ascend 950 AI Processor: Supports the ND (cache_mode = "Norm") and FRACTAL_NZ (cache_mode = "PA_NZ") data formats.
- value_cache: Value cache tensor. The format and the shape depends on cache_mode.
  - The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
    and Atlas A3 Training Series Product/Atlas A3 Inference Series Product: The format is ND.
  - Ascend 950 AI Processor: Supports the ND (cache_mode = "Norm") and FRACTAL_NZ (cache_mode = "PA_NZ") data formats.
- block_tables: Tensor mapping logical blocks to physical blocks in each batch.
  - Data types: int32, int64.
  - format: ND
- seq_lens: Tensor for sequence lengths for each batch.
  - Data types: int32, int64.
  - format: ND
- key: Tensor for gathered key values. Shape depends on cache_mode.
  - The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
    and Atlas A3 Training Series Product/Atlas A3 Inference Series Product: The format is ND.
  - Ascend 950 AI Processor: The format is ND.
- value: Tensor for gathered value values. Shape depends on cache_mode.
  - The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
    and Atlas A3 Training Series Product/Atlas A3 Inference Series Product: The format is ND.
  - Ascend 950 AI Processor: The format is ND.
- seq_offset: Optional. Starting offset for each sequence in the block_tables. Shape: [batch].
  - Data types: int32, int64.
  - format: ND

## Outputs

- key: Gathered key values from the cache, which is same as the input key.
- value: Gathered value values from the cache, which is same as the input value.

## Attributes

- cache_mode: An optional attribute describing the format of key_cache/value_cache. Valid values: "Norm" (default) or "PA_NZ".
- is_seq_lens_cumsum: An optional boolean attribute indicating whether `seq_lens` is provided as cumulative sum. Defaults to true.
  - If true, `seq_lens` has shape [batch + 1], where `seq_lens[i+1] - seq_lens[i]` gives the length of the i-th sequence.
  - If false, `seq_lens` has shape [batch], directly providing the length of each sequence.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 key_cache: bfloat16,float16,int8
- input1 value_cache: bfloat16,float16,int8
- input2 block_tables: int32
- input3 seq_lens: int32
- input4 key: bfloat16,float16,int8
- input5 value: bfloat16,float16,int8
- input6 seq_offset: int32
- output0 key: bfloat16,float16,int8
- output1 value: bfloat16,float16,int8


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
