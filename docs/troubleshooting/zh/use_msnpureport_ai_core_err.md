# 使用msnpureport工具收集更多AI Core Error信息

联系技术支持定位一些疑难AI Core Error问题时，除了[收集AI Core Error问题信息](collect_ai_core_error_info.md)中收集的信息外，还需借助msnpureport工具获取Device配置信息、设置TaskSchedule是否自动复位加速器、导出寄存器信息、设置AI Core上任务串联或并行执行、屏蔽指定AI Core或Vector Core上的任务执行等，以便更进一步排查算子问题、硬件问题。定位问题后，建议恢复配置，以免影响业务性能。

关于msnpureport工具的详细使用方法及约束请参见[《msnpureport工具》](https://support.huawei.com/enterprise/zh/ascend-computing/ascend-hdk-pid-252764743?category=reference-guides&subcategory=command-reference)中的“查询和设置Device维测配置信息”。应用进程运行过程中不支持使用“查询和设置Device维测配置信息”中的命令，可能会导致应用进程运行异常或本步骤中的命令执行异常，需应用进程退出后才能使用。
