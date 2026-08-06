# StatelessMultinomial

```c
REG_OP(StatelessMultinomial)
    .INPUT(logits, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE}))
    .INPUT(num_samples, TensorType({DT_INT32}))
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(output_dtype, Type, DT_INT64)
    .OP_END_FACTORY_REG(StatelessMultinomial)
```

## Brief

Draws samples from a multinomial distribution. 

## Inputs

include:
- logits:2-D Tensor with shape [batch_size, num_classes]. Each slice [i, :]
represents the unnormalized log probabilities for all classes.
- num_samples:0-D. Number of independent samples to draw for each row slice.
- seed:The seed to generate random.

## Outputs

y:Output random number. 
@see StatelessMultinomial()

## Attributes

- output_dtype: Output data type. Must be one of the following types: int32, int64. Defaults to int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 logits: double,float16,float32
- input1 num_samples: int32
- input2 seed: int32,int64
- output0 y: int32,int64

## Third-party framework compatibility

compatible with StatelessMultinomial op of tensorflow.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
