# GlobalLpPool

```c
REG_OP(GlobalLpPool)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(p, Float, 2.0)
    .OP_END_FACTORY_REG(GlobalLpPool)
```

## Brief

Computes GlobalLpPool, GlobalLpPool consumes an input tensor X and applies lp pool pooling across the
values in the same channel.

## Inputs

x: A 4D or 5D Tensor of type float16, float32 or bfloat16, with format ND. 

## Outputs

y: A 4D or 5D Tensor. Has the same type and format as "x". 
When x is a 4D Tensor, the shape of y is [x.shape[0],x.shape[1],1,1]. 
When x is a 5D Tensor, the shape of y is [x.shape[0],x.shape[1],1,1,1].

## Attributes

- p: p value of the Lp norm used to pool over the input data. Must be one of the following types: float32. Defaults
to 2.0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the ONNX operator GlobalLpPool.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
