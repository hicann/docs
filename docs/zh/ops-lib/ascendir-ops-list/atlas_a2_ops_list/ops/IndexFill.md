# IndexFill

```c
REG_OP(IndexFill)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT64, DT_INT32, DT_BOOL, DT_INT8, DT_UINT8, DT_INT16,
                          DT_DOUBLE}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(val, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT64, DT_INT32, DT_BOOL, DT_INT8, DT_UINT8, DT_INT16,
                            DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT64, DT_INT32, DT_BOOL, DT_INT8, DT_UINT8, DT_INT16,
                           DT_DOUBLE}))
    .REQUIRED_ATTR(dim, Int)
    .OP_END_FACTORY_REG(IndexFill)
```

## Brief

Fills the elements of the input tensor x with value val by selecting the indices in the order given in index.
This is a non in-place replacement operator and does not affect the input tensor of the element.

## Inputs

Three inputs, including:
- x: A tensor that serves as the source; its duplicate is created and subsequently filled with the specified values.
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or Atlas A3
Training Series
Product/Atlas A3 Inference Series Product, a tensor of type float16, float32, bfloat16, int64, int32, bool can be
supported. 
In Ascend 950 AI Processor, a tensor of type float16, float32, bfloat16, int64, int32, bool, int8, uint8, int16,
double can be supported. 
- indices: A tensor, which equivalent to a vector or scalar. indices of input tensor to fill in. Must be one of the
following types:
    int32, int64. 
- val: The value to fill with. It's a scalar or a one-dimensional tensor with only one element.
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or Atlas A3
Training Series
Product/Atlas A3 Inference Series Product, a tensor of type float16, float32, bfloat16, int64, int32, bool can be
supported. 
In Ascend 950 AI Processor, a tensor of type float16, float32, bfloat16, int64, int32, bool, int8, uint8, int16,
double can be supported. 

## Outputs

y: A tensor with the same shape as 'x'. 

## Attributes

dim: A required int. Used to select the dimension of the input tensor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int32,int64
- input1 indices: int32,int64
- output0 y: bfloat16,bool,float16,float32,int32,int64

## Attention Constraints

- The input x and output y must have same shape.
- The data type of element in tensor x must be same with the data type of input val.
- The input indices must be either a 1D tensor (equivalent to vector) or a 0D tensor (equivalent to scalar).

## Third-party framework compatibility

Compatible with the Pytorch operator index_fill. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
