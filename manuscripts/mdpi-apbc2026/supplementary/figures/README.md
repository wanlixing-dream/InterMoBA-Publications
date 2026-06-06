# manuscripts/mdpi-apbc2026/supplementary/figures/ — supplementary 图镜像

## 当前内容

- 27 个 `.png` 镜像自 `shared/figures/`, 与 `manuscripts/mdpi-apbc2026/figures/` 内容一致
- 命名: 与主稿 figures 一致 (`1.png` … `15.png` 等)

## 同步规则

当 `shared/figures/` 更新时, 同步:

```powershell
Get-ChildItem -Force ..\..\..\..\shared\figures | Copy-Item -Destination . -Force
```

## supp.tex 引用方式

`supp.tex` 中, 图路径写法:

```latex
\includegraphics[width=0.8\textwidth]{figures/1.png}
```

(因 supp.tex 与 figures/ 同级在 supplementary/ 内)
