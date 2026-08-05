# MlaPrologV2

```c
REG_OP(MlaPrologV2)
.INPUT(token_x, TensorType({DT_INT8, DT_BF16}))
.INPUT(weight_dq, TensorType({DT_INT8, DT_BF16}))
.INPUT(weight_uq_qr, TensorType({DT_INT8, DT_BF16}))
.INPUT(weight_uk, TensorType({DT_FLOAT16, DT_BF16}))
.INPUT(weight_dkv_kr, TensorType({DT_INT8, DT_BF16}))
.INPUT(rmsnorm_gamma_cq, TensorType({DT_FLOAT16, DT_BF16}))
.INPUT(rmsnorm_gamma_ckv, TensorType({DT_FLOAT16, DT_BF16}))
.INPUT(rope_sin, TensorType({DT_FLOAT16, DT_BF16}))
.INPUT(rope_cos, TensorType({DT_FLOAT16, DT_BF16}))
.INPUT(cache_index, TensorType({DT_INT64}))
.INPUT(kv_cache, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
.INPUT(kr_cache, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
.OPTIONAL_INPUT(dequant_scale_x, TensorType({DT_FLOAT}))
.OPTIONAL_INPUT(dequant_scale_w_dq, TensorType({DT_FLOAT}))
.OPTIONAL_INPUT(dequant_scale_w_uq_qr, TensorType({DT_FLOAT}))
.OPTIONAL_INPUT(dequant_scale_w_dkv_kr, TensorType({DT_FLOAT}))
.OPTIONAL_INPUT(quant_scale_ckv, TensorType({DT_FLOAT}))
.OPTIONAL_INPUT(quant_scale_ckr, TensorType({DT_FLOAT}))
.OPTIONAL_INPUT(smooth_scales_cq, TensorType({DT_FLOAT}))
.OUTPUT(query, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
.OUTPUT(query_rope, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
.OUTPUT(kv_cache, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
.OUTPUT(kr_cache, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
.OUTPUT(dequant_scale_q_nope, TensorType({DT_FLOAT}))
.ATTR(rmsnorm_epsilon_cq, Float, 1e-05)
.ATTR(rmsnorm_epsilon_ckv, Float, 1e-05)
.ATTR(cache_mode, String, "PA_BSND")
.OP_END_FACTORY_REG(MlaPrologV2)
```

## Inputs

- token_x: A matrix tensor. The type support int8 and bfloat16.
- weight_dq: A matrix tensor. The downsampling weight matrix of query. The type support int8 and bfloat16.
- weight_uq_qr: A matrix tensor. The upsampling and positional encoding weight matrix of query.
The type support int8 and bfloat16.
- weight_uk: A matrix tensor. The second upsampling weight matrix of query. The type support float16 and bfloat16.
- weight_dkv_kr: A matrix tensor. The upsampling and positional encoding weight matrix of key.
The type support int8 and bfloat16.
- rmsnorm_gamma_cq: A matrix tensor. The gamma factor for the rmsnorm of query. The type support float16 and bfloat16.
- rmsnorm_gamma_ckv: A matrix tensor. The gamma factor for the rmsnorm of key. The type support float16 and bfloat16.
- rope_sin: A matrix tensor. The position encoding sin information of each token. The type support float16 and bfloat16.
- rope_cos: A matrix tensor. The position encoding cos information of each token. The type support float16 and bfloat16.
- cache_index: A matrix tensor. The index of the cache in each batch. The type support int64.
- kv_cache: A matrix tensor, representing the cache of kv matrix. The type support float16 and bfloat16 and int8.
- kr_cache: A matrix tensor, representing the cache of kv postion embedding matrix. The type support float16 and bfloat16 and int8.
- dequant_scale_x: A matrix tensor. This parameter is used for dequantization after downsampling when tokenX is of the int8 type. The quantization mode of tokenX is per-token.
The type support float32.
- dequant_scale_w_dq: A matrix tensor. This parameter is used for dequantization after downsampling when tokenX is of the int8 type. The quantization mode is per-channel.
The type support float32.
- dequant_scale_w_uq_qr: A matrix tensor. Parameter used for dequantization after matrix multiplication during dynamic quantization of MatmulQcQr.
The type support float32.
- dequant_scale_w_dkv_kr: A matrix tensor. This parameter is used for quantization after MatmulCkvKr when tokenX is of the int8 type.
The type support float32.
- quant_scale_ckv: A matrix tensor. Parameter used for quantizing the RmsNormCkv output. The parameter is aclTensor on the device side.
The type support float32.
- quant_scale_ckr: A matrix tensor. This parameter is used for quantizing the RoPEKr output. It is aclTensor on the device side.
The type support float32.
- smooth_scales_cq: A matrix tensor. Smoothquant parameter required for dynamic quantization of RmsNormDq output.

## Outputs

- query: A matrix tensor, representing the query for Multi-Head Latent Attention. The type support float16 and bfloat16 and int8.
- query_rope: A matrix tensor, representing the position embedding of query. The type support float16 and bfloat16 and int8.
- kv_cache: A matrix tensor, representing the updated kv cache. This parameter uses the same memory of kv_cache. The type support float16 and bfloat16 and int8.
- kr_cache: A matrix tensor, representing the updated kr cache. This parameter uses the same memory of kr_cache. The type support float16 and bfloat16 and int8.
- dequant_scale_q_nope: A matrix tensor, representing the dequant weights for query if query is quantilized. The type support float32.

## Attributes

- rmsnorm_epsilon_cq: An optional float32. The epsilon factor for the rmsnorm of query. Default: 1e-5.
- rmsnorm_epsilon_ckv: An optional float32. The epsilon factor for the rmsnorm of key. Default: 1e-5.
- cache_mode: An optional int. The mode of kvcache. The type support PA_NZ and PA_BSND. Default: PA_BSND.
PA stands for page attention. This means kv_cache and kr_cache are stored in the page attention format, and updated by the order of BSND or NZ.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 token_x: bfloat16,int8
- input1 weight_dq: bfloat16,int8
- input2 weight_uq_qr: bfloat16,int8
- input3 weight_uk: bfloat16
- input4 weight_dkv_kr: bfloat16,int8
- input5 rmsnorm_gamma_cq: bfloat16
- input6 rmsnorm_gamma_ckv: bfloat16
- input7 rope_sin: bfloat16
- input8 rope_cos: bfloat16
- input9 cache_index: int64
- input10 kv_cache: bfloat16,int8
- input11 kr_cache: bfloat16,int8
- input12 dequant_scale_x: float32
- input13 dequant_scale_w_dq: float32
- input14 dequant_scale_w_uq_qr: float32
- input15 dequant_scale_w_dkv_kr: float32
- input16 quant_scale_ckv: float32
- input17 quant_scale_ckr: float32
- input18 smooth_scales_cq: float32
- output0 query: bfloat16,int8
- output1 query_rope: bfloat16
- output2 kv_cache: bfloat16,int8
- output3 kr_cache: bfloat16,int8
- output4 dequant_scale_q_nope: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
