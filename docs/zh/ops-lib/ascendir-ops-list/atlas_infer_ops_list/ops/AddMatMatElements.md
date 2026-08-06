# AddMatMatElements

```c
REG_OP(AddMatMatElements)
    .INPUT(c, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(a, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(b, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(beta, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(alpha, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(c, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(AddMatMatElements)
```

## Brief

Calculates the reversed outputs of the function "AddMatMatElements"
 c = c * beta + alpha * a * b

## Inputs

Three inputs, including:
- c: A mutable Tensor. Must be one of the following types:
    float16, float32.
- a: A mutable Tensor of the same dtype as "c".
- b: A mutable Tensor of the same dtype as "c".
- beta: A mutable scalar of the same dtype as "c".
- alpha: A mutable scalar of the same dtype as "c".

## Outputs

- c: A mutable Tensor. Has the same dtype as "c".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 c: float16,float32
- input1 a: float16,float32
- input2 b: float16,float32
- input3 beta: float16,float32
- input4 alpha: float16,float32
- output0 c: float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator AddMatMatElements.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
