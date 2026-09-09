# OP_PCIE_THROUGH_ACCESS_HOST_MEM_CHECK_ENABLE

## 功能描述

PCIe through是Ascend NPU硬件能力，允许Device侧算子通过PCIe总线直接访问Host内存，从而减少数据搬运开销。

该环境变量用于使能PCIe through特性的地址检测：配置并生效后，单算子执行时会校验各Tensor的data地址是否落在PCIe地址段范围内。命中PCIe地址段的算子将使能PCIe through特性。

取值为：

- 1：使能PCIe through特性的地址检测。
- 其他取值（含 0）或未配置：关闭该特性（默认关闭）。

## 配置示例

```bash
export OP_PCIE_THROUGH_ACCESS_HOST_MEM_CHECK_ENABLE=1
```

## 使用约束

互联方式要求：仅当Host与Device通过PCIe互联时该特性才能生效；若非PCIe互联（如：HCCS、UB），即使配置了该环境变量，特性也不生效。

算子支持说明：Ascend NPU芯片中仅有两条访存指令原生支持PCIe through访问。开启本环境变量后，支持PCIe through的算子会自动选择使用这两条指令对应的计算模板，以确保访存路径满足硬件要求。当前PCIe through特性为部分算子支持，若使用的算子不在支持范围内，即使开启本环境变量，算子运行也可能会发生AI Core Error。建议在使用前确认目标算子是否已适配该特性。

性能提示：开启地址检测会引入额外的内存校验开销，可能增加Host侧的性能负担，按需使用即可。

功能提示：DataDump功能暂未支持PCIe through场景，因此使能PCIe through后暂不支持DataDump。

## 支持的型号

<!-- npu="950" id1 -->
Ascend 950PR/Ascend 950DT
<!-- end id1 -->
