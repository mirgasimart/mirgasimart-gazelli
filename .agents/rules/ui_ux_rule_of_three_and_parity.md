# UI/UX Design System: Rule of Three & Web-Mobile Parity

This rule governs all interactive interfaces, layouts, navigation, and customizer controls across the Mirgasim Art Studio web applications.

---

## 1. The Rule of Three (Cognitive Elegance & Hick's Law)
To eliminate decision fatigue and maintain a serene, museum-grade user experience, **never overwhelm the user with more than three primary options at any decision level**:

1. **Viewing Modes (Core Curatorial Perspectives)**:
   - Max 3–4 punchy, single-word perspectives:
     - `Stage` (1:1 Museum Scale Wall Hanging)
     - `Walk` (Continuous Panoramic Gallery Walk)
     - `In-Situ` (Architectural Living / Corporate Interior)
     - `Loupe` (4K Macro Raw Mineral Inspection)
2. **Architectural Wall Plasters (Canonical 3)**:
   - `Limestone` (Absheron Coquina Limestone — signature warm quarry plaster)
   - `Plaster` (Curatorial White Cube — neutral museum off-white)
   - `Anthracite` (Architectural Charcoal Concrete — dramatic dark contrast)
3. **Turnkey Framing Styles (Canonical 3)**:
   - `Walnut` (Matte Dark Walnut Floater Frame)
   - `Wrap` (Unframed Raw Mineral Gallery Wrap)
   - `Steel` (Blackened Industrial Metal Floater Frame)
4. **Curatorial Variations per Plate (Canonical 3)**:
   - When companion variations exist for a plate (e.g. Plate 03), restrict to 3 curated iterations:
     - `1: Master` (Canonical Proposal Piece)
     - `2: Cretti` (Alberto Burri Geological Cretti dialogue)
     - `3: Tectonic` (Anselm Kiefer Subterranean Ash dialogue)

---

## 2. Three-Dot (`···`) Overflow Menu Pattern
Secondary, environmental, and engineering tools must never clutter the primary interface:
- **Always preserve secondary controls** (lighting intensity, 2700K color warmth, interactive follow-beam, ambient synthesized soundscapes, direct PDF downloads, keyboard guides) under an unobtrusive, glassmorphic **Three-Dot (`···`) Overflow Menu**.
- Tapping `···` opens the unified **Curatorial Environment** popover without disrupting the primary artwork stage.

---

## 3. Strict Web & Mobile Parity Rule
Desktop web and mobile phone experiences must remain strictly on par:
- **No Feature Amputation**: Every capability accessible on desktop (geological anatomy wings, turnkey specifications, curatorial dossiers, scale figures, framing switchers, variation cycles) must be fully accessible on mobile phones.
- **Unified Mental Model**: Header actions on mobile and desktop share the exact same logical layout:
  - `[ Finishes ]` / `[ Scale ]`
  - `[ Minerals ]` (full slideout anatomy)
  - `[ Dossier ]` (full curatorial statement, specs & PDF download)
  - `[ ··· ]` (overflow environment popover)
- **Single-Word Button Labels**: Avoid multi-word button labels. Use concise, evocative single words (`Stage`, `Walk`, `Loupe`, `Scale`, `Minerals`, `Dossier`, `More`).

---

## 4. Single Fixed Brand Identity Rule
To maintain museum-grade dignity and avoid commercial visual noise:
- **One Fixed Location**: Brand logo medallion, studio seal, and series title ("Absheron Tectonics") are permanently anchored in **one fixed place**: the Top Curatorial Header (`.brand-section`).
- **No Redundant Repetition**: Never repeat "Mirgasim Art Studio" or the studio year on artwork placards, labels, or secondary cards. The artwork placard under each canvas must function as a pure museum tombstone displaying only the artwork title, curatorial variation selector, physical dimensions & medium, and the Curatorial Dossier link.
- **Vertical Height Priority**: On mobile viewports, eliminating redundant artist headers from placards saves 30–35px of vertical screen real estate, letting the painting expand and breathe without crowding bottom controls.

---

## 5. Trilingual System & 2-Character Language Toggle
- **Canonical 3 Languages**:
  1. `EN` (English — Canonical Default)
  2. `AZ` (Azerbaijani — Endemic Cultural Heritage)
  3. `RU` (Russian — Regional Academic Lineage)
- **2-Character Toggle (`#langToggleBtn`)**:
  - Displays as a sleek, 2-character glassmorphic badge (`EN` / `AZ` / `RU`) anchored directly beside the brand titles in the top header.
  - Tapping cycles `EN` -> `AZ` -> `RU` -> `EN` with an instant tactile micro-pulse.
  - Synchronizes brand titles, viewing mode tabs, action buttons, artwork titles, and curatorial narratives across the entire application, persisting preference in `localStorage`.

---

## 6. Universal Interactivity & Cross-Mode Feedback
- **Zero "Dead" Clicks**: Never present a button that fails to produce immediate visual feedback when tapped.
- **Cross-Mode Intelligence**:
  - Tapping `Scale` while in `Walk` (panoramic) or `Loupe` (macro) mode seamlessly switches to `Stage` (1:1 gallery) view and highlights the human scale figure.
  - Tapping `Minerals` on mobile/tablets or while in `Walk`/`Loupe` mode smoothly opens the Curatorial Dossier and scrolls directly to the Absheron Geological Mineral Anatomy section.
  - Tapping thumbnails in the bottom strip while in `Walk` mode smoothly scrolls the promenade to the selected artwork station.
