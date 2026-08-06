# ConfusionMatrix

```c
REG_OP(ConfusionMatrix)
    .INPUT(labels, TensorType({DT_FLOAT, DT_INT32, DT_FLOAT16, DT_INT8, DT_UINT8}))
    .INPUT(predictions, TensorType({DT_FLOAT, DT_INT32, DT_FLOAT16, DT_INT8, DT_UINT8}))
    .OPTIONAL_INPUT(weights, TensorType({DT_FLOAT, DT_INT32, DT_FLOAT16, DT_INT8, DT_UINT8}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_FLOAT16, DT_INT8, DT_UINT8}))
    .REQUIRED_ATTR(num_classes, Int)
    .REQUIRED_ATTR(dtype, String)
    .OP_END_FACTORY_REG(ConfusionMatrix)
```

## Brief

Computes the confusion matrix from predictions and labels .

## Inputs

Three inputs, including:
- labels: A Tensor. Must be one of the following types: float16, float32,
int32, int8, uint8. 1D. Has format ND.
- predictions: A Tensor. Must be one of the following types: float16,
float32, int32, int8, uint8. 1D. Has format ND.
- weights: A optional Tensor. Must be one of the following types: float16, float32,
int32, int8, uint8. 1D. Has format ND. 

## Outputs

y: A Tensor. 1D. Has format ND. Has the same type and format as input "labels" . 

## Attributes

- num_classes: An integer for the shape of the output matrix.
- dtype: Data type of the confusion matrix.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 labels: float16,float32,int8,int32,uint8
- input1 predictions: float16,float32,int8,int32,uint8
- input2 weights: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8

## Attention Constraints

- "weights", "labels", and "predictions" are 1D tensors.
- The output is with shape (num_classes, num_classes),
where, 1 <= num_classes <= 4096 . 
@see Region()

## Third-party framework compatibility

Compatible with the TensorFlow operator ConfusionMatrix.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
