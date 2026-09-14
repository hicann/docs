---
name: md-review-skill
description: Markdown文档审查Skill - 用于 Committer/Reviewer 审查 PR 中的 Markdown 文档变更，覆盖原型与头文件一致性、参数解释准确性、代码样例正确性、开源写作规范等。触发词：检视md、文档检视、md review、文档规范检查、PR审查、审查PR、检查PR、评审PR。
---

# Markdown 文档审查 Skill

## 概述

Markdown 文档审查工具，帮助Committer高效审查GitCode上 Pull Request 中的 `.md` 文件变更。仅关注 Markdown 文档内容质量，不审查代码文件（`.h`、`.py`、`.cpp` 等）。

## 安全机制

- **Token 不暴露给 LLM**：Token 存储在本 skill 的 `gitcode-config.json` 中。
- **API 调用通过本 skill 自带的 api_client.py**：使用 `scripts/api_client.py --config <path>` 调用。
- **写操作需用户确认**：提交评论等操作需要用户显式确认。

## 功能特性

- 支持手动触发模式。
- **Markdown 文档规范检视**：当 PR 包含 `.md` 文件变更时，按内置规则进行文档写作规范检查，覆盖原型与头文件一致性、参数解释准确性、代码样例正确性、15 类开源写作规范、语言通顺性、敏感词检测、术语规范性。
- **评论提交需用户确认**：生成报告后询问用户需要提交哪些问题，未经用户确认不得自动提交评论。

## 使用方法

### 触发方式

在 OpenCode 中加载此 skill 后，用户输入以下任意触发词即可启动文档审查：

| 触发词 | 说明 |
|------|------|
| `请审查PR <pr_number>` | 标准触发，审查指定 PR 中的 `.md` 文件变更 |
| `请审查PR：<pr_number>` | 触发词变体（中文冒号） |
| `请检查PR <pr_number>` | 等效触发词 |
| `请检查PR：<pr_number>` | 等效触发词变体 |
| `请评审PR <pr_number>` | 等效触发词 |
| `请评审PR：<pr_number>` | 等效触发词变体 |
| `检视md` | 通用触发，需后续补充 PR 编号 |
| `文档检视` | 通用触发，需后续补充 PR 编号 |
| `md review` | 通用触发，需后续补充 PR 编号 |

**触发流程**：

1. 用户输入触发词 + PR 编号（或仅输入触发词后交互补充编号）
2. Skill 自动执行完整审查流程（见「工作流程」章节）
3. 生成审查报告并展示给用户
4. 用户确认后提交评论到 GitCode PR

**示例**：
```
请审查PR 1411
请检查PR：1411
请评审PR #1411
```

### 切换到 PR 分支

**审查前必须切换到 PR 对应的本地分支**，否则无法看到 PR 新增的文件！这是审查流程的前置步骤，触发后自动执行：

```
# 1. 确保远程 master 已同步
git fetch origin master

# 2. 获取 PR 的远程引用并创建本地分支
git fetch origin refs/merge-requests/<pr_number>/head:pr_<pr_number>

# 3. 切换到该分支（关键步骤！）
git checkout pr_<pr_number>

# 4. 开始文档审查
# 此时可以查看 PR 新增的 .md 文件、分析文档内容等
```

**常见问题**：
- 如果不执行 `git checkout`，后续分析仍停留在原分支（如 master）
- PR 新增的文件（如 `docs/api/aclnnAdd.md`）只有在切换到 PR 分支后才能看到
- `git show pr_<pr_number>:<path>` 只查看特定文件，不会切换工作区
- **使用三个点 (...) 而非两个点 (..)**：`git diff master..pr` 会包含 master 上的其他提交，正确做法是 `git diff master...pr`
- **本地 master 与远程不同步**：如果本地 master 落后于远程，`git diff master...pr` 会包含不属于 PR 的变更。**必须先执行 `git fetch origin master` 并使用 `remotes/origin/master` 进行比较**

## 审查维度

### Markdown 文档审查维度（重点）

当 PR 包含 `.md` 文件变更时，**必须**按以下维度逐项审查。

#### 审查维度总表

| 维度 | 严重程度 | 说明 |
|------|---------|------|
| 原型与头文件一致性 | HIGH | 文档中函数原型、宏定义、常量值、参数名必须与头文件定义完全一致 |
| 参数解释准确性 | HIGH | 每个参数有对应说明，数据类型、约束条件、取值范围、默认值描述准确 |
| 代码样例正确性 | HIGH | 代码示例中无未定义的变量/函数/类，所有引用符号已声明或说明来源 |
| 文档写作规范 | MEDIUM | 文件命名、标题层级、字体样式、图片、列表、链接、表格、标点、目录结构、编码格式等 15 类规则 |
| 语言通顺性 | HIGH | 语句通顺、语法正确、无错别字、无歧义表达、中英文混排规范 |
| 敏感词检测 | HIGH | 不包含政治敏感、种族歧视、性别歧视、夸大宣传等违规内容 |
| 术语规范性 | HIGH | 所有专业术语首次出现时必须有解释或全称说明，不得使用未定义的缩写或术语 |

---

#### 原型与头文件一致性

审查时**可参考仓库中已有的**头文件（`.h`/`.hpp`）定义，逐项核对 Markdown 文档中的原型描述。注意：头文件仅作为参考来源，不是审查目标。

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| PH-01 | 文档中声明的函数原型必须与头文件定义完全一致：函数名、参数列表（类型、顺序、个数）、返回值类型 | CRITICAL |
| PH-02 | 参数名称应与头文件中定义的参数名一致；如文档为可读性改用别名，需在同一行注明头文件原始名称 | HIGH |
| PH-03 | 文档中的宏定义名称、常量值、枚举值必须与头文件一致 | HIGH |
| PH-04 | 函数说明中提到的默认值、取值范围、数据类型支持列表必须与头文件/代码实现一致 | HIGH |
| PH-05 | 当头文件有多个版本接口（如 V1/V2、WeightNz 变体）时，文档需明确标注对应版本，不得混淆 | MEDIUM |
| PH-06 | 文档中引用的头文件路径（`#include` 路径）必须与实际头文件位置一致 | HIGH |
| PH-07 | 若 PR 修改了头文件中的接口定义，对应的 Markdown 文档必须同步更新，不得遗留旧版原型 | CRITICAL |

**审查方法**：
1. 识别 PR 中变更的 `.md` 文件
2. 如文档涉及函数原型说明，参考仓库中已有的 `.h`/`.hpp` 文件提取函数签名、宏定义、枚举
3. 与 Markdown 文档中的原型声明逐字段对比
4. 记录不一致项，标注文档行号

---

#### 参数解释准确性

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| PA-01 | 函数的每个参数必须在文档中有对应的解释说明，不得遗漏任何参数 | HIGH |
| PA-02 | 参数的数据类型描述必须准确（如 "Tensor" 不得描述为 "标量"，"int64_t" 不得描述为 "float"） | HIGH |
| PA-03 | 参数的约束条件必须准确说明：支持的数据类型范围、shape 约束、内存对齐要求、值域限制 | HIGH |
| PA-04 | 输入参数（IN）与输出参数（OUT）必须明确区分标注 | MEDIUM |
| PA-05 | 参数的取值范围和默认值需准确说明，与头文件/代码实现一致 | HIGH |
| PA-06 | 可选参数需标注"可选"，并说明省略时的默认行为 | MEDIUM |
| PA-07 | 参数说明中不得出现与头文件参数类型矛盾的限制（如头文件为 `int8_t` 但文档写"float 类型"） | CRITICAL |
| PA-08 | 若参数为结构体/枚举类型，需说明结构体各字段含义或枚举各值的含义 | MEDIUM |
| PA-09 | 返回值说明必须准确：返回值类型、成功/失败的返回值含义、错误码说明 | HIGH |

---

#### 代码样例正确性

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| CC-01 | 代码示例中不得包含未定义的变量、函数或类 | HIGH |
| CC-02 | 所有引用的符号必须在示例中声明或明确说明来源 | HIGH |
| CC-03 | 代码逻辑必须正确，不得包含会导致编译错误或运行时错误的语句 | HIGH |
| CC-04 | 代码示例中使用的 API 参数值必须在合法取值范围内 | MEDIUM |

---

#### 开源写作规范检视规则

以下 15 类规则来源于 CANN 开源资料写作规范，用于检查 Markdown 文档的格式规范性。

##### 1 文件命名

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| FN-01 | 文件名必须以英文字母命名 | MEDIUM |
| FN-02 | 多个单词以下划线（_）或中划线（-）连接 | MEDIUM |
| FN-03 | 文件名不宜超过 50 个字符 | LOW |
| FN-04 | 中文 README 命名为 `README.md`，英文命名为 `README_en.md` | HIGH |
| FN-05 | 同一目录下不能出现重名文件 | CRITICAL |
| FN-06 | 新增文档必须以 `.md` 结尾 | HIGH |

##### 2 标题

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| HD-01 | 标题应简洁明了，概括章节核心内容 | LOW |
| HD-02 | 操作类标题使用动宾结构（如"申请权限"）；同级别同类型标题结构保持一致 | MEDIUM |
| HD-03 | 标题末尾不加标点，避免使用特殊字符（如"?"），补充说明使用圆括号 | MEDIUM |
| HD-04 | 标题与正文间空一行 | LOW |
| HD-05 | 标题使用 `# [标题名]` 格式，标题级别需逐级递增，第一个标题应该是顶层标题 | HIGH |
| HD-06 | 标题中不能手工添加序号（如 `## 1. 安装CANN` 应改为 `## 安装CANN`） | MEDIUM |
| HD-07 | 标题建议最多四级 | LOW |

##### 3 字体样式

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| FS-01 | 斜体使用一个星号 `*文本*` | LOW |
| FS-02 | 粗体使用两个星号 `**文本**` | LOW |
| FS-03 | 粗斜体使用三个星号 `***文本***` | LOW |
| FS-04 | 对特定内容使用转义符 `\` | LOW |

##### 4 图片

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| IMG-01 | 图片以英文小写命名，多单词下划线连接，名称不超过 50 字符 | MEDIUM |
| IMG-02 | 图片统一存放到文档同级目录下的 `figures` 文件夹中，使用相对路径引用 | HIGH |
| IMG-03 | 使用原创图片，避免侵权 | HIGH |
| IMG-04 | 图文配合使用，切忌图文分离 | MEDIUM |
| IMG-05 | 图片格式首选 PNG，次选 JPG | LOW |
| IMG-06 | 中/英文文档须分别使用对应语言的插图 | MEDIUM |
| IMG-07 | 截图应只保留核心内容，关键信息可用红框或文字标注 | LOW |
| IMG-08 | 确保图片清晰可辨 | LOW |

图片插入格式：

```markdown
![alt 属性文本](图片地址)
![alt 属性文本](图片地址 "可选标题")
```

##### 5 代码块

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| CB-01 | 确保代码的逻辑和语法正确 | HIGH |
| CB-02 | 清晰区分输入与输出部分 | MEDIUM |
| CB-03 | 关键步骤须有注释说明 | MEDIUM |
| CB-04 | 行内代码和命令行使用 1 对反引号 | LOW |
| CB-05 | 块级代码使用 3 个反引号，并声明语言类型，上下空一行 | MEDIUM |
| CB-06 | 语言类型应正确声明（python、c、c++、bash、json、yaml 等） | LOW |

##### 6 列表

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| LS-01 | 有明显先后逻辑顺序使用有序列表，并列关系/多选一使用无序列表 | MEDIUM |
| LS-02 | 术语/短语列表项统一不加标点；完整句子统一加句号；混合情况统一加句号 | LOW |
| LS-03 | 无序列表标记（`*`/`+`/`-`）后必须添加空格 | MEDIUM |
| LS-04 | 同一文件中同一层级的无序列表建议使用同一符号 | LOW |
| LS-05 | 有序列表使用数字加 `.` 号，不支持字母序号 | MEDIUM |
| LS-06 | 嵌套列表在子列表项前添加两个或四个空格（不使用 tab） | MEDIUM |

##### 7 注释符号

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| NT-01 | 根据使用场景选择恰当的注释符号（NOTE/CAUTION/WARNING） | MEDIUM |
| NT-02 | 注释块内可嵌套列表，不建议嵌套表格和代码块 | LOW |
| NT-03 | 使用连续的 `>` 符号以保证样式不中断 | MEDIUM |
| NT-04 | 说明/注意等样式中内容应简洁，过长可迁移至正文或分段处理 | LOW |

注释格式：

```markdown
> [!NOTE]说明
> 正文

> [!CAUTION]注意
> 正文

> [!WARNING]警告
> 正文
```

##### 8 链接

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| LK-01 | 确保链接目标有效，避免死链 | HIGH |
| LK-02 | 引用文档时建议用书名号包裹并添加超链接 | LOW |

##### 9 锚点

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| AN-01 | 引用文档内标题、图片或表格时使用锚点 | MEDIUM |
| AN-02 | 锚点方法一：大写字母转小写，空格替换为中划线 `-`，去除特殊符号 | LOW |
| AN-03 | 锚点方法二：使用 `<a>` 标签自定义锚点 ID | LOW |

##### 10 表格

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| TB-01 | 使用标准 markdown 表格语法，不建议使用 HTML 表格 | MEDIUM |
| TB-02 | 术语/短语列统一不加标点；句子列统一加句号；混合情况统一加句号 | LOW |

##### 11 标点符号

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| PN-01 | 单位与数字、中文与英文、中文与中文之间不加空格（例外：产品名称如 Atlas 350 加速卡） | MEDIUM |
| PN-02 | `=`、`~`、`>`、`<` 符号前后加空格 | LOW |
| PN-03 | 列表项标点使用保持一致 | MEDIUM |
| PN-04 | 中文文档使用全角标点，数字使用半角字符 | MEDIUM |
| PN-05 | 感叹号仅用于可能引发严重人身或设备安全后果的警告 | HIGH |
| PN-06 | 引用其他文档时添加书名号，并建议增加跳转链接 | LOW |

##### 12 目录结构

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| DS-01 | 单一项目的多个文档统一存放于 `docs` 目录下，按子目录分类管理 | MEDIUM |
| DS-02 | `docs` 目录下区分 `zh`（中文）与 `en`（英文）子目录 | MEDIUM |
| DS-03 | 文档数量少时可不区分 `zh/en`，采用文件后缀区分（英文加 `_en` 后缀） | LOW |
| DS-04 | 与代码强关联的文档直接归档在对应代码目录下 | LOW |
| DS-05 | 每个 API 或类对应一个 markdown 文件，项目内保持统一 | MEDIUM |
| DS-06 | API 文档必须提供目录索引文件（如 `README.md` 或 `xx_list.md`） | HIGH |
| DS-07 | API 按框架/组件/语言分类时须通过子目录区分 | MEDIUM |

##### 13 文件编码

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| EC-01 | 必须使用 UTF-8 编码（无 BOM） | HIGH |
| EC-02 | 不可使用 UTF-8 with BOM（文件头不含 EF BB BF） | HIGH |

##### 14 文档内容要求

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| CT-01 | 开源项目须包含：概述、编译安装、本地验证、贡献指南、许可证 | HIGH |
| CT-02 | 可选内容：样例使用指导、参考文档、定制开发指导、API 参考 | LOW |

##### 15 贡献合规

| 编号 | 规则 | 严重级别 |
|------|------|---------|
| CP-01 | 提交内容必须与 CANN 特性相关 | HIGH |
| CP-02 | 不能包含敏感信息、种族歧视或性别歧视内容 | CRITICAL |
| CP-03 | 提交内容必须原创，不得侵犯他人知识产权 | CRITICAL |
| CP-04 | 内容必须客观真实，不允许使用夸大宣传词汇 | HIGH |
| CP-05 | 禁止短时间通过自动化工具提交大量"无害错误"修正 | MEDIUM |

---

#### 检视输出格式

每条检视意见使用以下 JSON 格式：

```json
{
  "severity": "CRITICAL|HIGH|MEDIUM|LOW",
  "file": "docs/path/to/file.md",
  "line": 42,
  "rule_id": "HD-05",
  "dimension": "标题规范",
  "title": "标题级别未逐级递增",
  "body": "第 42 行使用了 `####` 四级标题，但其上级为二级标题 `##`，跳过了三级标题。请补充 `###` 三级标题或调整层级。",
  "code_snippet": "该行内容片段"
}
```

#### Markdown 检视流程

1. 识别 PR 中变更的 `.md` 文件
2. **原型一致性检查**：可参考仓库中已有的 `.h`/`.hpp` 头文件提取函数签名，与文档原型逐字段对比
3. **参数准确性检查**：核对每个参数的类型、约束、默认值描述是否准确
4. **代码样例正确性检查**：验证示例中无未定义符号、无编译/运行时错误
5. **写作规范检查**：逐文件按上述 15 类规则检查
6. **语言与敏感词检查**：通顺性、术语规范性、敏感词检测
7. 记录每条违规的规则编号、严重级别、具体位置
8. 输出结构化检视意见
9. 汇总报告：按严重级别统计违规数量，列出高频违规类型

## 工作流程

用户触发后，Skill 自动按以下步骤执行：

1. **同步远程 master**
   ```bash
   git fetch origin master
   ```
   **重要**：这会更新 `remotes/origin/master` 指针。如果本地 master 落后于远程，对比 PR 时会包含不属于 PR 的变更，导致审查结果不准确。
2. **获取并切换到 PR 分支**
   ```bash
   git fetch origin refs/merge-requests/<pr_number>/head:pr_<pr_number>
   git checkout pr_<pr_number>
   ```
3. **获取变更文件列表**
   - 使用三个点查看 PR 的真正 diff：
     ```bash
     git diff remotes/origin/master...pr_<pr_number> --stat   # 变更文件列表
     git diff remotes/origin/master...pr_<pr_number> -p       # 详细变更
     ```
   - **必须使用 `remotes/origin/master`**，不能使用本地 `master`，因为本地 master 可能与远程不同步
4. **检测 Markdown 文档变更**
   - 检查 diff 中是否包含 `.md` 文件的变更：
     ```bash
     git diff remotes/origin/master...pr_<pr_number> --stat | grep '\.md'
     ```
   - 本 skill **仅审查 `.md` 文件**，不审查代码文件（`.h`、`.py`、`.cpp` 等）。当需要核对文档中原型与头文件一致性时，可读取仓库中已有的 `.h`/`.hpp` 文件作为参考，但不对其进行审查。
   - 如果检测到 `.md` 文件变更，**必须按本文档「Markdown 文档审查维度（重点）」中的规则逐项检视**：
     - **原型与头文件一致性**：可参考仓库中已有的 `.h`/`.hpp` 头文件，核对文档中的函数原型、参数名、宏定义、常量值是否完全一致（规则 PH-01 ~ PH-07）
     - **参数解释准确性**：核对每个参数是否有说明，类型、约束、取值范围、默认值是否准确（规则 PA-01 ~ PA-09）
     - **代码样例正确性**：验证无未定义符号、无编译/运行时错误（规则 CC-01 ~ CC-04）
     - **开源写作规范**：按 15 类规则逐项检查文件命名、标题、字体样式、图片、代码块、列表、注释符号、链接、锚点、表格、标点符号、目录结构、编码格式、文档内容、贡献合规
     - **语言通顺性、敏感词检测、术语规范性**：通读全文检查
   - 将 Markdown 检视结果合并到审查报告中，维度标记为 `[文档规范]`
5. **生成审查报告**
   - 输出结构化的问题列表
   - 按严重程度分类
6. **询问用户确认提交评论**
   - 生成报告后，向用户展示问题编号列表，询问需要将哪些问题提交到远程 PR
   - 用户可选择：提交全部问题、提交部分问题（指定编号）、不提交任何评论
   - **严禁未经用户确认就自动提交评论**，只有在用户明确要求时才执行提交操作
7. **按用户选择提交评论**
   - 仅提交用户选定的评论到 GitCode PR
   - 通过本 skill 自带的 API 工具提交

## 审查报告格式

```markdown
## 文档审查报告: PR #1411 - [PR标题]

**作者:** @author
**分支:** feature/xxx → main

### 概览

| 维度 | 问题数 | 严重 |
|------|--------|------|
| 原型与头文件一致性 | 2 | HIGH |
| 参数解释准确性 | 1 | HIGH |
| 代码样例正确性 | 1 | HIGH |
| 文档写作规范 | 3 | MEDIUM |
| 语言通顺性 | 1 | HIGH |

### 严重问题 (3)

**[1]** [原型一致性] docs/api/aclnnAdd.md:45
- **问题:** 文档中函数原型参数列表与头文件不一致，缺少 `workspaceSize` 参数
- **建议:** 补充 `workspaceSize` 参数，与头文件定义保持一致

### 警告问题 (10)

...
```

## 评论提交

⚠️ **重要规则：评论提交必须经过用户确认，严禁自动提交！**

生成审查报告后，必须向用户询问：
- 需要将哪些问题提交到远程 PR？
- 用户可以选择：提交全部、提交部分（指定问题编号）、不提交

只有在用户明确要求提交评论时，才通过本 skill 自带的 API 工具提交到 PR。

### 行内评论字段格式

**重要**：GitCode 接受 GitHub 风格的三个扁平字段：

| 字段 | 含义 |
|------|------|
| `path` | 文件路径（必填，PR 变更中的文件） |
| `position` | **绝对行号**（PR head 侧文件中的行号，**不是 diff hunk 偏移**） |
| `side` | `"RIGHT"`（默认，新增/上下文）或 `"LEFT"`（被删除的行） |

**绝对行号 = 审查报告中的 `文件:行号` 直接使用**。无需做 diff hunk 偏移反算。

提交后 GitCode 内部把 `position` 存为 `position.new_line`，把 `path` 存为
`position.old_path` / `position.new_path`，但这是 Gitea 内部存储格式——**POST
时只接受扁平字段，不要写嵌套的 `position` 对象**（会被 400 拒绝）。

### 评论正文格式

```
[严重] [维度] docs/path/to/file.md:行号
问题描述
建议修复方案
```

### API 调用方式（Token 不暴露）

⚠️ **必须使用 `python3`**：Linux 系统中 `python` 通常不存在，使用 `python3` 调用。

```bash
python3 ~/.config/opencode/skills/md-review-skill/scripts/api_client.py POST \
  /repos/cann/hcomm/pulls/2086/comments \
  --config ~/.config/opencode/skills/md-review-skill/config/gitcode-config.json \
  --data '{
    "body": "[严重] [原型一致性] docs/api/aclnnAdd.md:45 ...",
    "path": "docs/api/aclnnAdd.md",
    "position": 45,
    "side": "RIGHT"
  }'
```

**POST 响应字段**：返回的 JSON 包含两个关键字段：
- `id`：数字类型的 `note_id`（用于后续 GET/DELETE 验证）
- `discussion_id`：SHA 字符串（**不是**用于 API 路径的 ID）

### 提交后必须验证

提交一条后立即 `GET /pulls/comments/{note_id}` 验证 `position.new_line` 是否
就是你想要的行号。**这是 GitCode 文档不完整情况下唯一可信的对错验证**。
批量提交前务必先发 1 条做 smoke test。

⚠️ **路径参数是 `note_id`（数字），不是 `discussion_id`（SHA）**：用 `discussion_id` 调用会返回 400 `Invalid path parameter: note_id, number required`。

```bash
# 验证位置正确（用 POST 响应中的数字 id）
python3 ~/.config/opencode/skills/md-review-skill/scripts/api_client.py GET \
  /repos/cann/hcomm/pulls/comments/<note_id> \
  --config ~/.config/opencode/skills/md-review-skill/config/gitcode-config.json
# 检查返回 JSON 中 position.new_line 与目标行号一致
```

### 撤回错位评论

如果验证发现评论被错位（`new_line` 不对、文件路径不对），立刻撤回：

⚠️ **同样使用 `note_id`（数字）作为路径参数**：

```bash
# 撤回单条
python3 ~/.config/opencode/skills/md-review-skill/scripts/api_client.py DELETE \
  /repos/cann/hcomm/pulls/comments/<note_id> \
  --config ~/.config/opencode/skills/md-review-skill/config/gitcode-config.json
# 返回 204 No Content 即成功
```

撤回后修正字段重新 POST，**不要**先批量提交 14 条再发现全错位。

### 完整流程示意

1. 写完审查报告（含绝对行号）
2. 用户确认要提交哪些 issue
3. 先 POST 1 条 smoke test
4. GET 单条验证 `new_line` 正确
5. 通过后批量 POST 剩余
6. 全部提交后 GET 列表复核
7. 如发现错位，DELETE + 修正 + 重提

## 配置文件

- `~/.config/opencode/skills/md-review-skill/config/gitcode-config.json` - 专属 Token 配置

## Token 配置

本 skill 使用独立的 `gitcode-config.json` 配置 Token：

```json
{
  "token": "your-gitcode-token"
}
```

- Token 仅在本 skill 的配置文件中，调用 API 时通过 `--config` 传递给 `api_client.py`
- LLM 只能看到配置文件路径，无法获取 Token 内容

## 依赖

- **Python 3.8+（必须用 `python3` 命令调用）**：Linux 系统通常没有 `python` 软链接
- OpenCode LLM 集成
- Python `requests` 库（`api_client.py` 依赖）
- 本 skill 自带的 `scripts/api_client.py`（API 调用封装，Token 不暴露）

## 文件结构

```
~/.config/opencode/skills/md-review-skill/
├── SKILL.md                    # 本文件（含 Markdown 文档审查规则，已合并 md_skill.md 内容）
├── scripts/
│   ├── api_client.py           # GitCode API 调用封装（Token 不暴露）
│   └── get_config.py           # 配置读取工具
└── config/
    ├── gitcode-config.json     # Token 配置（需手动创建）
    └── gitcode-config.example.json
```
