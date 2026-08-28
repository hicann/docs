# EL0016 Invalid\_Argument

## 错误信息

报错格式如下，占位符%s的含义依次为接口名、参数值、参数名、报错原因：

```text
%s failed. Value %s for parameter %s is invalid. Reason: %s.
```

报错示例如下：

```text
MemMap failed. Value 10 for parameter cmd is invalid. Reason: The input address does not meet the 4 KB alignment requirement.
```

## 解决方法

检查接口的输入参数范围。
