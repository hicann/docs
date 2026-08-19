# EL0017 Invalid\_Argument\_Null\_Pointer

## 错误信息

报错格式如下，占位符%s的含义依次为接口名、参数值：

```text
%s failed because %s cannot be a null pointer.
```

报错示例如下：

```text
halEschedQueryInfo failed because inPut cannot be a null pointer.
```

## 解决方法

检查接口的输入参数取值。
