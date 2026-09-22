# 示例代码
<!-- npu="910,310p,310b" id1 -->
您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/resnet50_async_imagenet_classification)中查看完整样例代码。
<!-- end id1 -->
<!-- npu="910,310p,310b" id2 -->
在acl_resnet50_async样例中：
<!-- end id2 -->
- 运行可执行文件，不带参数时：
  - 执行模型异步推理的次数默认为10次。
  - device_id默认使用编号为0的设备。
  - callback间隔默认为1，表示1次异步推理后，下发一次callback任务。
  - 内存池中的内存块的个数默认为10个。

- 运行可执行文件，带参数时：
  - 第一个参数表示使用设备ID。
  - 第二个参数表示执行模型异步推理的次数。
  - 第三个参数表示下发callback间隔，参数值为0时表示不下发callback任务，参数值为非0值（例如m）时表示m次异步推理后下发一次callback任务。
  - 第四个参数表示内存池中内存块的个数，内存块个数需大于等于模型异步推理的次数，用户可根据输入图片数量，来调整内存块的个数。
    - 例1：有2张输入图片、内存块个数为2时，则1张图片1个内存块。
    - 例2：有3张输入图片、内存块个数为10时，则执行10次循环，每（10/3取整）个内存块对应同一张图片，剩下1个内存块随机对应1张图片。
    - 内存块中存放的是模型推理的输入数据、输出数据，若多个内存块对应的是同一张图片，则多个内存块中存放的是相同的输入数据、输出数据，用于输入图片少但又想模拟大量图片数据的场景。

  - 第五个参数表示要加载执行的模型的路径。
  - 第六个参数表示输入的图片路径。支持图片格式如下：

        ```text
        IMG_EXT = ['.jpg', '.JPG', '.png', '.PNG', '.bmp', '.BMP', '.jpeg', '.JPEG']
        ```

```python
import acl
import argparse
# ......

images_list = [os.path.join(args.images_path, img) for img in os.listdir(args.images_path) \
               if os.path.splitext(img)[1] in IMG_EXT]
data_list = []
for image in images_list:
    # 自定义函数transfer_pic，完成以下功能：
    # 加载图片到内存，并resize成 224x224尺寸。
    transfer_pic(image)
    dst_im = np.fromfile(image.replace(".jpg", ".bin"), dtype=np.byte)
    data_list.append(dst_im)

# 1.资源初始化： 样例中通过Net类实现资源初始化操作。
# 1.1 初始化。
ret = acl.init()
# 1.2 运行时资源申请。
ret = acl.rt.set_device(self.device_id)
self.context, ret = acl.rt.create_context(self.device_id)
self.stream, ret = acl.rt.create_stream()
# 获取当前昇腾AI软件栈的运行模式，根据不同的运行模式，后续的内存申请、内存复制等接口调用方式不同。
self.run_mode, ret = acl.rt.get_run_mode()
# 1.3 申请模型推理资源。
# 1.4 加载模型。
# 加载离线模型文件，模型加载成功，返回标识模型的ID。
self.model_id, ret = acl.mdl.load_from_file(self.model_path)
# 1.5 根据模型的ID，获取该模型的描述信息。
self.model_desc = acl.mdl.create_desc()
ret = acl.mdl.get_desc(self.model_desc, self.model_id)

# 2.模型推理。
# 2.1 根据输入参数内存池中内存块的个数申请内存，拷贝图片数据到device侧。
def _data_interaction(self, images_dataset_list):
    for idx in range(self.memory_pool):
        img_idx = idx % len(images_dataset_list)
        img_input = self._load_input_data(images_dataset_list[img_idx])
        infer_output = self._load_output_data()
        self.dataset_list.append([img_input, infer_output])
# 2.2 创建线程tid，并将该tid线程指定为处理Stream上回调函数的线程。
# 其中ProcessCallback为线程函数，在该函数内调用acl.rt.process_report接口，等待指定时间后，触发回调函数处理。
tid, ret = acl.util.start_thread(self._process_callback, [self.context, 50])
# 2.3 指定处理Stream上回调函数的线程。
ret = acl.rt.subscribe_report(tid, self.stream)
# 2.4 创建回调函数，用户处理模型推理的结果，由用户自行定义。
def callback_func(self, delete_list):
    for temp in delete_list:
        _, infer_output = temp
        # device to host
        num = acl.mdl.get_dataset_num_buffers(infer_output)
        for i in range(num):
            temp_output_buf = acl.mdl.get_dataset_buffer(infer_output, i)
            infer_output_ptr = acl.get_data_buffer_addr(temp_output_buf)
            infer_output_size = acl.get_data_buffer_size(temp_output_buf)
            output_host, ret = acl.rt.malloc_host(infer_output_size)
            ret = acl.rt.memcpy(output_host,
                                 infer_output_size,
                                 infer_output_ptr,
                                 infer_output_size,
                                 ACL_MEMCPY_DEVICE_TO_HOST)
            output_host_dict = [{"buffer": output_host, "size": infer_output_size}]
            result = self.get_result(output_host_dict)
            st = struct.unpack("1000f", bytearray(result[0]))
            vals = np.array(st).flatten()
            top_k = vals.argsort()[-1:-6:-1]
            print("\n======== top5 inference results: =============")
            for n in top_k:
                print("[%d]: %f" % (n, vals[n]))
            ret = acl.rt.free_host(output_host)
# 2.5 自定义函数forward，执行模型推理。
def forward(self):
    self.execute_dataset = []
    for idx in range(self.execute_times):
        img_data, infer_output = self.dataset_list.pop(0)
        ret = acl.mdl.execute_async(self.model_id,
                                      img_data,
                                      infer_output,
                                      self.stream)
        if self.is_callback:
            self.execute_dataset.append([img_data, infer_output])
            self._get_callback(idx)
# 2.6 对于异步推理，需阻塞应用程序运行，直到指定Stream中的所有任务都完成。
ret = acl.rt.synchronize_stream(self.stream)
# 2.7 取消线程注册，Stream上的回调函数不再由指定线程处理。
ret = acl.rt.unsubscribe_report(tid, self.stream)
self.is_exist = True
ret = acl.util.stop_thread(tid)

# 3.释放运行时资源。
ret = acl.rt.destroy_stream(self.stream)
ret = acl.rt.destroy_context(self.context)
ret = acl.rt.reset_device(self.model_id)

# 4.去初始化。
ret = acl.finalize()
# ......
```
