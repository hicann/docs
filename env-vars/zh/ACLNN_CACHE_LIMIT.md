# ACLNN_CACHE_LIMIT

## 功能描述

此环境变量用于配置aclnn API在Host侧缓存的算子信息条目个数。缓存的算子信息包含workspace大小、算子计算的执行器、Tiling信息等。

单位：个，取值范围：\[0,10000000\]，默认值为10000。当取值为0时，表示不开启算子信息缓存功能。

**一般不建议设置ACLNN_CACHE_LIMIT环境变量，保持默认值即可。**针对动态shape场景，若算子的shape范围较大，开发者可结合业务需求适当增加此环境变量取值，以增加算子缓存条目，从而提升调度性能。但需要注意，增加算子信息缓存条目会增加Host内存开销，具体请参见[使用约束](#使用约束)。

## 配置示例

```bash
export ACLNN_CACHE_LIMIT=10000
```

## 使用约束

- 单算子的缓存按线程管理，线程之间使用不同的缓存，互不影响。ACLNN_CACHE_LIMIT配置的是每个线程的算子缓存条目个数。因此线程越多，算子缓存条目越多。

    每个算子缓存条目大约占2KB左右的Host内存，单算子cache的总内存占用大小为：ACLNN_CACHE_LIMIT \* 线程数 \* 2KB。

    以10个线程，ACLNN_CACHE_LIMIT=100000为例，这种情况下单算子cache的总内存占用为：10\*100000\*2KB=2GB。

- 融合算子（大kernel算子）的缓存在进程级单独的内存池管理，单条cache占约20KB左右的Host内存，融合算子cache的总内存占用是：ACLNN_CACHE_LIMIT \* 20KB。
- 使用者应结合Host的内存总大小、线程数以及每一个算子缓存条目的大小合理地设置ACLNN_CACHE_LIMIT，设置过大可能导致Host内存占用过多，造成调度性能下降。

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->

<!-- npu="910" id2 -->
Atlas 训练系列产品
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
