# 算子调优

1. Dump算子信息。

    算子调优前，需要先获取模型中算子信息统计文件（\*.json），包括算子的shape、dtype、format等信息。目前支持两种方式Dump算子json文件，请根据实际情况选择合适的方式。

    - **使用PyTorch的Python接口编程时**，可通过Ascend PyTorch Profiler接口dump算子json文件，具体介绍参见[《性能调优工具》](https://hiascend.com/document/redirect/CannCommunityToolProfiling)中“性能数据其他采集方式 \> Ascend PyTorch Profiler”。

        1. 在训练前，开启扩展参数experimental\_config中“算子信息统计功能”，即参数**record\_op\_args**置为True。

        2. 查看采集到的PyTorch训练性能数据结果文件。

            训练结束后，Dump的算子信息统计文件默认在\{worker\_name\}\_\{时间戳\}\_ascend\_pt\_op\_args/\{pid\}目录下。

    - **使用acl接口时**，可通过aclopStartDumpArgs和aclopStopDumpArgs接口将算子信息统计文件Dump到指定目录下，接口详见[《Runtime运行时 API》](https://hiascend.com/document/redirect/CannCommunityRuntimeApi)中的“Dump配置”。

2. 编译静态Kernel包。

    在任意目录下，以运行用户（如HwHiAiUser）身份执行如下静态编译命令：

    ```bash
    op_compiler --op_params_dir=<dump_dir>  --soc_version=<soc_version> --log=info --job=8 --output=<output_dir>
    ```

    关键参数释义如下，全量参数详细介绍请参考[《算子编译工具》](https://hiascend.com/document/redirect/CannCommunityopcompiler)中“**参数说明**”章节，请根据实际情况设置。

    - --op\_params\_dir：简写为-p，必选，Dump工具导出的统计数据所在的文件夹路径，支持绝对和相对路径。
    - --soc\_version：简写为-v，执行算子编译功能时必选，指定算子编译时AI处理器的型号。

        > **说明：** 如果无法确定当前设备的soc\_version，则在安装NPU驱动包的服务器执行**npu-smi info**命令进行查询，在查询到的“Name”前增加Ascend信息，例如“Name”对应取值为_xxxyy_，实际配置的soc\_version值为Ascend_xxxyy_。

    - --log：简写为-l，可选，设置算子编译过程中日志的级别。可设置为debug/info/warning/error/null级别，默认为null。
    - --job：简写为-j，可选，设置编译时工作进程数。最小取值为1，默认为16。
    - --output：简写为-o，可选，编译输出的安装包路径+名称，如xxx/xxx/xxx.run，支持相对路径和绝对路径。不输入路径的情况下，在当前路径下生成；不输入安装包名称的情况下，安装包默认命名为“static\_kernel\_$\{datetime\}\_$\{pid\}.run”。

    当出现类似如下回显信息代表编译成功。

    ```text
    generate run package static_kernel_${datetime}_${pid}.run success
    ```

    > **说明：**
    > - 算子编译工具提供了**--count**参数和-p参数配合使用，用于统计-p参数指定的目录下算子信息统计json文件的数目。
    >   样例如下：
    >
    >   ```bash
    >   op_compiler -p <dump_dir> --count
    >   ```
    >
    >   只有动态shape才能dump出算子统计信息，安装静态Kernel包后，静态Kernel包对应算子的统计信息就不会dump出来。所以在安装静态Kernel包后，如果网络有调整，可以通过调整前后dump的json文件的数量来判断静态Kernel包和当前网络是否匹配。
    >   通过调整网络前后，各执行一次dump操作，并通过`--count`命令来统计dump生成的json文件的数目，如果调整后的数目比调整前
    >   大，则说明静态Kernel包中有部分算子不再匹配当前网络，此时开发者可以：
    >
    >   - 卸载静态Kernel包，重新走dump流程，编译安装新的静态Kernel包。
    >   - 仍使用当前静态Kernel包，此时需要注意不匹配的算子会走动态流程，得不到性能收益。
    > - 不支持在**dump\_dir**下执行编译命令。

3. 安装静态Kernel包。

    进入static\_kernel\_$\{datetime\}\_$\{pid\}.run包所在目录，以运行用户（如HwHiAiUser）身份运行run包：

    ```bash
    ./static_kernel_${datetime}_${pid}.run
    ```

    当出现如下回显信息代表安装成功。

    ```text
    Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
    Uncompressing STATIC KERNEL RUN PACKAGE  100%
    ```

    目前暂不支持指定目录安装，run包默认安装到`{install_path}/opp/static_kernel`路径下，其中$\{install\_path\}为CANN软件安装后文件存储路径，请根据实际情况替换该路径。

    > **说明：** run包默认安装路径\$\{install\_path\}/opp/static\_kernel的默认权限为770（本用户、同组用户访问）。如果权限不足导致静态Kernel包安装失败，可联系CANN软件包的安装用户修改static\_kernel目录权限来解决。

    run包安装后的目录结构样例如下：

    ```text
    |-- ${install_path}/opp/static_kernel
        |-- ai_core
            |-- config
               |-- ascendxxxx
                   |-- binary_info_config.json             # 全量静态Kernel包的总索引
            |-- config.ini                                 # 记录安装顺序的配置文件。
            |-- static_kernel_250924103634186357_988879    # 时间戳为“250924103634186357”且进程号为"988879"的静态Kernel文件
               |-- ascendxxxx
               |   |-- Add                                 # 算子二进制目录
               |      |-- static_kernel_Add_float16_NCL_xxxx_d0.json
               |      |-- static_kernel_Add_float16_NCL_xxxx_d1.json
               |      |-- static_kernel_Add_float16_NCL_xxxx_d0.o
               |      |-- static_kernel_Add_float16_NCL_xxxx_d1.o
               |   |-- xxxx
               |      |-- static_kernel_xxx.json
               |      |-- static_kernel_xxx.o
               |   |-- ......
               |-- config                              # 单个静态Kernel包索引
               |   |-- ascendxxxx
               |       |-- binary_info_config.json
               |-- scripts                             # 工具涉及的通用脚本
               |   |-- ......
               |-- uninstall.sh                        # 单包卸载脚本
            |-- static_kernel_xxxx                     # 不同时间戳的静态Kernel文件
            |-- uninstall.sh                           # 全量卸载脚本
            |-- version.info                           # 版本信息
    ```

    > **说明：** 支持多个Kernel包安装，如果多个包中存在相同的算子Kernel，以后安装的Kernel包为准。

4. （可选）当不再需要静态Kernel包时，可以单包卸载或全量卸载。
    - 单包卸载

        进入static\_kernel\_$\{datetime\}\_$\{pid\}.run包的安装目录，以运行用户（如HwHiAiUser）身份运行uninstall.sh。

        ```bash
        cd ${install_path}/opp/static_kernel/ai_core/static_kernel_${datetime}_${pid}
        ./uninstall.sh
        ```

        卸载成功，ai\_core目录下static\_kernel\_$\{datetime\}\_$\{pid\}文件夹将会被删除。

    - 全量卸载

        进入`${install_path}/opp/static_kernel/ai_core`目录下，以运行用户（如HwHiAiUser）身份运行uninstall.sh。

        ```bash
        cd ${install_path}/opp/static_kernel/ai_core/
        ./uninstall.sh
        ```

        卸载成功，ai\_core目录下所有内容将会被删除，所有已安装的Kernel包均被卸载。
