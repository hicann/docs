# 算子原型未注册报错

## 问题现象

查看日志， 存在报错某个算子没有原型定义：

```bash
op[%s] type[%s] have no ir factory.
```

或者

```bash
IR for op[%s] optype[%s] is not registered.
```

>**说明：** 
>op\[%s\] type\[%s\]中的%s分别表示具体的算子名称和算子类型。

## 可能原因

- 算子原型so未加载成功。
- 算子未定义注册该类型算子，并编译到算子的原型so中。

## 解决方法

1. 确认算子原型so是否加载成功。
    - 算子原型so加载成功打印类似信息：

        ```bash
        OpsProtoManager plugin load ******/opp/built-in/op_proto/libopsproto.so success.
        ```

    - 加载失败的告警关键信息：

        ```bash
        OpsProtoManager dlopen failed, plugin name:%s. Message(%s).
        ```

2. 如果算子原型so加载成功，需要确认算子原型定义是否编译进加载的so中了。

    使用nm查看so符号表，如果没有注册，则需要注册该算子原型，可以参考[《TBE&AI CPU算子开发》](https://hiascend.com/document/redirect/CannCommunityOpdevWizard)中的“算子开发过程 \> 算子原型定义”章节内容实现。

    >**说明：** 
    >**nm -D**命令可查看so文件符号表。

3. 如果算子原型so未加载成功，参考失败告警中Message提示内容处理。
