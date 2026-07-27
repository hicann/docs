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

3. 配置环境变量。

    CANN提供进程级环境变量设置脚本，供用户在进程中引用，以自动完成环境变量设置。执行命令参考如下，以下示例均为root或非root用户默认安装路径，请以实际安装路径为准。

    ```bash
    # 以root用户安装toolkit包后配置环境变量
    source /usr/local/Ascend/cann/set_env.sh
    # 以非root用户安装toolkit包后配置环境变量
    source ${HOME}/Ascend/cann/set_env.sh
    ```

## 工具获取

工具所在目录：`${INSTALL_DIR}/bin/op_compiler`

\$\{INSTALL\_DIR\}请替换为CANN软件安装后文件存储路径。以root用户为例，安装后文件默认路径为`/usr/local/Ascend/cann`。
