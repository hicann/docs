# RotaryPositionEmbedding

```c
REG_OP(RotaryPositionEmbedding)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(cos, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(sin, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OPTIONAL_INPUT(rotate, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .ATTR(mode, Int, 0)
    .OP_END_FACTORY_REG(RotaryPositionEmbedding)
```

## Brief

Apply rotary position embedding for a single tensor.

## Inputs

- x: A 4D tensor which rotary position embedding is applied, format supports ND, and data type must be float16, float or bfloat16.
- cos: A 4D tensor which is "cos" in rotary position embedding, format supports ND, data type must be the same as "x", and shape must be the same as "sin".
- sin: A 4D tensor which is "sin" in rotary position embedding, format supports ND, data type must be the same as "x", and shape must be the same as "cos".
- rotate: An optional 2D tensor which is the transformation matrix for position transformation of the "x" in rotary position embedding,
format supports ND, data type must be the same as "x", both dimensions are the same and equal to the last dimension of "x", rotate does not support back propagation.

## Outputs

y: A 4D tensor which is the result of rotary position embedding, format supports ND, data type must be the same as "x", and shape must be the same as "x".

## Attributes

mode: An optional attribute of type int, specifying the mode of rotary position embedding, must be 0-"half", 1-"interleave", 2-"quarter" or 3-"interleave-half". Defaults to 0.
Atlas A2 Training Series Product/ Atlas 800I A2 Inference Product and Atlas A3 Training Series Product only support 0-"half" and 1-"interleave".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 cos: bfloat16,float16,float32
- input2 sin: bfloat16,float16,float32
- input3 rotate: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

Let (B, S, N, D) represents the shape of the 4-D input "x". Under this representation, the shape constraints of each parameter can be described as follows:
- The D of "x", "cos", "sin", "rotate" and "y" must be equal. For Ascend 950 AI Processor, D should be less or equal to 1024.
For Atlas A2 Training Series Product/ Atlas 800I A2 Inference Product and Atlas A3 Training Series Product, D should be less or equal to 896.
- In half, interleave and interleave-half mode, D must be a multiple of 2. In quarter mode, D must be a multiple of 4.
- B, S, N of "cos" and "sin" must meet one of the following four conditions:
 - B, S, N are 1, means the shape is (1, 1, 1, D).
 - B, S, N are the same as that of "x", means the shape is (B, S, N, D).
 - One of S and N is 1, the remaining one dimension and B are the same as that of "x", means the shape is (B, 1, N, D) or (B, S, 1, D).
 - Two of B, S and N are 1, the remaining one dimension is the same as that of "x", means the shape is (1, 1, N, D), (1, S, 1, D) or (B, 1, 1, D).
 - The shape for rotate should be (D, D).


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
