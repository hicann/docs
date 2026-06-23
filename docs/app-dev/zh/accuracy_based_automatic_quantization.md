# 基于精度的自动量化

基于精度的自动量化是为了方便用户在对量化精度有一定要求时所使用的功能，是借助AMCT工具提供的Python接口实现。该方法能够在保证用户所需的模型精度前提下，自动搜索模型的量化配置并执行**训练后量化**的流程，最终生成满足精度要求的量化模型。

**当前仅PyTorch框架、TensorFlow框架、Caffe框架支持使用基于精度的自动量化，详细使用指导请参见[《AMCT模型压缩工具》](https://hiascend.com/document/redirect/CannCommunityToolAmct)**。
