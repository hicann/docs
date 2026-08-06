# StringNormalizer

```c
REG_OP(StringNormalizer)
    .INPUT(input, TensorType({DT_STRING}))
    .OUTPUT(output, TensorType({DT_STRING}))
    .ATTR(stopwords, ListString, {})
    .ATTR(is_case_sensitive, Bool, false)
    .ATTR(case_change_action, String, "NONE")
    .ATTR(locale, String, "C")
    .OP_END_FACTORY_REG(StringNormalizer)
```

## Brief

StringNormalization performs string operations for basic cleaning . 

## Inputs

input: only accepts [C] or [1, C] UTF-8 strings tensor . 

## Outputs

output: UTF-8 strings tensor after cleaning . 

## Attributes

- stopwords : list of strings (default is empty).
List of stop words. If not set, no word would be removed from input strings
tensor.
- is_case_sensitive : bool (default is false).
Boolean. Whether the identification of stop words in input strings tensor is
case-sensitive. Default is false.
- case_change_action : string (default is "NONE").
string enum that cases output to be lowercased/uppercases/unchanged. Valid
values are "LOWER", "UPPER", "NONE". Default is "NONE".
- locale : string (default is "C").
Environment dependent string that denotes the locale according to which output
strings needs to be upper/lowercased.Default C or platform specific equivalent
as decided by the implementation. 

## Attention Constraints

input can be either a 1-D or 2-D tensor, the shape of 2-D tensor must be [1, C].


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
