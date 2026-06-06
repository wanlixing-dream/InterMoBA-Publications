# shared/figures/ — 跨 target 共享原图

## 当前内容

- 主稿图: `fig1.png` … `fig4.png` (来自 IEEE 版)
- 补充图: `1.png` … `15.png`, `22.png`, `88.png`, `99.png`, `1010.png`, `1212.png`, `1313.png`, `1414.png`, `1515.png` (来自 IEEE supplementary)
- 命名**与 `_archive/ieee-journal-2026/supplementary/` 同步**, 方便交叉引用

## 谁引用了这些图

- `_archive/ieee-journal-2026/InterMoBA.tex` — 主稿 (用 `fig{n}.png`)
- `_archive/ieee-journal-2026/supplementary/InterMoBA_supplimentary.tex` — 补充材料
- `manuscripts/mdpi-apbc2026/main.tex` — 主投 (主稿占位, 后续写作时引用)
- `manuscripts/mdpi-apbc2026/supplementary/supp.tex` — 主投补充材料 (主投占位)

## 命名不重命名原则

刻意保留原 IEEE 版 png 命名 (1.png, 22.png, 88.png, 99.png, 1010.png, …) — 重命名会:
- 丢失原补充材料的图号语义 (22/88/99/1010 看起来像 1.xx sub-numbering)
- 破坏 archive 侧与共享侧的同步

## 同步规则 (Manuscript 侧 → shared)

新主投 target 不需要反过来同步到 shared — shared 是源, manuscript 是镜像。

当新 png 加入 (例如新实验结果) 时:
1. 放进 `shared/figures/`
2. 同步到所有 active target 的 `figures/`
3. archive 不动
