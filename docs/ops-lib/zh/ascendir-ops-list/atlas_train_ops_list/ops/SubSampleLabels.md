# SubSampleLabels

```c
REG_OP(SubSampleLabels)
    .INPUT(labels, TensorType({DT_INT32}))
    .INPUT(shuffle_matrix, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .REQUIRED_ATTR(batch_size_per_images, Int)
    .REQUIRED_ATTR(positive_fraction, Float)
    .OP_END_FACTORY_REG(SubSampleLabels)
```

## Brief

Randomly sample a subset of positive and negative examples,and overwrite
the label vector to the ignore value (-1) for all elements that are not
included in the sample.

## Inputs

two inputs, including:
- labels: shape of labels,(N, ) label vector with values:.
- shuffle_matrix: random matrix with shape (N, ).

## Outputs

y: The result of subSample. 

## Attributes

- batch_size_per_images: A require attribute of type int.
- positive_fraction: A require attribute of type float.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 labels: int32
- input1 shuffle_matrix: int32
- output0 y: int32

## Attention Constraints

Warning: This operator can be integrated only by MaskRcnn. Please do not use it directly.

## Third-party framework compatibility

Compatible with the Pytorch operator SubSampleLabels.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
