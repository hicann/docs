# EL0024 Resource\_Busy\_Memory\_In\_Use

## 错误信息

报错格式如下，占位符%s的含义依次为接口名、内存地址：

```text
%s failed. Reason: The memory corresponding to address %s is still in use.
```

报错示例如下：

```text
halMemFree failed. Reason: The memory corresponding to address 0x40000000000 is still in use.
```

## 可能原因

其他操作仍在使用该内存，例如内存复制、地址转换、内存映射或内存注册，或者与该内存关联的资源尚未释放。

## 解决方法

释放该内存前，请确保所有涉及该内存的操作均已完成，并且与该内存关联的资源均已释放，然后重试。
