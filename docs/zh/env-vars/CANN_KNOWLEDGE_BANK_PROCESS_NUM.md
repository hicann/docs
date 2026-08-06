# CANN_KNOWLEDGE_BANK_PROCESS_NUM

## 功能描述

CANN_KNOWLEDGE_BANK_PROCESS_NUM用于设置知识库管理模块查询知识库的进程数。

取值范围\[0, 8\]。默认值8（即在算子编译阶段，默认会启动8个进程查询知识库）。

启动的进程数越多，消耗的host内存越多，编译越快。

启动的进程数越少，消耗的host内存越少，编译越慢。

当CANN_KNOWLEDGE_BANK_PROCESS_NUM=0时，表示不启动知识库管理模块，不查询知识库。

## 配置示例

```bash
export CANN_KNOWLEDGE_BANK_PROCESS_NUM=5
```

## 使用约束

无

## 支持的型号

全量芯片支持
