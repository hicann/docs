# GroupedBiasAddGrad

```c
REG_OP(GroupedBiasAddGrad)
    .INPUT(grad_y, "T")
    .OPTIONAL_INPUT(group_idx, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(grad_bias, "T")
    .ATTR(group_idx_type, Int, 0)
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OP_END_FACTORY_REG(GroupedBiasAddGrad)
```

## Brief

Backwards calculation of GroupedBiasAdd.

## Inputs

- grad_y: A Tensor. Type is:BFloat16, Float16 or Float32. When group_idx is inputted, the shape only supports 2 dimensions.
            When group_idx is not inputted, the shape only supports 3 dimensions, supports non-continuous tensors, and the data format supports ND.
- group_idx: An optional Tensor. Type is:Int32 or Int64.
            Optional parameter, the end position of each group, shape only supports 1 dimension, supports non-continuous tensors, and the data format supports ND.

## Outputs

- grad_bias: A Tensor. Data type must match that of 'grad_y' (BFloat16, Float16 or Float32).
            - Shape constraints are determined based on the dimensionality of 'grad_y':
              - If 'grad_y' has 3 dimensions ('group_idx' is not provided), then:
                   'grad_bias.shape = [grad_y.shape[0], grad_y.shape[2]]'
              - If 'grad_y' has 2 dimensions ('group_idx' is provided), then:
                   'grad_bias.shape = [group_idx.shape[0], grad_y.shape[1]]'
            - Supports non-continuous tensors, and data format supports "ND".

## Attributes

- group_idx_type: An optional Int, specifying the significance of group_idx, default to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_y: bfloat16,float16,float32
- input1 group_idx: int32,int64
- output0 grad_bias: bfloat16,float16,float32

## Attention Constraints

group_idx: A maximum of 2048 groups are supported. 
When group_idx is inputted, it is required to ensure that the values of the tensor do not exceed the maxium value of INT32 and are non-negative. 
When group_idx is inputted and group_idx_type is 0, it is necessary to ensure that the tensor data is in ascending order, and the last numerical value is equal to the
size of the 0th dimension of grad_y. 
When group_idx is inputted and group_idx_type is 1, it is necessary to ensure that the sum of the tensor values must equal the size of grad_y in the 0th dimension.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
