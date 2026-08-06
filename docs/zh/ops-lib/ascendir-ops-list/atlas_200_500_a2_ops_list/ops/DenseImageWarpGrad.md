# DenseImageWarpGrad

```c
REG_OP(DenseImageWarpGrad)
    .INPUT(grad, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(image, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(flow, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(grad_image, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(grad_flow, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(DenseImageWarpGrad)
```

## Brief

Computes the gradients of DenseImageWarp with respect to image and flow. 

## Inputs

- grad: gradients with respect to DenseImageWarp output.
- image: 4-D Tensor with shape `[batch, height, width, channels]`.
- flow: 4-D Tensor with shape `[batch, height, width, 2]`.

## Outputs

- grad_image: Returns 4-D with the same shape and dtype as `image`.
- grad_flow: Returns 4-D with the same shape and dtype as `flow`.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 grad: float16,float32
- input1 image: float16,float32
- input2 flow: float16,float32
- output0 grad_image: float16,float32
- output1 grad_flow: float16,float32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
