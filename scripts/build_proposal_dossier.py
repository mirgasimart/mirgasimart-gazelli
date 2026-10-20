#!/usr/bin/env python3
"""
Mirgasim Art Studio - Fine Art Commission Proposal & Curatorial Dossier Builder
=============================================================================
Generates a luxury, museum-grade exhibition proposal and curatorial response dossier
formatted according to international art advisory and high-end gallery standards.
Includes studio trademarks, running headers/footers, dynamic page numbering,
and high-resolution artwork plates (with modular wordmark support).
"""

import os
import sys
import argparse
import subprocess

def generate_dossier_html(use_watermarked=True):
    """Builds the comprehensive HTML dossier with print CSS."""
    img_dir = "docs/output/latest/watermarked" if use_watermarked else "docs/output/latest"
    if not os.path.exists(img_dir):
        img_dir = "docs/output/latest"

    # Resolve absolute paths for reliable Chrome rendering
    cwd = os.getcwd()

    def get_img_uri(rel_path):
        full_path = os.path.join(cwd, img_dir, rel_path)
        if not os.path.exists(full_path):
            full_path = os.path.join(cwd, "docs/output/latest", rel_path)
        return f"file://{full_path}"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MIRGASIM ART™ | Curatorial Commission Proposal & Artist Dossier</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');

  @page {{
    size: A4 portrait;
    margin-top: 24mm;
    margin-bottom: 24mm;
    margin-left: 20mm;
    margin-right: 20mm;
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
    line-height: 1.6;
    margin: 0;
    padding: 0;
    font-size: 10pt;
  }}

  /* Page Break Utilities */
  .page {{
    page-break-after: always;
    clear: both;
    position: relative;
    min-height: 245mm;
  }}

  .page-last {{
    page-break-after: avoid;
    clear: both;
  }}

  /* Cover Page */
  .cover {{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 255mm;
    padding: 40px 10px 20px 10px;
    border: 1px solid #e8e8e8;
    background: radial-gradient(circle at 50% 20%, #fafafa 0%, #ffffff 100%);
  }}

  .cover-header {{
    text-align: center;
    border-bottom: 2px solid #111;
    padding-bottom: 25px;
  }}

  .brand-wordmark {{
    font-family: 'Cinzel', serif;
    font-size: 24pt;
    font-weight: 700;
    letter-spacing: 6px;
    color: #0f0f12;
    margin: 0;
    text-transform: uppercase;
  }}

  .brand-subtitle {{
    font-size: 8.5pt;
    letter-spacing: 3.5px;
    color: #666;
    margin-top: 8px;
    text-transform: uppercase;
  }}

  .cover-main {{
    text-align: center;
    margin: auto 0;
  }}

  .dossier-label {{
    font-size: 9pt;
    font-weight: 600;
    letter-spacing: 3px;
    color: #8c734b; /* Subtle gallery bronze */
    text-transform: uppercase;
    margin-bottom: 15px;
    display: inline-block;
    padding: 4px 16px;
    border: 1px solid #d4c4a8;
    border-radius: 20px;
    background: #fdfbf7;
  }}

  .dossier-title {{
    font-family: 'Playfair Display', serif;
    font-size: 28pt;
    font-weight: 600;
    line-height: 1.25;
    color: #111;
    margin: 10px 0 16px 0;
    letter-spacing: -0.5px;
  }}

  .dossier-subtitle {{
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 15pt;
    color: #4a4a4a;
    margin: 0 auto 30px auto;
    max-width: 600px;
    line-height: 1.4;
  }}

  .cover-meta {{
    margin-top: 35px;
    display: flex;
    justify-content: center;
    gap: 40px;
    font-size: 9.5pt;
    color: #444;
  }}

  .cover-meta-item {{
    text-align: left;
    border-left: 2px solid #111;
    padding-left: 12px;
  }}

  .cover-meta-item strong {{
    display: block;
    font-size: 8pt;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #888;
    margin-bottom: 2px;
  }}

  .cover-footer {{
    border-top: 1px solid #eee;
    padding-top: 18px;
    font-size: 8pt;
    color: #777;
    text-align: center;
    line-height: 1.5;
  }}

  /* Standard Content Headings */
  h2.section-title {{
    font-family: 'Cinzel', serif;
    font-size: 16pt;
    font-weight: 600;
    letter-spacing: 2px;
    color: #111;
    text-transform: uppercase;
    border-bottom: 1.5px solid #111;
    padding-bottom: 8px;
    margin-top: 0;
    margin-bottom: 18px;
  }}

  h3.plate-title {{
    font-family: 'Playfair Display', serif;
    font-size: 15pt;
    font-weight: 600;
    color: #111;
    margin: 0 0 4px 0;
    line-height: 1.3;
  }}

  .plate-subtitle {{
    font-style: italic;
    font-size: 10pt;
    color: #666;
    margin-bottom: 12px;
  }}

  .plate-badge {{
    display: inline-block;
    background: #111;
    color: #fff;
    font-size: 8pt;
    font-weight: 600;
    letter-spacing: 2px;
    padding: 3px 10px;
    text-transform: uppercase;
    border-radius: 2px;
    margin-bottom: 8px;
  }}

  /* Artwork Presentation Plate */
  .artwork-showcase {{
    text-align: center;
    margin: 10px 0 16px 0;
    background: #fbfbfb;
    border: 1px solid #eee;
    padding: 14px;
    border-radius: 4px;
  }}

  .artwork-showcase img {{
    max-width: 100%;
    max-height: 380px;
    height: auto;
    display: inline-block;
    border-radius: 2px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  }}

  .specs-grid {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0 14px 0;
    font-size: 8.5pt;
  }}

  .specs-grid td {{
    padding: 6px 10px;
    border-bottom: 1px solid #f0f0f0;
    vertical-align: top;
  }}

  .specs-grid td.spec-name {{
    width: 28%;
    font-weight: 600;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    background: #fafafa;
    border-right: 1px solid #f0f0f0;
  }}

  .specs-grid td.spec-val {{
    width: 72%;
    color: #111;
  }}

  .curatorial-text {{
    font-size: 9.2pt;
    line-height: 1.55;
    color: #2b2b2b;
    margin: 10px 0;
    text-align: justify;
  }}

  /* Study Variations Grid */
  .studies-header {{
    font-size: 8pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #8c734b;
    margin-top: 14px;
    margin-bottom: 8px;
    border-top: 1px solid #eee;
    padding-top: 8px;
  }}

  .studies-table {{
    width: 100%;
    border-collapse: collapse;
  }}

  .studies-table td {{
    width: 50%;
    padding: 4px 8px;
    text-align: center;
    vertical-align: top;
  }}

  .studies-table img {{
    max-width: 95%;
    max-height: 120px;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  }}

  .studies-table-4col td {{
    width: 25%;
  }}

  .studies-table-4col img {{
    max-height: 90px;
  }}

  .study-caption {{
    font-size: 7.5pt;
    color: #666;
    font-style: italic;
    display: block;
    margin-top: 3px;
  }}

  /* Material Matrix Table */
  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 8.5pt;
  }}

  table.data-table th {{
    background: #111;
    color: #fff;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    font-size: 8pt;
  }}

  table.data-table td {{
    padding: 7px 10px;
    border-bottom: 1px solid #eaeaea;
    vertical-align: top;
  }}

  table.data-table tr:nth-child(even) td {{
    background: #fafafa;
  }}

  /* Signature & Seal Block */
  .sign-off-block {{
    margin-top: 40px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    padding-top: 20px;
    border-top: 1.5px solid #111;
  }}

  .sign-col {{
    font-size: 9pt;
  }}

  .studio-seal {{
    width: 90px;
    height: 90px;
    border: 2px solid #8c734b;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #8c734b;
    font-family: 'Cinzel', serif;
    font-size: 6.5pt;
    letter-spacing: 1px;
    padding: 4px;
    text-transform: uppercase;
  }}
</style>
</head>
<body>

<!-- PAGE 1: TITLE & COVER -->
<div class="page cover">
  <div class="cover-header">
    <div class="brand-wordmark">MIRGASIM ART™</div>
    <div class="brand-subtitle">FINE ART ATELIER • BAKU & ABSHERON</div>
  </div>

  <div class="cover-main">
    <div class="dossier-label">Official Gallery Submission</div>
    <h1 class="dossier-title">Curatorial Commission Proposal &amp; Artist Dossier</h1>
    <div class="dossier-subtitle">Absheron Tectonics: Primordial Matter &amp; Geological Strata</div>

    <div class="cover-meta">
      <div class="cover-meta-item">
        <strong>Commissioning Body</strong>
        Gazelli Art House (London / Baku)
      </div>
      <div class="cover-meta-item">
        <strong>Representing Artist</strong>
        Mirgasim (Mirgasim Art Studio)
      </div>
      <div class="cover-meta-item">
        <strong>Dossier Date</strong>
        October 2026
      </div>
      <div class="cover-meta-item">
        <strong>Document Status</strong>
        Final Master Proposal
      </div>
    </div>
  </div>

  <div class="cover-footer">
    <strong>CONFIDENTIAL &amp; PROPRIETARY • EXCLUSIVELY PREPARED FOR GAZELLI ART HOUSE</strong><br/>
    MIRGASIM ART™ is a registered trademark of Mirgasim Art Studio. All concepts, visual plates, material chemistries, and curatorial narratives are protected under international copyright law.<br/>
    © 2026 Mirgasim Art Studio. All rights reserved.
  </div>
</div>

<!-- PAGE 2: EXECUTIVE CURATORIAL STATEMENT & STRATEGY -->
<div class="page">
  <h2 class="section-title">Executive Curatorial Statement</h2>

  <p style="font-size: 10.5pt; line-height: 1.6; color: #222; font-family: 'Playfair Display', serif; font-style: italic; margin-bottom: 18px;">
    "True regional modernism does not decorate with heritage; it builds from the literal mineral dust, salt crust, and petroleum strata of the homeland."
  </p>

  <p class="curatorial-text">
    Responding directly to the curatorial brief for <strong>Gazelli Art House</strong>, this body of work represents a radical evolution of Azerbaijani contemporary fine art. Grounded in the modernist lineage of the <strong>Absheron School</strong>—reverberating with the monumental expressionism of Javad Mirjavadov, the luminous atmospheric landscapes of Sattar Bahlulzade, and the uncompromising graphic vigor of Rasim Babayev—these five works abandon decorative tourist clichés in favor of raw geological matter.
  </p>

  <p class="curatorial-text">
    <strong>Rigorous Curatorial Constraints Adhered To:</strong>
  </p>
  <ul style="font-size: 9.2pt; line-height: 1.6; padding-left: 20px; color: #333;">
    <li><strong>Authentic Raw Substances</strong>: Every canvas incorporates direct geological extractions: crystallized pink-and-white Masazir lake salt, dried Lokbatan mud-volcano craquelure clay, raw Binagadi bitumen, Turkan coquina limestone, and Caspian coastal shell-sand.</li>
    <li><strong>Caspian Endemic Biodiversity</strong>: Form and texture are informed exclusively by endemic wildlife: the prehistoric armored Caspian tadpole goby (<em>Benthophilus</em>), Caspian marine shad (<em>Alosa braschnikowi</em>), ancient Didacna bivalve fossils, and the primordial Caspian lamprey (<em>Caspiomyzon wagneri</em>).</li>
    <li><strong>Strictly Carpet-Free Fine Art Discipline</strong>: By curatorial mandate, all repetitive carpet patterns, rug motifs, and textile fringes have been completely eliminated, ensuring the mineral substances, petroglyphs, and architectural masonry speak with unfiltered fine art purity.</li>
    <li><strong>Strategic 3:2 Hybrid Straddle</strong>: Balancing serene, meditative mineral-infused earth-art (Works 1, 2, and 4) with dynamic industrial-petroleum and mythic archaeological drama (Works 3 and 5).</li>
  </ul>

  <h3 style="font-family: 'Cinzel', serif; font-size: 11pt; letter-spacing: 1px; margin-top: 22px; border-bottom: 1px solid #eee; padding-bottom: 4px;">Collection Master Overview</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th>No.</th>
        <th>Artwork Title</th>
        <th>Format / Size</th>
        <th>Primary Material</th>
        <th>Endemic Focus</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>01</strong></td>
        <td><em>Strata of Masazir: Crystalline Salt Landscape</em></td>
        <td>185 × 120 cm (Landscape)</td>
        <td>Masazir Pink Lake Salt, Limestone</td>
        <td>Lacustrine Evaporite Strata</td>
      </tr>
      <tr>
        <td><strong>02</strong></td>
        <td><em>The Shebeke Reliquary: Fossil Didacna</em></td>
        <td>150 × 200 cm (Vertical)</td>
        <td>Coquina, Caspian Sand, Shells</td>
        <td>Caspian Cockle (<em>Didacna</em> spp.)</td>
      </tr>
      <tr>
        <td><strong>03</strong></td>
        <td><em>The Binagadi Derrick: Hydrocarbon Strata</em></td>
        <td>120 × 200 cm (Vertical)</td>
        <td>Binagadi Bitumen, Pyrite Ore</td>
        <td>Caspian Marine Shad (<em>Alosa</em>)</td>
      </tr>
      <tr>
        <td><strong>04</strong></td>
        <td><em>[Work in Progress / Forthcoming]</em></td>
        <td>180 × 180 cm (Square 1:1)</td>
        <td>Mud-Volcano Clay, Verdigris Glazes</td>
        <td>Armored Caspian Goby (<em>Benthophilus</em>)</td>
      </tr>
      <tr>
        <td><strong>05</strong></td>
        <td><em>The Gobustan Solar Oracle: Lamprey</em></td>
        <td>100 × 150 cm (Portrait)</td>
        <td>Beach Sand, Lake Salt, Plaster</td>
        <td>Caspian Lamprey (<em>Caspiomyzon</em>)</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- PAGE 3: PLATE 01 -->
<div class="page">
  <div class="plate-badge">Plate 01 • Pure Mineral Abstraction</div>
  <h3 class="plate-title">Strata of Masazir: Crystalline Salt Landscape</h3>
  <div class="plate-subtitle">Masazır Layları: Çəhrayı Duz Abstraksiyası</div>

  <div class="artwork-showcase">
    <img src="{get_img_uri('01_lacustrine_strata_masazir_salt.jpg')}" alt="Strata of Masazir"/>
  </div>

  <table class="specs-grid">
    <tr>
      <td class="spec-name">Dimensions</td>
      <td class="spec-val"><strong>185 × 120 cm</strong> (Horizontal Fine Art Canvas, Specification from Brief)</td>
    </tr>
    <tr>
      <td class="spec-name">Medium / Techniques</td>
      <td class="spec-val">Genuine Masazir Pink Salt Encrustations, Porous Absheron Limestone Plaster, Heavy Palette-Knife Sculptural Impasto, Deep Incised Sgraffito Fissures</td>
    </tr>
    <tr>
      <td class="spec-name">Material Provenance</td>
      <td class="spec-val">Lake Masazir Saline Evaporites (Masazır gölü, Absheron) &amp; Badamdar Limestone Dust</td>
    </tr>
    <tr>
      <td class="spec-name">Curatorial Concept</td>
      <td class="spec-val">
        A tranquil, meditative horizontal abstract landscape capturing the primordial mineral strata of Lake Masazir. Soft undulating terraces of rose-quartz, blush pink, oyster cream, and warm alabaster white are built with thick palette-knife impasto. Embedded in high relief are sparkling crystalline salt clusters, scored with razor-thin sgraffito fissures. Completely non-figurative and free of portraits, figures, seals, or textiles.
      </td>
    </tr>
  </table>

  <div class="studies-header">Alternative Study Variations (Studio Iterations)</div>
  <table class="studies-table">
    <tr>
      <td>
        <img src="{get_img_uri('01_variant_b_crystalline_terraces.jpg')}" alt="Study B: Crystalline Terraces"/>
        <span class="study-caption"><strong>Study B</strong>: Stepped Crystalline Salt Terraces</span>
      </td>
      <td>
        <img src="{get_img_uri('01_variant_c_luminescence_dawn.jpg')}" alt="Study C: Luminescence of Masazir Dawn"/>
        <span class="study-caption"><strong>Study C</strong>: Luminescent Sunrise over Misty Saline Shoreline</span>
      </td>
    </tr>
  </table>
</div>

<!-- PAGE 4: PLATE 02 -->
<div class="page">
  <div class="plate-badge">Plate 02 • Architectural Masonry &amp; Fossil Strata</div>
  <h3 class="plate-title">The Shebeke Reliquary: Fossil Didacna in Absheron Stone</h3>
  <div class="plate-subtitle">Şəbəkə Qalığı: Qədim Didakna və Daş Pəncərə</div>

  <div class="artwork-showcase">
    <img src="{get_img_uri('02_the_weaver_of_sunken_shells_didacna.jpg')}" alt="The Shebeke Reliquary"/>
  </div>

  <table class="specs-grid">
    <tr>
      <td class="spec-name">Dimensions</td>
      <td class="spec-val"><strong>150 × 200 cm</strong> (Vertical Monumental Canvas, Specification from Brief)</td>
    </tr>
    <tr>
      <td class="spec-name">Medium / Techniques</td>
      <td class="spec-val">Porous Coquina Stone Relief, Absheron Beach Sand Plaster, Fossilized Caspian <em>Didacna</em> Shells in High Sculptural Relief, Turquoise &amp; Lapis Lazuli Glazes</td>
    </tr>
    <tr>
      <td class="spec-name">Endemic Organism</td>
      <td class="spec-val">Caspian Cockle (<em>Didacna trigonoides</em> / <em>Didacna pyramidata</em>)</td>
    </tr>
    <tr>
      <td class="spec-name">Curatorial Concept</td>
      <td class="spec-val">
        Honoring Absheron's thousand-year stone-carving heritage (<em>daş yonma</em>), a heavy coquina wall reveals an intricate geometric stone Shebeke window lattice. Behind the carved aperture glows deep Caspian turquoise and lapis lazuli light. Protruding from the masonry are radiant <em>Didacna</em> cockles, while an elongated, sculpted hand touches the stone frame, symbolizing human craftsmanship rooted in deep geological time.
      </td>
    </tr>
  </table>
</div>

<!-- PAGE 5: PLATE 03 -->
<div class="page">
  <div class="plate-badge">Plate 03 • Industrial-Geological Abstraction</div>
  <h3 class="plate-title">The Binagadi Derrick: Hydrocarbon Strata &amp; Pyrite Shad</h3>
  <div class="plate-subtitle">Binaqədi Buruğu: Qara Qızıl və Pirit Şad</div>

  <div class="artwork-showcase">
    <img src="{get_img_uri('03_keeper_of_the_cold_depths_caspian_shad.jpg')}" alt="The Binagadi Derrick"/>
  </div>

  <table class="specs-grid">
    <tr>
      <td class="spec-name">Dimensions</td>
      <td class="spec-val"><strong>120 × 200 cm</strong> (Vertical Panoramic Canvas, Specification from Brief)</td>
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
        Confronting Baku's iconic heritage as the cradle of the world petroleum industry, minimal structural scaffolding beams inspired by historic wooden oil derricks slice across visceral slabs of pitch-black Binagadi bitumen. Leaping through the dark matrix is an armored Caspian marine shad adorned with metallic golden pyrite ore, set above the eternal subterranean gas flame (<em>Yanar Dağ / Ateshgah</em>).
      </td>
    </tr>
  </table>
</div>

<!-- PAGE 6: PLATE 04 -->
<div class="page">
  <div class="plate-badge">Plate 04 • Work in Progress / Reserved</div>
  <h3 class="plate-title">[Work 04: Atelier Development in Progress]</h3>
  <div class="plate-subtitle">Lökbatan Nəfəsi: Yeni Seriya Üzərində İş Gedir</div>

  <div class="artwork-showcase" style="padding: 25px 14px;">
    <img src="{get_img_uri('04_placeholder_work_in_progress.png')}" alt="Plate 04 Placeholder" style="max-height: 360px;"/>
  </div>

  <table class="specs-grid">
    <tr>
      <td class="spec-name">Status</td>
      <td class="spec-val"><strong>Reserved for Forthcoming Atelier Review</strong> (Work in Progress)</td>
    </tr>
    <tr>
      <td class="spec-name">Target Dimensions</td>
      <td class="spec-val"><strong>180 × 180 cm</strong> (Square Format 1:1, Specification from Brief)</td>
    </tr>
    <tr>
      <td class="spec-name">Proposed Medium</td>
      <td class="spec-val">Subterranean Lokbatan Mud-Volcano Clay, Luminous Caspian Greenish-Blue Mineral Glazes (Celadon, Seafoam, Verdigris), Natural Craquelure Fissures &amp; Pyrite Vein Infiltration</td>
    </tr>
    <tr>
      <td class="spec-name">Proposed Endemic Fauna</td>
      <td class="spec-val">Armored Caspian Tadpole Goby (<em>Benthophilus</em> spp.)</td>
    </tr>
    <tr>
      <td class="spec-name">Curatorial Note</td>
      <td class="spec-val">
        Work #4 is currently being redesigned from scratch in the atelier to replace earlier dark earthy tones with radiant, pleasing Caspian greenish-blue palettes and a strict 1:1 square composition. The final artwork plate and alternative studies will be integrated upon completion of the new generation series.
      </td>
    </tr>
  </table>
</div>

<!-- PAGE 7: PLATE 05 -->
<div class="page">
  <div class="plate-badge">Plate 05 • Mythological Archaeological Totem</div>
  <h3 class="plate-title">The Gobustan Solar Oracle: Ouroboros Lamprey</h3>
  <div class="plate-subtitle">Qobustan Günəşi: İlanbalığı və Qədim Qaya Təsvirləri</div>

  <div class="artwork-showcase">
    <img src="{get_img_uri('05_the_lampreys_vigil_caspian_lamprey.jpg')}" alt="The Gobustan Solar Oracle"/>
  </div>

  <table class="specs-grid">
    <tr>
      <td class="spec-name">Dimensions</td>
      <td class="spec-val"><strong>100 × 150 cm</strong> (Vertical Portrait Canvas, Specification from Brief)</td>
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

<!-- PAGE 8: STUDIO ARCHIVAL CHEMISTRY & PRODUCTION SPECIFICATIONS -->
<div class="page page-last">
  <h2 class="section-title">Studio Archival Chemistry &amp; Production Standards</h2>

  <p class="curatorial-text">
    To ensure every commissioned artwork meets the archival and conservation standards of international museums and tier-one private collections, <strong>Mirgasim Art Studio</strong> executes all works under strict chemical binding and material stability protocols:
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th>Substance / Material</th>
        <th>Geological Sourcing Origin</th>
        <th>Studio Conservation &amp; Archival Protocol</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Masazir Lake Salt</strong></td>
        <td>Lake Masazir, Absheron</td>
        <td>Dehydrated at 60°C to eliminate deliquescence risk; embedded in high-grade acrylic gloss gel and sealed with 2 coats of UV mineral fixative varnish.</td>
      </tr>
      <tr>
        <td><strong>Lokbatan Volcanic Clay</strong></td>
        <td>Lokbatan Mud Volcano, Absheron</td>
        <td>Centrifuged and blended with archival acrylic co-polymer emulsion to regulate craquelure tensile strength and prevent structural flaking.</td>
      </tr>
      <tr>
        <td><strong>Binagadi Bitumen</strong></td>
        <td>Binagadi Outcrops, Absheron</td>
        <td>Pure asphaltite dissolved in odorless archival spirits and bound in heavy-body gloss polymer, ensuring rich black depth without softening.</td>
      </tr>
      <tr>
        <td><strong>Turkan Coquina &amp; Shells</strong></td>
        <td>Turkan &amp; Mardakan Coastal Quarries</td>
        <td>Sterilized in dilute hydrogen peroxide, dry-sawn into relief plates, and anchored into structural limestone gesso with fiberglass reinforcing mesh.</td>
      </tr>
      <tr>
        <td><strong>Absheron Beach Sand</strong></td>
        <td>Pirshaghi &amp; Bilgah Coastal Waterline</td>
        <td>Triple-rinsed in freshwater to eliminate sodium chloride traces; oven-baked and sifted for controlled tactile grain gradation.</td>
      </tr>
    </tbody>
  </table>

  <h3 style="font-family: 'Cinzel', serif; font-size: 11pt; letter-spacing: 1px; margin-top: 22px; border-bottom: 1px solid #eee; padding-bottom: 4px;">Milestone Production Timelines</h3>
  <div style="display: flex; gap: 20px; margin-top: 10px;">
    <div style="flex: 1; border: 1px solid #eee; padding: 12px; background: #fafafa; border-radius: 4px;">
      <strong style="text-transform: uppercase; font-size: 8pt; letter-spacing: 1px; color: #8c734b; display: block; margin-bottom: 4px;">Standard Production Track</strong>
      <div style="font-size: 12pt; font-weight: 700; color: #111;">4 Months (16 Weeks)</div>
      <p style="font-size: 8pt; color: #666; margin: 4px 0 0 0;">Allows full natural craquelure curing, multi-layer oil/bitumen oxidation, and complete studio condition reporting.</p>
    </div>
    <div style="flex: 1; border: 1px solid #eee; padding: 12px; background: #fafafa; border-radius: 4px;">
      <strong style="text-transform: uppercase; font-size: 8pt; letter-spacing: 1px; color: #8c734b; display: block; margin-bottom: 4px;">Accelerated Commission Track</strong>
      <div style="font-size: 12pt; font-weight: 700; color: #111;">2 Months (8 Weeks)</div>
      <p style="font-size: 8pt; color: #666; margin: 4px 0 0 0;">Utilizes parallel studio atelier workflows and controlled thermal drying protocols for expedited institutional handover.</p>
    </div>
  </div>

  <div class="sign-off-block">
    <div class="sign-col">
      <strong>MIRGASIM ART STUDIO</strong><br/>
      Chief Master Artist &amp; Atelier Director<br/>
      Baku, Absheron Peninsula, Azerbaijan<br/>
      <span style="font-size: 8pt; color: #888;">studio@mirgasimart.com • www.mirgasimart.com</span>
    </div>

    <div class="studio-seal">
      <span>★ ★ ★</span>
      <strong>MIRGASIM</strong>
      <span>ART STUDIO</span>
      <span>BAKU • 2026</span>
    </div>
  </div>
</div>

</body>
</html>'''
    return html

def build_pdf(use_watermarked=True):
    """Compiles HTML into a high-resolution PDF via headless Chrome."""
    html_content = generate_dossier_html(use_watermarked=use_watermarked)

    tmp_html = "docs/output/latest/temp_dossier.html"
    with open(tmp_html, "w") as f:
        f.write(html_content)

    out_pdf = "docs/output/latest/MIRGASIM_ART_GAZELLI_COMMISSION_DOSSIER.pdf"
    readme_pdf = "docs/output/latest/README.pdf"

    header_html = (
        '<div style="font-size: 7.5pt; width: 100%; display: flex; justify-content: space-between; '
        'padding: 0 20mm; font-family: -apple-system, sans-serif; color: #888; text-transform: uppercase; letter-spacing: 1px;">'
        '<span>MIRGASIM ART™ | Curatorial Commission Dossier</span>'
        '<span>Gazelli Art House</span>'
        '</div>'
    )

    footer_html = (
        '<div style="font-size: 7.5pt; width: 100%; display: flex; justify-content: space-between; '
        'padding: 0 20mm; font-family: -apple-system, sans-serif; color: #888; letter-spacing: 0.5px;">'
        '<span>Confidential Fine Art Proposal © 2026 Mirgasim Art. All Rights Reserved.</span>'
        '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>'
        '</div>'
    )

    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        "--display-header-footer",
        f"--header-template={header_html}",
        f"--footer-template={footer_html}",
        f"--print-to-pdf={out_pdf}",
        f"file://{os.path.abspath(tmp_html)}"
    ]

    print(f"Compiling Luxury PDF Dossier via Google Chrome Headless...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)

    if os.path.exists(out_pdf):
        # Also copy to README.pdf so that the standard catalog PDF is identical to the luxury dossier
        subprocess.run(["cp", out_pdf, readme_pdf])
        size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
        print(f"SUCCESS: Generated Luxury Dossier ({size_mb:.2f} MB):")
        print(f"  -> {out_pdf}")
        print(f"  -> {readme_pdf}")
    else:
        print("ERROR: Failed to generate PDF dossier.")
        print(res.stderr.decode())

def main():
    parser = argparse.ArgumentParser(description="Mirgasim Art - Luxury PDF Dossier Builder")
    parser.add_argument("--clean", action="store_true", help="Use unwatermarked master artworks instead of watermarked")
    args = parser.parse_args()

    build_pdf(use_watermarked=(not args.clean))

if __name__ == "__main__":
    main()
