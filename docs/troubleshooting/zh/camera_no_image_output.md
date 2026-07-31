# Camera不出图

## 适用场景

- 业务场景：Camera出图
- 适用处理器：Atlas 200I/500 A2 推理产品
- 处理器形态：EP、RC

## 问题现象描述

取Sensor数据失败，创建ISP失败，日志中有类似的打印信息：

```bash
[imx477_sensor_ctl.c:121][sensor]viPipe:0, addr:100, data:0
[imx477_sensor_ctl.c:149][sensor]I2C WRITER DATA error!
[imx477_sensor_ctl.c:209][sensor]imx477 vipipe:0, i2caddr:256,i2cval
```

## 可能原因

sensor没有安装好，或者sensor型号与预期设置不匹配。

## 处理步骤

1. 插拔sensor，或者检查相应配置。
2. 如果步骤1无法解决，替换新sensor设备。
3. 再次启动Camera。
