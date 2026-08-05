# AddN

```c
REG_OP(AddN)
    .DYNAMIC_INPUT(x, TensorType({NumberType(), DT_VARIANT}))
    .OUTPUT(y, TensorType({NumberType(), DT_VARIANT}))
    .REQUIRED_ATTR(N, Int)
    .OP_END_FACTORY_REG(AddN)
```

## Brief

Adds all input tensors element-wise.

## Inputs

Dynamic inputs, including:
x: A list of tensor objects, each with same shape and type. The supported types are:
bfloat16, float16, float32, int32, int64. It's a dynamic input. 

## Outputs

y: An ND tensor. Has the same shape and type as the elements of "x". 

## Attributes

N: A required attribute of type int32, means nums of inputs. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- output0 y: float16,float32,int32
### AI CPU
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64,variant

## Third-party framework compatibility

Compatible with the TensorFlow operator AddN.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
