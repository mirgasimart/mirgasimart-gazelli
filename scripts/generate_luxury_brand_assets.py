#!/usr/bin/env python3
"""
Generate ultra-luxury brand assets from the Caspian Fire Muse medallion.
Produces:
- assets/branding/brand_medallion.png (1024x1024 transparent circular cutout with supersampled anti-aliased border)
- assets/branding/apple-touch-icon.png (180x180 square on obsidian dark luxury backing)
- assets/branding/favicon-32x32.png
- assets/branding/favicon-16x16.png
- assets/branding/favicon.ico
- assets/branding/favicon.svg
"""

import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

SRC_PATH = "/Users/jmj/.gemini/antigravity-ide/brain/e7c2de84-e26a-4c28-b374-718f1588f00c/mirgasim_luxury_medallion_icon_1792847900406.jpg"
OUT_DIR = "/Users/jmj/repos/mirgasimart-gazelli/assets/branding"

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = Image.open(SRC_PATH).convert("RGBA")
    w, h = src.size
    
    # Exact center and radius for the golden rim
    cx, cy = 500, 501
    r = 472
    
    # Crop a square bounding box around the medallion with padding
    pad = 8
    box = (cx - r - pad, cy - r - pad, cx + r + pad, cy + r + pad)
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
    
    # Resize to clean square 1024x1024
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
    
    # 3. Favicon 32x32 & 16x16 with contrast enhancement for micro clarity
    # Slight micro sharpening so features pop at 32px
    enhancer = ImageEnhance.Sharpness(medallion)
    medallion_crisp = enhancer.enhance(1.8)
    
    fav32 = medallion_crisp.resize((32, 32), Image.Resampling.LANCZOS)
    fav32_path = os.path.join(OUT_DIR, "favicon-32x32.png")
    fav32.save(fav32_path, "PNG")
    print(f"Saved: {fav32_path}")
    
    fav16 = medallion_crisp.resize((16, 16), Image.Resampling.LANCZOS)
    fav16_path = os.path.join(OUT_DIR, "favicon-16x16.png")
    fav16.save(fav16_path, "PNG")
    print(f"Saved: {fav16_path}")
    
    # 4. Favicon.ico containing 16, 32, 48
    fav48 = medallion_crisp.resize((48, 48), Image.Resampling.LANCZOS)
    ico_path = os.path.join(OUT_DIR, "favicon.ico")
    fav48.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Saved: {ico_path}")
    
    # Also save favicon.ico to root if standard browser fallback expects it
    root_ico = "/Users/jmj/repos/mirgasimart-gazelli/favicon.ico"
    fav48.save(root_ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Saved: {root_ico}")
    
    # 5. Favicon SVG wrapper
    import base64
    with open(fav32_path, "rb") as f:
        b64_32 = base64.b64encode(f.read()).decode("utf-8")
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

if __name__ == "__main__":
    main()
