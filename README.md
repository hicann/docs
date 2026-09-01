# CANN产品文档

## 简介

本仓库托管[CANN文档中心](https://www.hiascend.com/cann/document)公共文档的源文件，而与各组件密切关联的文档则由各组件仓库单独维护。

## 贡献

欢迎您参与文档贡献！详细请参考[贡献指南](./CONTRIBUTION.md)，请您务必遵守文档写作规范，并按照流程规则提交。如果您对文档有任何意见或建议，请在Issues中提交。

## 目录说明

关键目录结构如下：

```txt
docs/
├── docs/                       # 文档
│   ├── app-dev                 # 应用开发
│   ├── env-vars                # 环境变量参考
│   ├── ops-lib                 # 算子库公共
│   └── troubleshooting         # 故障处理
└── README.md                   # 本文件
```

## CANN产品文档源文件

下面提供[CANN文档中心](https://www.hiascend.com/cann/document)中所有已开源文档的源文件路径。

### 编程指南

- [Ascend C算子开发](https://gitcode.com/cann/asc-devkit/blob/9.2.0-beta.2/docs/zh/guide/index.md)
- [PyPTO算子开发](https://gitcode.com/cann/pypto/blob/9.2.0-beta.2/docs/zh/tutorials/index_hiascend.md)
- [通信算子开发](https://gitcode.com/cann/hcomm/blob/9.2.0-beta.2/docs/zh/comm_op_dev_guide/README.md)
- [应用开发](https://gitcode.com/cann/docs/blob/9.2.0-beta.2/docs/zh/app-dev/00_acl_cpp_dev.md)
- [图开发](https://gitcode.com/cann/ge/blob/9.2.0-beta.2/docs/zh/user_guides/graph_dev/README.md)

### API参考

- [Ascend C API](https://gitcode.com/cann/asc-devkit/blob/9.2.0-beta.2/docs/zh/api/README.md)
- [PyPTO API](https://gitcode.com/cann/pypto/blob/9.2.0-beta.2/docs/zh/api/index_hiascend.md)
- [Runtime运行时API](https://gitcode.com/cann/runtime/blob/9.2.0-beta.2/docs/zh/api_ref/README.md)
- [图引擎API](https://gitcode.com/cann/ge/blob/9.2.0-beta.2/docs/zh/api/graph_engine_api/README.md)
- [算子库](https://gitcode.com/cann/docs/blob/9.2.0-beta.2/docs/zh/ops-lib/0_README.md)
- [HCCL集合通信库](https://gitcode.com/cann/hccl/blob/9.2.0-beta.2/docs/zh/user_guide/README.md)
- [HIXL单边通信库](https://gitcode.com/cann/hixl/blob/9.2.0-beta.2/docs/zh/guide/README.md)

### 开发工具

- [ATC离线模型编译工具](https://gitcode.com/cann/ge/blob/9.2.0-beta.2/docs/zh/user_guides/atc_tools/README.md)
- [性能调优工具](https://gitcode.com/cann/oam-tools/blob/9.2.0-beta.2/docs/zh/profiling/README.md)
- [HCCL性能测试工具](https://gitcode.com/cann/oam-tools/blob/9.2.0-beta.2/docs/zh/hccl_test/README.md)

### 编译器

- [PTO虚拟指令集](https://gitcode.com/cann/pto-isa/blob/9.2.0-beta.2/docs/menu_ops_development.md)

### 参考

- [故障处理](https://gitcode.com/cann/docs/blob/9.2.0-beta.2/docs/zh/troubleshooting/00_troubleshooting.md)
- [日志参考](https://gitcode.com/cann/runtime/blob/9.2.0-beta.2/docs/zh/log_ref/README.md)
- [环境变量参考](https://gitcode.com/cann/docs/blob/9.2.0-beta.2/docs/zh/env-vars/README.md)
- [基础数据结构和接口](https://gitcode.com/cann/metadef/blob/9.2.0-beta.2/docs/api/README.md)

### 其他

- [LLM DataDist开发](https://gitcode.com/cann/ge/blob/9.2.0-beta.2/docs/zh/user_guides/llm_datadist/index.md)
- [DataFlow开发](https://gitcode.com/cann/ge/blob/9.2.0-beta.2/docs/zh/user_guides/dflow/index.md)
