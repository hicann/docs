# IsVariableInitialized

```c
REG_OP(IsVariableInitialized)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(IsVariableInitialized)
```

## Brief

Checks whether a tensor has been initialized. Outputs boolean scalar indicating whether the tensor has been initialized . 

## Inputs

x: A Tensor of type float16, float32, double, bool, int8, uint8, uint16, int16, int32, uint32, uint64, int64.

## Outputs

y: A tensor, indicating whether "x" has been initialized . 

## Third-party framework compatibility

Compatible with the TensorFlow operator IsVariableInitialized.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
