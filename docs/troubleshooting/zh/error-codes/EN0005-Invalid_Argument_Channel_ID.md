# EN0005 Invalid\_Argument\_Channel\_ID

## 错误信息

报错格式如下，占位符%s的含义依次为通道ID、报错原因：

```text
An error occurred on channel resource %s. Reason: %s.
```

报错示例1如下：

```text
An error occurred on channel resource 0. Reason: dev[0] all channels are being used.
```

报错示例2如下：

```text
An error occurred on channel resource 0. Reason: input stream addr invalid or too large len.
```

## 解决方法

检查输入通道ID或已创建通道的数量。
