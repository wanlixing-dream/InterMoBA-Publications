# _template/ — 原始投稿模板 (只读)

## 文件

- `paper-template.docx` — MDPI Word 模板 (`.docx` 格式, 含 `Type of the Paper (Article` 标题和 structured abstract 提示)
- `paper-template.zip` — MDPI LaTeX 模板压缩包
- `paper-template-extracted/` — zip 解压后的纯文本版本, 便于 grep
  - `paper_template.tex` — LaTeX 主模板
  - `image1.png` — 模板自带的图占位 (非 InterMoBA 真实图, 可忽略)

## 使用规则

- **不要直接编辑本目录下任何文件** — 它们是脚手架
- 把样式 (`\documentclass` / `authblk` / `lineno` / footer) 抄到 `../main.tex` 后**在 `../main.tex` 改**
- docx 模板用来检查 MDPI 投稿系统的 abstract / keywords 字段约束

## 模板识别信息

- `\fancyfoot[L]{\small APBC2026}` — 会议标识
- 文档类: `article` 11pt A4 (与 IEEEtran 完全不同, 投稿 MDPI 必须切换)
- structured abstract 4 段: Background / Methods / Results / Conclusions
- 关键词: 3-10 个, 出现在 abstract 之后、Introduction 之前
