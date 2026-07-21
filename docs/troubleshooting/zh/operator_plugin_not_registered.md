# 算子插件未注册报错

## 问题现象

查看日志， 存在报错某个算子类型不支持：

```bash
Check op[%s]'s type[%s] failed, it is not supported.
```

或者

进行模型转换的时候，某个算子类型转换不符合预期，被转换成了frameworkop类型。

## 可能原因

- 算子插件so未加载成功。
- 算子未注册映射关系，或者未编译到算子的插件so中。

## 解决方法

1. 确认算子插件so是否加载成功。
    - 算子插件so加载成功打印类似信息：

        ```bash
        plugin load ******/opp/built-in/framework/onnx/libops_all_onnx_plugin.so success.
        ```

    - 加载失败的告警关键信息：

        ```bash
        dlopen failed, plugin name:%s. Message(%s).
        ```

2. 如果算子插件so加载成功，则需要继续确认算子注册的映射关系是否编译进加载的插件so中了。

    使用nm命令查看so符号表，如果没有注册，则需要注册该算子插件，可以参考[《TBE&AI CPU算子开发》](https://hiascend.com/document/redirect/CannCommunityOpdevWizard)中的“算子开发过程 \> 算子适配”章节内容实现。

    >**说明：** 
    >**nm -D**命令可查看so文件符号表。

3. 如果算子插件so未加载成功，参考失败告警中Message提示内容处理。
