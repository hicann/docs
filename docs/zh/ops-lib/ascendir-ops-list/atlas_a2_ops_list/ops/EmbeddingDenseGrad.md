# EmbeddingDenseGrad

```c
REG_OP(EmbeddingDenseGrad)
    .INPUT(grad, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BF16}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(num_weights, Int)
    .ATTR(padding_idx, Int, -1)
    .ATTR(scale_grad_by_freq, Bool, false)
    .OP_END_FACTORY_REG(EmbeddingDenseGrad)
```

## Brief

Calculates the reversed outputs of the function "embedding". 

## Inputs

Two inputs, including:
- grad: A mutable Tensor of word grad. Must be one of the following types:
    float32, bfloat16, float16.
- indices: A mutable word index Tensor of the int32, int64 type.

## Outputs

y: A mutable output Tensor of new word grad has the same type as "grad". 

## Attributes

- num_weights: An int attr which use to judge how many words in dict.
- padding_idx: An integer attribute that specifies which word index should have its gradient filled with zeros.
Defaults to "-1". 
- scale_grad_by_freq: An optional bool. Defaults to "False".
    If "True", "grad_weight" will be scale by word_frequency.
    If "False", "grad_weight" will not be scale by word_frequency. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: float32
- input1 indices: int32,int64
- output0 y: float32

## Third-party framework compatibility

Compatible with the Pytorch operator EmbeddingDenseGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
