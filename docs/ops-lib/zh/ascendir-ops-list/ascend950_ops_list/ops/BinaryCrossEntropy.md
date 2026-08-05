# BinaryCrossEntropy

```c
REG_OP(BinaryCrossEntropy)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(output, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(BinaryCrossEntropy)
```

## Brief

Creates a criterion that measures the Binary Cross Entropy between the target and the output. 

## Inputs

Three inputs, including:
- x: A multi-dimensional tensor of type bfloat16, float16 or float32, specifying a predictive value. The value of "x" must range from 0 to 1.
- y: A multi-dimensional tensor of type bfloat16, float16 or float32, indicating a tag. The value of "y" must range from 0 to 1. Shape, dtype and format are the same as "x".
- weight: An optional multi-dimensional tensor, specifying the weight. If not null, shape, dtype and format are the same as "x"

## Outputs

output: Output loss. Has the same dimension with the inputs. When "reduction" is set to "none", a tensor with the same size as "x" is output. Otherwise, a scalar is output. 

## Attributes

reduction: A string specifying the reduction type to apply to the output, which must be one of: "none", "sum", or "mean". Defaults to "mean". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 y: bfloat16,float16,float32
- input2 weight: bfloat16,float16,float32
- output0 output: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch operator BCELoss.


---

[Back to Operator Specifications (Ascend950)](../README.md)
