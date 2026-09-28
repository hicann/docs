# ApplyAddOutputPass 

## Description

Adds optional outputs and prechecks for operators in Table 1.

**Table 1** Supported operators

|Operator|output1|output2|output3|precheck|
|--|--|--|--|--|
|ApplyRMSProp|ms|mom|-|ApplyRmsPropPreCheck|
|FusedMulApplyMomentumWithoutAccumOut|accum|-|-|FusedMulApplyMomentumPreCheck|
|FusedMulApplyMomentumExtern|accum|-|-|FusedMulApplyMomentumExternPreCheck|
|FusedMulApplyKerasMomentum|accum|-|-|FusedMulApplyKerasMomentumPreCheck|
|ApplyAdagrad|accum|-|-|-|
|ApplyAdagradDA|gradient_accumulator|gradient_squared_accumulator|-|-|
|ApplyAdadelta|accum|accum_update|-|-|
|ApplyPowerSign|m|-|-|-|
|ApplyProximalAdagrad|accum|-|-|-|
|ApplyAdaMax|m|v|-|-|
|ApplyAdagradV2|accum|-|-|ApplyAdagradV2PreCheck|
|ApplyKerasMomentum|accum|-|-|ApplyKerasMomentumPreCheck|
|ApplyFtrlV2|accum|linear|-|-|
|ApplyMomentum|accum|-|-|-|
|ApplyFtrl|accum|linear|-|-|
|ApplyAdam|m|v|-|-|
|ApplyCenteredRMSProp|mg|ms|mom|-|
|ApplyAddSign|m|-|-|-|
|ApplyAdamWithAmsgrad|m|v|vhat|-|

## Constraints

None

## Applicable Products

<!-- npu="910b" id1 -->
Atlas A2 training products/Atlas A2 inference products
<!-- end id1 -->
