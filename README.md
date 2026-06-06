# InterMoBA

**Interaction-aware Transformer with Mixture of Block Attention for Protein–Ligand Docking and Affinity Prediction**

This repository hosts the **LaTeX sources, bibliography, figures, and compiled PDFs** for the manuscript and its supplementary materials, prepared to facilitate double-blind peer review.

> **InterMoBA** is a deep-learning framework for **protein–ligand binding-pose prediction and binding-affinity scoring**. It couples a graph-based interaction encoder with a **Mixture of Block Attention (MoBA)** adapter, producing an interpretable, energy-based scoring function together with a sparse long-context attention mechanism.

---

## Repository layout

```
.
├── InterMoBA_conference/                    # Main manuscript
│   ├── InterMoBA.tex                        # LaTeX source
│   ├── InterMoBA.pdf                        # Compiled manuscript
│   ├── reference.bib                        # Bibliography
│   ├── IEEEtran.cls                         # IEEEtran class file
│   ├── fig1.png … fig4.png                  # Main-paper figures
│   └── *.aux, *.bbl, *.blg, *.log,
│       *.out, *.synctex.gz                  # LaTeX build artifacts
│
└── InterMoBA supplimentary file/            # Supplementary materials
    ├── InterMoBA_supplimentary.tex          # Supplementary LaTeX source
    ├── InterMoBA_supplimentary.pdf          # Compiled supplementary
    └── 1.png … 15.png, 22.png, 88.png,
        99.png, 1010.png, 1212.png,
        1313.png, 1414.png, 1515.png         # Supplementary figures
```

---

## Building the PDFs

A TeX Live / MiKTeX distribution that ships the standard `IEEEtran` class is required. The pre-built PDFs are committed so reviewers do not have to recompile.

**Main manuscript** (IEEE style; the four-pass build resolves citations and cross-references):

```bash
cd "InterMoBA_conference"
pdflatex InterMoBA.tex
bibtex   InterMoBA
pdflatex InterMoBA.tex
pdflatex InterMoBA.tex
```

**Supplementary materials** (one pass is enough):

```bash
cd "InterMoBA supplimentary file"
pdflatex InterMoBA_supplimentary.tex
```

`latexmk -pdf <file>` runs the same sequence automatically.

---

## Manuscript at a glance

|                  |                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| **Title**        | Interaction-aware Transformer with Mixture of Block Attention for Protein–Ligand Docking and Affinity Prediction |
| **Main style**   | `\documentclass[lettersize,journal]{IEEEtran}`                                                  |
| **Suppl. style** | `\documentclass[conference]{IEEEtran}`                                                          |
| **Keywords**     | Protein–Ligand Docking · Affinity Prediction · Mixture of Block Attention (MoBA) · Interaction Recovery |
| **Code & data**  | Anonymous mirror for double-blind review: <https://anonymous.4open.science/r/InterMoBA-8F21>    |

### Headline results — time-split PDBBind, pocket-residue setting

- **Top-1 docking success (RMSD < 2 Å): 65.5 %** (vs. Interformer 63.9 %)
- **Inference time: 23.1 s / sample** on a single NVIDIA RTX 3060
- **Hydrogen-bond recovery: 63.74 %** (≈ +13 % over prior best)
- **Hydrophobic-interaction recovery: 54.69 %** (≈ +13 % over prior best)

---

## Notes

- The committed `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`, and `*.synctex.gz` files are LaTeX build artifacts, kept so the build is fully reproducible on a clean checkout. They can be cleaned with `latexmk -c` and excluded from future commits via a `.gitignore`.
- For double-blind submission, no author information is recorded in this repository; the corresponding author block in the manuscript is left empty by design.