# 环境准备

## 软件包安装

1. 根据下方软件包列表准备软件包。

    **表 1**  软件包列表

    | 组件 | 简介 |
    | --- | --- |
    | Toolkit | 开发、调测、调优工具包。主要包括算子工具、模型工具、应用工具。 |
    | Firmware | 固件包。设备上的UEFI等基础固件，通常在device生产过程烧入该软件包，但也可以在后期通过安装该包实现固件版本升级。 |
    | Driver | 驱动包。用于承载Host和Device之间的交互、调度、传输等，包含设备管理、查询驱动，图执行任务调度驱动，训练数据传输预处理驱动，AICPU算子加载执行驱动等。 |
    | PyTorch（可选） | 当使用PyTorch的Python接口编程时，需安装PyTorch框架相关的软件。<br> 说明：您可以访问[Ascend/pytorch](https://gitcode.com/Ascend/pytorch/releases)仓下载最新PyTorch软件。注意，版本建议是v5.0.rc2.1-pytorch1.11.0及以上版本，否则影响后续Dump算子json文件能力。 |

2. 安装软件包。请参考[《CANN 软件安装》](https://hiascend.com/document/redirect/CannCommunityInstSoftware)完成驱动、固件、开发套件包Ascend-cann-toolkit的安装。
3. 配置环境变量。因为算子编译工具依赖AOE，所以要配置CANN软件基础环境变量和AOE工具所需的环境变量。
    - CANN软件基础环境变量

        CANN提供进程级环境变量设置脚本，供用户在进程中引用，以自动完成环境变量设置。执行命令参考如下，以下示例均为root或非root用户默认安装路径，请以实际安装路径为准。

        ```bash
        # 以root用户安装toolkit包后配置环境变量
        source /usr/local/Ascend/cann/set_env.sh 
        # 以非root用户安装toolkit包后配置环境变量
        source ${HOME}/Ascend/cann/set_env.sh 
        ```

    - AOE工具依赖Python，以Python3.7.5为例，请以运行用户执行如下命令设置Python3.7.5的相关环境变量。

        ```bash
        # 用于设置python3.7.5库文件路径
        export LD_LIBRARY_PATH=/usr/local/python3.7.5/lib:$LD_LIBRARY_PATH
        # 如果用户环境存在多个python3版本，则指定使用python3.7.5版本
        export PATH=/usr/local/python3.7.5/bin:$PATH
        ```

        Python3.7.5安装路径请根据实际情况进行替换，您也可以将以上命令写入\~/.bashrc文件中，然后执行**source \~/.bashrc**命令使其立即生效。

    - 调优前也可参考如下示例配置其他环境变量，但为可选配置，相关说明请参考[表2](#table2)。

        ```bash
        export ASCEND_DEVICE_ID=0
        export TUNE_BANK_PATH=/home/HwHiAiUser/custom_tune_bank
        export TE_PARALLEL_COMPILER=8
        export REPEAT_TUNE=False
        ```

        > **说明：** 用户可将设置环境变量的命令写入自定义脚本，方便后续执行。

        **表 2**  环境变量说明 <a id="table2"></a>

        | 环境变量 | 说明 |
        | --- | --- |
        | ASCEND_DEVICE_ID | 通过该环境变量指定AI处理器的逻辑ID。<br>取值范围[0,N-1]，默认为0。其中N为当前物理机/虚拟机/容器内的设备总数。 |
        | TUNE_BANK_PATH | 可通过此环境变量指定调优后自定义知识库的存储路径。<br> 设置的存储路径必须为绝对路径或相对于执行AOE调优引擎所在路径的相对路径，配置的路径需要为已存在的目录，且执行用户具有读、写、可执行权限。若配置的TUNE_BANK_PATH路径不存在或用户无权限，则调优进程会报错并退出。<br>自定义知识库存放路径的优先级为：TUNE_BANK_PATH>ASCEND_CACHE_PATH>默认，TUNE_BANK_PATH和ASCEND_CACHE_PATH详细信息请参考《环境变量参考》。<br>  **算子自定义知识库**：<br> <ul><li>若不配置此环境变量，请使用`env`命令查询ASCEND_CACHE_PATH是否存在，若存在，自定义知识库存储在`${ASCEND_CACHE_PATH}/aoe_data/${soc_version}`；若不存在，自定义知识库默认存储在`${HOME}/Ascend/latest/data/aoe/custom/op/${soc_version}`。</li><br>  <li>若配置此环境变量，则调优后的最优策略存储在配置路径的`${soc_version}`。</li></ul> **说明**：<br> 在多用户共享知识库场景下，共享知识库的用户需要设置TUNE_BANK_PATH为同一路径，并且对配置的路径具有读、写权限。<br>若调优时自定义了知识库路径，后续进行模型转换时，若想直接使用自定义知识库，也需要配置此环境变量。 |
        | TE_PARALLEL_COMPILER | 算子编译所需环境变量。<br>网络模型较大时，可通过配置此环境变量，开启算子的并行编译功能。<br>TE_PARALLEL_COMPILER的值代表算子编译进程数（配置为整数），当取值大于1时开启算子的并行编译功能。开启AOE调优场景下：配置不能超过CPU核数*80%/AI处理器的个数，取值范围：1~32，默认值为8。<br>由于该环境变量能够加速算子编译，所以可以加快涉及算子编译的相关流程调优。 |
        | REPEAT_TUNE | 是否重新发起调优，此环境变量在开启子图调优或算子调优的场景下生效。<br>如果知识库（内置或者自定义）中已经存在网络模型中的调优case（针对某shape的调优策略），则会跳过此case的调优流程，若想重新发起调优，可设置此环境变量为True。例如某些算子进行了逻辑的变更，如GEMM算子新增了支持ND的输入，该情况下需要设置此环境变量后，重新发起调优。<br>取值范围：True或者False，默认值为False。 |

## 工具获取

工具所在目录：`${INSTALL_DIR}/compiler/bin/op_compiler`

\$\{INSTALL\_DIR\}请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为`/usr/local/Ascend/cann`。
