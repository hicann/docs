# FixPipeAbilityProcessPass

## Description

Adds the `support_fixpipe_ability` attribute to a Fixpipe node. This attribute has the following enumerated values:

- `1`: The Conv2D and DepthwiseConv2D operators support Fixpipe dual outputs when the number of outputs is 2.
- `2`: Conv2DBackpropFilterD and DepthwiseConv2DBackpropFilterD use atomic write.
- `3`: Fixpipe processing is not supported.

## Constraints

This fusion pattern cannot be disabled.

The validity of this pass depends on whether the running product supports the corresponding operator type. For details, see [Ascend IR Operator Specifications](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/latest/API/aolapi/operatorlist_00094.html) in the operator library.

## Applicable Products

<!-- npu="910b" id1 -->
Atlas A2 training products/Atlas A2 inference products
<!-- end id1 -->

<!-- npu="950" id2 -->
950PR/950DT
<!-- end id2 -->
