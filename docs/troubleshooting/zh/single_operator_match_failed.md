# 单算子匹配失败

## 问题现象

单算子执行过程中，出现匹配失败，日志显示如下类似信息。

离线加载执行场景：

```bash
EH9999 [Match][OpModel]failed to match model, opName = xxx Has not been compiled or loaded, Please make sure the op executed and the op compiled is matched, you can check the op type, op inputs number, outputs number, input format, origin format, datatype, memtype, attr, dim range, and so on.
```

在线加载执行场景：

```bash
EH9999 [Match][OpModel]MatchOpModel fail from static map or dynamic map. Please make sure the op executed and the op compiled is matched, you can check the op type, op inputs number, outputs number, input format, origin format, datatype, memtype, attr, dim range, and so on.
```

## 可能原因

- 离线场景：算子om文件未出现在aclSetModelDir中指定的路径下。
- 在线场景：一些特殊的匹配规则未适配，导致算子匹配失败。

## 解决方法

- 离线场景：重新编译缺少的算子，并复制到aclSetModelDir中指定的路径下，余下步骤按离线单算子推理步骤进行。
- 在线场景：根据报错信息检查前后两次编译的算子的opType、dataType、format等信息是否一致。
