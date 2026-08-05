# CdistGrad

```c
REG_OP(CdistGrad)
    .INPUT(grad, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(x1, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(x2, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(cdist, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT}))
    .ATTR(p, Float, 2.0)
    .OP_END_FACTORY_REG(CdistGrad)
```

## Brief

Computes the grad of x1 in cdist. 

## Inputs

Four inputs, including:
- grad: Grad with shape BxPxR. Must be one of the following types:
    float16, float32. 
- x1: A tensor with shpae: BxPXM. Must be one of the following types:
    float16, float32. 
- x2: A tensor with shpae: BxRxM. Must be one of the following types:
    float16, float32. 
- cdist: Output tensor of cdist forward with shpae: BxPXR.
    Must be one of the following types: float16, float32. 

## Outputs

y: A Tensor with the same type and shape of x1's. 

## Attributes

- p: An optional float >= 0 or inf. Defaults to 2.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: float16,float32
- input1 x1: float16,float32
- input2 x2: float16,float32
- input3 cdist: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator Cdist Backward. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
