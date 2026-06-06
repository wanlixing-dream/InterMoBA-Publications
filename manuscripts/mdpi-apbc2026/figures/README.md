# manuscripts/mdpi-apbc2026/figures/ — 本地图镜像

## 当前内容

- 27 个 `.png` 镜像自 `shared/figures/`
- 命名:
  - 主稿图: `fig1.png` … `fig4.png`
  - 补充图: `1.png` … `15.png`, `22.png`, `88.png`, `99.png`, `1010.png`, `1212.png`, `1313.png`, `1414.png`, `1515.png`

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
