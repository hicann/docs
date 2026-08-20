# 安装后自动配置环境变量

描述CANN软件安装完成后，系统通过“set_env.sh”脚本默认配置的程序编译、执行相关的基础环境变量，以及后续程序编译执行时，需要手工配置的与安装包相关的环境变量。

CANN软件安装完成后，默认会自动配置程序编译、执行所依赖的基础环境变量，但用户进程结束后相关环境变量自动失效，您也可以通过如下环境变量脚本一键式配置。

```bash
# root用户安装时环境变量配置示例：
# 安装Toolkit包时
source /usr/local/Ascend/cann/set_env.sh
# 安装NNAL包ATB加速库时
source /usr/local/Ascend/nnal/atb/set_env.sh
# 安装NNAL包SiP加速库时
source /usr/local/Ascend/nnal/asdsip/set_env.sh
```

```bash
# 非root用户安装时环境变量配置示例：
# 安装Toolkit时
source ${HOME}/Ascend/cann/set_env.sh 
# 安装NNAL包时ATB加速库
source ${HOME}/Ascend/nnal/atb/set_env.sh
# 安装NNAL包SiP加速库
source ${HOME}/Ascend/nnal/asdsip/set_env.sh
```

用户也可以通过修改\~/.bashrc文件方式设置永久环境变量，操作如下：

1. 以运行用户在任意目录下执行vi \~/.bashrc命令，打开.bashrc文件，在文件最后一行后面添加上述内容。
2. 执行:wq!命令保存文件并退出。
3. 执行source \~/.bashrc命令使其立即生效。

## 环境变量说明

环境变量详细介绍参见以下内容。

- **开发套件包（Toolkit）**
  - PATH：可执行文件查找路径。
  - LD_LIBRARY_PATH：动态库的查找路径。
  - PYTHONPATH：Python搜索路径。
  - ASCEND_OPP_PATH：算子库根目录。
  - ASCEND_AICPU_PATH：AI CPU组件的安装路径。
  - TOOLCHAIN_HOME：工具链安装路径。
  - ASCEND_HOME_PATH：同ASCEND_TOOLKIT_HOME，代表Toolkit软件安装后文件存储路径。
  - ASCEND_TOOLKIT_HOME：Toolkit软件包安装后文件存储路径。
  - CMAKE_PREFIX_PATH：CMAKE的内置环境变量，用于指定CMake库配置文件路径，供'find_package ()'等命令检索。

- **神经网络加速库（NNAL）中ATB加速库**
  - ATB_HOME_PATH：ATB软件包安装后文件存储路径。
  - LD_LIBRARY_PATH：Linux系统中加载动态库时的搜寻路径列表。
  - PATH：将ATB软件包bin目录的路径添加到系统PATH环境变量中，推荐使用默认路径。
  - ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE：用于问题定位，确定报错所在的kernel。当变量配置为1时，每个Kernel的Execute结束时就做流同步。
  - ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE：用于问题定位，确定报错所在的runner。当变量配置为1时，每个Runner的Execute时就做流同步。
  - ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE：用于问题定位，确定报错所在的Operation。当变量配置为1时，每个Operation的Execute时就做同步。
  - ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT：本地kernelCache的槽位数。
    - 槽位数增加时：增加 cache 命中率，但降低检索效率。
    - 槽位数减少时：提高检索效率，但降低cache命中率。
  - ATB_OPSRUNNER_KERNEL_CACHE_GLOBAL_COUNT：全局kernelCache的槽位数。
    - 槽位数增加：增加cache命中率，但降低检索效率。
    - 槽位数减少：提高检索效率，但降低cache命中率。
  - ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE：workspace内存分配算法选择。根据环境变量配置不同，ATB会选择不同的算法去计算workspace大小与workspace分配，用户可通过选择不同算法自行测试workspace分配情况。
  - ATB_COMPARE_TILING_EVERY_KERNEL：每个Kernel运行后，比较运行前和后的NPU上tiling内容是否变化，一般用于检查是否发生tiling内存踩踏。
  - ATB_SHARE_MEMORY_NAME_SUFFIX：共享内存命名后缀，多用户同时使用通信算子时，需通过设置该值进行共享内存的区分。
  - ATB_MATMUL_SHUFFLE_K_ENABLE：Shuffle-K使能，矩阵乘的结果矩阵不同位置计算时的累加序一致/不一致。会影响matmul算子内部累加序。
  - LCCL_DETERMINISTIC：LCCL确定性AllReduce（保序加）是否开启。需注意，开启功能在rankSize<=8时生效。开启后会有如下影响：
    - 影响部分通信算子性能。
    - 影响lccl通信算子的累加序。
  - LCCL_PARALLEL：该功能和确定性计算无法同时开启，“LCCL_DETERMINISTIC”需要为0或者false。
    - 多通信域并行功能使用结束后，LCCL_PARALLEL需要设置回false，否则会导致基础场景性能下降。不支持在运行过程中修改。
    <!-- npu="910b" id2 -->
    - 该环境变量只支持AllReduce多线程并发场景使用，仅支持<trem>Atlas A2 训练系列产品</term>/<trem>Atlas A2 推理系列产品</term>8卡且数据量小于100MB。
    <!-- end id2 -->

- **神经网络加速库（NNAL）中SiP加速库**
  - ASDSIP_HOME_PATH：SiP软件包安装后文件存储路径。
  - LD_LIBRARY_PATH：Linux系统中加载动态库时的搜索路径列表。
