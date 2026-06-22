# ASCEND\_DUMP\_SCENE

## 功能描述

在复现问题场景时，使用该环境变量开启异常算子Dump，导出异常算子的输入输出数据、workspace信息和Tiling信息。

支持如下取值：

- aic\_err\_brief\_dump：表示轻量化exception dump，用于导出AI Core错误算子的输入&输出、workspace数据。
- aic\_err\_norm\_dump：表示普通exception dump，在轻量化exception dump基础上，还会导出Shape、Data Type、Format以及属性信息。
- aic\_err\_detail\_dump：在轻量化exception dump基础上，还会导出AI Core的内部存储、寄存器以及调用栈信息。

    配置该选项时，有以下注意事项：

  - 该选项仅支持以下型号：

    <!-- npu="910b" id1 -->
    Atlas A2 训练系列产品/Atlas A2 推理系列产品
    <!-- end id1 -->
    <!-- npu="A3" id2 -->
    Atlas A3 训练系列产品/Atlas A3 推理系列产品
    <!-- end id2 -->

  - 导出dump文件过程中，会暂停问题算子所在的AI Core，因此可能会影响Device上其他业务进程的正常执行，导出dump文件后，会自行恢复AI Core。
  - 导出dump文件后，会强制退出Host侧用户业务进程，强制退出过程中的报错可不作为AI Core问题分析的输入。
  - 配置aic\_err\_detail\_dump选项后，如果生成了dump文件，但不是\*.core文件，则表示aic\_err\_detail\_dump对应的功能没有启动成功，系统自动切换为按aic\_err\_brief\_dump选项进行dump。

## 配置示例

```bash
export ASCEND_DUMP_SCENE=aic_err_brief_dump
```

## 使用约束

- 开启异常算子Dump功能有多种方式，优先级从高到低依次为：ASCEND\_DUMP\_SCENE环境变量 \> NPU\_COLLECT\_PATH环境变量 \> 配置文件（aclInit接口、aclmdlSetDump接口）。
- 通过此环境变量导出的dump信息存储路径，优先级从高到低依次为：ASCEND\_DUMP\_PATH环境变量 \> ASCEND\_WORK\_PATH环境变量 \> 默认路径（应用程序的当前执行目录）。

## 支持的型号

<!-- npu="910" id1 -->
Atlas 训练系列产品
<!-- end id1 -->
<!-- npu="310p" id2 -->
Atlas 推理系列产品
<!-- end id2 -->
<!-- npu="910b" id3 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id3 -->
<!-- npu="A3" id4 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id4 -->
<!-- npu="950" id5 -->
Ascend 950PR/Ascend 950DT
<!-- end id5 -->
<!-- npu="310b" id6 -->
Atlas 200I/500 A2 推理产品
<!-- end id6 -->
<!-- npu="IPV350" id7 -->
IPV350
<!-- end id7 -->
<!-- @ref: runtime/res/docs/05_env-vars/ASCEND_DUMP_SCENE_res.md#id1 -->
