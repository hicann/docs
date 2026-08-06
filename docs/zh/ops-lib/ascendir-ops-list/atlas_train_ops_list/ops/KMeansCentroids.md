# KMeansCentroids

```c
REG_OP(KMeansCentroids)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(y, TensorType({DT_FLOAT}))
    .INPUT(sum_square_y, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(sum_square_x, TensorType({DT_FLOAT}))
    .OUTPUT(segment_sum, TensorType({DT_FLOAT}))
    .OUTPUT(segment_count, TensorType({DT_FLOAT}))
    .OUTPUT(kmean_total_sum, TensorType({DT_FLOAT}))
    .ATTR(use_actual_distance, Bool, false)
    .OP_END_FACTORY_REG(KMeansCentroids)
```

## Brief

Perform k-means clustering on a data matrix. 

## Inputs

Three required inputs and one optional inputs, including:
- x: A 2D tensor of data type float32.
- y: A 2D tensor of data type float32.
- sum_square_x: An optional 2D tensor of data type float32.
- sum_square_y: A 2D tensor of data type float32.

## Outputs

- segment_sum: A tensor of data type float32.
- segment_count: A tensor of data type float32.
- k_mean_total_sum: A tensor of data type float32.

## Attributes

use_actual_distance: Indicates whether to calculate the complete distance. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 y: float32
- input2 sum_square_y: float32
- input3 sum_square_x: float32
- output0 segment_sum: float32
- output1 segment_count: float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
