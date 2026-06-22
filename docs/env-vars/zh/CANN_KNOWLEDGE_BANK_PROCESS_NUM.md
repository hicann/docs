# CANN\_KNOWLEDGE\_BANK\_PROCESS\_NUM

## 功能描述

CANN\_KNOWLEDGE\_BANK\_PROCESS\_NUM用于设置知识库管理模块查询知识库的进程数。

取值范围\[0, 8\]。默认值8（即在算子编译阶段，默认会启动8个进程查询知识库）。

启动的进程数越多，消耗的host内存越多，编译越快。

启动的进程数越少，消耗的host内存越少，编译越慢。

当CANN\_KNOWLEDGE\_BANK\_PROCESS\_NUM=0时，表示不启动知识库管理模块，不查询知识库。

## 配置示例

```bash
export CANN_KNOWLEDGE_BANK_PROCESS_NUM=5
```

## 使用约束

无

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
<!-- @ref: docs/res/env-vars/zh/CANN_KNOWLEDGE_BANK_PROCESS_NUM_res.md#id1 -->
