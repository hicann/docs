# EO0006 Config\_Error

## 错误信息

报错格式如下，占位符%s的含义依次为配置项值、配置项、配置文件、报错原因：

```text
Value %s for configuration item %s in configuration file %s is invalid. Reason: %s
```

报错示例如下：

```text
Value [invalid_layers1, invalid_layers2] for configuration item skip_fusion_layers in configuration file CONFIG_FILE is invalid. Reason: The layer in [invalid_layers1, invalid_layers2] does not exist in the graph.
```

## 解决方法

根据报错提示检查并调整配置项的值，详细描述请参考官方网站上的文档。
