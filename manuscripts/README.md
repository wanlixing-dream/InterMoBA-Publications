# manuscripts/ — 索引

```
manuscripts/
├── mdpi-apbc2026/         # PRIMARY submission target — APBC2026 (MDPI)
└── _archive/
    └── ieee-journal-2026/ # HISTORICAL — 完整保留的 IEEE 期刊版 (含 .tex/.pdf/.bib/IEEEtran.cls/figs/LaTeX 构建产物/supplementary)
```

## 命名约定

- **Active target** 直接以期刊/会议短名命名, 不带 `_` 前缀: `mdpi-apbc2026/`, `nature-communications/` 等
- **历史 / 弃用 target** 放在 `_archive/<venue>-<year>/`, 保留完整结构以便日后查阅

## 添加新 target

```bash
# 1. 建目录
mkdir -p manuscripts/<venue>/_template
# 2. 拷贝 figures 镜像
Get-ChildItem -Force ..\shared\figures | Copy-Item -Destination <venue>\figures -Force
# 3. 拷贝 bib
Copy-Item ..\shared\bib\references.bib <venue>\reference.bib
# 4. 在 _template/ 放下原始投稿模板
# 5. 在 docs/journal-notes/<venue>.md 写要求
# 6. 在顶层 README.md "Submission status" 表加一行
```

## 共享素材引用

`manuscripts/<target>/figures/` 与 `manuscripts/<target>/reference.bib` 是**本地副本** (非 junction), 同步规则见各 `figures/README.md` 与 `shared/bib/README.md`。
