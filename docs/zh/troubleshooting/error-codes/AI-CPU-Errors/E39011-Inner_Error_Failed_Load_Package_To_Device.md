# E39011 Inner\_Error\_Failed\_Load\_Package\_To\_Device

## 错误信息

报错格式如下，占位符%s表示软件包名：

```text
Failed to load the package %s on the device.
```

报错示例如下：

```text
Failed to load the package Ascend-aicpu_legacy.tar.gz on the device.
```

## 可能原因

1. device侧软件包签名校验失败。
2. device侧软件包解压失败
3. device侧软件包安装失败

## 解决方法

获取Host侧和Device侧日志并联系技术支持，网址为<https://www.hiascend.com/support>。
