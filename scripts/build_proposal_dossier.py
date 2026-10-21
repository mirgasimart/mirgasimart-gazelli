#!/usr/bin/env python3
"""
Mirgasim Art Studio - 6-Page Luxury Curatorial Commission Dossier Builder
========================================================================
Compiles an exact 6-page museum-grade fine art commission proposal:
  - Page 1: Executive Curatorial Statement, Collection Matrix & Caspian Strategy
  - Page 2: Plate 01 — Luminescence of Masazir (130 × 100 cm)
  - Page 3: Plate 02 — The Shebeke Reliquary (40 × 60 cm)
  - Page 4: Plate 03 — Black Gold (80 × 100 cm)
  - Page 5: Plate 04 — Breath of Lokbatan (145 × 145 cm)
  - Page 6: Plate 05 — Solar Oracle (120 × 100 cm)
"""

import os
import sys
import argparse
import subprocess
import shutil

def generate_dossier_html(use_watermarked=True):
    """Builds the 7-page HTML document with bespoke museum-grade print layout."""
    cwd = os.getcwd()

    def get_img_uri(rel_path):
        target_dir = "docs/output/latest/_watermarked" if use_watermarked else "docs/output/latest/_clean"
        full_path = os.path.join(cwd, target_dir, rel_path)
        return f"file:///{full_path.replace(os.sep, '/')}"

    def get_insitu_uri(rel_path):
        full_path = os.path.join(cwd, "docs/output/latest/_insitu", rel_path)
        return f"file:///{full_path.replace(os.sep, '/')}"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Jeyran Mir-Gasim Jafarova | Project Proposal</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,500&display=swap');

  @page {{
    size: 210mm 297mm;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #1a1a1a;
    background: #ffffff;
    line-height: 1.45;
    margin: 0;
    padding: 0;
    font-size: 9pt;
  }}

  /* Exact A4 Page Container with Controlled Bleed Margins */
  .page {{
    page-break-after: always;
    page-break-inside: avoid;
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    padding: 12mm 16mm 10mm 16mm;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #ffffff;
  }}

  .page:last-child {{
    page-break-after: avoid;
  }}

  /* Curatorial Running Header (Pages 2-7) */
  .running-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 0.6pt solid #d4c9b8;
    padding-bottom: 5px;
    margin-bottom: 8px;
    font-size: 6.8pt;
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }}

  .running-header .rh-atelier {{
    font-family: 'Cinzel', serif;
    font-weight: 700;
    color: #1a1a1a;
    letter-spacing: 2px;
  }}

  .running-header .rh-title {{
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 7.8pt;
    color: #666;
    letter-spacing: 0.5px;
    text-transform: none;
  }}

  .running-header .rh-body {{
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    color: #8c734b;
    letter-spacing: 1.5px;
  }}

  /* Curatorial Running Footer (All Pages) */
  .running-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 0.6pt solid #d4c9b8;
    padding-top: 5px;
    margin-top: 6px;
    font-size: 6.8pt;
    color: #888;
    letter-spacing: 0.5px;
  }}

  .running-footer .rf-context {{
    color: #666;
  }}

  .running-footer .rf-copyright {{
    color: #999;
    font-size: 6.2pt;
  }}

  .running-footer .rf-folio {{
    font-family: 'Cinzel', serif;
    font-weight: 700;
    color: #1a1a1a;
    letter-spacing: 1.5px;
  }}

  /* Page 1: Cover Page */
  .cover-page {{
    text-align: center;
    height: 297mm;
    min-height: 297mm;
  }}

  .cover-center {{
    margin: auto 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }}

  .cover-artist {{
    font-family: 'Cinzel', serif;
    font-size: 26pt;
    font-weight: 700;
    letter-spacing: 5px;
    color: #111114;
    text-transform: uppercase;
    margin: 0;
  }}

  .cover-line {{
    width: 64px;
    height: 1.5px;
    background: #8c734b;
    margin: 22px auto;
  }}

  .cover-project {{
    font-family: 'Playfair Display', serif;
    font-size: 20pt;
    font-weight: 500;
    font-style: italic;
    color: #4a4a4a;
    letter-spacing: 0.5px;
    margin: 0;
  }}

  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 7.8pt;
  }}

  table.data-table th {{
    background: #111;
    color: #fff;
    padding: 5px 8px;
    text-align: left;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    font-size: 7.2pt;
  }}

  table.data-table td {{
    padding: 5px 8px;
    border-bottom: 1px solid #eaeaea;
    vertical-align: top;
  }}

  table.data-table tr:nth-child(even) td {{
    background: #fcfcfc;
  }}

  /* Standard Artwork Page Elements (Pages 2-6) */
  .plate-top {{
    margin-bottom: 6px;
  }}

  .plate-badge {{
    display: inline-block;
    background: #111;
    color: #fff;
    font-size: 7pt;
    font-weight: 600;
    letter-spacing: 1.5px;
    padding: 2px 7px;
    text-transform: uppercase;
    border-radius: 2px;
    margin-bottom: 3px;
  }}

  h3.plate-title {{
    font-family: 'Playfair Display', serif;
    font-size: 13.5pt;
    font-weight: 600;
    color: #111;
    margin: 0;
    line-height: 1.25;
  }}

  .plate-subtitle {{
    font-style: italic;
    font-size: 8.8pt;
    color: #666;
    margin: 1px 0 4px 0;
  }}

  .artwork-showcase {{
    text-align: center;
    margin: 4px 0 8px 0;
    background: #faf8f5;
    border: 1px solid #ece6dc;
    padding: 8px;
    border-radius: 3px;
  }}

  .artwork-showcase img {{
    max-width: 100%;
    max-height: 340px;
    height: auto;
    display: inline-block;
    border-radius: 2px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
  }}

  .specs-grid {{
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 8pt;
  }}

  .specs-grid td {{
    padding: 3.5px 7px;
    border-bottom: 1px solid #f0ece5;
    vertical-align: top;
  }}

  .specs-grid td.spec-name {{
    width: 25%;
    font-weight: 600;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    background: #fcfbfa;
    border-right: 1px solid #f0ece5;
    font-size: 7.2pt;
  }}

  .specs-grid td.spec-val {{
    width: 75%;
    color: #111;
  }}

  .curatorial-narrative {{
    font-size: 8.2pt;
    line-height: 1.46;
    color: #2a2a2a;
    margin: 4px 0;
    text-align: justify;
  }}
</style>
</head>
<body>

<!-- PAGE 1: COVER / TITLE PAGE -->
<div class="page cover-page">
  <div class="cover-center">
    <h1 class="cover-artist">Jeyran Mir-Gasim Jafarova</h1>
    <div class="cover-line"></div>
    <div class="cover-project">Project Proposal</div>
  </div>

  <div class="running-footer">
    <div class="rf-context"></div>
    <div class="rf-copyright">&copy; 2026 Jeyran Mir-Gasim Jafarova. All rights reserved.</div>
    <div class="rf-folio">01 / 06</div>
  </div>
</div>

<!-- PAGE 2: PLATE 01 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">JEYRAN MIR-GASIM JAFAROVA</div>
      <div class="rh-title">Project Proposal</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 01 &bull; Pure Mineral Abstraction</div>
      <h3 class="plate-title">Luminescence of Masazir</h3>
      <div class="plate-subtitle">Masazır Parıltısı</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('01_luminescence_of_masazir_salt_dawn.jpg')}" alt="Luminescence of Masazir"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>130 &times; 100 cm</strong> (Horizontal Landscape Canvas, Specification from Brief)</td>
      </tr>
      <tr>
        <td class="spec-name">Materials</td>
        <td class="spec-val">Genuine Masazir Pink Lake Salt, Textured Paste, Heavy Impasto, Oil Paint on Canvas</td>
      </tr>
      <tr>
        <td class="spec-name">Concept</td>
        <td class="spec-val">
          An ethereal, meditative abstract landscape capturing the tranquil morning horizon over Lake Masazir. Where misted pastel-pink saline waters meet white crystalline shores, thick palette-knife impasto sculpts the organic coastline, embedded with coarse pink-and-white mineral crystals that glisten naturally in ambient light. Scored with delicate geometric sgraffito fissures in the mineral foreground, this composition embodies pure lacustrine serenity. (Pure geological abstraction; zero portraits, zero figures, zero carpets).
        </td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 01: Luminescence of Masazir</div>
    <div class="rf-copyright">&copy; 2026 Jeyran Mir-Gasim Jafarova. All rights reserved.</div>
    <div class="rf-folio">02 / 06</div>
  </div>
</div>

<!-- PAGE 3: PLATE 02 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">JEYRAN MIR-GASIM JAFAROVA</div>
      <div class="rh-title">Project Proposal</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 02 &bull; Tactile Shell Assemblage &amp; Mineral Painting</div>
      <h3 class="plate-title">The Shebeke Reliquary</h3>
      <div class="plate-subtitle">Şəbəkə Qalığı</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('02_the_weaver_of_sunken_shells_didacna.jpg')}" alt="The Shebeke Reliquary"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>40 &times; 60 cm</strong> (Vertical Format Canvas, Specification from Brief)</td>
      </tr>
      <tr>
        <td class="spec-name">Medium / Techniques</td>
        <td class="spec-val">Absheron Coquina Ground, Concentric Caspian <em>Didacna</em> Shell Assemblage, Mother-of-Pearl Inlay, Crystalline Masazir Pink Lake Salt, Fine Beach Sand, Turquoise &amp; Celadon Mineral Pigments, Volcanic Craquelure Clay, Incised Geometric Sgraffito</td>
      </tr>
      <tr>
        <td class="spec-name">Endemic Organism</td>
        <td class="spec-val">Caspian Cockles (<em>Didacna trigonoides</em> &amp; <em>Didacna pyramidata</em>)</td>
      </tr>
      <tr>
        <td class="spec-name">Concept</td>
        <td class="spec-val">
          An architectural mandala and tactile stone reliquary fusing Absheron's stone-carving traditions (<em>daş yonma</em>) with sacred geometry. Arranged in precise concentric celestial rings, hundreds of natural Caspian <em>Didacna</em> cockle shells and iridescent mother-of-pearl segments radiate outward from an incandescent core of crystalline pink Masazir lake salt and vibrant turquoise mineral pigment. Encircled by golden Absheron coastal sand and framed within a square relief of cracked mud-volcano craquelure and incised geometric Shebeke stone tracery, the work fuses deep Caspian biological antiquity with timeless architectural harmony.
        </td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 02: The Shebeke Reliquary</div>
    <div class="rf-copyright">&copy; 2026 Jeyran Mir-Gasim Jafarova. All rights reserved.</div>
    <div class="rf-folio">03 / 06</div>
  </div>
</div>

<!-- PAGE 4: PLATE 03 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">JEYRAN MIR-GASIM JAFAROVA</div>
      <div class="rh-title">Project Proposal</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 03 &bull; Industrial-Geological Abstraction</div>
      <h3 class="plate-title">Black Gold</h3>
      <div class="plate-subtitle">Qara Qızıl</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('03_keeper_of_the_cold_depths_caspian_shad.jpg')}" alt="Black Gold"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>80 &times; 100 cm</strong> (Vertical Format Canvas, Specification from Brief)</td>
      </tr>
      <tr>
        <td class="spec-name">Medium / Techniques</td>
        <td class="spec-val">Raw Unrefined Binagadi Bitumen, Pyrite Sulfide Aggregates, Chalky Limestone Contrast Sgraffito, Oil &amp; Industrial Asphaltite Knife Impasto</td>
      </tr>
      <tr>
        <td class="spec-name">Endemic Wildlife</td>
        <td class="spec-val">Caspian Marine Shad / Brazhnikov’s Shad (<em>Alosa braschnikowi</em>)</td>
      </tr>
      <tr>
        <td class="spec-name">Concept</td>
        <td class="spec-val">
          Confronting Baku's historic role as the pioneer of world petroleum, minimal structural scaffolding beams inspired by historic wooden oil derricks slice across visceral slabs of pitch-black Binagadi bitumen. Leaping through the dark matrix is an armored Caspian marine shad adorned with metallic golden pyrite ore, set above the eternal subterranean gas flame (<em>Yanar Dağ / Ateshgah</em>).
        </td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 03: Black Gold</div>
    <div class="rf-copyright">&copy; 2026 Jeyran Mir-Gasim Jafarova. All rights reserved.</div>
    <div class="rf-folio">04 / 06</div>
  </div>
</div>

<!-- PAGE 5: PLATE 04 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">JEYRAN MIR-GASIM JAFAROVA</div>
      <div class="rh-title">Project Proposal</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 04 &bull; Earth-Art Vortex &bull; Geothermal Mineral Painting</div>
      <h3 class="plate-title">Breath of Lokbatan: Volcanic Crater and Armored Goby</h3>
      <div class="plate-subtitle">Lökbatan Nəfəsi: Palçıq Vulkanı və Zirehli Qobi</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('04_breath_of_lokbatan_tadpole_goby.jpg')}" alt="Breath of Lokbatan"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>145 &times; 145 cm</strong> (Monumental Square Format 1:1, Specification from Brief)</td>
      </tr>
      <tr>
        <td class="spec-name">Materials</td>
        <td class="spec-val">Subterranean Lokbatan Mud-Volcano Clay, Luminous Caspian Celadon &amp; Seafoam Glazes, Tactile Mineral Craquelure, Metallic Pyrite Vein Infiltration</td>
      </tr>
      <tr>
        <td class="spec-name">Concept</td>
        <td class="spec-val">
          A monumental square statement uniting subterranean geothermal energy with aquatic serenity. An aerial vortex of an active mud-volcano crater rendered in thick palette-knife impasto and authentic mud clay craquelure fissures opens into luminous, flowing glazes of Caspian celadon and seafoam green. Gliding through the geothermal currents, an armored Caspian tadpole goby (<em>Benthophilus</em>) gleams with metallic pyrite veins, harmonizing primordial geological power with tranquil ecological resilience.
        </td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 04: Breath of Lokbatan</div>
    <div class="rf-copyright">&copy; 2026 Jeyran Mir-Gasim Jafarova. All rights reserved.</div>
    <div class="rf-folio">05 / 06</div>
  </div>
</div>

<!-- PAGE 6: PLATE 05 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">JEYRAN MIR-GASIM JAFAROVA</div>
      <div class="rh-title">Project Proposal</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 05 &bull; Mythological Archaeological Totem</div>
      <h3 class="plate-title">Solar Oracle</h3>
      <div class="plate-subtitle">Günəş Orakulu</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('05_the_lampreys_vigil_caspian_lamprey.jpg')}" alt="Solar Oracle"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>120 &times; 100 cm</strong> (Horizontal Format Canvas, Specification from Brief)</td>
      </tr>
      <tr>
        <td class="spec-name">Medium / Techniques</td>
        <td class="spec-val">Absheron Coastal Beach Sand Mandala, Masazir Salt Encrustations, Incised Gobustan Petroglyphic Sgraffito, Oil &amp; Bone Plaster on Linen</td>
      </tr>
      <tr>
        <td class="spec-name">Endemic Wildlife</td>
        <td class="spec-val">Caspian Lamprey (<em>Caspiomyzon wagneri</em>)</td>
      </tr>
      <tr>
        <td class="spec-name">Concept</td>
        <td class="spec-val">
          A transcendental contemporary altar piece uniting prehistoric rock art with ecological mystery. The ancient Caspian lamprey coils into an Ouroboros circle of eternity around a concentric sand-and-salt solar mandala. Incised directly into the bone-plaster and limestone ground are Gobustan petroglyphs (reed boats, hunters, and sacred solar bulls), immortalizing Absheron's ancient rock art heritage within deep cosmological time.
        </td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 05: Solar Oracle</div>
    <div class="rf-copyright">&copy; 2026 Jeyran Mir-Gasim Jafarova. All rights reserved.</div>
    <div class="rf-folio">06 / 06</div>
  </div>
</div>

</body>
</html>'''
    return html

def find_browser_executable():
    """Finds Chrome or Edge browser executable across platforms."""
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "google-chrome",
        "chromium",
        "chrome",
        "msedge",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "chrome"

def build_pdf(use_watermarked=True):
    """Compiles HTML into an exact 7-page PDF with zero browser header/footer artifacts."""
    html_content = generate_dossier_html(use_watermarked=use_watermarked)

    tmp_html = "docs/output/latest/temp_dossier.html"
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    out_pdf = os.path.abspath("docs/output/latest/MIRGASIM_ART_GAZELLI_COMMISSION_DOSSIER.pdf")
    readme_pdf = os.path.abspath("docs/output/latest/README.pdf")

    # Strictly remove pre-existing files to ensure fresh generation
    if os.path.exists(out_pdf):
        os.remove(out_pdf)
    if os.path.exists(readme_pdf):
        os.remove(readme_pdf)

    browser_bin = find_browser_executable()
    cmd = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf}",
        os.path.abspath(tmp_html)
    ]

    print(f"Compiling 6-Page Luxury PDF Dossier via {browser_bin} (zero browser header/footer artifacts)...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)

    if os.path.exists(out_pdf):
        shutil.copyfile(out_pdf, readme_pdf)
        size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
        print(f"SUCCESS: Generated 6-Page Luxury Dossier ({size_mb:.2f} MB):")
        print(f"  -> {out_pdf}")
        print(f"  -> {readme_pdf}")
    else:
        print("ERROR: Failed to generate PDF dossier.")
        print("Stdout:", res.stdout)
        print("Stderr:", res.stderr)

def main():
    parser = argparse.ArgumentParser(description="Mirgasim Art Studio - 6-Page Luxury PDF Dossier Builder")
    parser.add_argument("--clean", action="store_true", help="Use unwatermarked master artworks instead of watermarked")
    args = parser.parse_args()

    build_pdf(use_watermarked=(not args.clean))

if __name__ == "__main__":
    main()
