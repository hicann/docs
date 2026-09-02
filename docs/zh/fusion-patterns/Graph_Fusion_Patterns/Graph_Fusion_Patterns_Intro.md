# 图融合规则说明

- [PoolingFusionPass](PoolingFusionPass.md)

<!-- npu="310p" id1 -->
- [V100RequantFusionPass](V100RequantFusionPass.md)  
<!-- end id1 -->

<!-- npu="310p" id2 -->
- [V200RequantFusionPass](V200RequantFusionPass.md)  
<!-- end id2 -->

<!-- npu="A3,910b,910,310p,310b" id3 -->
- [ConvToFullyConnectionFusionPass](ConvToFullyConnectionFusionPass.md)  
<!-- end id3 -->

<!-- npu="A3,910b,910,310p,310b" id4 -->
- [SoftmaxFusionPass](SoftmaxFusionPass.md)  
<!-- end id4 -->

<!-- npu="910b" id5 -->
- [SoftmaxSmallOpFusionPass](SoftmaxSmallOpFusionPass.md)  
<!-- end id5 -->

<!-- npu="910b" id6 -->
- [LayerNormFusionPass](LayerNormFusionPass.md)  
<!-- end id6 -->

<!-- npu="A3,910b,910,310p,310b" id7 -->
- [GeluFusionPass](GeluFusionPass.md)  
<!-- end id7 -->

<!-- npu="910b" id8 -->
- [GridSampler3DFusionPass](GridSampler3DFusionPass.md)  
<!-- end id8 -->

- [SplitConvConcatFusionPass](SplitConvConcatFusionPass.md)  

<!-- npu="A3,910b,910,310p,310b" id9 -->
- [ConvConcatFusionPass](ConvConcatFusionPass.md)  
<!-- end id9 -->  

- [BatchMatMulReduceMeanFusionPass](BatchMatMulReduceMeanFusionPass.md)  

<!-- npu="950,A3,910b,910,310p,310b" id10 -->
- [PadDepthwiseConv2dFusionPass](PadDepthwiseConv2dFusionPass.md)  
<!-- end id10 -->

<!-- npu="910,310p,310b" id11 -->
- [SameInputConv2dPass](SameInputConv2dPass.md)  
<!-- end id11 -->

<!-- npu="910,310p,310b" id12 -->
- [ConvScaleFusionPass](ConvScaleFusionPass.md)  
<!-- end id12 -->

<!-- npu="910,310p,310b" id13 -->
- [Conv2DSqueezeBiasaddFusionPass](Conv2DSqueezeBiasaddFusionPass.md)  
<!-- end id13 -->

<!-- npu="910,310p,310b" id14 -->
- [ConvBatchnormFusionPass](ConvBatchnormFusionPass.md)  
<!-- end id14 -->

<!-- npu="950,A3,910b,910,310p,310b" id15 -->
- [AConv2dMulFusion](AConv2dMulFusion.md)  
<!-- end id15 -->

- [DepthwiseDfFusionPass](DepthwiseDfFusionPass.md)  

<!-- npu="910" id16 -->
- [ZBNupdateReluV2Conv2DBNreducePass](ZBNupdateReluV2Conv2DBNreducePass.md)  
<!-- end id16 -->

<!-- npu="950,910,310p,310b" id17 -->
- [ASplitConv2dConcatPass](ASplitConv2dConcatPass.md)  
<!-- end id17 -->

- [Conv3DQuantProcessFusionPass](Conv3DQuantProcessFusionPass.md)  

<!-- npu="910,310p" id18 -->
- [MatmulCastFusionPass](MatmulCastFusionPass.md)  
<!-- end id18 -->

<!-- npu="950,A3,910b" id19 -->
- [MatMulBiasAddFusionPass](MatMulBiasAddFusionPass.md)  
<!-- end id19 -->

- [DeconvWeightTransFusionPass](DeconvWeightTransFusionPass.md)  

- [Conv2DbpInputBiasAddFusionPass](Conv2DbpInputBiasAddFusionPass.md)  

<!-- npu="A3,910b,910,310p,310b" id20 -->
- [BatchMatMulV2ReshapeFusionPass](BatchMatMulV2ReshapeFusionPass.md)  
<!-- end id20 -->

- [BatchMatMulFusionPass](BatchMatMulFusionPass.md)  

- [SwapMergeCastFusionPass](SwapMergeCastFusionPass.md)  

- [PSROIPoolingFusionPass](PSROIPoolingFusionPass.md)  

- [ConvWeightCompressFusionPass](ConvWeightCompressFusionPass.md)  

- [ConcatQuantFusionPass](ConcatQuantFusionPass.md)  

- [BatchMatMulV2ReduceFusionPass](BatchMatMulV2ReduceFusionPass.md)  

- [BatchMatMulNonAlignedFusionPass](BatchMatMulNonAlignedFusionPass.md)  

- [Conv3DbpInputBiasAddFusionPass](Conv3DbpInputBiasAddFusionPass.md)  

- [FullyConnectionPowerPass](FullyConnectionPowerPass.md)  

- [AFullyConnectionReshapePass](AFullyConnectionReshapePass.md)  

<!-- npu="310b" id21 -->
- [GemmTransFusionPass](GemmTransFusionPass.md)  
<!-- end id21 -->

- [MatmulTransdataFusionPass](MatmulTransdataFusionPass.md)  

- [Matmulv2FusionPass](Matmulv2FusionPass.md)  

<!-- npu="910" id22 -->
- [Resnet50DbnDwFusionPass](Resnet50DbnDwFusionPass.md)  
<!-- end id22 -->

- [AAMatMulNzToNdFusionPass](AAMatMulNzToNdFusionPass.md)  

- [CastReluCastFusionPass](CastReluCastFusionPass.md)  

<!-- npu="910b,910,310p,310b" id23 -->
- [StrideHoistingPass](StrideHoistingPass.md)  
<!-- end id23 -->

<!-- npu="950,A3,910b,910,310p,310b" id24 -->
- [PadConv2dFusionPass](PadConv2dFusionPass.md)  
<!-- end id24 -->

- [Conv2DTransposeBatchnormFusionPass](Conv2DTransposeBatchnormFusionPass.md)  

- [AvgPoolV2GradFusionPass](AvgPoolV2GradFusionPass.md)  

<!-- npu="A3,910b" id25 -->
- [DropOutDoMaskFusionPass](DropOutDoMaskFusionPass.md)  
<!-- end id25 -->

<!-- npu="310p" id26 -->
- [TransposeSigmoidMulAddPowConcatFusionPass](TransposeSigmoidMulAddPowConcatFusionPass.md)  
<!-- end id26 -->

<!-- npu="910,310p,310b" id27 -->
- [ConvCastFusionPass](ConvCastFusionPass.md)  
<!-- end id27 -->

<!-- npu="310p" id28 -->
- [YoloxBoundingBoxDecodeONNXFusionPass](YoloxBoundingBoxDecodeONNXFusionPass.md)  
<!-- end id28 -->

- [MatMulUnsqueezeSqueezeFusionPass](MatMulUnsqueezeSqueezeFusionPass.md)  

- [LayerNormSpecialTrainingFusionPass](LayerNormSpecialTrainingFusionPass.md)  

<!-- npu="910,310p" id29 -->
- [StridedSliceConcatFusionPass](StridedSliceConcatFusionPass.md)  
<!-- end id29 -->

<!-- npu="A3,910b,910,310p,310b" id30 -->
- [ZSplitVDFusionPassV2](ZSplitVDFusionPassV2.md)  
<!-- end id30 -->

<!-- npu="A3,910b" id31 -->
- [RGB2YUV422FusionPass](RGB2YUV422FusionPass.md)  
<!-- end id31 -->

<!-- npu="A3,910b" id32 -->
- [MatMulAlignInputsFusionPass](MatMulAlignInputsFusionPass.md)  
<!-- end id32 -->

<!-- npu="950,A3,910b" id33 -->
- [BatchMatMul2MulFusionPass](BatchMatMul2MulFusionPass.md)  
<!-- end id33 -->

<!-- npu="950,A3,910b,910,310p,310b" id34 -->
- [AInplaceAddFusionPass](AInplaceAddFusionPass.md)  
<!-- end id34 -->

<!-- npu="950,A3,910b,910,310p,310b" id35 -->
- [AInplaceSubFusionPass](AInplaceSubFusionPass.md)  
<!-- end id35 -->

<!-- npu="950,A3,910b,910,310p,310b" id36 -->
- [AInplaceUpdateFusionPass](AInplaceUpdateFusionPass.md)  
<!-- end id36 -->

<!-- npu="A3,910b" id37 -->
- [BatchMatmulFixpipeFusionPass](BatchMatmulFixpipeFusionPass.md)  
<!-- end id37 -->

<!-- npu="A3,910b" id38 -->
- [IncreFlashAttentionQuantFusionPass](IncreFlashAttentionQuantFusionPass.md)  
<!-- end id38 -->

<!-- npu="A3,910b" id39 -->
- [PromptFlashAttentionQuantFusionPass](PromptFlashAttentionQuantFusionPass.md)  
<!-- end id39 -->

<!-- npu="310b" id40 -->
- [BatchMatMulDequantElemwiseFusionPass](BatchMatMulDequantElemwiseFusionPass.md)  
<!-- end id40 -->

<!-- npu="950,910b" id41 -->
- [AddLayerNormFusionPass](AddLayerNormFusionPass.md)  
<!-- end id41 -->

<!-- npu="950,A3,910b" id42 -->
- [IndexByTensorStaticFusionPass](IndexByTensorStaticFusionPass.md)  
<!-- end id42 -->

<!-- npu="A3,910b,310p" id43 -->
- [MaskedSoftmaxWithRelPosBiasFusionPass](MaskedSoftmaxWithRelPosBiasFusionPass.md)  
<!-- end id43 -->

<!-- npu="950,A3,910b" id44 -->
- [WeightQuantBatchMatmulV2TransposeFusionPass](WeightQuantBatchMatmulV2TransposeFusionPass.md)  
<!-- end id44 -->

<!-- npu="A3,910b,310p" id45 -->
- [GeGluV2FusionPass](GeGluV2FusionPass.md)  
<!-- end id45 -->

<!-- npu="950,A3,910b" id46 -->
- [QuantBatchMatmulV3TransposeFusionPass](QuantBatchMatmulV3TransposeFusionPass.md)  
<!-- end id46 -->

<!-- npu="A3,910b" id47 -->
- [FusedInferAttentionScoreQuantFusionPass](FusedInferAttentionScoreQuantFusionPass.md)  
<!-- end id47 -->

- [ConfusionTransposeTransDataFusionPass](ConfusionTransposeTransDataFusionPass.md)  

<!-- npu="950,A3,910b" id48 -->
- [QuantizeAddLayerNormPass](QuantizeAddLayerNormPass.md)  
<!-- end id48 -->

<!-- npu="950,A3,910b,310p" id49 -->
- [InplaceAddRmsNormFusionPass](InplaceAddRmsNormFusionPass.md)  
<!-- end id49 -->

<!-- npu="A3,910b" id50 -->
- [ZInplaceAddLayerNormFusionPass](ZInplaceAddLayerNormFusionPass.md)  
<!-- end id50 -->

<!-- npu="310p" id51 -->
- [TransdataTransposeTransdataBatchMatMulv2FusionPass](TransdataTransposeTransdataBatchMatMulv2FusionPass.md)  
<!-- end id51 -->

<!-- npu="310p" id52 -->
- [MatmulLayerNormReduceFusionPass](MatmulLayerNormReduceFusionPass.md)  
<!-- end id52 -->

<!-- npu="910b" id53 -->
- [DynamicQuantUpdateScatterFusionPass](DynamicQuantUpdateScatterFusionPass.md)  
<!-- end id53 -->

<!-- npu="950,910b" id54 -->
- [AscendQuantV2ScatterFusionPass](AscendQuantV2ScatterFusionPass.md)  
<!-- end id54 -->

<!-- npu="950,910b" id55 -->
- [AddLayerNormDynamicQuantFusionPass](AddLayerNormDynamicQuantFusionPass.md)  
<!-- end id55 -->

<!-- npu="950,A3,910b,310p" id56 -->
- [AddRmsNormQuantFusionPass](AddRmsNormQuantFusionPass.md)  
<!-- end id56 -->

<!-- npu="910b" id57 -->
- [GeluQuantFusionPass](GeluQuantFusionPass.md)  
<!-- end id57 -->

<!-- npu="950" id58 -->
- [DeleteNoConstFolding](DeleteNoConstFolding.md)  
<!-- end id58 -->

<!-- npu="950" id59 -->
- [TfMergeWeightQuantFusionPass](TfMergeWeightQuantFusionPass.md)  
<!-- end id59 -->

- [LayerNormSpecialFourGradsTrainingFusionPass](LayerNormSpecialFourGradsTrainingFusionPass.md)  

- [GroupedMatmulTransFusionPass](GroupedMatmulTransFusionPass.md)  

<!-- npu="A3,910b,310b" id60 -->
- [SameInputConv2dFixpipePass](SameInputConv2dFixpipePass.md)  
<!-- end id60 -->

<!-- npu="910,310p,310b" id61 -->
- [SpaceToBatchConv2dBatchToSpacePass](SpaceToBatchConv2dBatchToSpacePass.md)  
<!-- end id61 -->

<!-- npu="A3,910b,910,310p,310b" id62 -->
- [ConcatTileFusionPass](ConcatTileFusionPass.md)  
<!-- end id62 -->

<!-- npu="950,A3,910b,310b" id63 -->
- [MatmulReshapeTransposeFusionPass](MatmulReshapeTransposeFusionPass.md)  
<!-- end id63 -->

<!-- npu="950,A3,910b" id64 -->
- [AddRmsNormFusionGraphPass](AddRmsNormFusionGraphPass.md)  
<!-- end id64 -->

<!-- npu="950,A3,910b" id65 -->
- [AddRmsNormDynamicQuantFusionPass](AddRmsNormDynamicQuantFusionPass.md)  
<!-- end id65 -->

<!-- npu="910b" id66 -->
- [ReluFusionPass](ReluFusionPass.md)  
<!-- end id66 -->

<!-- npu="910b" id67 -->
- [CubeTransFixpipeFusionPass](CubeTransFixpipeFusionPass.md)  
<!-- end id67 -->

<!-- npu="910b" id68 -->
- [MatMulTransposeWeightFusionPass](MatMulTransposeWeightFusionPass.md)  
<!-- end id68 -->

<!-- npu="950,A3,910b,910,310p,310b" id69 -->
- [ConvFormatRefreshFusionPass](ConvFormatRefreshFusionPass.md)  
<!-- end id69 -->

<!-- npu="910b" id70 -->
- [FIXPIPEFUSIONPASS](FIXPIPEFUSIONPASS.md)  
<!-- end id70 -->

<!-- npu="910b" id71 -->
- [ConstToAttrReduceSumFusion](ConstToAttrReduceSumFusion.md)  
<!-- end id71 -->

<!-- npu="910b" id72 -->
- [AReduceSumFusionPass](AReduceSumFusionPass.md)  
<!-- end id72 -->

<!-- npu="910b" id73 -->
- [TransposedUpdateFusionPass](TransposedUpdateFusionPass.md)  
<!-- end id73 -->

<!-- npu="910b" id74 -->
- [ConstToAttrStridedSliceFusion](ConstToAttrStridedSliceFusion.md)  
<!-- end id74 -->

<!-- npu="910b" id75 -->
- [ZSplitVFusionPass](ZSplitVFusionPass.md)  
<!-- end id75 -->

<!-- npu="910b" id76 -->
- [ZSplitFusionPassV2](ZSplitFusionPassV2.md)  
<!-- end id76 -->

<!-- npu="950,910b" id77 -->
- [ZConfusionSoftmaxGradFusionPass](ZConfusionSoftmaxGradFusionPass.md)  
<!-- end id77 -->

<!-- npu="950,910b" id78 -->
- [SoftmaxGradExtFusion](SoftmaxGradExtFusion.md)  
<!-- end id78 -->

<!-- npu="910b" id79 -->
- [TransposeReshapeFusionPass](TransposeReshapeFusionPass.md)  
<!-- end id79 -->

<!-- npu="910b" id80 -->
- [SoftmaxGradFusionPass](SoftmaxGradFusionPass.md)  
<!-- end id80 -->

<!-- npu="910b" id81 -->
- [SparseSoftMaxFusionPass](SparseSoftMaxFusionPass.md)  
<!-- end id81 -->

<!-- npu="950,910b" id82 -->
- [FixPipeAbilityProcessPass](FixPipeAbilityProcessPass.md)  
<!-- end id82 -->

<!-- npu="910b" id84 -->
- [ARefreshCubeC0FusionPass](ARefreshCubeC0FusionPass.md)  
<!-- end id84 -->

<!-- npu="910b" id85 -->
- [ApplyAddOutputPass](ApplyAddOutputPass.md)  
<!-- end id85 -->

<!-- npu="910b" id86 -->
- [ZZMatMulToMatmulV3FusionPass](ZZMatMulToMatmulV3FusionPass.md)  
<!-- end id86 -->

<!-- npu="910b" id87 -->
- [PaddUpdateFusionPass](PaddUpdateFusionPass.md)  
<!-- end id87 -->

<!-- npu="910b" id88 -->
- [PadFusionPass](PadFusionPass.md)  
<!-- end id88 -->

<!-- npu="910b" id89 -->
- [ForceFp16CastFusionPass](ForceFp16CastFusionPass.md)  
<!-- end id89 -->

<!-- npu="950,910b" id83 -->
- [TensorScatterUpdateFusionPass](TensorScatterUpdateFusionPass.md)  
<!-- end id83 -->

<!-- npu="910b" id91 -->
- [SubFusionPass](SubFusionPass.md)  
<!-- end id91 -->

<!-- npu="910b" id92 -->
- [ZZConfusionTransposeNdFusionPass](ZZConfusionTransposeNdFusionPass.md)  
<!-- end id92 -->

<!-- npu="910b" id93 -->
- [AddNFusionPass](AddNFusionPass.md)  
<!-- end id93 -->

<!-- npu="910b" id94 -->
- [ReshapeTransposeFusionPass](ReshapeTransposeFusionPass.md)  
<!-- end id94 -->

<!-- npu="910b" id95 -->
- [SoftmaxCrossEntropyWithLogitsPass](SoftmaxCrossEntropyWithLogitsPass.md)  
<!-- end id95 -->

<!-- npu="950,A3,910b" id90 -->
- [MulAddNPass](MulAddNPass.md)  
<!-- end id90 -->

<!-- npu="910b" id96 -->
- [ZConcatExt2FusionPass](ZConcatExt2FusionPass.md)  
<!-- end id96 -->

<!-- npu="950,910b" id97 -->
- [EinsumPass](EinsumPass.md)  
<!-- end id97 -->

<!-- npu="950,A3,910b" id98 -->
- [MatmulReshapeFusionPass](MatmulReshapeFusionPass.md)  
<!-- end id98 -->

<!-- npu="950,910b,910,310p,310b" id99 -->
- [AABiasaddConvFusion](AABiasaddConvFusion.md)  
<!-- end id99 -->

<!-- npu="A3,910b,310p,310b" id100 -->
- [TileConstToAttrFusion](TileConstToAttrFusion.md)  
<!-- end id100 -->

<!-- npu="950,A3,910b" id101 -->
- [MatMulReshapeBiasAddFusionPass](MatMulReshapeBiasAddFusionPass.md)  
<!-- end id101 -->

<!-- npu="910b,910,310p,310b" id102 -->
- [RealDiv2MulsFusionPass](RealDiv2MulsFusionPass.md)  
<!-- end id102 -->

- [TopKFusionPass](TopKFusionPass.md)  

<!-- npu="950" id103 -->
- [UniqueSortFusionPass](UniqueSortFusionPass.md)  
<!-- end id103 -->

<!-- npu="950,A3,910b" id104 -->
- [BatchMatMul2TransposeBatchMatMulFusionPass](BatchMatMul2TransposeBatchMatMulFusionPass.md)  
<!-- end id104 -->

<!-- npu="950" id105 -->
- [BatchMatMulToBatchMatmulV3FusionPass](BatchMatMulToBatchMatmulV3FusionPass.md)  
<!-- end id105 -->

<!-- npu="950" id106 -->
- [MatMulToMatmulV3FusionPass](MatMulToMatmulV3FusionPass.md)  
<!-- end id106 -->

<!-- npu="950" id107 -->
- [BatchMatMulTransposeFusionPass](BatchMatMulTransposeFusionPass.md)  
<!-- end id107 -->

<!-- npu="950" id108 -->
- [MatmulToGemmOpFusionPass](MatmulToGemmOpFusionPass.md)  
<!-- end id108 -->

<!-- npu="950" id109 -->
- [BernoulliFusionPass](BernoulliFusionPass.md)  
<!-- end id109 -->

<!-- npu="950" id110 -->
- [RotaryMul2RotaryPositionEmbeddingFusionPass](RotaryMul2RotaryPositionEmbeddingFusionPass.md)  
<!-- end id110 -->

<!-- npu="950" id111 -->
- [InterleaveRope2RotaryPositionEmbeddingFusionPass](InterleaveRope2RotaryPositionEmbeddingFusionPass.md)  
<!-- end id111 -->

<!-- npu="950" id112 -->
- [RotaryMulGrad2RotaryPositionEmbeddingGradFusionPass](RotaryMulGrad2RotaryPositionEmbeddingGradFusionPass.md)  
<!-- end id112 -->
