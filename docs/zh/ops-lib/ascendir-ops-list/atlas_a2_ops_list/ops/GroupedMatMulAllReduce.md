# GroupedMatMulAllReduce

```c
REG_OP(GroupedMatMulAllReduce)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .DYNAMIC_INPUT(weight, TensorType({DT_FLOAT16, DT_BF16}))
    .DYNAMIC_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(group_list, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .ATTR(splitItem, Int, 0)
    .REQUIRED_ATTR(group, String)
    .ATTR(reduceOp, String, "sum")
    .ATTR(commTurn, Int, 0)
    .OP_END_FACTORY_REG(GroupedMatMulAllReduce)
```

## Brief

Function GroupedMatMulAllReduce. This op computes multi groups of matmuls on multi-cards environment.

## Inputs

- x: A Tensor List, contains all left matrixs of inputs for matmuls. For each tensor, the data type of elements supports float16 or bfloat16; the format supports ND. The maximum length allowed is 64.
32B-aligned size of each dim should be smaller than 2147483647. The size of inner axis should be smaller than 65536.
- weight: A Tensor List of weight, contains all right matrixs of inputs for matmul. For each tensor, the data type of elements supports float16 or bfloat16; the format supports ND. The maximum length allowed is 64.
32B-aligned size of each dim should be smaller than 2147483647. The size of inner axis should be smaller than 65536.
- bias: A Tensor List of bias, contains all bias of inputs for matmul. For each tensor, the data type of elements supports float16 or float32; the format supports ND. The maximum length allowed is 64.
- group_list: a Tensor, indicates M-axis distributation of groups of matmuls for inputs and outputs.
Data type of elements is int64. Format: ND. The maximum length allowed is 64.

## Outputs

y: A Tensor List, contains all result of groups of matmuls. For each tensor,
the data type of elements supports float16 or bfloat16; the format supports ND. The maximum length allowed is 64.

## Attributes

- splitItem: An int64, indicates whether do tensor split for inputs and outputs.
0: no split for inputs and outputs; 1: inputs need tensor split; 2: outputs need tensor split;
3: both inputs and outputs need tensor split. Default value is 0.
- group: A string. A required String identifying the group of ranks.
- reduceOp: A string. A required string identifying the reduction operation to
perform. support "sum".
- commTurn: An int64. Number of communications with AICPU. Default: 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 weight: bfloat16,float16
- input2 bias: float16,float32
- input3 group_list: int64
- output0 y: bfloat16,float16

## Attention Constraints

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
