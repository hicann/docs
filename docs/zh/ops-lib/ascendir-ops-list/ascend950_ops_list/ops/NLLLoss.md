# NLLLoss

```c
REG_OP(NLLLoss)
    .INPUT(x, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .INPUT(target, TensorType({DT_INT32, DT_INT64, DT_UINT8}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .OUTPUT(total_weight, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .ATTR(reduction, String, "mean")
    .ATTR(ignore_index, Int, -100)
    .OP_END_FACTORY_REG(NLLLoss)
```

## Brief

The negative log likelihood loss .

## Inputs

The input x and weight must have the same type. Inputs include:
- x: A 2D or 4D tensor with shape (N, C) or (N, C, H, W). Support dtype: float32/bfloat16/float16.
- target: A 1D or 3D tensor with shape (N) or (N, H, W). When x is 2D(shape (N, C)),target should be 1D(shape(N)) or scalar, when x is 4D(shape(N, C, H, W)), target should be 3d(shape(N, H, W)). Indicating the real label. Support dtype: int32/int64/uint8.
- weight: A 1D tensor with shape (C) or none. Indicating the scale weight of each class. Support dtype:float32/bfloat16/float16.

## Outputs

- y: if reduction is "none", a 1D or 3D tensor with shape (N) or (N, H, W). When x is 2D(shape (N, C)), y should be 1D(shape(N)) or scalar, when x is 4D(shape(N, C, H, W)), y should be 3d(shape(N, H, W)). Otherwise, shape is (1). Support dtype: float32/bfloat16/float16.
- total_weight: A 1D tensor with shape (1). Support dtype: float32/bfloat16/float16.

## Attributes

- reduction: An optional attribute. Specifies the reduction to be applied to the output.
               Type is string. Defaults to "mean" .
- ignore_index: An optional attribute. Specifying a target that is ignored and does not affect the input gradient.
                  Type is int. Defaults to -100 . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 target: int32,int64,uint8
- input2 weight: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 total_weight: bfloat16,float16,float32
### AI CPU
- input0 x: float32
- input1 target: int32,int64
- input2 weight: float32
- output0 y: float32
- output1 total_weight: float32

## Third-party framework compatibility

Compatible with pytorch NLLLoss operator


---

[Back to Operator Specifications (Ascend950)](../README.md)
