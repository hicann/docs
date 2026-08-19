# E30009 Package\_Error\_Verify\_Package

## 错误信息

报错格式如下，占位符%s分别表示软件包名、报错原因：

```text
Failed to verify the signature of package %s on the device. Reason: %s.
```

报错示例如下：

```text
Failed to verify the signature of package Ascend-aicpu_legacy.tar.gz on the device. Reason: Signature verification failed. The possible cause is that a multi-bit ECC error occurred on the device or the software package has been tampered with. Obtain the device log, check whether ECC errors are reported, and contact technical support at https://www.hiascend.com/support.
```

## 解决方法

根据Reason中的提示使用正确的软件包。
