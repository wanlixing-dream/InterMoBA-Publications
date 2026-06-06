# manuscripts/mdpi-apbc2026/figures/ — 本地图镜像

## 当前内容

- 27 个 `.png` 镜像自 `shared/figures/`
- 命名:
  - 主稿图: `fig1.png` … `fig4.png`
  - 补充图: `1.png` … `15.png`, `22.png`, `88.png`, `99.png`, `1010.png`, `1212.png`, `1313.png`, `1414.png`, `1515.png`
  - SVG 源稿: `fig1_source.svg` … `fig4_source.svg`
  - 期刊风格工作稿: `fig1_nature.svg` … `fig4_nature.svg`

## SVG 工作稿说明

- `fig*_source.svg` 是从 `_archive/ieee-journal-2026/fig*.svg` 复制来的 draw.io 导出源稿, 用于保留原始结构。
- `fig*_nature.svg` 是按 SCI/Nature 风格整理的工作稿: 白底、低饱和配色、统一 Arial 字体、收敛线宽与面板标注。
- `fig3_nature.svg` 已重画为纯矢量示意图, 不含嵌入位图。
- `fig1_nature.svg`, `fig2_nature.svg`, `fig4_nature.svg` 仍包含 draw.io 导出的嵌入位图面板。若要完全矢量化, 需要对应的原始数据表、结构文件或绘图脚本。

## 同步规则

当 `shared/figures/` 里有新图或更新时, 镜像到此目录:

```powershell
# 复制所有
Get-ChildItem -Force ..\..\..\shared\figures | Copy-Item -Destination . -Force
```

## 为什么用 copy 而不是 junction / symlink

- **Junction 在 git 跨平台 checkout 时不可靠** (Windows-mklink 不被 macOS/Linux git 识别)
- **Copy 让 main.tex 无需改 \includegraphics 路径** (图与 .tex 同级, LaTeX 默认查找)
- **零工具依赖**, 不需要额外脚本

## 未来若改用 junction

可在 PowerShell 上:

```powershell
Remove-Item -Recurse -Force .\figures
New-Item -ItemType Junction -Path .\figures -Target ..\..\..\shared\figures
```

但请在 `shared/bib/README.md` 与本 README 里同步说明, 并在 `.gitattributes` 里加 `figures/* merge=ours` 防止 git 尝试把 junction 当 symlink 提交。
