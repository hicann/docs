# RefMerge

```c
REG_OP(RefMerge)
    .DYNAMIC_INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .OUTPUT(value_index, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(RefMerge)
```

## Brief

Forwards the value of an available tensor from input "x" to output "y".
      Merge waits for at least one of the input tensors to become available.
      It is usually combined with Switch to implement branching.
      Merge forwards the first tensor to become available to output "y",
      and sets "value_index" the index of the tensor in inputs .

## Inputs

x: The input tensors, one of which will become available.
  Must be one of the following types: float16, float32, float64, int8,
  int16, int32, int64, uint8, uint16, uint32, uint64, bool, string . It's a dynamic input. 

## Outputs

- y: The available tensor. Has the same type as "x".
- value_index: A scalar of type int32, for the index of the chosen input
                tensor . 
@see Switch() | Merge()

## Third-party framework compatibility

Compatible with the TensorFlow operator RefMerge.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
