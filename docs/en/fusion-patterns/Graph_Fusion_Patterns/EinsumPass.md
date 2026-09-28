# EinsumPass

## Description

Constructs a computational graph based on the expression of the Einsum operator. As shown in the following figure, the dotted-line nodes in the computational graph indicate that operators may be added based on the actual expression.

- For **static shapes**, there are two cases:

  Static shape and single input:

  ![](../figures/EinsumPass_1.png)

  After:

  ![](../figures/EinsumPass_2.png)

  Static shape and dual inputs (Depending on the specific expression, the two inputs of the MatMul operator may be swapped):

  ![](../figures/EinsumPass_3.png)

  After:

  ![](../figures/EinsumPass_4.png)

- For **dynamic shapes**, the graph to which the Einsum operator belongs before fusion has dual inputs, as shown in the following figure:

  ![](../figures/EinsumPass_5.png)

  Currently, 14 types of expressions are supported for dynamic shapes. The following figures show the graphs after fusion.

 1. The Einsum expression is in the form of "abc,cde->abde":

    ![](../figures/EinsumPass_6.png)

 2. The Einsum expression is in the form of "abcd,aecd->aceb" (the two inputs of the BatchMatMul operator are swapped):

    ![](../figures/EinsumPass_7.png)

 3. The Einsum expression is in the form of "abcd,adbe->acbe":

    ![](../figures/EinsumPass_8.png)

 4. The Einsum expression is in the form of "abcd,cde->abe":

    ![](../figures/EinsumPass_9.png)

 5. The Einsum expression is in the form of "abc,cd->abd":

    ![](../figures/EinsumPass_10.png)

 6. The Einsum expression is in the form of "abc,dc->abd":

    ![](../figures/EinsumPass_11.png)

 7. The Einsum expression is in the form of "abc,abd->dc" (the two inputs of the MatMulV2 operator are swapped):

    ![](../figures/EinsumPass_12.png)

 8. The Einsum expression is in the form of "abc,dec->abde":

    ![](../figures/EinsumPass_13.png)

 9. The Einsum expression is in the form of "abc,abde->dec":

    TensorB with a static shape: ![](../figures/EinsumPass_14.png)

    Tensor B with a dynamic shape:

    ![](../figures/EinsumPass_15.png)

10. The Einsum expression is in the form of "abcd,aecd->acbe":

    ![](../figures/EinsumPass_16.png)

11. The Einsum expression is in the form of "abcd,acbe->aecd":

    ![](../figures/EinsumPass_17.png)

12. The Einsum expression is in the form of "abcd,ecd->abe":

    ![](../figures/EinsumPass_18.png)

13. The einsum expression is in the form of "abcd,abe->ecd":

    Tensor A with a static shape:

    ![](../figures/EinsumPass_19.png)

    Tensor A with a dynamic shape:

    ![](../figures/EinsumPass_20.png)

14. The Einsum expression is "abcd,acbe->adbe":

    ![](../figures/EinsumPass_21.png)

    Based on whether the input shape is dynamic, the **Reshape dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_22.png)

    Based on whether the input shape is dynamic, the **Transpose dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_23.png)

- The Einsum expression is in the form of "abcd, abde->abce":

    ![](../figures/EinsumPass_24.png)

- The Einsum expression is in the form of "abcd, abce->abde":

    ![](../figures/EinsumPass_25.png)

    Based on whether the input shape is dynamic, the **Transpose dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_26.png)

- The Einsum expression is in the form of "abcd, aebd->aebc":

    ![](../figures/EinsumPass_27.png)

    Based on whether the input shape is dynamic, the **Reshape** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_28.png)

- The Einsum expression is in the form of "abcd, abce->acde":

    ![](../figures/EinsumPass_29.png)

    Based on whether the input shape is dynamic, the **Reshape** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_30.png)

- The Einsum expression is in the form of "abc, abd->acd":

    ![](../figures/EinsumPass_31.png)

    Based on whether the input shape is dynamic, the **Transpose dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_32.png)

- The Einsum expression is in the form of "ab, cb->ac":

    ![](../figures/EinsumPass_33.png)

    Based on whether the input shape is dynamic, the **Transpose dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_34.png)

- The Einsum expression is in the form of "abc, acd->abd":

    ![](../figures/EinsumPass_35.png)

- The Einsum expression is in the form of "abc, adc->abd":

    ![](../figures/EinsumPass_36.png)

    Based on whether the input shape is dynamic, the **Transpose dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_37.png)

- The Einsum expression is in the form of "abcd, ced->abce":

    ![](../figures/EinsumPass_38.png)

    Based on whether the input shape is dynamic, the **Reshape** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_39.png)

    Based on whether the input shape is dynamic, the **Transpose dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_40.png)

- The Einsum expression is in the form of "abcd, ebcd->bcae":

    ![](../figures/EinsumPass_41.png)

    Based on whether the input shape is dynamic, the **Reshape** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_42.png)

    Based on whether the input shape is dynamic, the **Transpose dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_43.png)

- The Einsum expression is in the form of "abcd, dabe->cabe":

    ![](../figures/EinsumPass_44.png)

    Based on whether the input shape is dynamic, the **Reshape** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_45.png)

- The Einsum expression is in the form of "a, b->ab":

    ![](../figures/EinsumPass_46.png)

- The Einsum expression is in the form of "abcd, aecd->eb":

    ![](../figures/EinsumPass_47.png)

    Based on whether the input shape is dynamic, the **Reshape** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_48.png)

    Based on whether the input shape is dynamic, the **Transpose dym/stc** node contains the operators shown in the following figure.

    ![](../figures/EinsumPass_49.png)

- The Einsum expression is in the form of "abcd, eb->aecd":

  ![](../figures/EinsumPass_50.png)

  Based on whether the input shape is dynamic, the **Reshape** node contains the operators shown in the following figure.

  ![](../figures/EinsumPass_51.png)

- For other dynamic shapes, there are two cases:
    1. Single-input:

        ![](../figures/EinsumPass_52.png)

        After fusion

        ![](../figures/EinsumPass_53.png)

    2. Dual-input:
        1. Scenario 1

            ![](../figures/EinsumPass_54.png)

            After fusion

            ![](../figures/EinsumPass_55.png)

            Unsqueeze, ReduceSum, and Squeeze are optional operators, and each of them may appear multiple times.

        2. Scenario 2

            ![](../figures/EinsumPass_56.png)

            After fusion

            ![](../figures/EinsumPass_57.png)

            Unsqueeze, ReduceSum, Unsqueeze/FlattenV2, Reshape, Transpose, and Squeeze are optional, and ReduceSum and Unsqueeze/FlattenV2 may appear multiple times.

## Constraints

- This fusion pattern is enabled by default and cannot be disabled.
- The Einsum operator can have only one or two inputs, and the number of elements of the input tensor cannot overflow the int64 representation range.
- For static shapes, the Einsum expression supports only a single input with a single output or dual inputs with a single output.
- For static shapes, the input or output expression cannot have duplicate dimension labels.
- For static shapes, if the fused operator is BatchMatMul, the data type of the input tensor can only be float16 or float32.
- For dynamic shapes, only 14 Einsum expressions are supported (the specific dimension label is only an example): "abc,cde->abde", "abcd,aecd->aceb", "abcd,adbe->acbe", "abcd,cde->abe", "abc,cd->abd", "abc,dc->abd", "abc,abd->dc", "abc,dec->abde", "abc,abde->dec", "abcd,aecd->acbe", "abcd,acbe->aecd", "abcd,ecd->abe", "abcd,abe->ecd", and "abcd,acbe->adbe". If the Einsum operator has only one input, the input cannot have a dynamic shape.
- For dynamic shapes, the number of input dimensions must be the same as that in the corresponding Einsum input expression.
- For dynamic shapes, the Einsum expression supports a single input with a single output, dual inputs with a single output, or empty output. The input or output expression cannot have duplicate dimension labels. A dimension label of the output must exist in the input.
- For dynamic shapes, only input tensors with a maximum of four dimensions are supported.

## Applicable Products

<!-- npu="910b" id1 -->
Atlas A2 training products/Atlas A2 inference products
<!-- end id1 -->

<!-- npu="950" id2 -->
950PR/950DT
<!-- end id2 -->
