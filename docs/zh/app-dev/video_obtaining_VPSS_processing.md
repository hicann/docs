# 视频数据获取+VPSS视频处理功能

VPSS必须配合VI模块一起使用，本节介绍其接口调用流程及注意事项。

**图 1**  VPSS调用流程  
![](figures/VPSS_API_call_process.png "VPSS调用流程")

接口调用流程说明如下：

1. **初始化**：
    1. 调用hi\_mpi\_sys\_init接口完成媒体系统初始化。
    2. 调用hi\_mpi\_rgn\_create创建区域。
    3. VPSS模块只能作为被绑定方，被动接收视频流数据并处理，所以需要调用hi\_mpi\_sys\_bind接口，将规划好的VI通道绑定到VPSS组上。
    4. 调用hi\_mpi\_vpss\_create\_grp接口创建VPSS组，作为hi\_mpi\_sys\_bind接口的被绑定方。
    5. 按需开启VPSS上功能：
        - 如果需要做组裁剪，则调用hi\_mpi\_vpss\_set\_grp\_crop接口，设置裁剪相关配置。
        - 如果需要开启3DNR，则除了在hi\_mpi\_vpss\_create\_grp接口时，打开nr开关并配置nr属性，还可通过hi\_mpi\_vpss\_set\_grp\_param接口设置NR高级参数。
        - 如果需要开启鱼眼矫正，并通过hi\_mpi\_vi\_set\_chn\_fisheye接口中hi\_fisheye\_attr属性开启了LMF\(Lens Map Function\)参数功能，则必须调用hi\_mpi\_vpss\_set\_grp\_fisheye\_cfg接口设置LMF参数。

    6. 调用hi\_mpi\_vpss\_start\_grp接口启用VPSS组。
    7. 调用hi\_mpi\_vpss\_set\_chn\_attr接口设置通道属性，通道输出分辨率可以与输入源分辨率不一致，当不一致时，自动开启缩放，不同通道的缩放能力不一样。
    8. 如果需要开启鱼眼畸变矫正，则还需要调用hi\_mpi\_vi\_set\_chn\_fisheye接口，设置鱼眼矫正参数。
    9. 调用hi\_mpi\_vpss\_enable\_chn接口启动VPSS通道。
    10. 调用hi\_mpi\_rgn\_attach\_to\_chn接口将区域叠加到VPSS通道上。

2. **采集并处理数据**：
    1. 使用MIPI Rx ioctl命令字初始化MIPI/Sensor硬件对接信息，接口调用流程请参见[初始化MIPI/Sensor硬件对接信息](video_obtaining.md#section5234939161715)。
    2. 使用VI（Video Input）功能接口初始化VI模块，接口调用流程请参见[初始化VI视频输入模块](video_obtaining.md#section140011491810)。
    3. 使用ISP（Image Signal Processing）系统控制接口初始化并运行ISP模块，接口调用流程请参见[初始化并运行ISP图像信号处理模块](video_obtaining.md#section0926122591813)。
    4. 根据hi\_mpi\_sys\_bind接口设置的绑定策略，系统内部自动将VI处理后的图像传递给VPSS；
    5. 根据VPSS设置的参数，系统内部自动执行裁剪/3dnr/鱼眼矫正/缩放处理。
    6. 按需更新修改区域信息：
        - 设置区域通道显示属性：
            1. 调用hi\_mpi\_rgn\_get\_display\_attr接口获取区域当前的通道显示属性。
            2. 调用hi\_mpi\_rgn\_set\_display\_attr接口设置区域的通道显示属性。

        - 设置区域的显示画布信息：
            1. 调用hi\_mpi\_rgn\_get\_canvas\_info接口获取当前区域的显示画布信息。
            2. 调用hi\_mpi\_rgn\_update\_canvas接口更新显示画布信息。

3. **获取处理结果数据**：

    此时，用户可调用hi\_mpi\_vpss\_get\_chn\_fd接口获取VPSS指定通道的句柄，并通过select/epoll接口等待VPSS处理结果。VPSS处理完后，会自动唤醒select/epoll等待，此时可调用hi\_mpi\_vpss\_get\_chn\_frame接口获取VPSS处理后的图像数据，做后续处理，最后调用hi\_mpi\_vpss\_release\_chn\_frame释放一帧通道图像。

4. **释放VI和VPSS初始化资源**。
    1. 使用ISP功能接口释放ISP模块资源，接口调用流程请参见[释放ISP图像信号处理模块资源](video_obtaining.md#section053155901816)。
    2. 使用VI功能接口释放VI模块资源，接口调用流程请参见[释放VI视频输入模块资源](video_obtaining.md#section1909173011193)。
    3. 使用MIPI Rx ioctl命令字退出MIPI/Sensor硬件，接口调用流程请参见[退出MIPI/Sensor硬件](video_obtaining.md#section440174412194)。
    4. 调用hi\_mpi\_rgn\_detach\_from\_chn接口将指定区域从通道中删除。
    5. 调用hi\_mpi\_vpss\_disable\_chn接口关闭VPSS通道。
    6. 调用hi\_mpi\_vpss\_stop\_grp接口停止VPSS组。
    7. 调用hi\_mpi\_vpss\_destroy\_grp接口销毁VPSS组。
    8. 调用hi\_mpi\_sys\_unbind接口取消VI和VPSS的绑定。
    9. 调用hi\_mpi\_rgn\_destroy接口销毁区域。
    10. 最后调用hi\_mpi\_sys\_exit接口完成媒体系统的退出。
