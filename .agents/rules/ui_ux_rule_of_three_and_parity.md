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
