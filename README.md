# InterMoBA Publications

**Interaction-aware Transformer with Mixture of Block Attention for Protein–Ligand Docking and Affinity Prediction**

This repository hosts the manuscript, figures, bibliography, and submission artefacts for the InterMoBA paper. The current primary submission target is **APBC2026**; the local working draft currently uses the APBC/MDPI-style template, while the final journal/template may be assigned by the APBC program committee. The previously drafted IEEE-journal version is preserved as a fully-traceable historical archive.

> InterMoBA is a deep-learning framework for **protein–ligand binding-pose prediction and binding-affinity scoring**. It couples a graph-based interaction encoder with a **Mixture of Block Attention (MoBA)** adapter, producing an interpretable, energy-based scoring function together with a sparse long-context attention mechanism.

---

## Submission status

| Target | Status | Deadline | Notes |
| --- | --- | --- | --- |
| **APBC2026** | preparing | 2026-06-15 | Primary target; journal/template assignment still to be confirmed |
| **IEEE journal** (historical) | archived | — | No longer maintained; kept under `_archive/ieee-journal-2026/` with full history |

> For status updates, edit `docs/submission-log.md`.

---

## Repository layout

```
.
├── README.md                                # this file — repository index
├── .gitignore                               # LaTeX build artifacts
│
├── shared/                                  # cross-target shared assets
│   ├── figures/                             # all PNG originals (fig{n}.png + supp 1-15, 22, 88, 99, 1010, …)
│   └── bib/references.bib                   # cross-target bibliography master
│
├── manuscripts/
│   ├── mdpi-apbc2026/                       # PRIMARY working draft for APBC2026
│   │   ├── main.tex                         # MDPI-style skeleton
│   │   ├── author-info.tex                  # author block (toggle for blind/non-blind)
│   │   ├── reference.bib                    # local copy of shared/bib/references.bib
│   │   ├── figures/                         # local copy of shared/figures/
│   │   ├── _template/                       # original MDPI/LaTeX templates (read-only)
│   │   └── supplementary/                   # independent supplementary PDF (required by MDPI)
│   │
│   └── _archive/
│       └── ieee-journal-2026/               # HISTORICAL target — full IEEE-journal draft
│           ├── InterMoBA.tex
│           ├── InterMoBA.pdf
│           ├── reference.bib
│           ├── IEEEtran.cls
│           ├── fig1.png … fig4.png
│           ├── *.aux *.bbl *.blg *.log *.out *.synctex.gz
│           └── supplementary/
│               ├── InterMoBA_supplimentary.tex
│               ├── InterMoBA_supplimentary.pdf
│               └── *.png
│
└── docs/
    ├── journal-notes/
    │   ├── README.md                        # index of journal/venue notes
    │   └── apbc2026.md                      # APBC2026 (MDPI) requirements + checklist
    └── submission-log.md                    # submission & review timeline per target
```

---

## Building the APBC2026 working manuscript

A TeX Live / MiKTeX distribution is required. The `.pdf` is **not** committed; reviewers / co-authors compile locally.

```bash
cd manuscripts/mdpi-apbc2026
pdflatex -interaction=nonstopmode main.tex
bibtex   main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

For the independent supplementary PDF:

```bash
cd manuscripts/mdpi-apbc2026/supplementary
pdflatex -interaction=nonstopmode supp.tex
```

`latexmk -pdf <file>` runs the same sequence automatically.

---

## Synchronising shared assets

`manuscripts/mdpi-apbc2026/{figures,supplementary/figures,reference.bib}` are **copies** of `shared/{figures,bib}/`. Whenever the shared source changes, mirror the change into the manuscript directory. See `manuscripts/mdpi-apbc2026/figures/README.md` and `shared/bib/README.md` for the exact mirroring recipe.

---

## Headline results (time-split PDBBind, pocket-residue setting)

- **Top-1 docking success (RMSD < 2 Å): 65.5 %** (vs. Interformer 63.9 %)
- **Inference time: 23.1 s / sample** on a single NVIDIA RTX 3060
- **Hydrogen-bond recovery: 63.74 %** (≥ +13 % over prior best)
- **Hydrophobic-interaction recovery: 54.69 %** (≥ +13 % over prior best)

---

## Notes

- Anonymous mirror (previously linked in the IEEE-version README) is retained for now; whether APBC2026 needs it is **TBD** — see `docs/journal-notes/apbc2026.md`.
- APBC 2026 may ask authors of accepted papers to revise the format according to the assigned journal; keep `_template/` read-only and update only the active manuscript files.
- The committed `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`, `*.synctex.gz` files under `_archive/ieee-journal-2026/` are historical LaTeX build artefacts preserved for reproducibility of the IEEE version. The MDPI manuscript directory does not commit build artefacts (see `.gitignore`).
