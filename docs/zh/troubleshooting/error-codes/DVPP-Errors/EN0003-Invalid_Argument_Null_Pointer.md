# EN0003 Invalid\_Argument\_Null\_Pointer

## 错误信息

报错格式如下，占位符%s表示参数名：

```text
%s failed because %s cannot be a NULL pointer.
```

报错示例如下：

```text
hi_mpi_vpc_crop_resize failed because source_pic cannot be a NULL pointer
```

## 解决方法

参数值为空，请使用正确的参数值重试。
