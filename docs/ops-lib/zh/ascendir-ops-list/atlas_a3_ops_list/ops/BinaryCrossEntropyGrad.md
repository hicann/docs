# BinaryCrossEntropyGrad

```c
REG_OP(BinaryCrossEntropyGrad)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(grad_output, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(output, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(BinaryCrossEntropyGrad)
```

## Brief

Performs the backpropagation of BinaryCrossEntropy for training scenarios .

## Inputs

Four inputs, including:
- x: A 1D or 2D Tensor of type bfloat16, float16 or float32, specifying a predictive value.
- y: A 1D or 2D Tensor of type bfloat16, float16 or float32, indicating a tag.
- grad_output: A 1D or 2D Tensor of type bfloat16, float16 or float32, specifying the backpropagation gradient.
- weight: An optional 1D or 2D Tensor of type bfloat16, float16 or float32, specifying the weight .

## Outputs

output: A 1D or 2D Tensor. When "reduction" is set to "none", a Tensor with the same size as "x" is output. Otherwise, a Scalar is output . 

## Attributes

reduction: A character string from "none", "mean", and "sum", specifying the gradient output mode. Defaults to "mean" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 y: bfloat16,float16,float32
- input2 grad_output: bfloat16,float16,float32
- input3 weight: bfloat16,float16,float32
- output0 output: bfloat16,float16,float32

## Attention Constraints

- The value of "x" must range from 0 to 1.
- The value of "y" must be "0" or "1" .

## Third-party framework compatibility

Compatible with PyTorch operator BCELossGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
