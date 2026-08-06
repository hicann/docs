# SoftmaxCrossEntropyWithLogits

```c
REG_OP(SoftmaxCrossEntropyWithLogits)
    .INPUT(features, TensorType({DT_DOUBLE,DT_FLOAT16,DT_BF16,DT_FLOAT}))
    .INPUT(labels, TensorType({DT_DOUBLE,DT_FLOAT16,DT_BF16,DT_FLOAT}))
    .OUTPUT(loss, TensorType({DT_DOUBLE,DT_FLOAT16,DT_BF16,DT_FLOAT}))
    .OUTPUT(backprop, TensorType({DT_DOUBLE,DT_FLOAT16,DT_BF16,DT_FLOAT}))
    .OP_END_FACTORY_REG(SoftmaxCrossEntropyWithLogits)
```

## Brief

Computes softmax cross entropy cost and gradients to backpropagate. Broadcasting is supported.

## Inputs

Two inputs, including:
- features: A Tensor. Unnormalized scores from model output. Must be one of the following types: float16, bfloat16, float32, double.
A "batch_size * num_classes" matrix. The format must be ND or NHWC. Support 2D, 4D.
When the shape of features is 4D, the data type supports bfloat16 in dynamic shape scenarios, and float32 in static shape scenarios.
- labels: A Tensor. of the same type and format as "features". The true labels of the samples. A "batch_size * num_classes" matrix.
Has the type, format and shape as "features". 

## Outputs

- loss: A Tensor for per example loss (a "batch_size" vector). Has the same type and format as "features". Support 1D, 3D.
If the shape of features and labels is not 4D, the shape of the loss is 1D.
If the shape of features and labels is 4D, the shape of the loss is 3D.
- backprop: A Tensor for the backpropagated gradients (a batch_size * num_classes matrix).
Has the same type, format and shape as "features". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 features: bfloat16,float16,float32
- input1 labels: bfloat16,float16,float32
- output0 loss: bfloat16,float16,float32
- output1 backprop: bfloat16,float16,float32
### AI CPU
- input0 features: double,float16,float32
- input1 labels: double,float16,float32
- output0 loss: double,float16,float32
- output1 backprop: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SoftmaxCrossEntropyWithLogits.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
