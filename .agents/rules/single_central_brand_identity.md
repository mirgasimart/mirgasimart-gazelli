# Single Central Brand Identity Rule

## Architectural Principle: Single Source of Truth for Brand Assets

To maintain museum-grade prestige, consistency, and professional integrity across all collector, curatorial, and gallery touchpoints, the repository enforces a strict **Single Source of Truth** for the Mirgasim Art Studio brand mark.

---

### Core Rules

1. **No Multiple or Divergent Logos**:
   - The studio must **never** maintain multiple different versions, ad-hoc variations, or competing designs of its logo/emblem across different folders or documents.
   - Any loose, rogue, or outdated emblems (e.g. root images, temporary sketches) must be removed immediately.

2. **Single Central Asset Location (`assets/branding/`)**:
   - The authoritative production studio seal is:
     `assets/branding/brand_medallion.png` (1024 × 1024 transparent circular cutout).
   - The hi-res master rendering source is:
     `assets/branding/master_golden_m_medallion.jpg`.

3. **Deterministic Derivation via Central Script**:
   - All derivative brand assets (favicons, Apple touch icon, Android Chrome manifest icons, and SVG wrapper) must **only** be generated from the master source via:
     `scripts/generate_luxury_brand_assets.py`.
   - Never manually crop, modify, or generate favicons or app icons out-of-band.

4. **Universal Reuse Across Touchpoints**:
   - All interfaces ([index.html](file:///Users/jmj/repos/mirgasimart-gazelli/index.html)), manifest files ([site.webmanifest](file:///Users/jmj/repos/mirgasimart-gazelli/site.webmanifest)), social share cards, and documentation must reference the central assets under `assets/branding/` rather than creating local duplicates.
