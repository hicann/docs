# 配置skip\_layers跳过量化损失大的层

使用精度比对工具比对原始模型、量化后模型各层的精度，查找精度损失大的层，在基于精度的自动量化时通过配置skip\_layers跳过量化损失大的层。

1. 修改基于精度的自动量化代码，增加skip\_layers配置，跳过不支持量化的层。

    代码示例如下，表示跳过某一层。如果涉及跳过多层，则每一层之间用逗号分隔，例如：skip\_layers=\['op1','op2','op3'\]

    ```py
    config_json_file = './config.json'
    skip_layers = ['Default/network-DeepLabV3/resnet-Resnet/layer4-SequentialCell/0-Bottleneck/downsample-SequentialCell/0-Conv2d/Conv2D-op311']
    batch_num = 1
    amct.create_quant_config(config_json_file, model, input_data,
                              skip_layers, batch_num)
    
    scale_offset_record_file = os.path.join(TMP, 'scale_offset_record.txt')
    result_path = os.path.join(RESULT, 'model')
    ```

2. 执行精度的自动量化。
3. 重新执行推理。

    如果跳过不支持量化的层影响模型推理的结果数据，则需要用户自行调整模型，再重新量化模型。
