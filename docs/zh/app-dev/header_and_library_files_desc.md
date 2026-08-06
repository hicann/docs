# 头文件和库文件说明

CANN应用开发场景涉及Runtime、图引擎（Graph Engine，简称GE）和DVPP（Digital Vision Pre-Processing）等组件提供的接口。各组件提供的接口及其详细说明，请参见各组件的API参考。本节仅介绍接口分类以及调用接口时依赖的头文件和库文件。

## 接口分类

接口名以acl作为前缀，命名风格为：acl+_接口类别缩写_+\*，其中，\*通常表示操作动词和对象，均采用首字母大写。下文为了描述方便，将本文中的接口统称为acl接口。

在acl接口中，参数顺序通常遵循输入参数在前、输出参数在后的原则。且需注意，不要因为某些参数是新增的，就将其随意添加到接口的末尾；相反，应将新的仅作为输入的参数放在输出参数之前。对于同时作为输入和输出的参数，情况会相对复杂，可能还需考虑与其他接口的一致性，需灵活处理。

**表 1**  接口类别列表

| 接口名前缀 | 描述 | 组件 |
| --- | --- | --- |
| acl | 系统配置类接口 | Runtime |
| aclrt | 运行时管理类的接口 | Runtime |
| aclop | 单算子模型执行类的接口 | Runtime |
| aclblas | blas类接口 | Graph Engine |
| aclmdl | 模型推理类的接口 | Graph Engine |
| acldvpp或aclvdec或aclvenc | 媒体数据处理的接口<br>其中，媒体数据处理V2版本下的接口命名例外，这一类接口命名以“hi_mpi”开头。 | DVPP（Digital Vision Pre-Processing） |
| aclprof | Profiling配置类接口 | Runtime |
| acltdt | 数据传输接口 | Runtime |
| aclfv | 特征向量检索接口 | Feature Vector |

由于软硬件差异，各产品型号支持的接口类别不同，具体以各接口说明为准。

## 调用接口依赖的头文件和库文件说明

安装固件、驱动及CANN软件包后，编译、运行应用程序时才能引用到acl接口的头文件、库文件。

acl接口的头文件在“$\{INSTALL\_DIR\}/include/”目录下，库文件在“$\{INSTALL\_DIR\}/lib64/”目录下。$\{INSTALL\_DIR\}请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：/usr/local/Ascend/cann。

您需要根据实际使用的acl接口来include依赖的文件，各头文件的用途如下表所示。

>**须知：** 
>编译acl接口程序时，请按照include的头文件依赖对应的库文件，如果引用多余的库文件（例如libascendcl.a），可能导致版本功能异常或后续版本升级时存在兼容性问题。

**表 2**  Runtime头文件和库文件列表

| 定义接口的头文件 | 用途 | 对应的库文件 |
| --- | --- | --- |
| acl/acl_rt.h | 用于定义初始化/去初始化、Device管理、Context管理、Stream管理、同步等待、内存管理等接口。 | libacl_rt.so<br>说明：为了兼容旧版本，旧版本中支持使用libascendcl.so，但后续版本这种方式会废弃，建议使用libacl_rt.so，防止后续版本出现兼容性问题。 |
| acl/acl_dump.h | 用于定义模型和算子Dump接口。 | libascend_dump.so |
| acl/acl_prof.h | 用于定义Profiling数据采集接口。 | libmsprofiler.so<br>说明：为了兼容旧版本，旧版本中支持使用libascendcl.so，但后续版本这种方式会废弃，建议使用libmsprofiler.so，防止后续版本出现兼容性问题。 |
| acl/acl_tdt.h | 用于定义Tensor数据传输接口。 | libacl_tdt_channel.so |
| acl/acl_tdt_queue.h | 用于定义共享队列管理、共享Buffer管理接口。 | libacl_tdt_queue.so |
| acl/acl_rt_api.h | 用于定义C++扩展接口，提供函数重载和模板封装（仅适用于C++ 程序）。<br>依赖acl_rt.h。 | libacl_rt.so |

**表 3**  Graph Engine组件头文件和库文件列表

| 定义接口的头文件 | 用途 | 对应的库文件 |
| --- | --- | --- |
| acl/acl_mdl.h | 用于定义模型管理接口。 | libacl_mdl.so<br>说明：为了兼容旧版本，旧版本中支持使用libascendcl.so，但后续版本这种方式会废弃，建议使用libacl_mdl.so，防止后续版本出现兼容性问题。 |
| acl/acl_op.h<br>acl/acl_op_compiler.h | 用于定义单算子调用接口（仅包含单算模型执行接口）。 | libacl_op_executor.so<br>libacl_op_compiler.so<br>说明：为了兼容旧版本，旧版本中支持使用libascendcl.so，但后续版本这种方式会废弃，建议使用libacl_op_executor.so和libacl_op_compiler.so，防止后续版本出现兼容性问题。 |
| acl/ops/acl_cblas.h | 用于定义CBLAS接口。 | libacl_cblas.so |

**表 4**  DVPP组件头文件和库文件列表

| 分类 | 定义接口的头文件 | 用途 | 对应的库文件 |
| --- | --- | --- | --- |
| 媒体数据处理算子 | acldvppop目录下：<br>acldvpp_base.h<br>acldvpp_op_api.h | 用于定义DVPP媒体数据处理类算子的功能接口。 | libacl_dvpp_op.so |
| 媒体数据处理算子 | aclnn目录下：<br>acl_meta.h<br>aclnn_base.h | 调用算子接口时依赖的公共Meta接口，如创建aclTensor、aclScalar、aclIntArray等。 | libnnopbase.so |
| 媒体数据处理V2 | acl/dvpp/hi_dvpp.h | 用于定义媒体数据处理V2版本中的DVPP接口。 | libacl_dvpp_mpi.so |
| 媒体数据处理V2 | acl/media目录下：<br>hi_mpi_vi.h<br>hi_common_vi.h<br>hi_common_dis.h<br>hi_common_gdc.h<br>hi_media_common.h<br>hi_media_type.h<br>hi_mpi_sys.h | 用于定义VI（Video Input）视频数据获取功能的接口。 | libacl_vi_mpi.so<br>libacl_dvpp_mpi.so |
| 媒体数据处理V2 | acl/media目录下：<br>hi_mpi_isp.h<br>hi_common_isp.h<br>hi_common_3a.h<br>hi_mpi_ae.h<br>hi_common_ae.h<br>hi_mpi_awb.h<br>hi_common_awb.h<br>hi_common_sns.h<br>hi_media_common.h<br>hi_media_type.h<br>hi_mpi_sys.h | 用于定义ISP（Image Signal Processing）系统控制功能的接口。 | libacl_isp_ae_mpi.so<br>libacl_isp_awb_mpi.so<br>libacl_isp_mpi.so<br>libacl_dvpp_mpi.so |
| 媒体数据处理V2 | acl/media目录下：<br>hi_mpi_vpss.h<br>hi_media_common.h<br>hi_media_type.h<br>hi_mpi_sys.h | 用于定义VPSS（Video Process Sub-System）图像处理功能的接口。 | libacl_vpss_mpi.so<br>libacl_dvpp_mpi.so |
| 媒体数据处理V2 | acl/media/hi_mipi_rx.h | 用于定义MIPI Rx ioctl命令字。 | - |
| 媒体数据处理V2 | acl/media目录下：<br>hi_mpi_audio.h<br>hi_common_aio.h | 用于定义音频输入、音频输出功能的接口。 | libacl_audio_mpi.so |
| 媒体数据处理V2 | acl/media/hi_acodec.h | 用于定义音量调整的命令字。 | - |
| 媒体数据处理V2 | acl/media目录下：<br>hi_common_vo.h<br>hi_mpi_vo.h | 用于定义视频输出接口。 | libacl_vo_mpi.so |
| 媒体数据处理V2 | acl/media/hi_mpi_hdmi.h | 用于定义对接外设的HDMI接口。 | libacl_hdmi_mpi.so |
| 媒体数据处理V2 | acl/media/hi_mpi_tde.h | 用于定义TDE图形绘制接口。 | libacl_tde_mpi.so |
| 媒体数据处理V2 | acl/media/hifb.h | 用于定义叠加图形层管理接口。 | - |
| 媒体数据处理V1 | acl/ops/acl_dvpp.h | 用于定义媒体数据处理V1版本的接口。 | libacl_dvpp.so |

**表 5**  特征向量检索头文件和库文件

| 定义接口的头文件 | 用途 | 对应的库文件 |
| --- | --- | --- |
| acl/ops/acl_fv.h | 用于定义特征向量检索的接口。 | libacl_retr.so |
