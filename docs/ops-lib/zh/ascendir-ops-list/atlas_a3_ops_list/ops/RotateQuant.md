# RotateQuant

```c
REG_OP(RotateQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(rot, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(alpha, TensorType({DT_BF16}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT4, DT_FLOAT4_E2M1, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(scale, TensorType({DT_FLOAT32, DT_FLOAT8_E8M0}))
    .ATTR(y_dtype, Int, DT_INT8)
    .ATTR(axis, Int, -1)
    .ATTR(round_mode, String, "rint")
    .ATTR(scale_alg, Int, 0)
    .ATTR(dst_type_max, Float, 0.0)
    .ATTR(trans, Bool, false)
    .OP_END_FACTORY_REG(RotateQuant)
```

## Brief

Performs rotation transformation on the input tensor x using a rotation matrix,
followed by per-token symmetric dynamic quantization or per-group dynamic MX quantization. 

## Inputs

- x: A tensor. Input data for rotation and quantization.
Must be one of the following types: float16, bfloat16. The format supports ND.
- rot: A tensor. Rotation matrix.
Must be one of the following types: float16, bfloat16. Has the same type as input "x".
The format supports ND.
- alpha: A tensor. Optional scaling coefficient for clamp range limitation.
Only supported when y_dtype is float4_e2m1, float8_e4m3fn, or float8_e5m2. Not supported when y_dtype is int4 or int8.
Must be bfloat16. The format supports ND. 

## Outputs

- y: When the output data type is int4 or int8, the shape is [M, N].
When the output data type is float4_e2m1, float8_e4m3fn, or float8_e5m2, the shape is [M, N]. 
- scale: When the output data type is float32, the shape is [M].
When the output data type is float8_e8m0, the shape is [M, ceilDiv(N,64), 2]. 

## Attributes

- y_dtype: An optional int. Specifies the output data type of y. Defaults to DT_INT8.
- axis: An optional int. Specifies the axis for quantization. Defaults to -1.
- round_mode: An optional string. Specifies the rounding mode. Defaults to "rint".
- scale_alg: An optional int. Specifies the scale algorithm. Defaults to 0.
- dst_type_max: An optional float. Specifies the max value of destination type. Defaults to 0.0.
- trans: An optional bool. Specifies whether to transpose. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 rot: bfloat16,float16
- input2 alpha: bfloat16
- output0 y: int4,int8
- output1 scale: float32

## Constraints

Atlas A3 supports per-token dynamic quantization.Atlas A5 supports per-group dynamic MX quantization.
Atlas A3 Training Series Products/Atlas A3 Inference Series Products, Atlas A2 Training Series Products/Atlas A2
Inference Series Products, Atlas 950 Series Products: 
- x shape is [M, N], rot shape is [K, K]. rot must be a square matrix.
- N must be a multiple of K, and N must be divisible by 8.
- x and rot must have the same data type.
- scale output shape must be [M].
- N range: [128, 16000], K range: [16, 1024]. 
Atlas A5 Series Products:
- x is 1-D to 7-D, with the last dimension being N.
- rot shape is [K, K] or [blockNum, K, K], where blockNum = K/N, and N must divide K.
- x and rot must have the same data type.
- scale output shape is [*, ceilDiv(N,64), 2].
- K must be one of {32, 64, 128}. 
| x        | rot      | alpha | y              | scale       |
|----------|----------|-------|----------------|-------------|
| BF16     | BF16     | N/A   | INT4           | FLOAT32     |
| BF16     | BF16     | N/A   | INT8           | FLOAT32     |
| FLOAT16  | FLOAT16  | N/A   | INT4           | FLOAT32     |
| FLOAT16  | FLOAT16  | N/A   | INT8           | FLOAT32     |
| FLOAT16  | FLOAT16  | BF16  | FLOAT4_E2M1    | FLOAT8_E8M0 |
| BF16     | BF16     | BF16  | FLOAT4_E2M1    | FLOAT8_E8M0 |
| FLOAT16  | FLOAT16  | BF16  | FLOAT8_E4M3FN  | FLOAT8_E8M0 |
| BF16     | BF16     | BF16  | FLOAT8_E4M3FN  | FLOAT8_E8M0 |
| FLOAT16  | FLOAT16  | BF16  | FLOAT8_E5M2    | FLOAT8_E8M0 |
| BF16     | BF16     | BF16  | FLOAT8_E5M2    | FLOAT8_E8M0 |


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
