# 安装后自动配置环境变量

描述CANN软件安装完成后，系统通过“set\_env.sh”脚本默认配置的程序编译、执行相关的基础环境变量，以及后续程序编译执行时，需要手工配置的与安装包相关的环境变量。

CANN软件安装完成后，默认会自动配置程序编译、执行所依赖的基础环境变量，但用户进程结束后相关环境变量自动失效，您也可以通过如下环境变量脚本一键式配置。

```bash
# root用户安装时环境变量配置示例：
# 安装toolkit包时
source /usr/local/Ascend/cann/set_env.sh
# 安装nnal包ATB加速库
source /usr/local/Ascend/nnal/atb/set_env.sh
# 安装nnal包SiP加速库
source /usr/local/Ascend/nnal/asdsip/set_env.sh
```

```bash
# 非root用户安装时环境变量配置示例：
# 安装toolkit时
source ${HOME}/Ascend/cann/set_env.sh 
# 安装nnal包时ATB加速库
source ${HOME}/Ascend/nnal/atb/set_env.sh
# 安装nnal包SiP加速库
source ${HOME}/Ascend/nnal/asdsip/set_env.sh
```

```bash
# root用户安装时配置示例
source /usr/local/Ascend/cann/set_env.sh
# 非root用户安装时配置示例
source ${HOME}/Ascend/cann/set_env.sh 
```

用户也可以通过修改\~/.bashrc文件方式设置永久环境变量，操作如下：

1. 以运行用户在任意目录下执行vi \~/.bashrc命令，打开.bashrc文件，在文件最后一行后面添加上述内容。
2. 执行:wq!命令保存文件并退出。
3. 执行source \~/.bashrc命令使其立即生效。
