# LayerNormUpdate

```c
REG_OP(LayerNormUpdate)
    .INPUT(x1, TensorType({DT_FLOAT16}))
    .INPUT(beta, TensorType({DT_FLOAT16}))
    .INPUT(gamma, TensorType({DT_FLOAT16}))
    .INPUT(sum, TensorType({DT_FLOAT}))
    .INPUT(square_sum, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16}))
    .ATTR(epsilon, Float, 0.00001f)
    .OP_END_FACTORY_REG(LayerNormUpdate)
```

## Brief

Layernorm operator interface implementation with given sum and square sum of input tensor 
 calculating: x, gamma, beta, sum, square_sum 
 mean  = sum / reduce_axis 
 variance = square_sum / reduce_aixs - mean * mean 
 variance = np.mean(np.power((x - mean),2), reduce_axis, keepdims=True) 
 y = gamma*((x - mean) / np.sqrt(variance + 0.001)) + beta

## Inputs

Five inputs, including:
- x: A Tensor. Must be one of the following types: float16.
- gamma: A Tensor. Must be one of the following types: float16.
- beta: A Tensor. Must be one of the following types: float16.
- sum. A Tensor. Must be one of the following types: float.
- square_sum. A Tensor. Must be one of the following types: float.

## Outputs

Three outputs, including:
- y: A Tensor. Must be one of the following types: float16.

## Attributes

- epsilon: A optional attribute, the type is float32. Defaults to 1e-5.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input1 gamma: float16
- input2 beta: float16
- input3 sum: float32
- input4 square_sum: float32
- output0 y: float16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
