# AnonymousSeedGenerator

```c
REG_OP(AnonymousSeedGenerator)
    .INPUT(seed, TensorType({DT_INT32,DT_INT64}))
    .INPUT(seed2, TensorType({DT_INT32,DT_INT64}))
    .INPUT(reshuffle, TensorType({DT_BOOL}))
    .OUTPUT(handle, TensorType({DT_RESOURSE}))
    .OUTPUT(deleter, TensorType({DT_VARIANT}))
    .OP_END_FACTORY_REG(AnonymousSeedGenerator)
```

## Brief

Create a random number seed generator. 

## Inputs

include:
- seed:1-D Tensor,the seed to generate random.
Must be one of the types:int32 or int64.
- seed2:1-D Tensor,the seed to generate random.
Must be one of the types:int32 or int64.
- reshuffle:1-D Tensor.Seed selection, True:random seed, False:fixed seed.
Must be one of the types:bool.  

## Outputs

output:
- handle:Handle to the random number generator.
- deleter:Handle to the remover.Used when deleting the random number seed generator.
@see AnonymousSeedGenerator()

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 seed: int32,int64
- input1 seed2: int32,int64
- input2 reshuffle: bool
- output0 handle: resource
- output1 deleter: variant

## Third-party framework compatibility

compatible with AnonymousSeedGenerator op of tensorflow.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
