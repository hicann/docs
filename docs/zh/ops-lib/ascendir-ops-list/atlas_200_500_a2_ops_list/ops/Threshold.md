# Threshold

```c
REG_OP(Threshold)
     .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
     .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
     .ATTR(threshold, Float, 0.0)
     .OP_END_FACTORY_REG(Threshold)
```

## Brief

Tests whether the input exceeds a threshold.

## Inputs

x: A ND Tensor with any format. Must be one of the following types: float16, float32, bfloat16. 

## Outputs

y: A ND Tensor with any format. Has the same dtype as the input. Must be one of the following types: float16, float32, bfloat16.

## Attributes

threshold: A required float32. Defaults to "0.0". "x" is compared with "threshold", outputs "1" for inputs above threshold; "0" otherwise. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Caffe operator Threshold.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
