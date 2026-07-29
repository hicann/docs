# 简介

本手册描述开发者基于CANN构建AI应用和业务过程中可使用的环境变量。

环境变量支持通过命令、接口、配置等方式实现，包括export命令、putenv/getenv/setenv/unsetenv/clearenv函数、os.environ、os.getenv等。建议用户在应用进程拉起前设置环境变量，否则可能引起环境变量访问冲突，导致程序异常。
