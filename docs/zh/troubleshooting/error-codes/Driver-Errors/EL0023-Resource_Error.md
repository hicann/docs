# EL0023 Resource\_Error

## 错误信息

报错格式如下，占位符%s的含义依次为接口名、报错原因：

```text
%s failed. Reason: %s.
```

报错示例如下：

```text
halMemSetAccess failed. Reason: UB memory address conversion failed because the UB Decoder configuration is abnormal.
```

## 解决方法

请检查灵衢UBM包是否正确安装，并且可以在管控节点内通过gmsysview工具检查UB Decoder是否配置正确。
