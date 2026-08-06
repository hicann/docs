# NLLLossGrad

```c
REG_OP(NLLLossGrad)
    .INPUT(x, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .INPUT(y_grad, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .INPUT(target, TensorType({DT_INT32, DT_INT64, DT_UINT8}))
    .INPUT(weight, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .INPUT(total_weight, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .OUTPUT(x_grad, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .ATTR(reduction, String, "mean")
    .ATTR(ignore_index, Int, -100)
    .OP_END_FACTORY_REG(NLLLossGrad)
```

## Brief

The negative log likelihood loss grad.

## Inputs

- x: A 2D or 4D tensor dtype of float32 or bfloat16 or float16 with shape (N, C) or (N, C, H, W).
- y_grad: A 1D or 3D tensor dtype of float32 or bfloat16 or float16 with shape (N) or (N, H, W) if reduction is "none". When x is 2D(shape (N, C)), y_grad should be 1D(shape(N)) or scalar, when x is 4D(shape(N, C, H, W)), y_grad should be 3d(shape(N, H, W)). Otherwise, shape is (1).
- target: Indicates the real label. A 1D or 3D tensor dtype of int32, int64 or uint8 with shape (N) or (N, H, W). When x is 2D(shape (N, C)), target should be 1D(shape(N)) or scalar, when x is 4D(shape(N, C, H, W)), target should be 3d(shape(N, H, W)).
- weight: Indicates the weight of each class. A 1D tensor dtype of float32 or bfloat16 or float16 with shape (C).
- total_weight: A 1D tensor dtype of float32 or bfloat16 or float16 with shape (1).

## Outputs

x_grad: A tensor has the same shape as "x". Must be the following type: float32, bfloat16, float16.

## Attributes

- reduction: Computation method of the loss function. An optional string. Defaults to "mean" .
- ignore_index: Specifies a target value that is ignored and does not affect the input gradient. An optional int. Defaults to -100.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 y_grad: float32
- input2 target: int32
- input3 weight: float32
- input4 total_weight: float32
- output0 x_grad: float32
### AI CPU
- input0 x: float32
- input1 y_grad: float32
- input2 target: int32,int64
- input3 weight: float32
- input4 total_weight: float32
- output0 x_grad: float32

## Third-party framework compatibility

Compatible with pytorch NLLLossGrad operator


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
