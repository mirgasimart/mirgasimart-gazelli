#!/usr/bin/env python3
"""
Mirgasim Art Studio - 7-Page Luxury Curatorial Commission Dossier Builder
========================================================================
Compiles an exact 7-page museum-grade fine art commission proposal:
  - Page 1: Executive Curatorial Statement, Collection Matrix & Caspian Strategy
  - Page 2: Plate 01 — Luminescence of Masazir Dawn (185 × 120 cm)
  - Page 3: Plate 02 — The Shebeke Reliquary (40 × 60 cm)
  - Page 4: Plate 03 — The Binagadi Derrick (120 × 200 cm)
  - Page 5: Plate 04 — Breath of Lokbatan (180 × 180 cm)
  - Page 6: Plate 05 — The Gobustan Solar Oracle (100 × 150 cm)
  - Page 7: Architectural In-Situ Integration & Turnkey Contractor Schedule
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
<title>MIRGASIM ART STUDIO | Curatorial Commission Proposal &amp; Artist Dossier</title>
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

  /* Page 1: Hero Cover Elements */
  .p1-masthead {{
    text-align: center;
    border-bottom: 1.5pt solid #111;
    padding-bottom: 10px;
    margin-bottom: 12px;
  }}

  .brand-wordmark {{
    font-family: 'Cinzel', serif;
    font-size: 21pt;
    font-weight: 700;
    letter-spacing: 6px;
    color: #0f0f12;
    margin: 0;
    text-transform: uppercase;
  }}

  .brand-subtitle {{
    font-size: 7.5pt;
    letter-spacing: 3.5px;
    color: #666;
    margin-top: 4px;
    text-transform: uppercase;
    font-weight: 500;
  }}

  .p1-title-box {{
    text-align: center;
    margin-bottom: 10px;
  }}

  .dossier-label {{
    font-size: 7pt;
    font-weight: 600;
    letter-spacing: 2.5px;
    color: #8c734b;
    text-transform: uppercase;
    display: inline-block;
    padding: 2px 14px;
    border: 1px solid #d4c4a8;
    border-radius: 12px;
    background: #fdfbf7;
    margin-bottom: 5px;
  }}

  .dossier-title {{
    font-family: 'Playfair Display', serif;
    font-size: 18pt;
    font-weight: 600;
    color: #111;
    margin: 3px 0 2px 0;
    letter-spacing: -0.2px;
  }}

  .dossier-subtitle {{
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 10.5pt;
    color: #555;
    margin: 0;
  }}

  .curatorial-quote {{
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 9pt;
    line-height: 1.45;
    color: #333;
    background: #fbf9f6;
    border-left: 2.5pt solid #8c734b;
    padding: 7px 12px;
    margin: 7px 0 10px 0;
  }}

  .p1-body-text {{
    font-size: 8.4pt;
    line-height: 1.48;
    color: #2a2a2a;
    margin-bottom: 8px;
    text-align: justify;
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

<!-- PAGE 1: EXECUTIVE CURATORIAL DOSSIER & COLLECTION MATRIX -->
<div class="page">
  <div>
    <div class="p1-masthead">
      <div class="brand-wordmark">MIRGASIM ART STUDIO</div>
      <div class="brand-subtitle">FINE ART ATELIER &bull; BAKU &bull; AZERBAIJAN</div>
    </div>

    <div class="p1-title-box">
      <div class="dossier-label">Curatorial Commission Dossier</div>
      <h1 class="dossier-title">Absheron Tectonics: Primordial Matter &amp; Geological Strata</h1>
      <div class="dossier-subtitle">Submitted in Formal Response to the Selection Brief | Gazelli Art House (London / Baku)</div>
    </div>

    <div class="curatorial-quote">
      "True regional modernism does not decorate with heritage; it builds directly from the primordial substances of the land: crystallized pink salt, volcanic craquelure, and ancient hydrocarbons."
    </div>

    <p class="p1-body-text">
      Responding to the international fine art standards of <strong>Gazelli Art House</strong>, this 5-work suite channels the pioneering spirit of the <strong>Absheron Modernist School</strong> (Javad Mirjavadov, Sattar Bahlulzade, Rasim Babayev, Tofig Javadov). Abandoning superficial decorative clich&eacute;s and carpet motifs, the artist explores authentic Absheron signatures through radical mineral materiality and Caspian scientific taxonomy.
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

    <p class="p1-body-text" style="font-size: 7.8pt; margin-top: 3px; line-height: 1.42;">
      <strong>Faunal Taxonomy &amp; Caspian Strategy:</strong> The suite deliberately privileges archaic benthic survivors (<em>Didacna</em>, <em>Alosa</em>, <em>Benthophilus</em>, <em>Caspiomyzon</em>) to represent primordial antiquity. The iconic <strong>Caspian Seal (<em>Pusa caspica</em>)</strong> is honored through the serene lacustrine sanctuaries of Masazir, with an authorial figurative study documented in studio archives as an available companion acquisition.
    </p>

    <p class="p1-body-text" style="font-size: 7.8pt; margin-top: 3px; line-height: 1.42;">
      <strong>Archival Conservation Protocol:</strong> All raw minerals are stabilized under museum standards: Masazir salt crystals undergo thermal dehydration and UV-matte acrylic encapsulation; mud-volcano craquelure is co-polymerized for zero shedding; and bitumen is mineral-dissolved into inert polymer glazes.
    </p>
  </div>

  <div class="running-footer">
    <div class="rf-context">Curatorial Commission Selection Dossier &bull; Baku &amp; London</div>
    <div class="rf-copyright">Submitted in Formal Response to Selection Brief | Gazelli Art House</div>
    <div class="rf-folio">FOLIO 01 / 07</div>
  </div>
</div>

<!-- PAGE 2: PLATE 01 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">MIRGASIM ART STUDIO</div>
      <div class="rh-title">Absheron Tectonics: Primordial Matter &amp; Geological Strata</div>
      <div class="rh-body">GAZELLI ART HOUSE</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 01 &bull; Pure Mineral Abstraction</div>
      <h3 class="plate-title">Luminescence of Masazir Dawn</h3>
      <div class="plate-subtitle">Masazır Şəfəqi: Çəhrayı Duz Gölü</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('01_luminescence_of_masazir_salt_dawn.jpg')}" alt="Luminescence of Masazir Dawn"/>
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
          An ethereal, meditative abstract landscape capturing the tranquil morning horizon over Lake Masazir. Where misted pastel-pink saline waters meet white crystalline shores, thick palette-knife impasto sculpts the organic coastline, embedded with coarse pink-and-white mineral crystals that glisten naturally in ambient light. Scored with delicate geometric sgraffito fissures in the mineral foreground, this composition embodies pure lacustrine serenity. (Pure geological abstraction; zero portraits, zero figures, zero carpets).
        </td>
      </tr>
      <tr>
        <td class="spec-name">Turnkey Mounting</td>
        <td class="spec-val">Mineral Impasto Continuous Wrap (or dark walnut floater) &bull; Dual Aluminum French Cleats (~14.5 kg) &bull; 2700K Warm Wash Lighting</td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 01: Luminescence of Masazir Dawn</div>
    <div class="rf-copyright">&copy; 2026 Mirgasim Art Studio. All rights reserved.</div>
    <div class="rf-folio">FOLIO 02 / 07</div>
  </div>
</div>

<!-- PAGE 3: PLATE 02 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">MIRGASIM ART STUDIO</div>
      <div class="rh-title">Absheron Tectonics: Primordial Matter &amp; Geological Strata</div>
      <div class="rh-body">GAZELLI ART HOUSE</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 02 &bull; Mixed-Media Painting on Canvas</div>
      <h3 class="plate-title">The Shebeke Reliquary: Fossil Didacna in Absheron Stone</h3>
      <div class="plate-subtitle">Şəbəkə Qalığı: Qədim Didakna və Daş Pəncərə</div>
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
      <tr>
        <td class="spec-name">Turnkey Mounting</td>
        <td class="spec-val">Limestone Gesso Wrap (or blackened steel floater) &bull; Single Aluminum Cleat w/ Locking Pin (~3.2 kg) &bull; 2700K-3000K Spot (15&deg; Beam)</td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 02: The Shebeke Reliquary</div>
    <div class="rf-copyright">&copy; 2026 Mirgasim Art Studio. All rights reserved.</div>
    <div class="rf-folio">FOLIO 03 / 07</div>
  </div>
</div>

<!-- PAGE 4: PLATE 03 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">MIRGASIM ART STUDIO</div>
      <div class="rh-title">Absheron Tectonics: Primordial Matter &amp; Geological Strata</div>
      <div class="rh-body">GAZELLI ART HOUSE</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 03 &bull; Industrial-Geological Abstraction</div>
      <h3 class="plate-title">The Binagadi Derrick: Hydrocarbon Strata &amp; Pyrite Shad</h3>
      <div class="plate-subtitle">Binaqədi Buruğu: Qara Qızıl və Pirit Şad</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('03_keeper_of_the_cold_depths_caspian_shad.jpg')}" alt="The Binagadi Derrick"/>
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
      <tr>
        <td class="spec-name">Turnkey Mounting</td>
        <td class="spec-val">Bitumen Polymer Continuous Wrap &bull; Dual Heavy-Duty French Cleats (~16.0 kg) &bull; 3000K Museum Track Lighting (Highlight Pyrite)</td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 03: The Binagadi Derrick</div>
    <div class="rf-copyright">&copy; 2026 Mirgasim Art Studio. All rights reserved.</div>
    <div class="rf-folio">FOLIO 04 / 07</div>
  </div>
</div>

<!-- PAGE 5: PLATE 04 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">MIRGASIM ART STUDIO</div>
      <div class="rh-title">Absheron Tectonics: Primordial Matter &amp; Geological Strata</div>
      <div class="rh-body">GAZELLI ART HOUSE</div>
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
      <tr>
        <td class="spec-name">Turnkey Mounting</td>
        <td class="spec-val">Volcanic Craquelure Gallery Wrap &bull; Triple Aluminum French Cleats (~19.5 kg) &bull; High-CRI 98 Wall Wash (Grazing Texture)</td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 04: Breath of Lokbatan</div>
    <div class="rf-copyright">&copy; 2026 Mirgasim Art Studio. All rights reserved.</div>
    <div class="rf-folio">FOLIO 05 / 07</div>
  </div>
</div>

<!-- PAGE 6: PLATE 05 -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">MIRGASIM ART STUDIO</div>
      <div class="rh-title">Absheron Tectonics: Primordial Matter &amp; Geological Strata</div>
      <div class="rh-body">GAZELLI ART HOUSE</div>
    </div>

    <div class="plate-top">
      <div class="plate-badge">Plate 05 &bull; Mythological Archaeological Totem</div>
      <h3 class="plate-title">The Gobustan Solar Oracle: Ouroboros Lamprey</h3>
      <div class="plate-subtitle">Qobustan Günəşi: İlanbalığı və Qədim Qaya Təsvirləri</div>
    </div>

    <div class="artwork-showcase">
      <img src="{get_img_uri('05_the_lampreys_vigil_caspian_lamprey.jpg')}" alt="The Gobustan Solar Oracle"/>
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
      <tr>
        <td class="spec-name">Turnkey Mounting</td>
        <td class="spec-val">Bone Plaster Gallery Edge (or oiled walnut floater) &bull; Dual Aluminum Z-Cleats (~11.0 kg) &bull; 2700K Framing Projector / Gimbal</td>
      </tr>
    </table>
  </div>

  <div class="running-footer">
    <div class="rf-context">Plate 05: The Gobustan Solar Oracle</div>
    <div class="rf-copyright">&copy; 2026 Mirgasim Art Studio. All rights reserved.</div>
    <div class="rf-folio">FOLIO 06 / 07</div>
  </div>
</div>

<!-- PAGE 7: ARCHITECTURAL IN-SITU SIMULATION & TURNKEY INSTALLATION MATRIX -->
<div class="page">
  <div>
    <div class="running-header">
      <div class="rh-atelier">MIRGASIM ART STUDIO</div>
      <div class="rh-title">Architectural Placement &amp; Turnkey Contractor Schedule</div>
      <div class="rh-body">GAZELLI ART HOUSE</div>
    </div>

    <div class="plate-top" style="margin-bottom: 4px;">
      <div class="plate-badge">Spatial Integration &bull; Contractor Specifications</div>
      <h3 class="plate-title" style="font-size: 13pt;">In-Situ Spatial Context &amp; Structural Mounting Matrix</h3>
      <div class="plate-subtitle">Photorealistic Architectural Previews on Honed Absheron Coquina Walls</div>
    </div>

    <!-- Dual In-Situ Image Row -->
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 6px;">
      <tr>
        <td style="width: 50%; padding-right: 5px; text-align: center; vertical-align: top;">
          <img src="{get_insitu_uri('insitu_plate_01_masazir_dawn.jpg')}" alt="Plate 01 In-Situ" style="width: 100%; border-radius: 3px; box-shadow: 0 3px 10px rgba(0,0,0,0.1);"/>
          <span style="font-size: 6.8pt; color: #666; font-style: italic; display: block; margin-top: 2px;">Plate 01: Honed Coquina Feature Wall &bull; Executive Salon Placement</span>
        </td>
        <td style="width: 50%; padding-left: 5px; text-align: center; vertical-align: top;">
          <img src="{get_insitu_uri('insitu_plate_04_breath_of_lokbatan.jpg')}" alt="Plate 04 In-Situ" style="width: 100%; border-radius: 3px; box-shadow: 0 3px 10px rgba(0,0,0,0.1);"/>
          <span style="font-size: 6.8pt; color: #666; font-style: italic; display: block; margin-top: 2px;">Plate 04: Grand Double-Height Atrium &bull; 2700K Ceiling Wash Lighting</span>
        </td>
      </tr>
    </table>

    <table class="data-table" style="font-size: 7.2pt; margin: 4px 0;">
      <thead>
        <tr>
          <th>Plate</th>
          <th>Dimensions</th>
          <th>Est. Weight</th>
          <th>Edge / Framing Profile</th>
          <th>Rigging Hardware</th>
          <th>Optimal Lighting</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>01</strong></td>
          <td>185 &times; 120 cm</td>
          <td>~14.5 kg</td>
          <td>Continuous Mineral Wrap / Floater</td>
          <td>Dual Aluminum Z-Cleats</td>
          <td>2700K Ceiling Wash (CRI 95+)</td>
        </tr>
        <tr>
          <td><strong>02</strong></td>
          <td>40 &times; 60 cm</td>
          <td>~3.2 kg</td>
          <td>Limestone Gesso / Black Steel</td>
          <td>Single Cleat w/ Locking Pin</td>
          <td>2700K-3000K Spot (15&deg;)</td>
        </tr>
        <tr>
          <td><strong>03</strong></td>
          <td>120 &times; 200 cm</td>
          <td>~16.0 kg</td>
          <td>Bitumen Polymer / Bronze Floater</td>
          <td>Dual Continuous Cleats (80kg)</td>
          <td>3000K Museum Track Light</td>
        </tr>
        <tr>
          <td><strong>04</strong></td>
          <td>180 &times; 180 cm</td>
          <td>~19.5 kg</td>
          <td>Volcanic Craquelure Wrap</td>
          <td>Triple Cleats (Seismic Rated)</td>
          <td>High-CRI 98 Wall Grazing</td>
        </tr>
        <tr>
          <td><strong>05</strong></td>
          <td>100 &times; 150 cm</td>
          <td>~11.0 kg</td>
          <td>Bone Plaster / Oiled Walnut</td>
          <td>Dual Aluminum Z-Cleats</td>
          <td>2700K Framing Projector</td>
        </tr>
      </tbody>
    </table>

    <div style="background: #fdfbf7; border: 1px solid #e8dfcf; border-radius: 3px; padding: 5px 8px; margin-top: 4px;">
      <div style="font-size: 7.2pt; font-weight: 600; color: #8c734b; text-transform: uppercase; letter-spacing: 0.5px;">Curatorial Material Palette Box ("The Tactile Verification")</div>
      <p style="font-size: 7.2pt; line-height: 1.4; color: #333; margin: 2px 0 0 0;">
        Mirgasim Art Studio offers to deliver a bespoke hand-crafted presentation box containing five 15 &times; 15 cm cured architectural plaques (Masazir lake salt in UV-acrylic, Lokbatan clay craquelure, cold-polymerized Binagadi bitumen, honed Absheron coquina, and pyrite ore aggregates) for direct tactile review by the selection committee.
      </p>
    </div>
  </div>

  <div class="running-footer">
    <div class="rf-context">Architectural Specifications &amp; Tactile Material Schedule</div>
    <div class="rf-copyright">Submitted in Formal Response to Selection Brief | Gazelli Art House</div>
    <div class="rf-folio">FOLIO 07 / 07</div>
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

    print(f"Compiling 7-Page Luxury PDF Dossier via {browser_bin} (zero browser header/footer artifacts)...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)

    if os.path.exists(out_pdf):
        shutil.copyfile(out_pdf, readme_pdf)
        size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
        print(f"SUCCESS: Generated 7-Page Luxury Dossier ({size_mb:.2f} MB):")
        print(f"  -> {out_pdf}")
        print(f"  -> {readme_pdf}")
    else:
        print("ERROR: Failed to generate PDF dossier.")
        print("Stdout:", res.stdout)
        print("Stderr:", res.stderr)

def main():
    parser = argparse.ArgumentParser(description="Mirgasim Art Studio - 7-Page Luxury PDF Dossier Builder")
    parser.add_argument("--clean", action="store_true", help="Use unwatermarked master artworks instead of watermarked")
    args = parser.parse_args()

    build_pdf(use_watermarked=(not args.clean))

if __name__ == "__main__":
    main()
