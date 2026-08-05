# ChunkCat

```c
REG_OP(ChunkCat)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(dim, Int)
    .REQUIRED_ATTR(num_chunks, Int)
    .OP_END_FACTORY_REG(ChunkCat)
```

## Brief

split input tensors and concat along one dimension .

## Inputs

One input:
x: Dynamic input. A ND Tensor.
   Must be one of the following types: float32, float16, bfloat16. 

## Outputs

y: A ND Tensor. concat by x . 

## Attributes

- dim: A required int32, or int64.
Specifies the dimension along which to chunk. No default value.
- num_chunks:  A required int32, or int64.
Specifies the number of chunks to split "x" into. No default value. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

- "x" is a list of at least 2 "tensor" objects of the same type.
- "dim" is in the range [-len(x.shape), len(x.shape)].
- "num_chunks" is larger than 0.

## Third-party framework compatibility

Compatible with the PyTorch operator ChunkCat. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
