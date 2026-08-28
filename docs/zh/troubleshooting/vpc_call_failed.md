# VPC调用失败

## 问题现象描述

VPC模块调用失败（不同版本的报错日志可能存在差别），查看日志有类似如下报错信息：

日志信息（1）：

```bash
RoiNum(0), inputArea rightOffset is 1918, it should be odd!
```

日志信息（2）：

```bash
Output bufferSize(65536) should not be smaller than widthStride(256) * heightStride(256) * 3 / 2 = 98304
```

日志信息（3）：

```bash
Input widthStride(300) is not right, it should be 16 aligned!
```

```bash
Input widthStride(16) is not right, it should not be smaller than 32!
```

日志信息（4）：

```bash
bareDataAddr(0xaaaadeccdcd0), bareDataBufferSize(3133440) should be allocated by acldvppMalloc!
```

日志信息（5）：

```bash
Both RoiNum(1) outputAddr(0xaaaadeccdcd0) and first roi outputAddr(0xffff00002000) should be allocated by acldvppMalloc!
```

日志信息（6）：

```bash
RoiNum(0): inputConfigure cropArea, leftOffset(26) should be smaller than rightOffset(25)!
```

```bash
RoiNum(0): inputConfigure cropArea, upOffset(80) should be smaller than downOffset(79)!
```

```bash
RoiNum(0): inputConfigure cropArea, cropWidth(1931) should not be bigger than width(1920)!
```

```bash
RoiNum(0): inputConfigure cropArea, cropHeight(1270) should not be bigger than height(1088)!
```

```bash
RoiNum(0): inputConfigure cropArea, cropWidth(9) should be between [10, 8192]!
```

```bash
RoiNum(0): inputConfigure cropArea, cropHeight(4) should be between [6, 8192]!
```

```bash
RoiNum(0): inputConfigure cropArea, rightOffset(1921) should be smaller than width(1920)!
```

```bash
RoiNum(0): inputConfigure cropArea, downOffset(1089) should be smaller than height(1088)!
```

日志信息（7）：

```bash
RoiNum(0): scale must be in [1/32, 16], cropWidth(1920), pasteWidth(10)!
```

```bash
RoiNum(0): scale must be in [1/32, 16], cropHeight(6), pasteHeight(100)!
```

## 可能原因

针对上面日志信息分析，可能存在以下对应原因：

- 日志信息（1）：VPC抠图区域右偏移坐标需是奇数，日志信息里1918是偶数，不符合要求。
- 日志信息（2）：输出内存大小应该大于等于宽stride\*高stride\*3/2，日志信息显示不满足这个条件。

- 日志信息（3）：输入图片的宽stride（即每行图像占用的内存大小）必须是16倍数、且最小值32。日志信息里宽stride是300，不满足16倍数的要求，需要将图像做对齐后，并将宽stride设置成对齐后的值。
- 日志信息（4）：VPC的输入内存需要使用acldvppMalloc接口申请。
- 日志信息（5）：VPC的输出内存需要使用acldvppMalloc接口申请。
- 日志信息（6）：VPC的抠图区域不符合约束要求，因此报错。
- 日志信息（7）：VPC的缩放范围为\[1/32, 16\]。日志信息提示了缩放范围，并且显示了抠图宽为1920，输出区域的宽为10，通过计算可以得到：10/1920 < 1/32，因此报错。

## 定位思路

1. 根据日志描述的错误信息，找到VPC对应的配置参数，根据提示进行修改。
2. 根据日志描述的错误信息，参考[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)中的“媒体数据处理V1 API \> VPC图像处理功能”或“媒体数据处理V2 API \> VPC图像处理功能”章节的约束修改。

## 解决方法

根据提示的错误信息进行修改：

1. 如果为日志信息（1），说明输入图片抠图区域的右偏移错误，应该设置为奇数。
2. 如果为日志信息（2），说明输入内存的大小不正确，应该检查申请输入内存的代码，申请内存大小应该为1920\*1088\*3/2，并且bareDataBufferSize这个值也要填写为1920\*1088\*3/2。
3. 如果为日志信息（3），说明输入图片的stride值不符合要求，需设置为16的倍数。
4. 如果为日志信息（4）和日志信息（5），代码中申请内存时，需要使用acldvppMalloc接口申请。
5. 如果为日志信息（6），需要修改抠图宽度。
6. 如果为日志信息（7），需要修改缩放范围。
