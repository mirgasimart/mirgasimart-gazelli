#!/usr/bin/env python3
"""
Generate ultra-luxury brand assets from the Mirgasim Golden 'M' Medallion.
Replaces the previous figurative muse bust with the monumental, regal golden 'M' seal.
Produces:
- assets/branding/brand_medallion.png (1024x1024 transparent circular cutout with supersampled anti-aliased border)
- assets/branding/apple-touch-icon.png (180x180 square on obsidian dark luxury backing)
- assets/branding/android-chrome-192x192.png (192x192)
- assets/branding/android-chrome-512x512.png (512x512)
- assets/branding/favicon-48x48.png
- assets/branding/favicon-32x32.png
- assets/branding/favicon-16x16.png
- assets/branding/favicon.ico
- assets/branding/favicon.svg
- ./favicon.ico (root)
"""

import os
import math
import base64
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE_DIR, "assets", "branding")
SRC_PATH = os.path.join(OUT_DIR, "master_golden_m_medallion.jpg")

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = Image.open(SRC_PATH).convert("RGBA")
    w, h = src.size
    
    # Exact center and radius for the golden rim
    cx, cy = 513.5, 513.5
    r = 509.5
    
    # Bounding box around the circular medallion
    pad = 2.0
    box = (int(cx - r - pad), int(cy - r - pad), int(math.ceil(cx + r + pad)), int(math.ceil(cy + r + pad)))
    cropped = src.crop(box)
    cw, ch = cropped.size
    
    # Create 4x supersampled mask for silk-smooth anti-aliasing
    scale = 4
    mask_large = Image.new("L", (cw * scale, ch * scale), 0)
    draw_large = ImageDraw.Draw(mask_large)
    
    large_cx = (cw / 2.0) * scale
    large_cy = (ch / 2.0) * scale
    large_r = r * scale
    
    draw_large.ellipse(
        [large_cx - large_r, large_cy - large_r, large_cx + large_r, large_cy + large_r],
        fill=255
    )
    
    # Slight smooth blur at 4x scale, then downsample with LANCZOS to 1x
    mask_large = mask_large.filter(ImageFilter.GaussianBlur(radius=1.2))
    alpha_mask = mask_large.resize((cw, ch), Image.Resampling.LANCZOS)
    
    # Apply mask
    medallion = cropped.copy()
    medallion.putalpha(alpha_mask)
    
    # 1. Primary brand medallion: 1024x1024 transparent circular cutout
    medallion_1024 = medallion.resize((1024, 1024), Image.Resampling.LANCZOS)
    medallion_path = os.path.join(OUT_DIR, "brand_medallion.png")
    medallion_1024.save(medallion_path, "PNG", optimize=True)
    print(f"Saved: {medallion_path}")
    
    # 2. Apple Touch Icon (180x180) - Square on deep obsidian black with subtle golden warm aura
    ati_size = 180
    ati = Image.new("RGBA", (ati_size, ati_size), (8, 8, 9, 255))
    
    # Medallion inside with slight breathing margin (168x168)
    med_ati = medallion.resize((168, 168), Image.Resampling.LANCZOS)
    
    # Add subtle warm golden rim glow behind medallion
    glow = Image.new("RGBA", (ati_size, ati_size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([6, 6, 174, 174], fill=(212, 168, 83, 35))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=4))
    
    ati.paste(glow, (0, 0), glow)
    ati.paste(med_ati, (6, 6), med_ati)
    ati_rgb = ati.convert("RGB")
    ati_path = os.path.join(OUT_DIR, "apple-touch-icon.png")
    ati_rgb.save(ati_path, "PNG", optimize=True)
    print(f"Saved: {ati_path}")
    
    # 3. Android Chrome Icons (192x192 & 512x512)
    ac_192 = medallion.resize((192, 192), Image.Resampling.LANCZOS)
    ac_192_path = os.path.join(OUT_DIR, "android-chrome-192x192.png")
    ac_192.save(ac_192_path, "PNG", optimize=True)
    print(f"Saved: {ac_192_path}")
    
    ac_512 = medallion.resize((512, 512), Image.Resampling.LANCZOS)
    ac_512_path = os.path.join(OUT_DIR, "android-chrome-512x512.png")
    ac_512.save(ac_512_path, "PNG", optimize=True)
    print(f"Saved: {ac_512_path}")
    
    # 4. Favicons with micro sharpness enhancement for crisp rendering at tiny resolutions
    enhancer = ImageEnhance.Sharpness(medallion)
    medallion_crisp = enhancer.enhance(1.8)
    
    fav48 = medallion_crisp.resize((48, 48), Image.Resampling.LANCZOS)
    fav48_path = os.path.join(OUT_DIR, "favicon-48x48.png")
    fav48.save(fav48_path, "PNG")
    print(f"Saved: {fav48_path}")
    
    fav32 = medallion_crisp.resize((32, 32), Image.Resampling.LANCZOS)
    fav32_path = os.path.join(OUT_DIR, "favicon-32x32.png")
    fav32.save(fav32_path, "PNG")
    print(f"Saved: {fav32_path}")
    
    fav16 = medallion_crisp.resize((16, 16), Image.Resampling.LANCZOS)
    fav16_path = os.path.join(OUT_DIR, "favicon-16x16.png")
    fav16.save(fav16_path, "PNG")
    print(f"Saved: {fav16_path}")
    
    # 5. Favicon.ico containing 16, 32, 48
    ico_path = os.path.join(OUT_DIR, "favicon.ico")
    fav48.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Saved: {ico_path}")
    
    # Root favicon.ico fallback
    root_ico = os.path.join(BASE_DIR, "favicon.ico")
    fav48.save(root_ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Saved: {root_ico}")
    
    # 6. Favicon SVG wrapper
    with open(medallion_path, "rb") as f:
        b64_hi = base64.b64encode(f.read()).decode("utf-8")
        
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="100%" height="100%">
  <defs>
    <filter id="goldGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#D4AF37" flood-opacity="0.3"/>
    </filter>
  </defs>
  <circle cx="512" cy="512" r="490" fill="#0A0A0B"/>
  <image href="data:image/png;base64,{b64_hi}" x="12" y="12" width="1000" height="1000" filter="url(#goldGlow)"/>
</svg>'''
    
    svg_path = os.path.join(OUT_DIR, "favicon.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Saved: {svg_path}")
    print("All luxury brand assets successfully created from the Golden 'M' Medallion.")

if __name__ == "__main__":
    main()
