# SdcaOptimizerV2

```c
REG_OP(SdcaOptimizerV2)
    .DYNAMIC_INPUT(sparse_example_indices, TensorType({DT_INT64}))
    .DYNAMIC_INPUT(sparse_feature_indices, TensorType({DT_INT64}))
    .DYNAMIC_INPUT(sparse_feature_values, TensorType({DT_FLOAT}))
    .DYNAMIC_INPUT(dense_features, TensorType({DT_FLOAT}))
    .INPUT(example_weights, TensorType({DT_FLOAT}))
    .INPUT(example_labels, TensorType({DT_FLOAT}))
    .DYNAMIC_INPUT(sparse_indices, TensorType({DT_INT64}))
    .DYNAMIC_INPUT(sparse_weights, TensorType({DT_FLOAT}))
    .DYNAMIC_INPUT(dense_weights, TensorType({DT_FLOAT}))
    .INPUT(example_state_data, TensorType({DT_FLOAT}))
    .OUTPUT(out_example_state_data, TensorType({DT_FLOAT}))
    .DYNAMIC_OUTPUT(out_delta_sparse_weights, TensorType({DT_FLOAT}))
    .DYNAMIC_OUTPUT(out_delta_dense_weights, TensorType({DT_FLOAT}))
    .ATTR(adaptive, Bool, false)
    .ATTR(num_sparse_features, Int, 0)
    .ATTR(num_sparse_features_with_values, Int, 0)
    .ATTR(num_dense_features, Int, 0)
    .ATTR(num_loss_partitions, Int, 1)
    .ATTR(num_inner_iterations, Int, 1)
    .ATTR(loss_type, String, "logistic_loss")
    .ATTR(l1, Float, 0.5)
    .ATTR(l2, Float, 0.5)
    .OP_END_FACTORY_REG(SdcaOptimizerV2)
```

## Brief

Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for
linear models with L1 + L2 regularization. As global optimization objective is
strongly-convex, the optimizer optimizes the dual objective at each step. The
optimizer applies each update one example at a time. Examples are sampled
uniformly, and the optimizer is learning rate free and enjoys linear convergence
rate . 

## Inputs

- sparse_example_indices: a list of vectors which contain example indices.It's a dynamic input.
- sparse_feature_indices: a list of vectors which contain feature indices.It's a dynamic input.
- sparse_feature_values: a list of vectors which contains feature value associated with each feature group.It's a dynamic input.
- dense_features: a list of matrices which contains the dense feature values.It's a dynamic input.
- example_weights: a vector which contains the weight associated with each example.
- example_labels: a vector which contains the label/target associated with each example.
- sparse_indices: a list of vectors where each value is the indices which has
corresponding weights in sparse_weights. This field maybe omitted for the dense approach.It's a dynamic input.
- sparse_weights: a list of vectors where each value is the weight associated with a sparse feature group.
- dense_weights: a list of vectors where the values are the weights associated with a dense feature group.It's a dynamic input.
- example_state_data: a list of vectors containing the example state data.

## Outputs

- out_example_state_data: A Returns a list of vectors containing the updated example state
data.a list of vectors where each value is the delta
- out_delta_sparse_weights:weights associated with a sparse feature group.a list of vectors where the values are the delta
- out_delta_dense_weights:weights associated with a dense feature group .

## Attributes

- adaptive: An optional bool that indicates whether to use adaptive algorithm. Defaults to false.
- num_sparse_features: An optional int that indicates the num of sparse. Defaults to 0.
- num_sparse_features_with_values: An optional int that indicates the num of sparse_feature_values. Defaults to 0.
- num_dense_features: An optional int that indicates the num of dense. Defaults to 0.
- loss_type: An optional string that indicates the type of the primal loss. Currently SdcaSolver supports logistic, squared and hinge losses. Defaults to "logistic_loss".
- l1: An optional float that indicates the symmetric l1 regularization strength. Defaults to 0.5.
- l2: An optional float that indicates the symmetric l2 regularization strength. Defaults to 0.5.
- num_loss_partitions: An optional int that indicates the number of partitions of the global loss function.  Defaults to 1.
- num_inner_iterations: An optional int that indicates the number of iterations per mini-batch.  Defaults to 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 sparse_example_indices: int64
- input1 sparse_feature_indices: int64
- input2 sparse_feature_values: float32
- input3 dense_features: float32
- input4 example_weights: float32
- input5 example_labels: float32
- input6 sparse_indices: int64
- input7 sparse_weights: float32
- input8 dense_weights: float32
- input9 example_state_data: float32
- output0 out_example_state_data: float32
- output1 out_delta_sparse_weights: float32
- output2 out_delta_dense_weights: float32

## Third-party framework compatibility

Compatible with tensorflow SdcaOptimizerV2 operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
