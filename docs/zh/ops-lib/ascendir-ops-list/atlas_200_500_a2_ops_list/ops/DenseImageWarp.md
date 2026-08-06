# DenseImageWarp

```c
REG_OP(DenseImageWarp)
    .INPUT(image, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(flow, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(DenseImageWarp)
```

## Brief

Image warping using per-pixel flow vectors. 

## Inputs

- image: 4-D Tensor with shape `[batch, height, width, channels]`.
- flow: 4-D Tensor with shape `[batch, height, width, 2]`.

## Outputs

y: Returns 4-D with the same shape and dtype as `image`. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 image: float16,float32
- input1 flow: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
