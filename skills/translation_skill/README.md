# 翻译skill使用方法

1. 将exclude_docs.json和translation_skill.md下载到本地。

2. 修改exclude_docs.json文件中需要排除翻译的信息：

   - exclude_docs.json文件中`excludeDocsPaths`配置信息是可以自己配置的，根据自己仓的情况，排除不需要翻译的内容。
   - `publicRepo`为用户clone到本地的仓库名字，该字段会和用户本地仓库的名字进行模糊匹配。

3. 在opencode中输入类似如下信息，启动skill翻译任务：

   根据translation_skill.md skill，处理xxx仓或yyy.md文件，其中，xxx为用户Fork到本地的组件仓库，yyy为仓中的md文档。

   说明：上述翻译skill会将翻译后的英文文档提交到远程仓库，如果不希望提交，可以在上面的描述后面补充：翻译完成后，无需提交到远程仓库。
