# ASCEND_DUMP_PATH

## 功能描述

指定异常算子Dump信息的存储路径，可配置为绝对路径或执行程序的相对路径。指定的路径支持大小写字母（a-z，A-Z）、数字（0-9）、下划线（_）、中划线（-）、句点（.）、中文字符，执行用户需具有读、写、执行权限，若路径不存在，系统会自动创建该路径中的目录。不指定路径时，异常算子Dump信息默认存放在应用程序的当前执行目录。

使用该环境变量需关注以下事项：

- 通过ASCEND_DUMP_SCENE环境变量开启异常算子Dump时，优先级从高到低依次为：ASCEND_DUMP_PATH环境变量 \> ASCEND_WORK_PATH环境变量 \> 默认路径（应用程序的当前执行目录）。
- 通过配置文件（aclInit接口、aclmdlSetDump接口）开启异常算子Dump时，优先级从高到低依次为：ASCEND_DUMP_PATH环境变量 \> ASCEND_WORK_PATH环境变量 \> 配置文件路径（dump_path字段）\> 默认路径（应用程序的当前执行目录）。
- 设置该环境变量，默认自动开启算子Kernel数据Dump功能。Dump信息存储路径优先级从高到低依次为：ASCEND_DUMP_PATH环境变量 \> ASCEND_WORK_PATH环境变量 \> 配置文件路径（dump_path字段）。

## 配置示例

```bash
export ASCEND_DUMP_PATH=/repo/task001
```

## 使用约束

- 开启异常算子Dump时，该环境变量需要和ASCEND_DUMP_SCENE配合使用。
- 开启算子Kernel数据Dump时，只需要配置该环境变量。

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
<!-- @ref: runtime/res/docs/05_env-vars/ASCEND_DUMP_PATH_res.md#id1 -->
