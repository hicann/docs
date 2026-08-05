# ResizeNearestNeighborV2Grad

```c
REG_OP(ResizeNearestNeighborV2Grad)
    .INPUT(grads, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32,
                              DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32,
                           DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .ATTR(scales, ListFloat, {0.0f, 0.0f})
    .OP_END_FACTORY_REG(ResizeNearestNeighborV2Grad)
```

## Brief

Computes the gradient of nearest neighbor interpolation . 

## Inputs

Inputs include:
- grads: A 4-D tensor. The gradient tensor that represents the reverse computation.
Must be one of the following types: uint8, int8, int16, uint16, int32, int64, float16, float, double, bfloat16.
Must set the format, supported format list ["NCHW, NHWC"].
- size: A 1-D tensor of 2 elements: orig_height, orig_width. Must be the type int32.
The original input size. 

## Outputs

y: A tensor. The output tensor representing the reverse computation.
Has the same dtype, shape and format as "grads". 

## Attributes

- align_corners: An optional bool. Defaults to "false". If "true", the centers
of the 4 corner pixels of the input and grad tensors are aligned.
- half_pixel_centers: An optional bool. Indicates if the offset coordinates are normalized. Defaults to "false".
- scales: An optional listfloat. Multiplier for spatial size. Defaults to {0.0f, 0.0f}.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float32
- input1 size: int32
- output0 y: float32
### AI CPU
- input0 grads: bfloat16,double,float16,float32,int8,int32,uint8
- input1 size: int32
- output0 y: bfloat16,double,float16,float32,int8,int32,uint8

## Attention Constraints

Input grads must be a 4-D tensor . 

## Third-party framework compatibility

Compatible with tensorflow ResizeNearestNeighborV2Grad operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
