# EN0007 Execution\_Error\_DVPP\_Operator\_Timeout（优化示例）

## 错误信息

报错格式如下，占位符%s的含义依次为操作任务名、报错原因：

```text
%s times out. Reason: %s.
```

报错示例如下：

```text
GetResult times out. Reason: the configured timeout might be too short.
```

## 可能原因

1. 输入超时时间设置不当。
2. 缓冲区已满。
3. 发生内部错误。

## 解决方法

需设置为合理的超时时间，尝试复跑业务，若还是同样的报错，您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
