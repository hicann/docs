# MatmulEmuSplitWeight

```c
REG_OP(MatmulEmuSplitWeight)
    .INPUT(x, TensorType({DT_BF16}))
    .INPUT(w_high, TensorType({DT_BF16}))
    .INPUT(w_low, TensorType({DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(w_low_scale, Float, 0.00390625)
    .ATTR(transpose_x, Bool, false)
    .ATTR(transpose_w, Bool, false)
    .ATTR(y_dtype, Int, 0)
    .OP_END_FACTORY_REG(MatmulEmuSplitWeight)
```

## Brief

Performs dual-path BF16 GEMM fusion to simulate FP32 precision matrix multiplication.
The FP32 weight is split offline into a high-bit BF16 weight and a low-bit residual BF16 weight.
At inference time, two BF16 GEMMs are executed and linearly combined. 

## Inputs

- x: A tensor. Activation matrix.
The types supports bfloat16. The format supports ND.
- w_high: A tensor. High-bit weight, obtained by truncating FP32 weight to BF16.
The types supports bfloat16. Has the same type as input "x".
The format supports ND.
- w_low: A tensor. Low-bit residual weight, obtained by dividing the residual by scale and truncating to BF16.
Must be one of the following types: bfloat16. Has the same type as input "x".
The shape must be identical to w_high. The format supports ND. 

## Outputs

- y: A tensor. Output matrix.
The types supports float32. The format supports ND. 

## Attributes

- w_low_scale: A required float. Scale factor for the low-bit residual weight. Defaults to 0.00390625 (1/256).
- transpose_x: An optional bool. Specifies whether to transpose input x. Defaults to false.
- transpose_w: An optional bool. Specifies whether to transpose weights w_high/w_low. Defaults to false.
- y_dtype: A required int. Specifies the output data type of y. 0 for FP32. Defaults to 0.
| x     | w_high | w_low | y      |
|-------|--------|-------|--------|
| BF16  | BF16   | BF16  | FLOAT  |

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16
- input1 w_high: bfloat16
- input2 w_low: bfloat16
- output0 y: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
