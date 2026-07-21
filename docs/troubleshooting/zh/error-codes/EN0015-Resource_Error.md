# EN0015 Resource\_Error

## 错误信息

报错格式如下，占位符%s分别表示功能模块、接口：

```text
The %s has not been initialized. Call %s to initialize the resource first.
```

报错示例如下：

```text
The vpc resource has not been initialized. Call hi_mpi_sys_init to initialize the resource first.
```

## 解决方法

请按照报错提示调整代码逻辑。
