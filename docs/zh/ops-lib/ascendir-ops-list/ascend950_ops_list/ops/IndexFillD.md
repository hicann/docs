# IndexFillD

```c
REG_OP(IndexFillD)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16}))
    .INPUT(assist1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16}))
    .INPUT(assist2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16}))
    .REQUIRED_ATTR(dim, Int)
    .OP_END_FACTORY_REG(IndexFillD)
```

## Brief

Fills the elements of the input tensor with value val by selecting the indices in the order given in index.

## Inputs

Three inputs, including:
- x: A tensor. Must be one of the following types:
    float16, float32, int32, bfloat16. 
- assist1: A tensor. Must be one of the following types:
    float16, float32, int32, bfloat16. 
- assist2: A tensor. Must be one of the following types:
    float16, float32, int32, bfloat16. 

## Outputs

y: A tensor with the same type and shape as 'x'. 

## Attributes

dim: A required int. Used to select the dimension of this tensor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int32,int64
- input1 assist1: bfloat16,bool,float16,float32,int32,int64
- input2 assist2: bfloat16,bool,float16,float32,int32,int64
- output0 y: bfloat16,bool,float16,float32,int32,int64

## Attention Constraints

The operator will not be enhanced in the future.

## Third-party framework compatibility

Compatible with the Pytorch operator IndexFill. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
