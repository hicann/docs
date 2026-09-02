# ApplyAddOutputPass 

## 融合模式

为表1中的算子增加可选输出和precheck。

**表 1**  支持的算子

|算子|output1|output2|output3|precheck|
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

## 使用约束

无

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
