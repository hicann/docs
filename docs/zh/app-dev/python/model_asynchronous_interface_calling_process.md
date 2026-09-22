# 接口调用流程

开发应用时，如果涉及异步场景下的同步等待，则应用程序中必须包含相关的代码逻辑，关于该场景的接口调用流程，请参见下图。

**图 1**  同步等待流程_Callback场景
![](figures/asynchronous_model_inference_process.png "同步等待流程_Callback场景")

关键接口说明如下：

1. 回调函数**需由用户提前创建**，用于获取并处理模型推理或算子执行的结果。
2. 线程需由用户提前创建，并自定义线程函数，在线程函数内调用`acl.rt.process_report`接口，设置超时时间，等待`acl.rt.launch_callback`接口下发的回调任务执行。
3. 调用`acl.rt.subscribe_report`接口：指定处理Stream上回调函数的线程，线程与上一步中创建的线程保持一致。
4. 异步推理时调用`acl.mdl.execute_async`接口。

    对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞应用程序运行，直到指定Stream中的所有任务都完成。

    用户可以在`acl.rt.synchronize_stream`接口之后一次性获取所有图片的异步推理结果，但如果图片数据量较大的情况下，需要等待的时间比较长，这时可以使用Callback功能，每隔一段时间下发一次Callback任务，获取前一段时间内的异步推理结果。

5. 调用`acl.rt.launch_callback`接口：在Stream的任务队列中下发一个函数回调任务，系统内部在执行到该回调任务时，会在Stream上订阅的线程（通过`acl.rt.subscribe_report`接口订阅的线程）中执行回调函数，回调函数与第一步中保持一致。

    每调用一次acl.rt.launch_callback接口，就会下发一个回调函数任务。

6. 调用`acl.rt.unsubscribe_report`接口：取消线程订阅（Stream上的回调函数不再由指定线程处理）。
