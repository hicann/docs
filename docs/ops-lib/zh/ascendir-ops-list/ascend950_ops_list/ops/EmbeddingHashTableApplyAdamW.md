# EmbeddingHashTableApplyAdamW

```c
REG_OP(EmbeddingHashTableApplyAdamW)
    .INPUT(table_handle, TensorType({DT_INT64}))
    .INPUT(keys, TensorType({DT_INT64}))
    .INPUT(m, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(v, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(beta1_power, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(beta2_power, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(lr, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(weight_decay, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(beta1, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(beta2, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(epsilon, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(max_grad_norm, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(m, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(v, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(beta1_power, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(beta2_power, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(max_grad_norm, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(embedding_dim, Int)
    .REQUIRED_ATTR(bucket_size, Int)
    .ATTR(amsgrad, Bool, false)
    .ATTR(maximize, Bool, false)
    .OP_END_FACTORY_REG(EmbeddingHashTableApplyAdamW)
```

## Brief

Updates embedding hash table according to the AdamW algorithm.

## Inputs

- table_handle: A Tensor, dtype is int64. 1-D. Stores the address of the hashtable.
- keys: A Tensor, dtype is int64. 1-D. Indicates the hashtable key.
          Should be deduplicated, otherwise can not guarantee the correctness of the results.
- m: A Tensor, dtype is float16 or float, 2-D. Indicates the first moment estimate.
       Shape is (bucket_size, embedding_dim).
- v: A Tensor, dtype is float16 or float, 2-D. Indicates the second moment estimate.
       Shape is (bucket_size, embedding_dim).
- beta1_power: A Tensor, dtype is float16 or float. 1-D. Used to cache intermediate calculated values.
                 Value is beta1*(step-1). Range is [0.0, 1.0).
- beta2_power: A Tensor, dtype is the same as "beta1_power". 1-D. Used to cache intermediate calculated values.
                 Value is beta2*(step-1). Range is [0.0, 1.0).
- lr: A Tensor, dtype is the same as "beta1_power". 1-D. Indicates the learning rate. Range is [0.0, INF).
- weight_decay: A Tensor, dtype is the same as "beta1_power". 1-D. Indicates the weight decay. Range is [0.0, INF).
- beta1: A Tensor, dtype is the same as "beta1_power". 1-D. Indicates the first order momentum. Range is [0.0, 1.0).
- beta2: A Tensor, dtype is the same as "beta1_power". 1-D. Indicates the second order momentum. Range is [0.0, 1.0).
- epsilon: A Tensor, dtype is the same as "beta1_power". 1-D. Indicates the small value param. Range is [0.0, 1.0).
- grad: A Tensor, dtype is the same as "beta1_power". 2-D. Indicates the grad. Shape is (keys number, embedding_dim).
- max_grad_norm: A mutable Tensor of the same type as "m". Indicates the gradient parameter.
                   Shape is (bucket_size, embedding_dim).

## Outputs

- m: A Tensor, dtype is float16 or float, 2-D. Update of the input m value.
- v: A Tensor, dtype is float16 or float, 2-D. Update of the input v value.
- beta1_power: Update the value of input beta1_power.
                 Used to cache intermediate calculated values. Dtype is float16 or float. 1-D.
- beta2_power: Update the value of input beta2_power.
                 Used to cache intermediate calculated values. Dtype is the same as "beta1_power". 1-D.
- max_grad_norm: A mutable Tensor of the same type as "m". Update of the input max_grad_norm value.

## Attributes

- embedding_dim: An Int, indicates the dim of embedding value in hashtable.
- bucket_size: An Int, indicates the size of hash map.
- amsgrad: An optional bool, indicates whether to use the AMSGrad variant of htis algorithm from
    the paper On the Convergence of Adam and Beyond.
    If "True", max_grad_norm input and output must be entered.
- maximize: An optional bool, maximize the params based on the objective.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 table_handle: int64
- input1 keys: int64
- input2 m: float16,float32
- input3 v: float16,float32
- input4 beta1_power: float16,float32
- input5 beta2_power: float16,float32
- input6 lr: float16,float32
- input7 weight_decay: float16,float32
- input8 beta1: float16,float32
- input9 beta2: float16,float32
- input10 epsilon: float16,float32
- input11 grad: float16,float32
- input12 max_grad_norm: float16,float32
- output0 m: float16,float32
- output1 v: float16,float32
- output2 beta1_power: float16,float32
- output3 beta2_power: float16,float32
- output4 max_grad_norm: float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
