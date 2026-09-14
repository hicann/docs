# Markdown 文档审查 Skill 安装指南

## 前置要求

- Python 3.8 或更高版本
- Python `requests` 库（`pip install requests`）
- OpenCode 已安装并配置
- GitCode 账号及 Personal Access Token

## 安装步骤

### 1. 放置 Skill 文件

```bash
cp -r md-review-skill ~/.config/opencode/skills/
```

### 2. 配置 Token

在 `~/.config/opencode/skills/md-review-skill/config/` 目录下创建 `gitcode-config.json`：

```bash
mkdir -p ~/.config/opencode/skills/md-review-skill/config
```

创建配置文件：

```json
{
  "token": "your-gitcode-token"
}
```

获取 Token 方式：

1. 登录 GitCode
2. 进入个人设置 → 访问令牌
3. 创建新令牌，勾选相关权限

### 3. 验证安装

在 OpenCode 中加载 skill 并验证：

```bash
/skills md-review-skill
```

## 安全说明

**Token 不暴露给 LLM**：

- Token存储在本skill的`gitcode-config.json`中。
- API调用通过本skill自带的 `scripts/api_client.py --config <path>` 执行。
- LLM只知道配置文件路径，无法获取Token内容。

## 目录结构

```text
md-review-skill/
├── SKILL.md                    # Skill定义文件（含 Markdown 文档审查规则）
├── README.md                   # 介绍文档
├── INSTALL.md                  # 安装指南
├── scripts/
│   ├── api_client.py           # GitCode API 调用封装（Token 不暴露）
│   └── get_config.py           # 配置读取工具
└── config/
    ├── gitcode-config.json      # Token 配置（需手动创建）
    └── gitcode-config.example.json
```

## 快速开始

1. 在 OpenCode 中加载 skill
2. 获取 PR 的远程引用并创建本地分支：

   ```bash
   git fetch origin refs/merge-requests/<pr_number>/head:pr_<pr_number>
   git checkout pr_<pr_number>
   ```

3. 开始审查：

   ```bash
   请审查 PR #<pr_number>
   ```

## 常见问题

### Q: Token 配置在哪里？

A: 在 `~/.config/opencode/skills/md-review-skill/config/gitcode-config.json` 中。

### Q: 为什么不切换分支就看不到 PR 的新文件？

A: PR 的文件在独立的分支上，必须通过 `git checkout` 切换到该分支才能看到新增的文件。
