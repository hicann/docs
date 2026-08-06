# DecodeCSV

```c
REG_OP(DecodeCSV)
    .INPUT(records, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(record_defaults, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32,
                                        DT_INT64, DT_STRING}))
    .DYNAMIC_OUTPUT(output, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32,
                                        DT_INT64, DT_STRING}))
    .ATTR(OUT_TYPE, ListType, {})
    .ATTR(field_delim, String, ",")
    .ATTR(use_quote_delim, Bool, true)
    .ATTR(na_value, String, ",")
    .ATTR(select_cols, ListInt, {})
    .OP_END_FACTORY_REG(DecodeCSV)
```

## Brief

Converts each string in the input Tensor to the specified numeric
type . 

## Inputs

Inputs include:
- records: Each string is a record/row in the csv and all records should have the
same format. 
- record_defaults: One tensor per column of the input record, with either a
scalar default value for that column or an empty vector if the column is
required. 

## Outputs

output: A Tensor. Has the same type as x. 

## Attributes

- OUT_TYPE: An optional attribute. The numeric type to interpret each string in string_tensor as.
- field_delim: An optional string. Defaults to ",". The char delimiter to separate fields in a record.
- use_quote_delim: An optional bool. Defaults to true. If false, treats double quotation marks as regular characters
inside of the string fields (ignoring RFC 4180, Section 2, Bullet 5). 
- na_value: An optional string. Defaults to ",". Additional string to recognize as NA/NaN.
- select_cols: An optional attribute that is a sorted list of column indices to select. If specified,
only this subset of columns will be parsed and returned.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 records: string
- input1 record_defaults: double,float32,int32,int64,string
- output0 output: double,float32,int32,int64,string

## Attention Constraints

The implementation for StringToNumber on Ascend uses AICPU, with bad
performance. 

## Third-party framework compatibility

- compatible with tensorflow StringToNumber operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
