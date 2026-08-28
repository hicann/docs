# EN0001 Invalid\_Argument

## 错误信息

报错格式如下，占位符%s的含义依次为接口名、参数值、参数名、报错原因：

```text
%s failed, Value %s for parameter %s is invalid. Reason: %s.
```

报错示例1如下：

```text
VdecWrapperHdc::hi_mpi_vdec_send_stream failed, Value -2 for parameter milli_sec is invalid. Reason: milli_sec must only be -1, 0 or positive number.
```

报错示例2如下：

```text
SysManager::hi_mpi_dvpp_malloc failed, Value -1 for parameter size is invalid. Reason: size must be greater than 0.
```

## 解决方法

参数值错误，需按照Reason中的提示输入正确的参数值。
