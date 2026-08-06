# APP使用dvpp接口编译失败

## 问题现象描述

编译提示DVPP的相关接口未定义，编译报错，日志关键字包括：undefined reference to \*\*\*

## 原因分析

分析上述日志信息，可能存在以下故障原因：

DVPP相关接口打包到libacl\_dvpp.so中，测试用例使用了DVPP的相关接口，但没有链接libacl\_dvpp.so。

## 解决方法

针对分析的可能原因，可以参考下面步骤处理：

排查测试用例是否使用了预处理的接口，但未链接libacl\_dvpp.so。如果未链接，需要在编译文件中链接libacl\_dvpp.so。

需要排查CmakeLists中的target\_link\_libraries\(\)选项是否连接了acl\_dvpp这个target。

示例：

```cmake
add_executable(main
utils.cpp
main.cpp)
target_link_libraries(main
ascendcl acl_dvpp stdc++)
```
