# StatelessDropOutGenMask

```c
REG_OP(StatelessDropOutGenMask)
    .INPUT(shape, TensorType({ DT_INT32, DT_INT64 }))
    .INPUT(prob, TensorType({ DT_FLOAT16, DT_FLOAT, DT_BF16 }))
    .INPUT(seed, TensorType({ DT_INT32, DT_INT64 }))
    .INPUT(seed1, TensorType({ DT_INT32, DT_INT64 }))
    .OPTIONAL_INPUT(offset, TensorType({ DT_INT64 }))
    .OUTPUT(y, TensorType({ DT_UINT8 }))
    .OP_END_FACTORY_REG(StatelessDropOutGenMask)
```

## Brief

Generate stateless random bit mask for dropout . 

## Inputs

include:
- shape:The shape of the output tensor.
- prob:0-D. Number of bit 1 .
- seed:Frist seed to avoid seed collision.
- seed1:Second seed to avoid seed collision .
- offset:Initial offset of random number .

## Outputs

y:Output (1-D) random number using uint data format . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 prob: float16,float32
- input2 seed: int32,int64
- input3 seed1: int32,int64
- input4 offset: int64
- output0 y: uint8

## Attention Constraints

The output is aligned with 128 bits.
@see StatelessDropOutGenMask()


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
