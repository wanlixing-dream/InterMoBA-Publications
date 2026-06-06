# shared/bib/ — 共享参考文献库

## 当前内容

- `references.bib` — 当前 = 仓库中唯一一份 `.bib` 源, 来自早期 IEEE 版 (`InterMoBA_conference/reference.bib`).
- 后续新加 target (例如未来再投一本期刊) 应当:
  1. 在主稿写作过程中**追加**新引用到此文件
  2. 同步镜像到对应 `manuscripts/<target>/reference.bib`

## 同步到具体 target

```bash
# PowerShell
Copy-Item -LiteralPath ..\..\shared\bib\references.bib -Destination <target>\reference.bib -Force
```

`manuscripts/mdpi-apbc2026/reference.bib` 当前是 `shared/bib/references.bib` 的副本, 应当保持同步.

## BibTeX style 警告

不同期刊要求的 bibliography style 不同:

- IEEE: `\bibliographystyle{IEEEtran}`
- MDPI / APBC2026: `\bibliographystyle{plain}` 或 MDPI 提供的 `.bst`

如需格式转换, 优先改主稿的 `\bibliographystyle{...}` 而**不要**手动改 .bib 条目结构。
