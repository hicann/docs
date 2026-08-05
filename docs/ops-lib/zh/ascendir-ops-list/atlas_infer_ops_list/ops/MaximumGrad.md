# MaximumGrad

```c
REG_OP(MaximumGrad)
    .INPUT(grads, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OUTPUT(y1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OUTPUT(y2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .ATTR(grad_x, Bool, true)
    .ATTR(grad_y, Bool, true)
    .OP_END_FACTORY_REG(MaximumGrad)
```

## Brief

Calculates the reversed outputs of the function "maximum".

## Inputs

Three inputs, including:
- grads: A ND Tensor. Must be one of the following types:
float16, float32, int32.
- x1: A ND Tensor of the same dtype as "grads".
- x2: A ND Tensor of the same dtype as "grads".

## Outputs

- y1: A ND Tensor. Has the same dtype as "grads".
- y2: A ND Tensor. Has the same dtype as "grads".

## Attributes

- grad_x: An optional bool. Defaults to "True".
If "True", "y1" will be output.
If "False", "y1" will not be output. 
- grad_y: An optional bool. Defaults to "True".
If "True", "y2" will be output.
If "False", "y2" will not be output. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float16,float32,int32
- input1 x1: float16,float32,int32
- input2 x2: float16,float32,int32
- output0 y1: float16,float32,int32
- output1 y2: float16,float32,int32

## Third-party framework compatibility

Compatible with the TensorFlow operator MaximumGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
