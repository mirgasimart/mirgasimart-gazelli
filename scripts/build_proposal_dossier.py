#!/usr/bin/env python3
"""
Mirgasim Art Studio - 6-Page Luxury Curatorial Commission Dossier Builder
========================================================================
Compiles an exact 6-page museum-grade fine art commission proposal:
  - Page 1: Executive Curatorial Statement, Collection Matrix & Studio Trademarks
  - Page 2: Plate 01 — Strata of Masazir (Salt Landscape + Studies)
  - Page 3: Plate 02 — The Shebeke Reliquary (Didacna & Limestone)
  - Page 4: Plate 03 — The Binagadi Derrick (Bitumen & Pyrite Shad)
  - Page 5: Plate 04 — Work in Progress Placeholder (Square 180x180 cm)
  - Page 6: Plate 05 — The Gobustan Solar Oracle (Lamprey Mandala)
"""

import os
import sys
import argparse
import subprocess
import re

def generate_dossier_html(use_watermarked=True):
    """Builds the 6-page HTML document with strict page-budget print CSS."""
    cwd = os.getcwd()

    def get_img_uri(rel_path):
        target_dir = "docs/output/latest/_watermarked" if use_watermarked else "docs/output/latest/_clean"
        full_path = os.path.join(cwd, target_dir, rel_path)
        return f"file:///{full_path.replace(os.sep, '/')}"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MIRGASIM ART™ | Curatorial Commission Proposal & Artist Dossier</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;1,400&display=swap');

  @page {{
    size: A4 portrait;
    margin-top: 18mm;
    margin-bottom: 18mm;
    margin-left: 18mm;
    margin-right: 18mm;
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
    line-height: 1.5;
    margin: 0;
    padding: 0;
    font-size: 9.5pt;
  }}

  /* Strict 1-Page per Section Utility */
  .page {{
    page-break-after: always;
    page-break-inside: avoid;
    height: 258mm;
    max-height: 258mm;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .page:last-child {{
    page-break-after: avoid;
  }}

  /* Page 1: Executive Cover & Curatorial Statement */
  .p1-header {{
    text-align: center;
    border-bottom: 1.5px solid #111;
    padding-bottom: 12px;
    margin-bottom: 14px;
  }}

  .brand-wordmark {{
    font-family: 'Cinzel', serif;
    font-size: 20pt;
    font-weight: 700;
    letter-spacing: 5px;
    color: #0f0f12;
    margin: 0;
    text-transform: uppercase;
  }}

  .brand-subtitle {{
    font-size: 8pt;
    letter-spacing: 3px;
    color: #666;
    margin-top: 4px;
    text-transform: uppercase;
  }}

  .p1-title-box {{
    text-align: center;
    margin-bottom: 14px;
  }}

  .dossier-label {{
    font-size: 7.5pt;
    font-weight: 600;
    letter-spacing: 2px;
    color: #8c734b;
    text-transform: uppercase;
    display: inline-block;
    padding: 2px 12px;
    border: 1px solid #d4c4a8;
    border-radius: 14px;
    background: #fdfbf7;
    margin-bottom: 6px;
  }}

  .dossier-title {{
    font-family: 'Playfair Display', serif;
    font-size: 19pt;
    font-weight: 600;
    color: #111;
    margin: 4px 0 2px 0;
    letter-spacing: -0.3px;
  }}

  .dossier-subtitle {{
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 11pt;
    color: #444;
    margin: 0;
  }}

  .curatorial-quote {{
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 9.5pt;
    line-height: 1.45;
    color: #333;
    background: #fbfbfb;
    border-left: 3px solid #8c734b;
    padding: 8px 14px;
    margin: 8px 0 12px 0;
  }}

  .p1-body-text {{
    font-size: 8.8pt;
    line-height: 1.5;
    color: #2a2a2a;
    margin-bottom: 10px;
    text-align: justify;
  }}

  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 8pt;
  }}

  table.data-table th {{
    background: #111;
    color: #fff;
    padding: 6px 8px;
    text-align: left;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    font-size: 7.5pt;
  }}

  table.data-table td {{
    padding: 5px 8px;
    border-bottom: 1px solid #eaeaea;
    vertical-align: top;
  }}

  table.data-table tr:nth-child(even) td {{
    background: #fcfcfc;
  }}

  .p1-footer {{
    border-top: 1px solid #eee;
    padding-top: 8px;
    font-size: 7.5pt;
    color: #777;
    text-align: center;
    line-height: 1.4;
  }}

  /* Standard Artwork Page Layout (Pages 2-6) */
  .plate-top {{
    margin-bottom: 8px;
  }}

  .plate-badge {{
    display: inline-block;
    background: #111;
    color: #fff;
    font-size: 7.5pt;
    font-weight: 600;
    letter-spacing: 1.5px;
    padding: 2px 8px;
    text-transform: uppercase;
    border-radius: 2px;
    margin-bottom: 4px;
  }}

  h3.plate-title {{
    font-family: 'Playfair Display', serif;
    font-size: 14pt;
    font-weight: 600;
    color: #111;
    margin: 0;
    line-height: 1.25;
  }}

  .plate-subtitle {{
    font-style: italic;
    font-size: 9pt;
    color: #666;
    margin: 2px 0 6px 0;
  }}

  .artwork-showcase {{
    text-align: center;
    margin: 6px 0 10px 0;
    background: #fafafa;
    border: 1px solid #eee;
    padding: 10px;
    border-radius: 4px;
  }}

  .artwork-showcase img {{
    max-width: 100%;
    max-height: 330px;
    height: auto;
    display: inline-block;
    border-radius: 2px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  }}

  .specs-grid {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8.2pt;
  }}

  .specs-grid td {{
    padding: 4px 8px;
    border-bottom: 1px solid #f0f0f0;
    vertical-align: top;
  }}

  .specs-grid td.spec-name {{
    width: 26%;
    font-weight: 600;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    background: #f9f9f9;
    border-right: 1px solid #f0f0f0;
  }}

  .specs-grid td.spec-val {{
    width: 74%;
    color: #111;
  }}

  .curatorial-narrative {{
    font-size: 8.5pt;
    line-height: 1.5;
    color: #2a2a2a;
    margin: 6px 0;
    text-align: justify;
  }}

  .studies-header {{
    font-size: 7.5pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #8c734b;
    margin-top: 8px;
    margin-bottom: 4px;
    border-top: 1px solid #eee;
    padding-top: 6px;
  }}

  .studies-table {{
    width: 100%;
    border-collapse: collapse;
  }}

  .studies-table td {{
    width: 50%;
    padding: 2px 6px;
    text-align: center;
    vertical-align: top;
  }}

  .studies-table img {{
    max-width: 95%;
    max-height: 95px;
    border-radius: 2px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }}

  .study-caption {{
    font-size: 7pt;
    color: #666;
    font-style: italic;
    display: block;
    margin-top: 2px;
  }}
</style>
</head>
<body>

<!-- PAGE 1: EXECUTIVE CURATORIAL DOSSIER & COLLECTION MATRIX -->
<div class="page">
  <div>
    <div class="p1-header">
      <div class="brand-wordmark">MIRGASIM ART™</div>
      <div class="brand-subtitle">FINE ART ATELIER • BAKU &amp; ABSHERON</div>
    </div>

    <div class="p1-title-box">
      <div class="dossier-label">Curatorial Commission Dossier</div>
      <h1 class="dossier-title">Absheron Tectonics: Primordial Matter &amp; Geological Strata</h1>
      <div class="dossier-subtitle">Prepared Exclusively for Gazelli Art House (London / Baku)</div>
    </div>

    <div class="curatorial-quote">
      "True regional modernism does not decorate with heritage; it builds directly from the primordial substances of the land: crystallized pink salt, volcanic craquelure, and ancient hydrocarbons."
    </div>

    <p class="p1-body-text">
      Responding to the international fine art standards of <strong>Gazelli Art House</strong>, this 5-work suite channels the modernist lineage of the <strong>Absheron School</strong> (Javad Mirjavadov, Sattar Bahlulzade, Rasim Babayev). Abandoning superficial decorative clich&eacute;s and tourist carpet motifs, this collection explores authentic Absheron signatures through radical mineral materiality and Caspian endemism.
    </p>

    <table class="data-table">
      <thead>
        <tr>
          <th>Plate</th>
          <th>Artwork Title</th>
          <th>Dimensions</th>
          <th>Primary Absheron Material</th>
          <th>Caspian Motif</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>01</strong></td>
          <td><em>Luminescence of Masazir Dawn</em></td>
          <td>185 &times; 120 cm</td>
          <td>Masazir Pink Lake Salt, Plaster</td>
          <td>Lacustrine Evaporites</td>
        </tr>
        <tr>
          <td><strong>02</strong></td>
          <td><em>The Shebeke Reliquary: Fossil Didacna</em></td>
          <td>40 &times; 60 cm</td>
          <td>Limestone Ground, Shell Accents</td>
          <td><em>Didacna</em> Cockle Shells</td>
        </tr>
        <tr>
          <td><strong>03</strong></td>
          <td><em>The Binagadi Derrick: Hydrocarbon Strata</em></td>
          <td>120 &times; 200 cm</td>
          <td>Binagadi Bitumen, Pyrite Ore</td>
          <td>Caspian Marine Shad</td>
        </tr>
        <tr>
          <td><strong>04</strong></td>
          <td><em>Breath of Lokbatan: Volcanic Crater &amp; Goby</em></td>
          <td>180 &times; 180 cm</td>
          <td>Volcanic Clay, Celadon Glazes, Pyrite</td>
          <td>Caspian Tadpole Goby</td>
        </tr>
        <tr>
          <td><strong>05</strong></td>
          <td><em>The Gobustan Solar Oracle: Lamprey</em></td>
          <td>100 &times; 150 cm</td>
          <td>Beach Sand, Lake Salt, Plaster</td>
          <td>Caspian Lamprey Mandala</td>
        </tr>
      </tbody>
    </table>

    <p class="p1-body-text" style="font-size: 8.2pt; margin-top: 6px;">
      <strong>Conservation Protocol:</strong> All raw substances are bound under archival museum standards: Masazir salt crystals are oven-dehydrated and sealed in UV-matte acrylic fixative; mud-volcano craquelure is co-polymer stabilized; and bitumen is mineral-dissolved into durable polymer glazes.
    </p>
  </div>

  <div class="p1-footer">
    <strong>CONFIDENTIAL &amp; PROPRIETARY &bull; MIRGASIM ART STUDIO &bull; BAKU &bull; OCTOBER 2026</strong><br/>
    MIRGASIM ART™ is a registered trademark. Master works protected under international copyright law. &copy; 2026 Mirgasim Art. All rights reserved.
  </div>
</div>

<!-- PAGE 2: PLATE 01 -->
<div class="page">
  <div>
    <div class="plate-top">
      <div class="plate-badge">Plate 01 &bull; Pure Mineral Abstraction</div>
      <h3 class="plate-title">Luminescence of Masazir Dawn</h3>
      <div class="plate-subtitle">Masazır Şəfəqi: Çəhrayı Duz Gölu</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('01_luminescence_of_masazir_salt_dawn.jpg')}" alt="Luminescence of Masazir Dawn" style="max-height: 380px;"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>185 &times; 120 cm</strong> (Horizontal Landscape Canvas, Specification from Brief)</td>
      </tr>
      <tr>
        <td class="spec-name">Materials</td>
        <td class="spec-val">Genuine Masazir Pink Lake Salt, Porous Absheron Limestone Plaster, Heavy Impasto, Incised Sgraffito</td>
      </tr>
      <tr>
        <td class="spec-name">Curatorial Concept</td>
        <td class="spec-val">
          An ethereal, meditative abstract landscape capturing the tranquil morning horizon over Lake Masazir. Where misted pastel-pink saline waters meet white crystalline shores, thick palette-knife impasto sculpts the organic coastline, embedded with coarse pink-and-white mineral crystals that glisten naturally in ambient light. Scored with delicate geometric sgraffito fissures in the mineral foreground, this composition embodies pure lacustrine serenity. (Pure geological abstraction; zero portraits, zero figures, zero seals, zero carpets).
        </td>
      </tr>
    </table>
  </div>
</div>

<!-- PAGE 3: PLATE 02 -->
<div class="page">
  <div>
    <div class="plate-top">
      <div class="plate-badge">Plate 02 &bull; Mixed-Media Painting on Canvas</div>
      <h3 class="plate-title">The Shebeke Reliquary: Fossil Didacna in Absheron Stone</h3>
      <div class="plate-subtitle">Şəbəkə Qalığı: Qədim Didakna və Daş Pəncərə</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('02_the_weaver_of_sunken_shells_didacna.jpg')}" alt="The Shebeke Reliquary" style="max-height: 380px;"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>40 &times; 60 cm</strong> (Vertical Format Canvas, Specification from Brief)</td>
      </tr>
      <tr>
        <td class="spec-name">Medium / Techniques</td>
        <td class="spec-val">Mixed-Media Oil &amp; Mineral Pigments on Stretched Canvas, Absheron Limestone Ground, Heavy Palette-Knife Impasto, Subtle Embedded <em>Didacna</em> Shell Elements, Turquoise &amp; Lapis Lazuli Glazes</td>
      </tr>
      <tr>
        <td class="spec-name">Endemic Organism</td>
        <td class="spec-val">Caspian Cockle (<em>Didacna trigonoides</em> / <em>Didacna pyramidata</em>)</td>
      </tr>
      <tr>
        <td class="spec-name">Curatorial Concept</td>
        <td class="spec-val">
          An intimate mixed-media painting on canvas honoring Absheron's stone-carving traditions (<em>daş yonma</em>). Thick palette-knife impasto and porous limestone-sand grounds evoke the tactile presence of Baku stone, framing an intricate painted Shebeke geometric window. Luminous glazes of Caspian turquoise and lapis lazuli glow within the tracery, accentuated by finely embedded small <em>Didacna</em> cockle shells providing delicate, low-relief tactile dimensionality to the canvas surface.
        </td>
      </tr>
    </table>
  </div>
</div>

<!-- PAGE 4: PLATE 03 -->
<div class="page">
  <div>
    <div class="plate-top">
      <div class="plate-badge">Plate 03 &bull; Industrial-Geological Abstraction</div>
      <h3 class="plate-title">The Binagadi Derrick: Hydrocarbon Strata &amp; Pyrite Shad</h3>
      <div class="plate-subtitle">Binaqədi Buruğu: Qara Qızıl və Pirit Şad</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('03_keeper_of_the_cold_depths_caspian_shad.jpg')}" alt="The Binagadi Derrick" style="max-height: 380px;"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>120 &times; 200 cm</strong> (Vertical Panoramic Canvas, Specification from Brief)</td>
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
        <td class="spec-name">Curatorial Concept</td>
        <td class="spec-val">
          Confronting Baku's historic role as the pioneer of world petroleum, minimal structural scaffolding beams inspired by historic wooden oil derricks slice across visceral slabs of pitch-black Binagadi bitumen. Leaping through the dark matrix is an armored Caspian marine shad adorned with metallic golden pyrite ore, set above the eternal subterranean gas flame (<em>Yanar Dağ / Ateshgah</em>).
        </td>
      </tr>
    </table>
  </div>
</div>

<!-- PAGE 5: PLATE 04 -->
<div class="page">
  <div>
    <div class="plate-top">
      <div class="plate-badge">Plate 04 &bull; Earth-Art Vortex &bull; Geothermal Mineral Painting</div>
      <h3 class="plate-title">Breath of Lokbatan: Volcanic Crater and Armored Goby</h3>
      <div class="plate-subtitle">Lökbatan Nəfəsi: Palçıq Vulkanı və Zirehli Qobi</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('04_breath_of_lokbatan_tadpole_goby.jpg')}" alt="Breath of Lokbatan" style="max-height: 380px;"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>180 &times; 180 cm</strong> (Monumental Square Format 1:1, Specification from Brief)</td>
      </tr>
      <tr>
        <td class="spec-name">Materials</td>
        <td class="spec-val">Subterranean Lokbatan Mud-Volcano Clay, Luminous Caspian Celadon &amp; Seafoam Glazes, Tactile Mineral Craquelure, Metallic Pyrite Vein Infiltration</td>
      </tr>
      <tr>
        <td class="spec-name">Curatorial Concept</td>
        <td class="spec-val">
          A monumental square statement uniting subterranean geothermal energy with aquatic serenity. An aerial vortex of an active mud-volcano crater rendered in thick palette-knife impasto and authentic mud clay craquelure fissures opens into luminous, flowing glazes of Caspian celadon and seafoam green. Gliding through the geothermal currents, an armored Caspian tadpole goby (<em>Benthophilus</em>) gleams with metallic pyrite veins, harmonizing primordial geological power with tranquil ecological resilience.
        </td>
      </tr>
    </table>
  </div>
</div>

<!-- PAGE 6: PLATE 05 -->
<div class="page">
  <div>
    <div class="plate-top">
      <div class="plate-badge">Plate 05 &bull; Mythological Archaeological Totem</div>
      <h3 class="plate-title">The Gobustan Solar Oracle: Ouroboros Lamprey</h3>
      <div class="plate-subtitle">Qobustan Günəşi: İlanbalığı və Qədim Qaya Təsvirləri</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('05_the_lampreys_vigil_caspian_lamprey.jpg')}" alt="The Gobustan Solar Oracle" style="max-height: 370px;"/>
    </div>

    <table class="specs-grid">
      <tr>
        <td class="spec-name">Dimensions</td>
        <td class="spec-val"><strong>100 &times; 150 cm</strong> (Vertical Portrait Canvas, Specification from Brief)</td>
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
        <td class="spec-name">Curatorial Concept</td>
        <td class="spec-val">
          A transcendental contemporary altar piece uniting prehistoric rock art with ecological mystery. The ancient Caspian lamprey coils into an Ouroboros circle of eternity around a concentric sand-and-salt solar mandala. Incised directly into the bone-plaster and limestone ground are Gobustan petroglyphs (reed boats, hunters, and sacred solar bulls), immortalizing Absheron's ancient rock art heritage within deep cosmological time.
        </td>
      </tr>
    </table>
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
    """Compiles HTML into an exact 6-page PDF via headless Chrome/Edge."""
    import shutil
    html_content = generate_dossier_html(use_watermarked=use_watermarked)

    tmp_html = "docs/output/latest/temp_dossier.html"
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    out_pdf = "docs/output/latest/MIRGASIM_ART_GAZELLI_COMMISSION_DOSSIER.pdf"
    readme_pdf = "docs/output/latest/README.pdf"

    header_html = (
        '<div style="font-size: 7pt; width: 100%; display: flex; justify-content: space-between; '
        'padding: 0 18mm; font-family: -apple-system, sans-serif; color: #888; text-transform: uppercase; letter-spacing: 1px;">'
        '<span>MIRGASIM ART™ | Curatorial Commission Dossier</span>'
        '<span>Gazelli Art House</span>'
        '</div>'
    )

    footer_html = (
        '<div style="font-size: 7pt; width: 100%; display: flex; justify-content: space-between; '
        'padding: 0 18mm; font-family: -apple-system, sans-serif; color: #888; letter-spacing: 0.5px;">'
        '<span>Confidential Fine Art Proposal © 2026 Mirgasim Art. All Rights Reserved.</span>'
        '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>'
        '</div>'
    )

    browser_bin = find_browser_executable()
    cmd = [
        browser_bin,
        "--headless",
        "--disable-gpu",
        "--display-header-footer",
        f"--header-template={header_html}",
        f"--footer-template={footer_html}",
        f"--print-to-pdf={out_pdf}",
        f"file:///{os.path.abspath(tmp_html).replace(os.sep, '/')}"
    ]

    print(f"Compiling 6-Page Luxury PDF Dossier via {browser_bin}...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
        print(res.stderr.decode(errors='ignore'))

def main():
    parser = argparse.ArgumentParser(description="Mirgasim Art - 6-Page Luxury PDF Dossier Builder")
    parser.add_argument("--clean", action="store_true", help="Use unwatermarked master artworks instead of watermarked")
    args = parser.parse_args()

    build_pdf(use_watermarked=(not args.clean))

if __name__ == "__main__":
    main()
