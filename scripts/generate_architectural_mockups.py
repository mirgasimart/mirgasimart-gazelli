#!/usr/bin/env python3
"""
Architectural In-Situ Mockup Generator for Mirgasim Art Works
============================================================
Composites the clean artwork masters into photorealistic high-end luxury interiors
featuring honed Absheron coquina limestone walls, warm ceiling wash lighting (2700K),
recessed shadow-line floater frames, travertine flooring, and bronze reveals.
"""

import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

def create_limestone_texture(width, height, base_color=(234, 228, 218)):
    """Creates a realistic honed limestone/coquina wall background."""
    img = Image.new("RGB", (width, height), base_color)
    draw = ImageDraw.Draw(img)

    # Add subtle masonry tile joint lines
    # Vertical panels every 400px
    for x in range(350, width, 450):
        draw.line([(x, 0), (x, height)], fill=(215, 208, 196), width=2)
    # Horizontal joint line
    y_joint = int(height * 0.45)
    draw.line([(0, y_joint), (width, y_joint)], fill=(215, 208, 196), width=2)

    # Add warm ceiling wash lighting gradient (2700K golden glow from top)
    gradient = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(gradient)
    
    for y in range(int(height * 0.75)):
        alpha = int(90 * (1.0 - (y / (height * 0.75)) ** 0.8))
        # Warm golden wash: 255, 235, 190
        g_draw.line([(0, y), (width, y)], fill=(255, 238, 200, alpha))
        
    img.paste(gradient, (0, 0), gradient)
    return img

def create_architectural_interior(artwork_path, output_path, orientation="horizontal", title=""):
    """Composites an artwork into a luxury architectural setting."""
    canvas_w, canvas_h = 1920, 1080
    
    # 1. Base Wall (Honed Limestone)
    wall = create_limestone_texture(canvas_w, canvas_h)
    draw = ImageDraw.Draw(wall)

    # 2. Add Lower Floor / Travertine Base
    floor_h = 180
    floor_y = canvas_h - floor_h
    # Floor: ivory travertine
    draw.rectangle([(0, floor_y), (canvas_w, canvas_h)], fill=(218, 212, 202))
    # Bronze baseboard reveal
    draw.rectangle([(0, floor_y - 8), (canvas_w, floor_y)], fill=(140, 115, 75))
    draw.line([(0, floor_y - 9), (canvas_w, floor_y - 9)], fill=(100, 80, 50), width=1)
    
    # Floor reflection / soft ambient shadow
    floor_grad = Image.new("RGBA", (canvas_w, floor_h), (0, 0, 0, 0))
    f_draw = ImageDraw.Draw(floor_grad)
    for y in range(floor_h):
        alpha = int(40 * (1.0 - y / floor_h))
        f_draw.line([(0, y), (canvas_w, y)], fill=(80, 75, 70, alpha))
    wall.paste(floor_grad, (0, floor_y), floor_grad)

    # 3. Add Minimalist Floating Credenza / Bench
    bench_w = int(canvas_w * 0.75)
    bench_h = 45
    bench_x = (canvas_w - bench_w) // 2
    bench_y = floor_y - 100
    
    # Bench shadow on wall
    draw.rectangle([(bench_x + 10, bench_y + 15), (bench_x + bench_w + 15, bench_y + bench_h + 20)], fill=(195, 188, 178))
    # Dark American walnut bench
    draw.rectangle([(bench_x, bench_y), (bench_x + bench_w, bench_y + bench_h)], fill=(42, 34, 28))
    # Top highlight of wood
    draw.line([(bench_x, bench_y), (bench_x + bench_w, bench_y)], fill=(75, 62, 52), width=2)
    # Bronze accent reveal underneath bench
    draw.rectangle([(bench_x + 30, bench_y + bench_h), (bench_x + bench_w - 30, bench_y + bench_h + 6)], fill=(140, 115, 75))

    # 4. Process and Scale Artwork
    art = Image.open(artwork_path).convert("RGB")
    
    # Calculate target dimensions for artwork on the wall
    max_art_w = int(canvas_w * 0.58) if orientation == "horizontal" else int(canvas_w * 0.38)
    max_art_h = int((bench_y - 80) * 0.85)
    
    art.thumbnail((max_art_w, max_art_h), Image.Resampling.LANCZOS)
    art_w, art_h = art.size
    
    art_x = (canvas_w - art_w) // 2
    art_y = int((bench_y - 40 - art_h) // 2 + 30)

    # 5. Realistic Multi-Layer Drop Shadow (French Cleat flush shadow gap)
    shadow_margin = 40
    shadow = Image.new("RGBA", (art_w + shadow_margin * 2, art_h + shadow_margin * 2), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    
    # Soft ambient occlusion shadow
    s_draw.rectangle(
        [(shadow_margin + 6, shadow_margin + 12), 
         (shadow_margin + art_w + 6, shadow_margin + art_h + 16)], 
        fill=(0, 0, 0, 85)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    wall.paste(shadow, (art_x - shadow_margin, art_y - shadow_margin), shadow)

    # 6. Recessed Dark Walnut / Blackened Steel Floater Frame (6px frame + 3px shadow gap)
    frame_border = 6
    gap = 4
    total_frame_w = art_w + (frame_border + gap) * 2
    total_frame_h = art_h + (frame_border + gap) * 2
    frame_x = art_x - frame_border - gap
    frame_y = art_y - frame_border - gap

    # Floater outer frame (matte blackened bronze/walnut)
    draw.rectangle([(frame_x, frame_y), (frame_x + total_frame_w, frame_y + total_frame_h)], fill=(28, 25, 23))
    # Shadow gap (recessed black reveal inside floater frame)
    draw.rectangle([(frame_x + frame_border, frame_y + frame_border), 
                    (frame_x + total_frame_w - frame_border, frame_y + total_frame_h - frame_border)], 
                   fill=(15, 12, 10))

    # 7. Paste Artwork
    wall.paste(art, (art_x, art_y))

    # 8. Subtle Lighting Glaze across canvas (simulating 2700K spotlight wash)
    art_lighting = Image.new("RGBA", (art_w, art_h), (0, 0, 0, 0))
    al_draw = ImageDraw.Draw(art_lighting)
    for y in range(int(art_h * 0.6)):
        alpha = int(25 * (1.0 - y / (art_h * 0.6)))
        al_draw.line([(0, y), (art_w, y)], fill=(255, 245, 220, alpha))
    wall.paste(art_lighting, (art_x, art_y), art_lighting)

    # 9. Minimalist Curatorial Caption in Lower Left
    cap_draw = ImageDraw.Draw(wall)
    caption_text = f"ARCHITECTURAL IN-SITU SIMULATION • {title.upper()}"
    cap_draw.text((60, canvas_h - 50), caption_text, fill=(120, 110, 100))
    sub_text = "Honed Absheron Coquina Wall • 2700K Recessed Wash Lighting • Flush Aluminum Cleat Mount"
    cap_draw.text((60, canvas_h - 34), sub_text, fill=(160, 150, 140))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wall.save(output_path, quality=95)
    print(f"Generated architectural mockup: {output_path}")

def main():
    base_dir = "docs/output/latest"
    clean_dir = os.path.join(base_dir, "_clean")
    insitu_dir = os.path.join(base_dir, "_insitu")
    os.makedirs(insitu_dir, exist_ok=True)

    items = [
        ("01_luminescence_of_masazir_salt_dawn.jpg", "insitu_plate_01_masazir_dawn.jpg", "horizontal", "Plate 01: Luminescence of Masazir (130 × 100 cm)"),
        ("02_the_weaver_of_sunken_shells_didacna.jpg", "insitu_plate_02_shebeke_reliquary.jpg", "vertical", "Plate 02: The Shebeke Reliquary (40 × 60 cm)"),
        ("03_keeper_of_the_cold_depths_caspian_shad.jpg", "insitu_plate_03_binagadi_derrick.jpg", "vertical", "Plate 03: Black Gold (80 × 100 cm)"),
        ("04_breath_of_lokbatan_tadpole_goby.jpg", "insitu_plate_04_breath_of_lokbatan.jpg", "vertical", "Plate 04: Breath of Lokbatan (145 × 145 cm)"),
        ("05_the_lampreys_vigil_caspian_lamprey.jpg", "insitu_plate_05_gobustan_oracle.jpg", "horizontal", "Plate 05: Solar Oracle (120 × 100 cm)")
    ]

    for clean_file, out_file, orient, title in items:
        in_p = os.path.join(clean_dir, clean_file)
        out_p = os.path.join(insitu_dir, out_file)
        if os.path.exists(in_p):
            create_architectural_interior(in_p, out_p, orientation=orient, title=title)

if __name__ == "__main__":
    main()
