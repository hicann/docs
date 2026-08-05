# StaticRegexReplace

```c
REG_OP(StaticRegexReplace)
    .INPUT(input, TensorType({DT_STRING}))
    .OUTPUT(output, TensorType({DT_STRING}))
    .ATTR(pattern, String, "")
    .ATTR(rewrite, String, "")
    .ATTR(replace_global, Bool, true)
    .OP_END_FACTORY_REG(StaticRegexReplace)
```

## Brief

Replaces the match of pattern in input with rewrite. 

## Inputs

include:
input:A Tensor of type string. The text to be processed. 

## Outputs

output: A Tensor of type string.

## Attributes

- pattern:An optional string. The regular expression to match the input.
- rewrite:An optional string. The rewrite to be applied to the matched expression.
- replace_global:An optional bool. Defaults to True. If True, the replacement is global,
otherwise the replacement is done only on the first match.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: string
- output0 output: string


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
