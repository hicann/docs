# 执行应用程序的权限不足导致acl接口初始化报错

## 问题现象描述

用户进程报错并退出。

查看应用类日志，提示获取Device信息失败，最终导致初始化失败，日志片段示例如下：

```bash
[ERROR] RUNTIME(89696,main):2023-03-07-17:13:27.994.635 [runtime.cc:1065]89696 CheckHaveDevice:[INIT][DEFAULT]Call halGetDeviceInfo failed: drvRet=4, module type=0, info type=1.
[ERROR] ASCENDCL(89696,main):2023-03-07-17:13:27.994.723 [acl.cpp:164]89696 aclInit: [INIT][DEFAULT][Init][Version]init soc version failed, ret = 507008
[ERROR] RUNTIME(89696,main):2023-03-07-17:13:27.994.774 [api_impl.cc:3490]89696 GetDevErrMsg:report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(89696,main):2023-03-07-17:13:27.994.798 [api_impl.cc:3490]89696 GetDevErrMsg:ctx is NULL!
[ERROR] RUNTIME(89696,main):2023-03-07-17:13:27.994.827 [api_impl.cc:3546]89696 GetDevMsg:Failed to GetDeviceErrMsg, retCode=0x7070001.
[ERROR] RUNTIME(89696,main):2023-03-07-17:13:27.994.849 [logger.cc:1348]89696 GetDevMsg:GetDeviceMsg failed, getMsgType=0.
[ERROR] RUNTIME(89696,main):2023-03-07-17:13:27.994.888 [api_c.cc:3595]89696 rtGetDevMsg:ErrCode=107002, desc=[context pointer null], InnerCode=0x7070001
[ERROR] RUNTIME(89696,main):2023-03-07-17:13:27.994.910 [error_message_manage.cc:49]89696 FuncErrorReason:report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(89696,main):2023-03-07-17:13:27.994.932 [error_message_manage.cc:49]89696 FuncErrorReason:rtGetDevMsg execute failed, reason=[context pointer null]
EL0003: The argument is invalid.
        Solution: Try again with a valid argument.
        TraceBack (most recent call last):
        [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:3490]
        rtGetDevMsg execute failed, reason=[context pointer null][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:49]
 
[ERROR] acl init failed
[ERROR] Sample init resource failed
```

## 原因分析

可能存在以下原因：

- Device状态异常，未正常启动。
- 执行应用程序的用户权限不足，无法查询Device信息。

## 解决办法

1. 首先，确认Device是否正常启动。
    1. 以root用户登录安装Driver包的环境，执行以下命令查询其安装路径。

        ```bash
        cat /etc/ascend_install.info
        ```

        在该文件中，Driver\_Install\_Path\_Param表示Driver包的安装路径。

    2. 进入Driver安装路径，使用upgrade-tool工具查看下Device侧运行文件系统版本，如果能正常查询，则说明Device侧已经正常启动。

        ```bash
        ./upgrade-tool --device_index -1 --system_version
        ```

        正常查询返回信息类似如下：

        ![](figures/zh-cn_image_0000001882036538.png)

2. 其次，检查运行应用程序的用户权限是否正确。

    要求运行应用程序的用户，需与Driver运行用户在一个属组内。在“cat /etc/passwd”文件中，可查看用户属组，Driver的默认运行用户为HwHiAiUser。

    修改用户属组的命令示例如下：

    ```bash
    usermod -g 组名 用户名
    ```

3. 如果以上方法解决不了问题，则需要参考如下步骤获取日志，联系技术支持。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
    1. 登录到运行应用程序的环境，执行如下命令将日志级别设置为Debug。

        ```bash
        export ASCEND_GLOBAL_LOG_LEVEL=0
        ```

    2. 重新运行应用程序。
    3. 从日志存放路径下获取应用类日志。

        存放日志的默认路径为“$HOME/ascend/log”。

    4. 使用msnpureport工具，获取指定Device上的Debug日志。

        命令示例如下，其中deviceID需要设置为指定Device的ID：

        ```bash
        msnpureport -g debug -d deviceID
        ```
