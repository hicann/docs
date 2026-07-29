# ASCEND_CACHE_PATH

## 功能描述

若开发者期望编译运行过程中产生的文件落盘到统一路径，可通过此环境变量设置**共享文件**的存储路径，各组件编译运行过程中产生的可共享文件会存储到此环境变量定义的路径中。

- 路径支持大小写字母（a-z，A-Z）、数字（0-9）、下划线（_）、中划线（-）、句点（.）、中文字符。
- 需要确保指定的路径存在且有效，执行用户具有读、写、执行权限。

**${ASCEND_CACHE_PATH}路径下的文件包括：**

- **${ASCEND_CACHE_PATH}/aoe_data**：AOE调优知识库文件，支持多机共享。

  优先级说明：

  TUNE_BANK_PATH> ASCEND_CACHE_PATH> 默认知识库路径

- **${ASCEND_CACHE_PATH}/kernel_cache**：算子编译缓存文件，支持单机多卡共享。

  以下场景提供了设置算子编译缓存文件存储路径的参数或接口，其优先级高于ASCEND_CACHE_PATH环境变量，详细描述如下：
  - 使用ATC工具进行离线模型编译的场景参数
  
    “--op_compiler_cache_dir” > ASCEND_CACHE_PATH  > 默认路径（$HOME/atc_data）
  - 使用AscendCL接口构建或编译模型的场景
  
    - 构图接口“aclgrphBuildInitialize”中参数“OP_COMPILER_CACHE_DIR”> ASCEND_CACHE_PATH  > 默认路径（$HOME/atc_data）
    - 构图接口“aclgrphBuildModel”中参数“OP_COMPILER_CACHE_DIR”> ASCEND_CACHE_PATH  > 默认路径（$HOME/atc_data）
    - 应用编译接口“aclCompileOpt”中编译选项“ACL_OP_COMPILER_CACHE_DIR” > ASCEND_CACHE_PATH  > 默认路径（$HOME/atc_data）
    <!-- npu="950,A3,910b,910,310p" id1 -->
  - TensorFlow网络训练或在线推理场景TF Adapter配置参数“op_compiler_cache_dir”> ASCEND_CACHE_PATH  > 默认路径（$HOME/atc_data）。
    <!-- end id1 -->

## 配置示例

```bash
export ASCEND_CACHE_PATH=/repo/task001/cache
```

## 使用约束

- 共享存储需要支持Linux文件锁（如NFSv4、OceanStor Pacific 9950和OceanStor Pacific 9550 ），对于不支持Linux文件锁的存储（如NFSv3），建议存储到本地目录。
- 多服务器场景下，各机器上的AI处理器型号以及固件驱动与CANN软件版本需要保持一致。

## 支持的型号

全量芯片支持
