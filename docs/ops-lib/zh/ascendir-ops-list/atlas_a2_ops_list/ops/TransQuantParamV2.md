# TransQuantParamV2

```c
REG_OP(TransQuantParamV2)
    .INPUT(scale, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_UINT64}))
    .ATTR(round_mode, Int, 0)
    .OP_END_FACTORY_REG(TransQuantParamV2)
```

## Brief

Transfer quant param from float32 to uint64.

## Inputs

- scale: A quantization parameter tensor. Must be one of the following types: float32.
The format support ND. The shape support 1D and 2D.
- offset: An optional quantization parameter tensor. Must be one of the following types: float32.
The format support ND. The shape support 1D and 2D. 

## Outputs

- y: output tensor. Must be one of the following types: uint64. The format support ND.
The shape support 1D and 2D. 

## Attributes

- round_mode: fp32 filing to fp19 mode; 0: truncation and filing; 1: r_int mode;

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 scale: float32
- input1 offset: float32
- output0 y: uint64

## Attention Constraints

- The passed scale, y cannot be a null pointer.
- Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product or Atlas Inference Series Product or
Ascend 950 AI Processor: 
This operator supports use with the matmul operator, such as QuantBatchMatmulV3. 
- Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product or Atlas Inference Series Product: 
This operator does not supports use with the grouped matmul operator, such as GroupedMatmul. 
- When there is no offset, the y shape is consistent with the scale shape:
- If y is used as matmul input(e.g., QuantBatchMatmulV3), the shape support 1D (t,), with t equal to 1 or n, or 2D(1, n),
where n is the same as that of the right matrix in the matmul calculation. 
- If y is used as grouped matmul input(e.g., GroupedMatmul), the shape support 1D (g,), or 2D(g, n), (g, 1),
where n is the same as that of the right matrix in the grouped matmul calculation, g is the same as that of
the number of group num(i.e., group_list parameter's shape). 
- When there is an offset, use it only as matmul input (e.g., QuantBatchMatmulV3):
The shape of scale, offet and y support 1D (t,), with t equal to 1 or n, or 2D(1, n), where n is the same as
that of the right matrix in the matmul calculation.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
