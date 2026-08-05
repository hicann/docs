# ScatterElementsV2

```c
REG_OP(ScatterElementsV2)
    .INPUT(var, TensorType({DT_FLOAT,DT_FLOAT16,DT_INT16,DT_INT32,DT_INT64,DT_INT8,DT_UINT8,DT_BF16,DT_FLOAT8_E5M2,DT_FLOAT8_E4M3FN,DT_FLOAT8_E8M0}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_FLOAT,DT_FLOAT16,DT_INT16,DT_INT32,DT_INT64,DT_INT8,DT_UINT8,DT_BF16,DT_FLOAT8_E5M2,DT_FLOAT8_E4M3FN,DT_FLOAT8_E8M0}))
    .OUTPUT(var, TensorType({DT_FLOAT,DT_FLOAT16,DT_INT16,DT_INT32,DT_INT64,DT_INT8,DT_UINT8,DT_BF16,DT_FLOAT8_E5M2,DT_FLOAT8_E4M3FN,DT_FLOAT8_E8M0}))
    .ATTR(axis, Int, 0)
    .ATTR(reduction, String, "none")
    .OP_END_FACTORY_REG(ScatterElementsV2)
```

## Brief

Uses "updates" to update tensor "var" by "indices". 

## Inputs

Three inputs, including:
- var: An ND Tensor .
Must be one of the following types: float32, float16, int16, int32, int64, int8, uint8, bfloat16.
- indices: An ND Tensor of type int32 or int64
- updates: An ND Tensor .
Must be one of the following types: float32, float16, int16, int32, int64, int8, uint8, bfloat16.

## Outputs

var: A Tensor. Has the same type and format as input "var" . 

## Attributes

- axis: An optional int. Defaults to 0.
- reduction: An optional string. Defaults to string "none" and can be
"add" or "mul". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,bool,float16,float32,int8,int32,uint8
- input1 indices: int32,int64
- input2 updates: bfloat16,bool,float16,float32,int8,int32,uint8
- output0 var: bfloat16,bool,float16,float32,int8,int32,uint8

## Attention Constraints

- In non-last axis scenarios, you are advised to convert x, indices, and updates to the last axes,
use ScatterElementsV2 for calculation, and then convert them to the original axes.
- Only Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component and
Atlas A3 Training Series Product/Atlas A3 Inference Series Product support ScatterElementsV2. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
