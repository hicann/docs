# E30006 Package\_Error\_Verify\_OPP

## 错误信息

```text
Failed to verify the OPP.
```

## 可能原因

1. Host侧AI CPU算子包被篡改。
2. Device侧出现ECC内存错误。

## 解决方法

1. 安装正确算子包。
2. 获取Host侧和Device侧日志后分析是否有ECC相关报错，并通过<https://www.hiascend.com/support>联系技术支持。
