# EO0001 Config\_Error

## 错误信息

报错格式如下，占位符%s的含义依次为配置项值、配置项、配置文件、期望值：

```text
Value %s for configuration item %s in configuration file %s is invalid. Expected value: %s
```

报错示例如下：

```text
Value in:z,16 for configuration item input_shape in configuration file compression_optimize_conf is invalid. Expected value: The entered shape must be a number.
```

## 解决方法

根据报错提示检查并调整配置项的值，详细描述请参考官方网站上的文档。
