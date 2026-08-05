# AvgPoolGrad

```c
REG_OP(AvgPoolGrad)
    .INPUT(orig_input_shape, TensorType({DT_INT32}))
    .INPUT(input_grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(out_grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(AvgPoolGrad)
```

## Brief

Computes avgpoograd function.

## Inputs

- orig_input_shape: A tensor of type int32.
- input_grad: A tensor of type float16, float32 or double.

## Outputs

- out_grad: A mutable tensor with the same shape as the value of "orig_input_shape" and the same type as "input_grad".

## Attributes

- ksize: A required tuple or list of ints that has length >= 4,
specifying the size of the window for each dimension of the input tensor.
- strides: A required tuple or list of ints that has length >= 4,
specifying the stride of the sliding window for each dimension of the input tensor.
- padding: A required string, specifying the type of the padding algorithm to use,
either "VALID" or "SAME". With "SAME" means that the outputs will have the
same spatial dimensions as its inputs. With "VALID" means no padding.
- data_format: An optional string. Defaults to "NHWC".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 orig_input_shape: int32
- input1 input_grad: float16
- output0 out_grad: float16

## Third-party framework compatibility

- Compatible with the TensorFlow operator AvgPoolGrad.
TensorFlow operator AvgPoolGrad are difference from our operator AvgPoolGrad in
following two case:
-- kernel_h > input_h && hernel_h // 2 < input_h - 1
-- kernel_w > input_w && hernel_w // 2 < input_w - 1


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
