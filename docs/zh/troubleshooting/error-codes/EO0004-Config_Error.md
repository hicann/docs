# EO0004 Config\_Error

## 错误信息

报错格式如下，占位符%s的含义依次为配置项、配置文件、报错原因：

```text
The content of configuration item %s in configuration file %s is invalid. Reason: %s
```

报错示例如下：

```text
The content of configuration item devid in configuration file compression_optimize_conf is invalid. Reason: Configuration item devid is not supported.
```

## 解决方法

根据报错提示检查并调整配置项的值，详细描述请参考官方网站上的文档。
