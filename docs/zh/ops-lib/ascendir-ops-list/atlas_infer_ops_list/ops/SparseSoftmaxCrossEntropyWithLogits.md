# SparseSoftmaxCrossEntropyWithLogits

```c
REG_OP(SparseSoftmaxCrossEntropyWithLogits)
    .INPUT(features, TensorType({DT_DOUBLE,DT_FLOAT16,DT_FLOAT,DT_BFLOAT16}))
    .INPUT(labels, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(loss, TensorType({DT_DOUBLE,DT_FLOAT16,DT_FLOAT,DT_BFLOAT16}))
    .OUTPUT(backprop, TensorType({DT_DOUBLE,DT_FLOAT16,DT_FLOAT,DT_BFLOAT16}))
    .OP_END_FACTORY_REG(SparseSoftmaxCrossEntropyWithLogits)
```

## Brief

Computes sparse softmax cross entropy cost and gradients to backpropagate.

## Inputs

Two inputs, including:
- features: A Tensor. Must be one of the following types: float16, float32, double, bfloat16.
A "batch_size * num_classes" matrix.
- labels: A Tensor. Must be one of the following types: 'int32', 'int64'.
batch_size vector with values in [0, num_classes).
This is the label for the given minibatch entry. 

## Outputs

- loss: A Tensor for per example loss (a "batch_size" vector). Has the same type as "features".
- backprop: A Tensor for the backpropagated gradients (a batch_size * num_classes matrix).
Has the same type as "features" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 features: double,float16,float32
- input1 labels: int32,int64
- output0 loss: double,float16,float32
- output1 backprop: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseSoftmaxCrossEntropyWithLogits.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
