# SearchN

```c
REG_OP(SearchN)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(scale_d, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(scale_w, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(n, TensorType({DT_INT8}))
    .OP_END_FACTORY_REG(SearchN)
```

## Brief

find an optimal n for shift-n. 

## Inputs

- x: A Tensor. indicates the output of quantizable layers.
- scale_d: A Tensor, one number. indicates the scale of data.
- scale_w: A Tensor, must be one number or the same size as dim-C when x is NHWC/NCHW.
             indicates the scale of weight. 

## Outputs

- n: A Tensor, has the same shape as scale_w. indicates the optimal n.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 scale_d: float16,float32
- input2 scale_w: float16,float32
- output0 n: int8


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
