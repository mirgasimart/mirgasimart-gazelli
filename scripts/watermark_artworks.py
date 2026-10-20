#!/usr/bin/env python3
"""
Mirgasim Art Studio - Modular Artwork Copyright Watermarking Utility
===================================================================
Applies an elegant, museum-grade typographic wordmark onto generated artworks
to protect copyright and provenance for external client and gallery distribution.

Usage:
    # Watermark all active artworks in docs/output/latest:
    python3 scripts/watermark_artworks.py

    # Watermark a specific file:
    python3 scripts/watermark_artworks.py --input path/to/img.jpg --output path/to/out.jpg

    # Generate standalone transparent PNG wordmark assets:
    python3 scripts/watermark_artworks.py --export-wordmark-assets
"""

import os
import sys
import argparse
import glob
from PIL import Image, ImageDraw, ImageFont

FONT_PATH_HELVETICA = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_PATH_ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_PATH_GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"

def get_font(size, bold=False):
    """Load system font with graceful fallback."""
    for path in [FONT_PATH_HELVETICA, FONT_PATH_ARIAL, FONT_PATH_GEORGIA]:
        if os.path.exists(path):
            try:
                index = 1 if bold and "HelveticaNeue" in path else 0
                return ImageFont.truetype(path, size, index=index)
            except Exception:
                pass
    return ImageFont.load_default()

def create_wordmark_badge(scale=1.0, is_dark_bg=True):
    """
    Renders the modular MIRGASIM ART wordmark badge as a transparent RGBA image.
    Features:
      - Main brand: 'MIRGASIM ART™'
      - Sub-brand: '© 2026 MIRGASIM ART • ALL RIGHTS RESERVED'
    """
    title_size = max(18, int(22 * scale))
    sub_size = max(9, int(10 * scale))
    pad_x = int(24 * scale)
    pad_y = int(14 * scale)

    font_title = get_font(title_size, bold=True)
    font_sub = get_font(sub_size, bold=False)

    title_text = "M I R G A S I M   A R T ™"
    sub_text = "© 2026 MIRGASIM ART • ALL RIGHTS RESERVED"

    # Measure text bounds
    dummy_img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
    dummy_draw = ImageDraw.Draw(dummy_img)
    t_bbox = dummy_draw.textbbox((0, 0), title_text, font=font_title)
    s_bbox = dummy_draw.textbbox((0, 0), sub_text, font=font_sub)

    t_w = t_bbox[2] - t_bbox[0]
    t_h = t_bbox[3] - t_bbox[1]
    s_w = s_bbox[2] - s_bbox[0]
    s_h = s_bbox[3] - s_bbox[1]

    badge_w = max(t_w, s_w) + pad_x * 2
    badge_h = t_h + s_h + pad_y * 2 + int(6 * scale)

    badge = Image.new('RGBA', (badge_w, badge_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(badge)

    # Adaptive pill background (frosted glass look)
    bg_color = (12, 12, 14, 185) if not is_dark_bg else (245, 245, 248, 195)
    border_color = (255, 255, 255, 60) if not is_dark_bg else (0, 0, 0, 50)
    text_primary = (255, 255, 255, 240) if not is_dark_bg else (15, 15, 18, 240)
    text_sub = (200, 200, 205, 210) if not is_dark_bg else (60, 60, 65, 210)

    # Rounded rectangle background
    radius = int(8 * scale)
    draw.rounded_rectangle([(0, 0), (badge_w - 1, badge_h - 1)], radius=radius, fill=bg_color, outline=border_color, width=1)

    # Draw centered title
    t_x = (badge_w - t_w) // 2
    t_y = pad_y
    draw.text((t_x, t_y), title_text, font=font_title, fill=text_primary)

    # Draw centered sub-text
    s_x = (badge_w - s_w) // 2
    s_y = t_y + t_h + int(6 * scale)
    draw.text((s_x, s_y), sub_text, font=font_sub, fill=text_sub)

    return badge

def is_area_dark(image, box):
    """Calculates relative luminance of target bounding box."""
    crop = image.crop(box).convert('L')
    stat = crop.resize((1, 1)).getpixel((0, 0))
    return stat < 128

def apply_watermark(image_path, output_path, position="bottom-right", margin=30):
    """Applies the modular wordmark to an image file and saves result."""
    with Image.open(image_path) as base:
        base_rgb = base.convert('RGBA')
        img_w, img_h = base_rgb.size

        # Responsive scale relative to 1200px
        scale = max(0.65, min(1.6, img_w / 1200.0))

        # Check background brightness at target position
        sample_w = int(350 * scale)
        sample_h = int(70 * scale)

        if position == "bottom-right":
            box = (img_w - sample_w - margin, img_h - sample_h - margin, img_w - margin, img_h - margin)
        elif position == "bottom-left":
            box = (margin, img_h - sample_h - margin, margin + sample_w, img_h - margin)
        elif position == "bottom-center":
            box = ((img_w - sample_w) // 2, img_h - sample_h - margin, (img_w + sample_w) // 2, img_h - margin)
        else: # center
            box = ((img_w - sample_w) // 2, (img_h - sample_h) // 2, (img_w + sample_w) // 2, (img_h + sample_h) // 2)

        dark_bg = is_area_dark(base_rgb, box)
        badge = create_wordmark_badge(scale=scale, is_dark_bg=dark_bg)
        badge_w, badge_h = badge.size

        if position == "bottom-right":
            pos = (img_w - badge_w - margin, img_h - badge_h - margin)
        elif position == "bottom-left":
            pos = (margin, img_h - badge_h - margin)
        elif position == "bottom-center":
            pos = ((img_w - badge_w) // 2, img_h - badge_h - margin)
        else: # center
            pos = ((img_w - badge_w) // 2, (img_h - badge_h) // 2)

        # Composite watermark badge onto base image
        watermarked = Image.new('RGBA', (img_w, img_h))
        watermarked.paste(base_rgb, (0, 0))
        watermarked.paste(badge, pos, badge)

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        watermarked.convert('RGB').save(output_path, "JPEG", quality=95, optimize=True)
        print(f"  [Watermarked] {os.path.basename(image_path)} -> {output_path}")

def export_standalone_assets(dest_dir="assets/branding"):
    """Exports standalone high-res wordmark PNGs."""
    os.makedirs(dest_dir, exist_ok=True)
    light_badge = create_wordmark_badge(scale=2.0, is_dark_bg=True)
    dark_badge = create_wordmark_badge(scale=2.0, is_dark_bg=False)

    light_path = os.path.join(dest_dir, "mirgasimart_wordmark_light_badge.png")
    dark_path = os.path.join(dest_dir, "mirgasimart_wordmark_dark_badge.png")

    light_badge.save(light_path, "PNG")
    dark_badge.save(dark_path, "PNG")
    print(f"Exported standalone wordmarks to {dest_dir}:")
    print(f"  - {light_path}")
    print(f"  - {dark_path}")

def watermark_catalog():
    """Watermarks all primary artworks in docs/output/latest and study iterations."""
    base_dir = "docs/output/latest"
    target_dir = "docs/output/latest/watermarked"
    os.makedirs(target_dir, exist_ok=True)

    artworks = [
        "01_luminescence_of_masazir_salt_dawn.jpg",
        "02_the_weaver_of_sunken_shells_didacna.jpg",
        "03_keeper_of_the_cold_depths_caspian_shad.jpg",
        "04_breath_of_lokbatan_tadpole_goby.jpg",
        "05_the_lampreys_vigil_caspian_lamprey.jpg",
    ]

    print(f"=== Watermarking Master Artworks with MIRGASIM ART™ Wordmark ===")
    for fname in artworks:
        src = os.path.join(base_dir, fname)
        if os.path.exists(src):
            dst = os.path.join(target_dir, fname)
            apply_watermark(src, dst)
        else:
            print(f"  [Skipped] {fname} not found in {base_dir}")

    # Also watermark in root docs/output/watermarked for standalone delivery
    root_wm_dir = "docs/output/watermarked"
    os.makedirs(root_wm_dir, exist_ok=True)
    for fname in artworks:
        src = os.path.join(base_dir, fname)
        if os.path.exists(src):
            dst = os.path.join(root_wm_dir, fname)
            apply_watermark(src, dst)

def main():
    parser = argparse.ArgumentParser(description="Mirgasim Art - Modular Copyright Watermarker")
    parser.add_argument("--input", "-i", help="Input image path")
    parser.add_argument("--output", "-o", help="Output image path")
    parser.add_argument("--position", "-p", default="bottom-right", choices=["bottom-right", "bottom-left", "bottom-center", "center"])
    parser.add_argument("--export-wordmark-assets", action="store_true", help="Export standalone transparent PNG wordmark files")
    args = parser.parse_args()

    if args.export_wordmark_assets:
        export_standalone_assets()
        return

    if args.input and args.output:
        apply_watermark(args.input, args.output, position=args.position)
    else:
        export_standalone_assets()
        watermark_catalog()

if __name__ == "__main__":
    main()
