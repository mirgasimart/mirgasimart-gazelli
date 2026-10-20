---
trigger: always_on
description: Rule for organizing, saving, and versioning artwork deliverables and iterations.
---

# Artwork Organization & Versioning Rule

When creating, generating, or modifying artworks and deliverables for the Gazelli Art House project:

## 1. Latest Production Deliverables (`gazelli_artworks`)
- The **latest, active, and final production version** of the artwork series and its official exhibition proposal/catalog must **always** be stored in:
  `output/gazelli_artworks/` (mapped to `docs/output/gazelli_artworks/`).
- Filenames in `gazelli_artworks/` must follow consistent sequence numbers:
  - `01_<title_slug>_<species_or_motif>.jpg`
  - `02_<title_slug>_<species_or_motif>.jpg`
  - `03_<title_slug>_<species_or_motif>.jpg`
  - `04_<title_slug>_<species_or_motif>.jpg`
  - `05_<title_slug>_<species_or_motif>.jpg`
  - `README.md` (Curatorial statement, species taxonomy, Absheron materials, technical notes)

## 2. In-Between Iterations (`attempt N`)
- Whenever generating a new variation, alternative vision, or iterative revision:
  - **Never discard** or lose previous versions.
  - Previous versions and intermediate drafts must be preserved in their own dedicated folder named **`attempt N`** (e.g., `output/attempt 1/`, `output/attempt 2/`, etc.) inside the `output/` directory.
  - In-between iteration folders must increment sequentially: `attempt 1`, `attempt 2`, `attempt 3`, etc.
  - Each `attempt N` folder should contain the exact artworks from that round and an accompanying `README.md` summarizing the concepts and materials of that specific attempt.

## 3. Workflow for New Generations
1. Inspect existing `attempt N` directories under `output/` to determine the next sequential number.
2. If replacing the current contents of `gazelli_artworks`, ensure the outgoing version is safely preserved in `output/attempt N/`.
3. Save the new, updated creation directly into `output/gazelli_artworks/`.
4. Update `output/gazelli_artworks/README.md` to reflect the latest series vision.
