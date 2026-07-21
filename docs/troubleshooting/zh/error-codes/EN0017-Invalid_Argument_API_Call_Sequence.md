# EN0017 Invalid\_Argument\_API\_Call\_Sequence

## 错误信息

报错格式如下，占位符%s分别表示文件名、报错原因：

```text
Call the following APIs in order: %s and %s.
```

报错示例如下：

```text
Call the following APIs in order: hi_mpi_vdec_start_recv_stream and hi_mpi_vdec_send_stream.
```

## 解决方法

接口调用顺序错误，需按照报错提示调整代码逻辑。
