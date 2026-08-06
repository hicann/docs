# PReluGrad

```c
REG_OP(PReluGrad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(features, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(weights, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(da, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(PReluGrad)
```

## Brief

Performs the backpropagation of PRelu for training scenarios .

## Inputs

- grads: Input gradient. ND Tensors are supported.
The data type can be float16, float32 or bfloat16.
- features: A ND Tensor of type float16, float32 or bfloat16. Has same dtype with grads. Support 2D~8D tensor.
- weights: A Scalar or 1D Tensor, has same dtype with grads.
specifying the weight.
The number of dimensions must be the same as the number of
channels(the dim1 number of features's shape) or 1.

## Outputs

- dx: Reverse gradient of "features".
Has the same shape and dtype with "features".
- da: Reverse gradient of "weights".
Has the same shape and dtype with "weights". 

## Third-party framework compatibility

Compatible with PyTorch operator PReluGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
