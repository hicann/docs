# GenADC

```c
REG_OP(GenADC)
    .INPUT(query, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(code_book, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(centroids, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(bucket_list, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(adc_tables, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(distance_type, String, "l2sqr")
    .OP_END_FACTORY_REG(GenADC)
```

## Brief

Generate ADC(asymmetric distance computation) table. 

## Inputs

Four inputs, including:
- query: A 1D Tensor of type float16 or float32, with shape [D,].
The format of the tensor is ND. The support value of D is in range(start=16, end=1024, step=16).
If D is greater than 128, it should be a multiple of 128.
- code_book: A 3D Tensor of type float16 or float32, with shape [M, ksub, dsub].
Support values are as follows:
M = D / dsub, and M is a multiple of 8;
ksub in {256, 512};
dsub in {2, 4, 8}.
The format of the tensor is ND.
- centroids: A 2D Tensor of type float16 or float32 with shape [nc, D]. The format of the tensor is ND.
The value of nc is in range(start=1, end=1e7, step=1). The value of D is the same as query.
- bucket_list: A 1D Tensor of type int32 or int64, with shape [ns,]. The format of the tensor is ND.
The value of ns is in range(start=1, end=nc, step=1). 

## Outputs

adc_tables: A 3D Tensor of type float16 or float32, with shape [ns, M, ksub].
Values of dimensions are the same as those of the input tensor. The format of the tensor is ND. 

## Attributes

distance_type: A optional string. The string indicates the distance type
of ADC tables. The default value is "l2sqr".
Examples: `"l2sqr", "inner_product"`.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: float16,float32
- input1 code_book: float16
- input2 centroids: float16
- input3 bucket_list: int32,int64
- output0 adc_tables: float16


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
