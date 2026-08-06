# RopeWithSinCosCache

```c
REG_OP(RopeWithSinCosCache)
      .INPUT(positions, TensorType({DT_INT32, DT_INT64}))
      .INPUT(queryIn, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
      .INPUT(keyIn, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
      .INPUT(cosSinCache, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
      .OUTPUT(queryOut, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
      .OUTPUT(keyOut, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
      .REQUIRED_ATTR(numQHeads, Int)
      .REQUIRED_ATTR(numKHeads, Int)
      .REQUIRED_ATTR(headSize, Int)
      .ATTR(mropeSection, ListInt, {0,0,0})
      .ATTR(qStride, Int, 0)
      .ATTR(kStride, Int, 0)
      .ATTR(isNeoxStyle, Bool, true)
      .OP_END_FACTORY_REG(RopeWithSinCosCache)
```

## Brief

RopeWithSinCosCache.

## Inputs

- positions: A tensor of type int32 of int64.
- queryIn: A tensor of type float, bf16, float16.
- keyIn: A tensor of type float, bf16, float16.
- cosSinCache: A tensor of type float, bf16, float16.

## Outputs

- queryOut: A tensor of type FP16/FP32/BF16.
- keyOut: A tensor of type FP16/FP32/BF16.

## Attributes

- numQHeads: A int attr.
- numKHeads: A int attr.
- headSize: A int attr.
- mropeSection: A ListInt attr.
- qStride: A int attr.
- KStride: A int attr.
- isNeoxStyle: A bool attr.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 positions: int64
- input1 queryIn: bfloat16,float16,float32
- input2 keyIn: bfloat16,float16,float32
- input3 cosSinCache: bfloat16,float16,float32
- output0 queryOut: bfloat16,float16,float32
- output1 keyOut: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
