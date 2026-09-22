# 编程接口

## 接口命名规则

接口命名同时满足如下规则：

1. acl+_接口类别缩写_+_操作动词_+_对象_
2. 操作动词和对象均采用首字母大写。

## 接口类别

| 接口类别 | 缩写 | 描述 |
| --- | --- | --- |
| runtime | rt | 表示运行管理类的接口 |
| DVPP | media | 表示媒体数据处理类的接口 |
| AIPP | aipp | 表示aipp（AI Preprocessing）类的接口 |
| CBLAS | blas | 表示blas类的接口 |
| model | mdl | 表示模型推理类的接口 |
| OP | op | 表示算子执行类的接口 |
| fv | fv | 表示特征向量检索的接口 |
| Profiling | prof | 表示Profiling配置类接口 |

>[!NOTE]
>
>- 缩写原则上不超过4个字母。
>- 在接口命名中，如果类别与操作对象重叠时，操作动词后的对象将省略。如：acl.mdl.load\_from\_file\_with\_mem，表示model类接口，这个接口表示含义是load model from file，因此在接口命名中Load后面mdl将被省略。

## 变量命名

本文代码示例中涉及的变量，其中，命名带下划线的变量（例如：\_deviceId\_）表示类的私有变量。
