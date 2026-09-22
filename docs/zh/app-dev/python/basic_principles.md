# 基本原理

## 同步机制

提供以下几种同步机制：

- Event的同步等待：调用`acl.rt.synchronize_event`接口，阻塞应用程序运行，等待Event完成。
- Stream内任务的同步等待：调用`acl.rt.synchronize_stream`接口，阻塞应用程序运行，直到指定Stream中的所有任务都完成。
- Stream间任务的同步等待：调用`acl.rt.stream_wait_event`接口，阻塞指定Stream的运行，直到指定的Event完成。支持多个Stream等待同一个Event的场景。接口调用流程请参见[关于Stream间任务的同步等待（通过Event实现）](synchronous_waiting_Implemented_via_Event.md)。
- Device的同步等待：调用`acl.rt.synchronize_device`接口，阻塞应用程序运行，直到正在运算中的Device完成运算。多Device场景下，调用该接口等待的是当前Context对应的Device。
