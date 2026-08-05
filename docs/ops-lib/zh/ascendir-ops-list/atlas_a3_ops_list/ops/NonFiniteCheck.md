# NonFiniteCheck

```c
REG_OP(NonFiniteCheck)
    .DYNAMIC_INPUT(tensor_list, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(found_flag, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(NonFiniteCheck)
```

## Brief

Check if there are non-finite numbers (+inf/-inf/nan) in the tensor_list.
If there are, set found_flag to 1, otherwise, set found_flag to 0.

## Inputs

One input:
tensor_list: Dynamic input, A tensor list containing multiple ND format tensors,
Support 1D ~ 8D, dtype can be float16, bfloat16, float32.
The dtype of each tensor in the tensor_list must be consistent,
and the tensor_list can contain a maximum of 256 tensors.

## Outputs

found_flag: A tensor with only one element, the shape must be (1,), must be float.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 tensor_list: bfloat16,float16,float32
- output0 found_flag: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
