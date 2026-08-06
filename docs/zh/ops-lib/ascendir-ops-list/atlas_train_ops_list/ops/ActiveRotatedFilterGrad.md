# ActiveRotatedFilterGrad

```c
REG_OP(ActiveRotatedFilterGrad)
    .INPUT(y_grad, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32}))
    .INPUT(indices, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(x_grad, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32}))
    .OP_END_FACTORY_REG(ActiveRotatedFilterGrad)
```

## Brief

The backward of ActiveRotatedFilter. 

## Inputs

Two inputs, including:
- y_grad: Input features with shape [num_output_planes * num_rotations, num_input_planes * num_orientations, H, W].
- indices: Indices with shape [num_orientations, H, W, num_rotations].

## Outputs

One output, including:
- x_grad: Refined features with shape [num_output_planes, num_input_planes, num_orientations, H, W].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 y_grad: float16,float32,int32
- input1 indices: int32,int64
- output0 x_grad: float16,float32,int32

## Third-party framework compatibility

Compatible with the mmcv operator ActiveRotatedFilterGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
