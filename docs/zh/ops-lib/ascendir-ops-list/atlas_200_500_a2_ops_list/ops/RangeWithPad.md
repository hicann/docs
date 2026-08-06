# RangeWithPad

```c
REG_OP(RangeWithPad)
    .INPUT(start, TensorType({DT_FLOAT16, DT_INT16, DT_INT32, DT_INT8}))
    .INPUT(limit, TensorType({DT_FLOAT16, DT_INT16, DT_INT32, DT_INT8}))
    .INPUT(delta, TensorType({DT_FLOAT16, DT_INT16, DT_INT32, DT_INT8}))
    .INPUT(pad_value, TensorType({DT_FLOAT16, DT_INT16, DT_INT32, DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_INT16, DT_INT32, DT_INT8}))
    .ATTR(max_element_num, Int, 10000)
    .OP_END_FACTORY_REG(RangeWithPad)
```

## Brief

Creates a sequence of numbers.

## Inputs

start: A 0D Tensor (scalar) of type float16, int16, int32 or int8.
  The initial value of the range sequence, format supports ND.
limit: A 0D Tensor (scalar) of type float16, int16, int32 or int8.
  Upper limit of sequence, exclusive, format supports ND.
delta: A 0D Tensor (scalar) of type float16, int16, int32 or int8.
  Number that increments "start", format supports ND.
pad_value: A 0D Tensor (scalar) of type float16, int16, int32 or int8.
  For excess parts, the value of this input should be used to fill in. 

## Outputs

y: A 1D tensor which is the sequence of numbers, format supports ND.
   The supported types are:float16, int16, int32 or int8. 
   The types of start/limit/delta and output should be the same. 

## Attributes

max_element_num: An optional attribute of type int, representing the size of the output. 
Users need to ensure that the attribute value is greater than or equal to the actual range sequence size. 
Default value is 10000. 

## Quantization supported or not

Not supported

## Quantized inference supported or not

Not supported

## Multiple batches supported or not

Supported
@see Range()
@since V100R001C33


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
