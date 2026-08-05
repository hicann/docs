# AccumulateNV2

```c
REG_OP(AccumulateNV2)
   .DYNAMIC_INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8}))
   .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8}))
   .REQUIRED_ATTR(N, Int)
   .OP_END_FACTORY_REG(AccumulateNV2)
```

## Brief

Returns the element-wise sum of a list of tensors.
AccumulateNV2 performs the same operation as AddN, but does not wait for all of its inputs
to be ready before beginning to sum. This can save memory if inputs are ready at different times,
since minimum temporary storage is proportional to the output size rather than the inputs size.
Returns a Tensor of same shape and type as the elements of inputs.

## Inputs

Dynamic inputs, including:
x: A tensor. Must be one of the following types: float16, float32, int32, int8, uint8. It's a dynamic input. 

## Outputs

y: A tensor. Has the same dtype as "x".

## Attributes

N: the size of x. Must be "int".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8

## Third-party framework compatibility

Compatible with the TensorFlow operator AccumulateNV2.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
