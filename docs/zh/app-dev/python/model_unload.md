# 模型卸载

关于模型卸载的接口调用流程，请参见[接口调用流程](interface_calling_process.md)。

## 基本原理

在模型推理结束后，还需要通过`acl.mdl.unload`接口卸载模型，并销毁aclmdlDesc类型的模型描述信息。

## 示例代码

```python
# 卸载模型。
ret = acl.mdl.unload(self.model_id)

# 释放模型描述信息。
if self.model_desc:
    ret = acl.mdl.destroy_desc(self.model_desc)
    self.model_desc = None
```
