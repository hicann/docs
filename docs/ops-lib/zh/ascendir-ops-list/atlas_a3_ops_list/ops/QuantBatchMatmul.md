# QuantBatchMatmul

```c
REG_OP(QuantBatchMatmul)
    .INPUT(x1, TensorType({DT_INT8}))
    .INPUT(x2, TensorType({DT_INT8}))
    .INPUT(deq_scale, TensorType({DT_UINT64}))
    .OPTIONAL_INPUT(bias, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16}))
    .ATTR(adj_x1, Bool, false)
    .ATTR(adj_x2, Bool, false)
    .OP_END_FACTORY_REG(QuantBatchMatmul)
```

## Brief

Quant Batch Matmul Calculation.

## Inputs

Four inputs:
- x1: A matrix Tensor. The format support ND. The shape ranges from 2D to 3D,
with the same dimensions as that of x2.
Must be one of the following types: int8. Boardcasting is not supported between x1 and x2.
The data types of x1 and x2 must meet the deduction relationship.
The shape is (batch,m,k), where batch is optional.
- x2: A matrix Tensor. The format support ND. The shape ranges from 2D to 3D,
with the same dimensions as that of x1.
Must be one of the following types: int8. Boardcasting is not supported between x1 and x2.
The data types of x1 and x2 must meet the deduction relationship.
The shape is (batch,k,n), where batch is optional.
- deq_scale: A quantization parameter Tensor. The format support ND. Must be one of the following types: uint64.
- bias: A 1D optional matrix Tensor. The format support ND.
The shape is (n,), where n is the same as that of x2. Must be one of the following types: int32. 

## Outputs

y: A matrix Tensor. Must be one of the following types: float16.
The format support ND. The shape must be deduced from x1 and x2.
The shape is (batch,m,n), where batch is optional. 

## Attributes

- adj_x1: A bool. If true, changes the shape of "x1" from [m, k] to
[k, m] before multiplication. Default: false.
- adj_x2: A bool. If true, changes the shape of "x2" from [k, m] to
[m, k] before multiplication. Default: false. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: int8
- input1 x2: int8
- input2 deq_scale: uint64
- input3 bias: int32
- output0 y: float16

## Attention Constraints

1. The data type, format, or shape of x1, x2, bias and out should be supported.
2. Data type deduction can be performed for x1 and x2.
3. The input shapes of x1 adn x2 must meet the matrix multiplication relationship.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
