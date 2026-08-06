# StaticRegexFullMatch

```c
REG_OP(StaticRegexFullMatch)
    .INPUT(input, TensorType({DT_STRING}))
    .OUTPUT(output, TensorType({DT_BOOL}))
    .ATTR(pattern, String, "")
    .OP_END_FACTORY_REG(StaticRegexFullMatch)
```

## Brief

The input is a string tensor of any shape. The pattern is the
regular expression to be matched with every element of the input tensor.
The boolean values (True or False) of the output tensor indicate
if the input matches the regex pattern provided.

## Inputs

include:
input:A Tensor of type string. The text to be processed. 

## Outputs

output:A bool tensor with the same shape as `input`.

## Attributes

pattern:A string. The regular expression to match the input.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: string
- output0 output: bool


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
