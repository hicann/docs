# MedianDim

```c
REG_OP(MedianDim)
        .INPUT(self, TensorType({ DT_FLOAT, DT_FLOAT16 }))
        .OUTPUT(valuesOut, TensorType({ DT_FLOAT, DT_FLOAT16 }))
        .OUTPUT(indicesOut, TensorType({ DT_INT32 }))
        .ATTR(dim, Int, -1)
        .ATTR(keepdim, Bool, false)
        .OP_END_FACTORY_REG(MedianDim)
```

## Brief

Return values and indices where values contains the median of each row of input in the dim,
and indices contains the index of the median values found in the dim.

## Inputs

One input:
- self: A Tensor with any format. Support float, float16.

## Outputs

valuesOut: A Tensor, which is the same dtype as self. Support float, float16.
indicesOut: A Tensor, which contains the index of the median values found in the dim. Support int32.

## Attributes

dim: An optional int32, specifying the dim to reduce. Defaults to -1.
keepdim: An optional bool, specifying whether the output has dim retained or not.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 self: float32
- output0 valuesOut: float32
- output1 indicesOut: int32

## Attention Constraints

"dim" must be within the rank of the input tensor.

## Third-party framework compatibility

Compatible with the PyTorch operator the median.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
