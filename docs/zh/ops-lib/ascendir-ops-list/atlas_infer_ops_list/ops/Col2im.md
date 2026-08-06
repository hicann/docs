# Col2im

```c
REG_OP(Col2im)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(output_size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(kernel_size, ListInt)
    .REQUIRED_ATTR(dilation, ListInt)
    .REQUIRED_ATTR(padding, ListInt)
    .REQUIRED_ATTR(stride, ListInt)
    .OP_END_FACTORY_REG(Col2im)
```

## Brief

Performs Col2im for each batch entry.

## Inputs

- x: A tensor. Must be one of the following types: float16, float32, bfloat16. 4-D, shape: `(n, c, kernel_h*kernel_w, ho*wo)`.
where ho = (output_h + 2 * padding_h - dilation_h * (kernel_h - 1) - 1) // stride_h + 1
and wo = (output_w + 2 * padding_w - dilation_w * (kernel_w - 1) - 1) // stride_w + 1
- output_size: The img shape tensor. Must be int32, 1-D, shape:`(2)`, value: (output_h, output_w).

## Outputs

y: A tensor. Must be one of the following types: float32, float16, bfloat16. 4-D, shape: `(n, c, output_h, output_w)`.

## Attributes

- kernel_shape: A listInt. Must be int64, 1-D, shape:`(2)`. value: `(kernel_h, kernel_w)`, the shape of kernel in convolution.
- dilation: A listInt. Must be int64, 1-D, shape:`(2)`. value: `(dilation_h, dilation_w)`, the dilation in convolution.
- padding: A listInt. Must be int64, 1-D, shape:`(2)`. value: `(padding_h, padding_w)`, the padding in convolution.
- stride: A listInt. Must be int64, 1-D, shape:`(2)`. value: `(stride_h, stride_w)`, the stride in convolution, value of stride should be greater than zero.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 output_size: int32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with PyTorch torch.nn.Fold operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
