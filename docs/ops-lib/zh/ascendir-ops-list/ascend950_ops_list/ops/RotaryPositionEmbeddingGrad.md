# RotaryPositionEmbeddingGrad

```c
REG_OP(RotaryPositionEmbeddingGrad)
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(cos, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(sin, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OPTIONAL_INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OUTPUT(dcos, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OUTPUT(dsin, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .ATTR(mode, Int, 0)
    .OP_END_FACTORY_REG(RotaryPositionEmbeddingGrad)
```

## Brief

Backwards calculation of RotaryPositionEmbedding.

## Inputs

- dy: A 4D tensor which represents the gradient of output "y" in RotaryPositionEmbedding, format supports ND, and data type must be float16, float or bfloat16.
- cos: A 4D tensor which is input "cos" in RotaryPositionEmbedding, format supports ND, data type must be the same as "dy", and shape must be the same as "sin".
- sin: A 4D tensor which is input "sin" in RotaryPositionEmbedding, format supports ND, data type must be the same as "dy", and shape must be the same as "cos".
- x: An optional 4D tensor which is input "x" in RotaryPositionEmbedding, format supports ND, data type must be the same as "dy", and shape must be the same as "dy".
If "x" is nullptr, the output "dcos" and "dsin" is meaningless.

## Outputs

- dx: A 4D Tensor which is the grad of input "x" in RotaryPositionEmbedding, format supports ND, data type must be the same as "dy", and shape must be the same as "dy".
- dcos: A 4D Tensor which is the grad of input "cos" in RotaryPositionEmbedding, format supports ND, data type must be the same as "dy", and shape must be the same as "cos".
- dsin: A 4D Tensor which is the grad of input "sin" in RotaryPositionEmbedding, format supports ND, data type must be the same as "dy", and shape must be the same as "sin".

## Attributes

mode: An optional attribute of type int, specifying the mode of rotary position embedding, must be 0-"half", 1-"interleave", 2-"quarter" or 3-"interleave-half". Defaults to 0.
Atlas A2 Training Series Product/ Atlas 800I A2 Inference Product and Atlas A3 Training Series Product only support 0-"half" and 1-"interleave".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 cos: bfloat16,float16,float32
- input2 sin: bfloat16,float16,float32
- input3 x: bfloat16,float16,float32
- output0 dx: bfloat16,float16,float32
- output1 dcos: bfloat16,float16,float32
- output2 dsin: bfloat16,float16,float32

## Attention Constraints

Let (B, S, N, D) represents the shape of the 4-D input "dy". Under this representation, the shape constraints of each parameter can be described as follows:
- The D of "dy", "cos", "sin", "x", "dx", "dcos" and "dsin" must be equal. For Ascend 950 AI Processor, D should be less or equal to 1024.
For Atlas A2 Training Series Product/ Atlas 800I A2 Inference Product and Atlas A3 Training Series Product, D should be less or equal to 896.
- In half, interleave and interleave-half mode, D must be a multiple of 2. In quarter mode, D must be a multiple of 4.
- B, S, N of "cos", "sin", "dcos" and "dsin" must meet one of the following four conditions:
 - B, S, N are 1, means the shape is (1, 1, 1, D).
 - B, S, N are the same as that of "dy", means the shape is (B, S, N, D).
 - One of S and N is 1, the remaining one dimension and B are the same as that of "dy", means the shape is (B, 1, N, D) or (B, S, 1, D).
 - Two of B, S and N are 1, the remaining one dimension is the same as that of "dy", means the shape is (1, 1, N, D), (1, S, 1, D) or (B, 1, 1, D).


---

[Back to Operator Specifications (Ascend950)](../README.md)
