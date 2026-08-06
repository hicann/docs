# DeformableOffsetsGrad

```c
REG_OP(DeformableOffsetsGrad)
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(offsets, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(grad_x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(grad_offsets, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .REQUIRED_ATTR(ksize, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(data_format, String, "NCHW")
    .ATTR(deformable_groups, Int, 1)
    .ATTR(modulated, Bool, true)
    .OP_END_FACTORY_REG(DeformableOffsetsGrad)
```

## Brief

Computes the gradients of DeformableOffsets with respect to input and offsets

## Inputs

Three inputs:
- grad: A Tensor of type float16,float32, bfloat16. gradients with respect to DeformableOffsets output
- x: A Tensor of type float16,float32,bfloat16.
- offsets: A Tensor of type float16,float32,bfloat16.Deformation offset parameter.

## Outputs

- grad_x: A Tensor of type float16, float32, bfloat16. Gradients with respect to input_x
- grad_offsets: A Tensor of type float16, float32, bfloat16. Gradients with respect to input_offsets
     out_height = (in_height + pad_top + pad_bottom -
                   (dilation_h * (ksize_height - 1) + 1))
                  / stride_h + 1
     out_width = (in_width + pad_left + pad_right -
                  (dilation_w * (ksize_width - 1) + 1))
                 / stride_w + 1

## Attributes

- strides: A tuple/list of 4 integers.The stride of the sliding window for
height and width for H/W dimension.
- pads: A tuple/list of 4 integers.Padding added to H/W dimension
of the input.
- ksize: A tuple/list of 2 integers.kernel size.
- dilations: A tuple/list of 4 integers, The dilation factor for each dimension
of input.  Defaults to [1, 1, 1, 1]
- data_format: An optional string from: "NCHW", "NHWC". Defaults to "NCHW". Specify the data format of the input x.
- deformable_groups: Specify the c-axis grouping number of input x.
- modulated: Specify version of DeformableConv2D, true means v2, false means v1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: bfloat16,float32
- input1 x: bfloat16,float32
- input2 offsets: bfloat16,float32
- output0 grad_x: float32
- output1 grad_offsets: float32
### AI CPU
- input0 grad: float16,float32
- input1 x: float16,float32
- input2 offsets: float16,float32
- output0 grad_x: float16,float32
- output1 grad_offsets: float16,float32

## Attention Constraints

Multiplying the H/W of offsets by the H/W of ksize equals the H/W of grad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
