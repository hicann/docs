# 内存被提前释放，导致VENC编码数据花屏

## 问题现象描述

编码出来的数据花屏，其他无异常日志信息。

## 可能原因

VENC输入内存是YUV图片数据，输入内存被踩或者被提前释放。

## 处理步骤

在DVPP内存释放接口处、以及hi\_mpi\_venc\_get\_stream/aclvencCallback/acldvppJpegEncodeAsync接口处，增加内存大小及地址的打印日志，确认内存释放时序，是否存在输入内存在编码完成前被提前释放的情况。
