# StringUpper

```c
REG_OP(StringUpper)
    .INPUT(input, TensorType({DT_STRING}))
    .OUTPUT(output, TensorType({DT_STRING}))
    .ATTR(encoding, String, "")
    .OP_END_FACTORY_REG(StringUpper)
```

## Brief

Inputs to TensorFlow operations are outputs of another TensorFlow operation.
This method is used to obtain a symbolic handle that represents the computation of the input.

## Inputs

include:
input:A Tensor of type string. The text to be processed.

## Outputs

output:A Tensor of type string.

## Attributes

encoding:An optional string. Defaults to "".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: string
- output0 output: string


---

[Back to Operator Specifications (Ascend950)](../README.md)
