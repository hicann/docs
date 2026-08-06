# AddLora

```c
REG_OP(AddLora)
    .INPUT(y, TensorType({DT_FLOAT16}))
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(weightB, TensorType({DT_FLOAT16}))
    .INPUT(indices, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(weightA, TensorType({DT_FLOAT16}))
    .ATTR(layer_idx, Int, 0)
    .ATTR(scale, Float, 1e-3)
    .ATTR(y_offset, Int, 0)
    .ATTR(y_slice_size, Int, -1)
    .OUTPUT(y_out, TensorType({DT_FLOAT16}))
    .OP_END_FACTORY_REG(AddLora)
```

## Brief

AddLora, the operation kernel for batch gather matmul.

## Inputs

- y: A tensor. Indicates the tensor to be updated by accumulation. The data type is float16. Shape dimension is 2D: [B, H3].
Supported format "ND". The first dimension needs to be consistent with the first dimension of x, both represented by B.
- x: A tensor. Input tensor before grouping. Data type supports float16. Shape dimension is 2D: [B, H1],
where H1 is a multiple of 16. Supported format "ND".
- weightB: A weight tensor of type float16. Supported format "ND". Represents the second weight matrix for matrix multiplication.
Shape dimension is 4D: [W, L, H2, R]. The third dimension needs to be smaller than the second dimension of y (H2<H3),
and H2 is an integer multiple of 16.
- indices: A tensor. Indicates the group index of the input x. The data type is int32. Shape dimension is 1D: [B],
which must be the same as the first dimension of x and y. Both of them are represented by B. Supported format "ND".
- weightA: A optional weight tensor of type float16. Indicates the first weight matrix for matrix multiplication.
If the value is null, the first matrix multiplication is skipped.
Shape dimension is 4D: [W, L, R, H1]. The first two dimensions must be consistent with the first two dimensions of weightB,
which are represented by W and L. The third dimension must be consistent with the fourth dimension of weightB,
and both dimensions are represented by R. The fourth dimension must be the same as the second dimension of x,
both are represented by H1, and must be an integer multiple of 16. Supported format "ND".

## Outputs

y_out: A tensor of type float16, the shape requirements are consistent with the shape of y.
The shape dimension is two dimensions. Supported format "ND". Has the same as type as y.

## Attributes

- layer_idx: A optional int, default value is 0, indicates the layer id of weight tensors.
The value must be less than the second dimension L of weightB.
- scale: A optional float, default value is 1e-3, scales up the multiplication results.
- y_offset: A optional int, default value is 0,  represents the offset of y.
The value needs to be less than the second dimension H3 of y.
- y_slice_size: A optional int, default value is -1, represents the slice_size of y to be updated.
The value needs to be less than the second dimension H3 of y.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: float16
- input1 x: float16
- input2 weightB: float16
- input3 indices: int32
- input4 weightA: float16
- output0 y_out: float16


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
