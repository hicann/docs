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
│   └── ops-lib                 # 算子库公共
└── README.md                   # 本文件
```

## CANN产品文档源文件

下面提供[CANN文档中心](https://www.hiascend.com/cann/document)中所有已开源文档的源文件路径。

### 编程指南

- [Ascend C算子开发](https://gitcode.com/cann/asc-devkit/blob/master/docs/guide/index.md)
- [PyPTO算子开发](https://gitcode.com/cann/pypto/blob/master/docs/zh/tutorials/index_hiascend.md)
- [通信算子开发](https://gitcode.com/cann/hcomm/blob/master/docs/zh/comm_op_dev_guide/README.md)
- [应用开发](docs/app-dev/zh/00_acl_cpp_dev.md)

### API参考

- [Ascend C API](https://gitcode.com/cann/asc-devkit/blob/master/docs/api/README.md)
- [PyPTO API](https://gitcode.com/cann/pypto/blob/master/docs/zh/api/index_hiascend.md)
- [HCCL集合通信库](https://gitcode.com/cann/hccl/blob/master/docs/zh/user_guide/README.md)
- [算子库](docs/ops-lib/README.md)
