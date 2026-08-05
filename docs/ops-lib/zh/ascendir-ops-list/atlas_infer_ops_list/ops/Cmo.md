# Cmo

```c
REG_OP(Cmo)
    .INPUT(src, TensorType::NumberType())
    .REQUIRED_ATTR(max_size, Int)
    .ATTR(type, Int, 6)
    .ATTR(offset, Int, 0)
    .OP_END_FACTORY_REG(Cmo)
```

## Brief

Operators for managing cache memory.

## Inputs

src: A ND Tensor with TensorType::NumberType().

## Attributes

- max_size: The maximum memory size required for caching operation.
- type: An optional int32 or int64 which has a default value of 6, indicating a prefetch operation.
- offset: An optional int32 or int64 specifies the offset of the CMO operation address, which must not exceed the
size of the input memory. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
