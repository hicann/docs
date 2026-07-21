# 编译运行应用样例报错，提示找不到头文件或库文件

## 问题现象描述

获取samples仓的样例代码（以[图片分类应用](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/resnet50_imagenet_classification)为例）：

- 编译源码时，提示找不到头文件acl.h，报错片段举例如下：

    ```bash
     fatal error: acl/acl.h: No such file or directory
     #include "acl/acl.h"
              ^~~~~~~~~~~
    compilation terminated.
    CMakeFiles/main.dir/build.make:62: recipe for target 'CMakeFiles/main.dir/main.cpp.o' failed
    make[2]: *** [CMakeFiles/main.dir/main.cpp.o] Error 1
    CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/main.dir/all' failed
    make[1]: *** [CMakeFiles/main.dir/all] Error 2
    Makefile:129: recipe for target 'all' failed
    ```

- 编译源码时，提示找不到库文件libascendcl.so（报错中的-lascendcl，-l表示查找库文件，ascendcl前后分别加上lib和.so组成库文件的名称libascendcl.so），报错片段举例如下：

    ```bash
    /usr/bin/ld: cannot find -lascendcl
    collect2: error: ld returned 1 exit status
    CMakeFiles/main.dir/build.make:94: recipe for target '/home/HwHiAiUser/sample/resnet50_firstapp/out/main' failed
    make[2]: *** [/home/HwHiAiUser/sample/resnet50_firstapp/out/main] Error 1
    CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/main.dir/all' failed
    make[1]: *** [CMakeFiles/main.dir/all] Error 2
    Makefile:129: recipe for target 'all' failed
    ```

## 原因分析

编译应用源码依赖定义acl接口的头文件和库文件，本样例是通过分别配置\{DDK\_PATH\}、\{NPU\_HOST\_LIB\}环境变量来查找头文件、库文件，当前报错提示找不到头文件、库文件，则可能是\{DDK\_PATH\}、\{NPU\_HOST\_LIB\}环境变量配置得不正确。

## 解决方法

<a id="li20951151565"></a>

1. 登录编译源码的环境，分别使用如下命令查看\{DDK\_PATH\}、\{NPU\_HOST\_LIB\}环境变量的值。
    - 查看\{DDK\_PATH\}环境变量的值：

        ```bash
        echo $DDK_PATH
        ```

        若无回显信息，则环境变量未配置，跳转到[4](#li1078418329210)配置该环境变量。

    - 查看\{NPU\_HOST\_LIB\}环境变量的值：

        ```bash
        echo $NPU_HOST_LIB
        ```

        若无回显信息，则环境变量未配置，跳转到[4](#li1078418329210)配置该环境变量。

2. 根据[1](#li20951151565)中获取到的\{DDK\_PATH\}环境变量值，检查对应路径下是否存在头文件。

    样例中的编译脚本会根据“\{DDK\_PATH\}环境变量值/runtime/include/acl”目录查找编译依赖的头文件，因此可先检查“\{DDK\_PATH\}环境变量值/runtime/include/acl”路径是否存在，若存在，则检查该路径下的acl.h头文件是否存在；若路径或头文件有一个不存在，则需要重新配置\{DDK\_PATH\}环境变量，跳转到[4](#li1078418329210)。

    进入到\{DDK\_PATH\}环境变量配置的路径下，命令示例如下：

    ```bash
    cd $DDK_PATH
    ```

3. 根据[1](#li20951151565)中获取到的\{NPU\_HOST\_LIB\}环境变量值，检查对应路径下是否存在库文件。

    样例中的编译脚本会根据\{NPU\_HOST\_LIB\}环境变量指向的路径查找编译依赖的库文件，因此可先检查\{NPU\_HOST\_LIB\}环境变量指向的路径是否存在，若存在，则检查该路径下的libascendcl.so库文件是否存在；若路径或库文件有一个不存在，则需要重新配置\{NPU\_HOST\_LIB\}环境变量，跳转到[4](#li1078418329210)。

    进入到\{NPU\_HOST\_LIB\}环境变量配置的路径下，命令示例如下：

    ```bash
    cd $NPU_HOST_LIB
    ```

4. 配置环境变量。<a id="li1078418329210"></a>

    编译脚本会根据“\{DDK\_PATH\}环境变量值/runtime/include/acl”目录查找编译依赖的头文件，根据\{NPU\_HOST\_LIB\}环境变量指向的目录查找编译依赖的库文件。

    $\{INSTALL\_DIR\}请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：/usr/local/Ascend/cann。

    - 当开发环境与运行环境的操作系统架构相同时，配置示例如下所示：

        ```bash
        export DDK_PATH=${INSTALL_DIR}
        export NPU_HOST_LIB=$DDK_PATH/runtime/lib64/stub
        ```

    - 当开发环境与运行环境的操作系统架构不同时，配置示例如下所示：

        例如，当开发环境为X86架构、运行环境为AArch64架构时，则涉及交叉编译，需在开发环境上安装AArch64架构的软件包，将\{DDK\_PATH\}环境变量的路径指向AArch64架构的软件包安装目录（如下所示），便于使用与运行环境架构相同的软件包中的头文件和库文件来编译代码。

        ```bash
        export DDK_PATH=${INSTALL_DIR}/arm64-linux
        export NPU_HOST_LIB=$DDK_PATH/runtime/lib64/stub
        ```

    >**说明：** 
    >- 您可以登录对应的环境，执行**uname -a**命令查询其操作系统的架构。
    >- 如果不清楚头文件acl.h、库文件libascendcl.so所在的路径，也可以使用**find -name "_filename_"**命令查找文件路径，再配置环境变量。
