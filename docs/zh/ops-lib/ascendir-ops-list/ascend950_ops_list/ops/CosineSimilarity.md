# CosineSimilarity

```c
REG_OP(CosineSimilarity)
    .INPUT(input_x1, TensorType({DT_FLOAT}))
    .INPUT(input_x2, TensorType({DT_FLOAT}))
    .OUTPUT(output_y, TensorType({DT_FLOAT}))
    .ATTR(dim, Int, 1)
    .ATTR(eps, Float, 1e-8f)
    .OP_END_FACTORY_REG(CosineSimilarity)
```

## Brief

Returns cosine similarity between x1 and x2,computed along dim. 

## Inputs

Two inputs, including:
- input_x1: A tensor. Must be the following types: float32.
- input_x2: A tensor. Must of the following types: float32.

## Outputs

output_y: A ND Tensor with the same dtype of input_x's. 

## Attributes

- dim:The type is Int and the default value is 1.
- eps:The type is Float and the default value is 1e-8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x1: float32
- input1 input_x2: float32
- output0 output_y: float32

## Third-party framework compatibility

Compatible with the PyTorch operator CosineSimilarity. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
