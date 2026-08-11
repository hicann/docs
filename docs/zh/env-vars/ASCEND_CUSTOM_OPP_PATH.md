# ASCEND_CUSTOM_OPP_PATH

## 功能描述

用户自定义算子运行时搜索路径。配置该路径后，算子入图场景下，GE框架在图编译和执行时根据该环境变量搜索算子二进制并使用。支持配置多个路径，以英文冒号分隔。

支持的自定义算子编译方式及路径配置：

-   **自定义算子包**：编译成自定义算子包，且算子包通过`--install-path=<path>`安装到指定路径时，在调用算子前需要执行：`source <path>/vendors/<vendor_name>/bin/set_env.bash`。该脚本会将算子包目录`<path>/vendors/<vendor_name>`添加到ASCEND_CUSTOM_OPP_PATH环境变量的首部，供框架在运行时查找自定义算子包。
-   **动态库**：编译成动态库时，需配置动态库的安装路径。此时也可以通过动态库链接的方式使用动态库，动态库链接优先级高于环境变量配置的方式。

动态库编译和自定义算子包编译功能同时使用时，前者生成的动态库优先级更高。

## 配置示例

如下示例中，`<path1>`和`<path2>`为开发者指定的算子包安装目录，编译产物的优先级为`1>2`。

```bash
export ASCEND_CUSTOM_OPP_PATH=<path1>/vendors/vendor_name1:<path2>/vendors/vendor_name2
```

如下示例中，`<path1>`和`<path3>`为开发者指定的算子包安装目录，`<path2>`和`<path4>`是动态库编译产物的存放目录，编译产物的优先级为`2>4>1>3`。

```bash
export ASCEND_CUSTOM_OPP_PATH=<path1>/vendors/vendor_name1:<path2>/op_api/lib/:<path3>/vendors/vendor_name3:<path4>/op_api/lib/
```

## 使用约束

无

## 支持的型号

全量芯片支持

