# SubSample

```c
REG_OP(SubSample)
    .INPUT(labels, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .REQUIRED_ATTR(batch_size_per_images, Int)
    .REQUIRED_ATTR(positive_fraction, Float)
    .OP_END_FACTORY_REG(SubSample)
```

## Brief

Randomly sample a subset of positive and negative examples,and overwrite
the label vector to the ignore value (-1) for all elements that are not
included in the sample.

## Inputs

One input:
labels: shape of labels,(N, ) label vector with values. 

## Outputs

y: The result of subSample. 

## Attributes

- batch_size_per_images: A require attribute of type int.
- positive_fraction: A require attribute of type float.

## Attention Constraints

Warning: This operator can be integrated only by MaskRcnn. Please do not use it directly.

## Third-party framework compatibility

Compatible with the Pytorch operator SubSample.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
