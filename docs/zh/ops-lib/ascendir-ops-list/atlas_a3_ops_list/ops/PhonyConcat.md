# PhonyConcat

```c
REG_OP(PhonyConcat)
    .DYNAMIC_INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .REQUIRED_ATTR(concat_dim, ListInt)
    .REQUIRED_ATTR(N, ListInt)
    .ATTR(keep_input_offset, Bool, true)
    .OP_END_FACTORY_REG(PhonyConcat)
```

## Brief

Concatenates a list of "N" tensors along "concat_dim".
All input of the PhonyConcat are allocated with the same memory block.
GE calculates the memory offset of each input,
and the custom operators before write the memory by offset.
Warning: This operator is used only to identify that the GE allocates continuous memory and does not perform any
calculation.

## Inputs

Dynamic input: A list of input tensors. Has the same type and format as "x" .
- x:An ND Tensor.
Must be one of the following types: float16, float32, int32, int8, int16,
int64, uint8, uint16, uint32, uint64, bool, bfloat16.

## Outputs

- y:One output.

## Attributes

- concat_dim: A required list of int32. Specifies the dimensions along which to concat. No default value.
- N: A required list of int32. Specifies the number of concat tensors. No default value .
- keep_input_offset: A optional Bool. Specifies whether calculate the memory offset of input tensors. Default
True .

## Attention Constraints

- "concat_dim" is in the range [-len(x.shape), (x.shape)-1] .
- "N" is greater than or equals to 1.

## Third-party framework support

Support ONNX  framework.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
