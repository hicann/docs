# PhonySplit

```c
REG_OP(PhonySplit)
    .INPUT(x, TensorType::ALL())
    .DYNAMIC_OUTPUT(y, TensorType::ALL())
    .REQUIRED_ATTR(split_dim, ListInt)
    .REQUIRED_ATTR(num_split, ListInt)
    .ATTR(keep_output_offset, Bool, true)
    .OP_END_FACTORY_REG(PhonySplit)
```

## Brief

Splits a tensor along dimension "split_dim" into "num_split" smaller tensors.
All outputs of the PhonySplit are allocated with the same memory block.
GE calculates the memory offset of each output,
and the custom operators next read the memory by offset.
Warning: This operator is used only to identify that the GE allocates continuous memory and does not perform any
calculation.

## Inputs

One input:
- x:An ND Tensor.
Must be one of the following types: float16, float32, int32, int8, int16,
int64, uint8, uint16, uint32, uint64, bool, bfloat16.

## Outputs

- y:Dynamic output. A list of output tensors. Has the same type and format as "x" .

## Attributes

- split_dim: A required int32. Specifies the dimension along which to split. No default value.
- num_split: A required int32. Specifies the number of output tensors. No default value .
- keep_output_offset: A optional Bool. Specifies whether calculate the memory offset of outpute tensors. Default
True .

## Attention Constraints

- "num_split" is greater than or equals to 1.
- "num_split" is divisible by the size of dimension "split_dim".
- "split_dim" is in the range [-len(x.shape), (x.shape)-1] .

## Third-party framework support

Support ONNX  framework.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
