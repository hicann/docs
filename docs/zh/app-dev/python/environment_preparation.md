# 环境准备

**开发应用前，需安装NPU固件和NPU驱动及CANN软件（Toolkit开发者套件包、CANN ops算子包）**，请参见[《CANN软件安装》](https://hiascend.com/document/redirect/CannCommunityInstSoftware)部署环境。

- 部署开发环境后，才能获取调用接口所需的依赖、运行Python代码文件。

    对于昇腾设备，已安装驱动、固件场景下，该环境可直接作为运行环境，执行包含pyacl接口的Python代码文件。

    对于非昇腾设备，开发环境部署后**不可直接执行**包含pyacl接口的Python代码文件，开发完成后，可将Python代码文件上传至**已部署运行环境的昇腾设备环境**中执行验证。

- 部署运行环境后，才能在运行环境上执行Python代码文件。

## 设置生成文件落盘路径

（可选）通过环境变量“ASCEND\_CACHE\_PATH”、“ASCEND\_WORK\_PATH”设置应用运行过程中产生的文件的落盘路径，涉及ATC模型转换、AOE模型智能调优、性能数据采集、日志采集等功能，落盘文件包括知识库文件、调优结果文件、性能数据文件、日志文件等。

配置示例如下，详细配置说明请参见[《环境变量参考》](https://hiascend.com/document/redirect/CannCommunityEnvRef)：

```bash
export ASCEND_CACHE_PATH=/repo/task001/cache
export ASCEND_WORK_PATH=/repo/task001/172.16.1.12_01_03
```

## pyacl的依赖

- pyacl没有安装依赖，但是有运行依赖。详情请参见[《CANN软件安装》](https://hiascend.com/document/redirect/CannCommunityInstSoftware)。
- 生成pyacl中的“acl.so”依赖的Python版本范围为3.7.5 \~ 3.13.9。

## 安装后的环境变量设置

**在安装完CANN软件包之后，请务必自行配置以下环境变量，否则，将无法正常使用**“import acl”。

<!-- npu="910b,910,310p,310b" id1 -->
若环境中安装了cann-toolkit和ops软件包：

```bash
# 以root用户安装CANN软件包
. /usr/local/Ascend/cann/set_env.sh
# 以非root用户安装CANN软件包
. ${HOME}/Ascend/cann/set_env.sh
```
<!-- end id1 -->
设置完环境变量后，在Python脚本中加入“import acl”，就可以使用pyacl中的函数了。
