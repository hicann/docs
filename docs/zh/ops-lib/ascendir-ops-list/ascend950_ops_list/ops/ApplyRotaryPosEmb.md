# ApplyRotaryPosEmb

```c
REG_OP(ApplyRotaryPosEmb)
    .INPUT(query, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(key, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(cos, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(sin, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .ATTR(layout, Int, 1)
    .ATTR(rotary_mode, String, "half")
    .OUTPUT(query,TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OUTPUT(key,TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OP_END_FACTORY_REG(ApplyRotaryPosEmb)
```

## Brief

Apply rotary position embedding.

## Inputs

- query: A tensor for transformer query. Must be one of the following types: float16, float32, bfloat16.
- key: A tensor for transformer key. Must be one of the following types: float16, float32, bfloat16.
- cos: A tensor for rotary position embedding cos. Must be one of the following types: float16, float32, bfloat16.
- sin: A tensor for rotary position embedding sin. Must be one of the following types: float16, float32, bfloat16.

## Outputs

- query: A tensor for transformer query. Has the same shape as "query".
- key: A tensor for transformer key. Has the same shape as "key".

## Attributes

- layout: Optional.Explanation input format. 1-"BSND" 2-"SBND" 3-"BNSD". Defaults to 1.
- rotary_mode: Optional.Explanation rotary mode. Support "half","interleave","quarter". Defaults to "half".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16,float16,float32
- input1 key: bfloat16,float16,float32
- input2 cos: bfloat16,float16,float32
- input3 sin: bfloat16,float16,float32
- output0 query: bfloat16,float16,float32
- output1 key: bfloat16,float16,float32

## Attention Constraints

- Inputs  tensor of query, key, cos, sin must be 4D.
- query, key must be the same except for the N dimension, the shape of sin and cos must be the same.
- The B dimension of cos and sin must be consistent with query and key or equal to 1.
- The S dimension of query, key, sin, cos must be the same.
- The N dimension of cos and sin must be equal to 1.
- The D dimension of query, key, sin, cos must be the same and not greater than 1024.
- The dtype of input tensor query, key, sin, cos must be the same.
- When the rotary_mode is "half" or "interleave", the D dimension must be divisible by 2.
when the rotary_mode is "quarter", the D dimension must be divisible by 4
- Atlas Inference Series Product and Atlas Trainning Series Product:
- support types: float16, float32.
- support layout: not support.
- support rotary_mode: not support.
- Atlas A2 Training Series Product/ Atlas 800I A2 Inference Product and Atlas A3 Training Series Product:
- support types: float16, float32.
- support layout: 1.
- support rotary_mode: not support.
- Ascend 950 AI Processor
- support types: float16, float32, bfloat16.
- support layout: 1, 2, 3.
- support rotary_mode: "half","interleave","quarter".


---

[Back to Operator Specifications (Ascend950)](../README.md)
