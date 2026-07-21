# 使用dump功能未获取dump结果

## 问题现象描述

日志显示正确执行了Dump功能，但在Dump结果路径下没有Dump的结果。日志信息包含了以下关键字：

```bash
[INFO] ASCENDCL ****** "HandleDumpConfig end in HandleDumpConfig."
[INFO] ASCENDCL ****** "set HandleDumpConfig success in aclInit"
```

## 可能原因

分析上述日志信息，可能存在以下故障原因：Dump配置的模型名与实际的模型名不匹配。

## 处理步骤

针对分析的故障可能原因，可以参考下面步骤处理：

检查Dump配置文件acl.json，确保Dump配置文件合法，例如model\_name是否配置正确。示例如下：

```json
{
    "dump":{
        "dump_list":[
             {
                "model_name":"ResNet-50",
                  "layer":[
                             "conv1conv1_relu"
                          ]
             },
             {
                "model_name":"mxnet-model"
             }
        ],
        "dump_mode":"output",
        "dump_path":"/home/test/output/dump"
    }
}
```

通过ATC命令生成模型的json文件，在json文件中查找“name”字段对应值，查找模型名称和算子名称，模型名称在"graph"字段外、算子名称在"graph"字段内。
