# MhcSinkhorn

```c
REG_OP(MhcSinkhorn)
    .INPUT(h_res, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OUTPUT(norm_out, TensorType({DT_FLOAT}))
    .OUTPUT(sum_out, TensorType({DT_FLOAT}))
    .ATTR(eps, Float, 1.00e-06)
    .ATTR(num_iters, Int, 20)
    .ATTR(out_flag, Int, 0)
    .OP_END_FACTORY_REG(MhcSinkhorn)
```

## Brief

Perform the Sinkhorn normalization on the input tensor h_res to generate
a doubly stochastic matrix, and compute related normalization and summation results.

## Inputs

- h_res: A Tensor of type Float32. Input matrix to be normalized by Sinkhorn algorithm.

## Outputs

- y: A Tensor of type Float32. The doubly stochastic matrix generated after Sinkhorn normalization.
- norm_out: A Tensor of type Float32. Normalization factor tensor computed during the iteration process.
- sum_out: A Tensor of type Float32. Summation result tensor of the normalized matrix rows/columns.

## Attributes

- eps: Float type, default value 1.00e-06. A small epsilon value to prevent division by zero during normalization.
- num_iters: Int type, default value 20. Number of iteration steps for the Sinkhorn-Knopp algorithm. Range: [1,
100].
- out_flag: Int type, default value 0. Control flag for output mode (0: basic output, 1: extended output,
etc.).Currently, only value 0 is supported in this version.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 h_res: float32
- output0 y: float32
- output1 norm_out: float32
- output2 sum_out: float32

## Description

This operator implements the Sinkhorn-Knopp algorithm to iteratively normalize
the rows and columns of the input matrix h_res, making it close to a doubly stochastic matrix.
It outputs the normalized matrix, normalization factor, and summation result based on configuration.


---

[Back to Operator Specifications (Ascend950)](../README.md)
