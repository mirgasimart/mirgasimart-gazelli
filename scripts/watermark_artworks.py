#!/usr/bin/env python3
"""
Mirgasim Art Studio - Luxury Typographic Watermarking & Exhibition Plate Utility
================================================================================
Renders ultra-premium, museum-grade typographic wordmarks and archival exhibition
plates for Gazelli Art House commission proposals.
"""

import os
import sys
import argparse
from PIL import Image, ImageDraw, ImageFont

# Cross-platform font discovery with full Azerbaijani Unicode support (Segoe UI, Arial, Calibri)
CANDIDATE_FONTS = {
    "title_bold": [
        r"C:\Windows\Fonts\segoeuib.ttf",
        r"C:\Windows\Fonts\arialbd.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ],
    "body_regular": [
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arial.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ],
    "body_italic": [
        r"C:\Windows\Fonts\segoeuii.ttf",
        r"C:\Windows\Fonts\ariali.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
    ],
    "serif_bold": [
        r"C:\Windows\Fonts\timesbd.ttf",
        r"C:\Windows\Fonts\georgiab.ttf",
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    ],
    "serif_regular": [
        r"C:\Windows\Fonts\times.ttf",
        r"C:\Windows\Fonts\georgia.ttf",
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
    ],
}

def resolve_font(style, size):
    """Finds available system font matching requested style with graceful fallback."""
    for path in CANDIDATE_FONTS.get(style, []):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def render_tracked_text(draw, pos, text, font, fill, tracking=3):
    """Renders text with bespoke letter-spacing (tracking)."""
    x, y = pos
    total_w = 0
    for char in text:
        draw.text((x + total_w, y), char, font=font, fill=fill)
        bbox = draw.textbbox((0, 0), char, font=font)
        char_w = bbox[2] - bbox[0]
        total_w += char_w + tracking
    return total_w - tracking

def measure_tracked_text(text, font, tracking=3):
    """Calculates width and height of tracked text string."""
    dummy = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
    draw = ImageDraw.Draw(dummy)
    total_w = 0
    max_h = 0
    for char in text:
        bbox = draw.textbbox((0, 0), char, font=font)
        char_w = bbox[2] - bbox[0]
        char_h = bbox[3] - bbox[1]
        total_w += char_w + tracking
        if char_h > max_h:
            max_h = char_h
    return (max_w := max(0, total_w - tracking), max_h)

def create_luxury_watermark(scale=1.0):
    """
    Renders an ultra-sharp, high-fashion contemporary studio watermark badge.
    Inspired by top global contemporary studios (Studio Drift, Hauser & Wirth, Pace).
    Obsidian slate backdrop with clean architectural typography and subtle hairline border.
    """
    ss = 2 # 2x supersampling for razor-sharp anti-aliased output
    title_size = int(14 * scale * ss)
    sub_size = int(8.5 * scale * ss)
    tag_size = int(7 * scale * ss)

    font_title = resolve_font("title_bold", title_size)
    font_sub = resolve_font("body_regular", sub_size)
    font_tag = resolve_font("title_bold", tag_size)

    title_text = "MIRGASIM ART"
    sub_text = "ABSHERON TECTONICS  |  GAZELLI COMMISSION 2026"
    tag_text = "CONFIDENTIAL CURATORIAL PREVIEW"

    tw, th = measure_tracked_text(title_text, font_title, tracking=int(4 * scale * ss))
    sw, sh = measure_tracked_text(sub_text, font_sub, tracking=int(2 * scale * ss))
    gw, gh = measure_tracked_text(tag_text, font_tag, tracking=int(3 * scale * ss))

    content_w = max(tw, sw, gw)
    pad_x = int(22 * scale * ss)
    pad_y = int(16 * scale * ss)

    badge_w = content_w + pad_x * 2
    badge_h = th + sh + gh + pad_y * 2 + int(14 * scale * ss)

    badge = Image.new('RGBA', (badge_w, badge_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(badge)

    # Obsidian dark card background (92% opacity)
    bg_color = (12, 14, 18, 235)
    border_color = (255, 255, 255, 45)
    accent_gold = (212, 175, 55, 240) # Subtle refined metallic gold accent
    text_white = (255, 255, 255, 250)
    text_muted = (180, 185, 195, 220)

    # Rounded rectangle with delicate border
    radius = int(8 * scale * ss)
    draw.rounded_rectangle([(0, 0), (badge_w - 1, badge_h - 1)], radius=radius, fill=bg_color, outline=border_color, width=max(1, int(1 * ss)))

    # Accent diamond glyph & Title
    cur_y = pad_y
    # Draw small studio diamond
    d_size = int(4 * scale * ss)
    d_x = pad_x
    d_y = cur_y + (th // 2)
    draw.polygon([(d_x, d_y - d_size), (d_x + d_size, d_y), (d_x, d_y + d_size), (d_x - d_size, d_y)], fill=accent_gold)

    # Render main title
    render_tracked_text(draw, (pad_x + d_size * 2 + int(6 * scale * ss), cur_y), title_text, font_title, text_white, tracking=int(4 * scale * ss))

    # Divider hairline
    cur_y += th + int(8 * scale * ss)
    draw.line([(pad_x, cur_y), (badge_w - pad_x, cur_y)], fill=(255, 255, 255, 35), width=max(1, int(1 * ss)))

    # Subline
    cur_y += int(7 * scale * ss)
    render_tracked_text(draw, (pad_x, cur_y), sub_text, font_sub, text_muted, tracking=int(2 * scale * ss))

    # Confidential Tag
    cur_y += sh + int(6 * scale * ss)
    render_tracked_text(draw, (pad_x, cur_y), tag_text, font_tag, accent_gold, tracking=int(3 * scale * ss))

    # Downsample
    final_w = badge_w // ss
    final_h = badge_h // ss
    return badge.resize((final_w, final_h), Image.Resampling.LANCZOS)

def apply_watermark(image_path, output_path, position="bottom-right", margin=32):
    """Applies the luxury floating studio watermark to an artwork."""
    with Image.open(image_path) as base:
        base_rgb = base.convert('RGBA')
        img_w, img_h = base_rgb.size

        # Responsive scale relative to 1400px
        scale = max(0.85, min(1.35, img_w / 1400.0))
        badge = create_luxury_watermark(scale=scale)
        bw, bh = badge.size

        if position == "bottom-right":
            pos = (img_w - bw - margin, img_h - bh - margin)
        elif position == "bottom-left":
            pos = (margin, img_h - bh - margin)
        else:
            pos = ((img_w - bw) // 2, img_h - bh - margin)

        # Composite
        watermarked = Image.new('RGBA', (img_w, img_h))
        watermarked.paste(base_rgb, (0, 0))
        watermarked.paste(badge, pos, badge)

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        watermarked.convert('RGB').save(output_path, "JPEG", quality=95, optimize=True)
        print(f"  [Watermarked] {os.path.basename(image_path)} -> {output_path}")

# ==============================================================================
# MUSEUM ARCHIVAL EXHIBITION PLATES (PASSE-PARTOUT GALLERY EDITIONS)
# ==============================================================================

CATALOG_METADATA = {
    "01_luminescence_of_masazir_salt_dawn.jpg": {
        "plate": "PLATE 01 / 05",
        "title_en": "Luminescence of Masazir Dawn",
        "title_az": "Masazır Şəfəqi: Çəhrayı Duz Gölü",
        "genre": "Pure Mineral Abstraction / Lacustrine Strata",
        "dimensions": "185 × 120 cm (Horizontal Landscape Canvas)",
        "materials": "Genuine Masazir Pink Lake Salt, Porous Absheron Limestone Plaster & Sgraffito",
        "fauna": "Absheron Lacustrine Strata (Pure geological meditation)",
    },
    "02_the_weaver_of_sunken_shells_didacna.jpg": {
        "plate": "PLATE 02 / 05",
        "title_en": "The Shebeke Reliquary: Fossil Didacna in Absheron Stone",
        "title_az": "Şəbəkə Qalığı: Qədim Didakna və Daş Pəncərə",
        "genre": "Mixed-Media Painting on Canvas / Tactile Stone Relief",
        "dimensions": "40 × 60 cm (Vertical Architectural Canvas)",
        "materials": "Absheron Coquina Ground, Coastal Beach Sand, Low-Relief Didacna Cockles",
        "fauna": "Caspian Cockles (Didacna trigonoides & Didacna pyramidata)",
    },
    "03_keeper_of_the_cold_depths_caspian_shad.jpg": {
        "plate": "PLATE 03 / 05",
        "title_en": "The Binagadi Derrick: Hydrocarbon Strata & Pyrite Shad",
        "title_az": "Binaqədi Buruğu: Qara Qızıl və Pirit Şad",
        "genre": "Industrial-Geological Abstraction / Hydrocarbon Matter Painting",
        "dimensions": "120 × 200 cm (Vertical Panoramic Canvas)",
        "materials": "Pure Binagadi Bitumen, Brassy Pyrite Sulfide Ore, Limestone Ground",
        "fauna": "Caspian Marine Shad (Alosa braschnikowi)",
    },
    "04_breath_of_lokbatan_tadpole_goby.jpg": {
        "plate": "PLATE 04 / 05",
        "title_en": "Breath of Lokbatan: Volcanic Crater and Armored Goby",
        "title_az": "Lökbatan Nəfəsi: Palçıq Vulkanı və Zirehli Qobi",
        "genre": "Earth-Art Vortex / Geothermal Mineral Painting",
        "dimensions": "180 × 180 cm (Monumental 1:1 Square Canvas)",
        "materials": "Subterranean Lokbatan Mud-Volcano Clay, Celadon & Seafoam Glazes, Pyrite Veins",
        "fauna": "Armored Caspian Tadpole Goby (Benthophilus spp.)",
    },
    "05_the_lampreys_vigil_caspian_lamprey.jpg": {
        "plate": "PLATE 05 / 05",
        "title_en": "The Gobustan Solar Oracle: Ouroboros Lamprey",
        "title_az": "Qobustan Günəşi: İlanbalığı və Qədim Qaya Təsvirləri",
        "genre": "Mythological Contemporary Altar Piece / Archaeological Totem",
        "dimensions": "100 × 150 cm (Vertical Portrait Canvas)",
        "materials": "Absheron Coastal Beach Sand Mandala, Masazir Salt Halos, Gobustan Petroglyphic Sgraffito",
        "fauna": "Caspian Lamprey (Caspiomyzon wagneri)",
    },
}

def generate_exhibition_plate(image_path, output_path, meta):
    """
    Renders the artwork mounted on a museum-grade archival passe-partout mat
    with refined gallery typography, turning every artwork into a Sotheby's-grade
    presentation plate.
    """
    with Image.open(image_path) as base:
        base_rgb = base.convert('RGB')
        art_w, art_h = base_rgb.size

        # Mat proportions
        pad_top = int(art_h * 0.08)
        pad_sides = int(art_w * 0.08)
        pad_bottom = int(art_h * 0.18)

        plate_w = art_w + pad_sides * 2
        plate_h = art_h + pad_top + pad_bottom

        # Warm museum archival mat background (#FAF9F6)
        mat_color = (250, 249, 246)
        mat = Image.new('RGB', (plate_w, plate_h), mat_color)
        draw = ImageDraw.Draw(mat)

        # Subtle shadow behind canvas
        shadow_color = (220, 218, 212)
        for offset in range(1, 8):
            draw.rectangle(
                [(pad_sides + offset, pad_top + offset), (pad_sides + art_w + offset, pad_top + art_h + offset)],
                outline=shadow_color,
                width=1
            )

        # Mount artwork
        mat.paste(base_rgb, (pad_sides, pad_top))

        # Delicate canvas edge reveal
        draw.rectangle([(pad_sides - 1, pad_top - 1), (pad_sides + art_w, pad_top + art_h)], outline=(205, 202, 195), width=1)

        # Gallery Typography below canvas (Segoe UI / Times with full Azerbaijani glyphs)
        scale = max(1.0, plate_w / 1400.0)
        font_plate = resolve_font("title_bold", int(11 * scale))
        font_title = resolve_font("serif_bold", int(21 * scale))
        font_sub = resolve_font("body_italic", int(13 * scale))
        font_specs = resolve_font("body_regular", int(10.5 * scale))
        font_footer = resolve_font("body_regular", int(9 * scale))

        text_y = pad_top + art_h + int(24 * scale)

        # Top Badge / Plate number
        plate_label = f"M I R G A S I M   A R T   S T U D I O   •   {meta['plate']}"
        tw, _ = measure_tracked_text(plate_label, font_plate, tracking=int(3 * scale))
        render_tracked_text(draw, ((plate_w - tw) // 2, text_y), plate_label, font_plate, (120, 122, 128), tracking=int(3 * scale))

        # Title EN
        text_y += int(22 * scale)
        title_text = meta["title_en"]
        bbox = draw.textbbox((0, 0), title_text, font=font_title)
        draw.text(((plate_w - (bbox[2] - bbox[0])) // 2, text_y), title_text, font=font_title, fill=(18, 20, 24))

        # Title AZ (with full Azerbaijani character support)
        text_y += int(28 * scale)
        title_az = meta["title_az"]
        bbox = draw.textbbox((0, 0), title_az, font=font_sub)
        draw.text(((plate_w - (bbox[2] - bbox[0])) // 2, text_y), title_az, font=font_sub, fill=(90, 94, 102))

        # Thin divider
        text_y += int(20 * scale)
        div_w = int(240 * scale)
        draw.line([((plate_w - div_w) // 2, text_y), ((plate_w + div_w) // 2, text_y)], fill=(215, 212, 205), width=1)

        # Metadata Line 1: Dimensions & Genre
        text_y += int(14 * scale)
        specs_1 = f"{meta['dimensions']}   |   {meta['genre']}"
        bbox = draw.textbbox((0, 0), specs_1, font=font_specs)
        draw.text(((plate_w - (bbox[2] - bbox[0])) // 2, text_y), specs_1, font=font_specs, fill=(60, 64, 72))

        # Metadata Line 2: Materials & Taxonomy
        text_y += int(16 * scale)
        specs_2 = f"Materials: {meta['materials']}"
        bbox = draw.textbbox((0, 0), specs_2, font=font_footer)
        draw.text(((plate_w - (bbox[2] - bbox[0])) // 2, text_y), specs_2, font=font_footer, fill=(100, 104, 112))

        # Curatorial Footer
        text_y += int(16 * scale)
        footer_text = "Curatorial Commission Proposal for Gazelli Art House • Baku / London • © 2026 Mirgasim Art Studio"
        tw, _ = measure_tracked_text(footer_text, font_footer, tracking=int(1.5 * scale))
        render_tracked_text(draw, ((plate_w - tw) // 2, text_y), footer_text, font_footer, (150, 152, 158), tracking=int(1.5 * scale))

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        mat.save(output_path, "JPEG", quality=95, optimize=True)
        print(f"  [Exhibition Plate] {os.path.basename(image_path)} -> {output_path}")

def watermark_catalog(generate_plates=True):
    """Processes all 5 artworks in docs/output/latest."""
    base_dir = "docs/output/latest"
    wm_dir = "docs/output/latest/watermarked"
    plates_dir = "docs/output/latest/exhibition_plates"

    print("=== 1. Generating Luxury Floating Obsidian Watermarks for Master Works ===")
    for fname in CATALOG_METADATA.keys():
        src = os.path.join(base_dir, fname)
        if os.path.exists(src):
            dst = os.path.join(wm_dir, fname)
            apply_watermark(src, dst)
            apply_watermark(src, os.path.join("docs/output/watermarked", fname))

    if generate_plates:
        print("\n=== 2. Generating Museum Archival Exhibition Passe-Partout Plates ===")
        for fname, meta in CATALOG_METADATA.items():
            src = os.path.join(base_dir, fname)
            if os.path.exists(src):
                dst = os.path.join(plates_dir, f"plate_{fname}")
                generate_exhibition_plate(src, dst, meta)
                generate_exhibition_plate(src, os.path.join("docs/output/exhibition_plates", f"plate_{fname}"), meta)

def main():
    parser = argparse.ArgumentParser(description="Mirgasim Art Studio - Luxury Watermark & Exhibition Plate Builder")
    parser.add_argument("--plates", action="store_true", help="Generate museum archival exhibition plates")
    args = parser.parse_args()

    watermark_catalog(generate_plates=True)

if __name__ == "__main__":
    main()
