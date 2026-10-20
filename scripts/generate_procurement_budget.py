#!/usr/bin/env python3
"""
Mirgasim Art Studio - Comprehensive Procurement & Cost Budget Generator
Generates itemized cost lists in AZN and EUR for the Gazelli Art House 5-artwork commission.
Value Studio Tier: Royal Talens (Amsterdam/Van Gogh) + NL Cargo Logistics + Local Absheron Sourcing.
"""

import os
import csv

# Exchange rate: 1 EUR = 1.85 AZN
EUR_TO_AZN = 1.85

ITEMS = [
    # -------------------------------------------------------------
    # CATEGORY A: SUBSTRATES & MODULAR STRETCHER BARS (NL ONLINE)
    # -------------------------------------------------------------
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Primed/Unprimed Heavy Cotton-Linen Canvas Roll (2.10m x 10m, ~420 gsm)",
        "item_az": "Ağır Kətan Rulonu (2.10m x 10m, ~420 q/m²)",
        "source": "NL Online (Van Beek / Gerstaecker NL)",
        "qty": 1,
        "unit": "roll",
        "unit_eur": 185.00,
        "est_weight_kg": 9.5,
        "notes": "Covers all 5 canvases (12.4 m² needed + ample buffer for studies)"
    },
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Heavy-Duty Modular Stretcher Bars: 185 cm (Pairs)",
        "item_az": "Ağır Modul Altlıq Şamaları: 185 sm (Cüt)",
        "source": "NL Online (Gerstaecker / Van Beek)",
        "qty": 1,
        "unit": "pair (2 pcs)",
        "unit_eur": 28.50,
        "est_weight_kg": 2.2,
        "notes": "For Work 01 (185 x 120 cm)"
    },
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Heavy-Duty Modular Stretcher Bars: 120 cm (Pairs)",
        "item_az": "Ağır Modul Altlıq Şamaları: 120 sm (Cüt)",
        "source": "NL Online (Gerstaecker / Van Beek)",
        "qty": 2,
        "unit": "pair (4 pcs)",
        "unit_eur": 19.50,
        "est_weight_kg": 3.0,
        "notes": "1 pair for Work 01 (120cm), 1 pair for Work 03 (120cm)"
    },
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Heavy-Duty Modular Stretcher Bars: 200 cm (Pairs)",
        "item_az": "Ağır Modul Altlıq Şamaları: 200 sm (Cüt)",
        "source": "NL Online (Gerstaecker / Van Beek)",
        "qty": 1,
        "unit": "pair (2 pcs)",
        "unit_eur": 31.00,
        "est_weight_kg": 2.5,
        "notes": "For Work 03 (120 x 200 cm)"
    },
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Heavy-Duty Modular Stretcher Bars: 180 cm (Pairs)",
        "item_az": "Ağır Modul Altlıq Şamaları: 180 sm (Cüt)",
        "source": "NL Online (Gerstaecker / Van Beek)",
        "qty": 2,
        "unit": "pair (4 pcs)",
        "unit_eur": 27.50,
        "est_weight_kg": 4.2,
        "notes": "For Work 04 Square (180 x 180 cm)"
    },
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Heavy-Duty Modular Stretcher Bars: 150 cm (Pairs)",
        "item_az": "Ağır Modul Altlıq Şamaları: 150 sm (Cüt)",
        "source": "NL Online (Gerstaecker / Van Beek)",
        "qty": 1,
        "unit": "pair (2 pcs)",
        "unit_eur": 23.00,
        "est_weight_kg": 1.8,
        "notes": "For Work 05 (100 x 150 cm)"
    },
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Heavy-Duty Modular Stretcher Bars: 100 cm (Pairs)",
        "item_az": "Ağır Modul Altlıq Şamaları: 100 sm (Cüt)",
        "source": "NL Online (Gerstaecker / Van Beek)",
        "qty": 1,
        "unit": "pair (2 pcs)",
        "unit_eur": 16.50,
        "est_weight_kg": 1.3,
        "notes": "For Work 05 (100 x 150 cm)"
    },
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Standard Stretcher Bars: 40 cm & 60 cm (Pairs)",
        "item_az": "Standart Altlıq Şamaları: 40 sm və 60 sm (Cüt)",
        "source": "NL Online (Gerstaecker / Van Beek)",
        "qty": 1,
        "unit": "set",
        "unit_eur": 12.00,
        "est_weight_kg": 0.8,
        "notes": "For Work 02 (40 x 60 cm)"
    },
    {
        "category": "A. Substrates & Stretcher Bars",
        "item_en": "Internal Modular Cross-Braces & Heavy Corner Keys Pack",
        "item_az": "Daxili Çarpaz Dəstək Tirələri və Bərkidici Tıxaclar",
        "source": "NL Online (Gerstaecker / Van Beek)",
        "qty": 1,
        "unit": "set",
        "unit_eur": 45.00,
        "est_weight_kg": 4.0,
        "notes": "Cross braces for 185x120, 120x200, 180x180, 100x150"
    },

    # -------------------------------------------------------------
    # CATEGORY B: ACRYLIC GROUNDS, GELS & BINDERS (ROYAL TALENS AMSTERDAM)
    # -------------------------------------------------------------
    {
        "category": "B. Acrylic Mediums & Grounds",
        "item_en": "Amsterdam Acrylic Gesso White (1000 ml Bucket)",
        "item_az": "Amsterdam Ağ Akril Qrunt/Qesso (1000 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 3,
        "unit": "bucket",
        "unit_eur": 21.50,
        "est_weight_kg": 4.2,
        "notes": "Base for Recipe A (Absheron Mineral Ground) across all 5 canvases"
    },
    {
        "category": "B. Acrylic Mediums & Grounds",
        "item_en": "Amsterdam Acrylic Gesso Black (1000 ml Bucket)",
        "item_az": "Amsterdam Qara Akril Qesso (1000 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 1,
        "unit": "bucket",
        "unit_eur": 22.50,
        "est_weight_kg": 1.4,
        "notes": "Deep dark ground for Bitumen and Lamprey works"
    },
    {
        "category": "B. Acrylic Mediums & Grounds",
        "item_en": "Amsterdam Extra Heavy Gel Medium Gloss (1000 ml Tub)",
        "item_az": "Amsterdam Əlavə Ağır Parlaq Gel Medium (1000 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 2,
        "unit": "tub",
        "unit_eur": 26.00,
        "est_weight_kg": 2.4,
        "notes": "Essential for embedding Masazir pink salt crystals & pyrite aggregates"
    },
    {
        "category": "B. Acrylic Mediums & Grounds",
        "item_en": "Amsterdam Extra Heavy Gel Medium Matt (1000 ml Tub)",
        "item_az": "Amsterdam Əlavə Ağır Mat Gel Medium (1000 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 2,
        "unit": "tub",
        "unit_eur": 26.00,
        "est_weight_kg": 2.4,
        "notes": "High shear strength bedding for Didacna shells and coquina stone relief"
    },
    {
        "category": "B. Acrylic Mediums & Grounds",
        "item_en": "Amsterdam Modeling Paste / Impasto Paste (1000 ml Tub)",
        "item_az": "Amsterdam relyef / Modelləşdirmə Pastası (1000 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 2,
        "unit": "tub",
        "unit_eur": 24.50,
        "est_weight_kg": 2.6,
        "notes": "Key binder for Recipe C (Lokbatan Mud-Volcano controlled craquelure)"
    },
    {
        "category": "B. Acrylic Mediums & Grounds",
        "item_en": "Amsterdam Acrylic Matt Varnish / Fixative (1000 ml Bottle)",
        "item_az": "Amsterdam Akril Mat Lak / Fiksator (1000 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 1,
        "unit": "bottle",
        "unit_eur": 23.00,
        "est_weight_kg": 1.2,
        "notes": "Sealing coat for mineral grounds before oil application"
    },

    # -------------------------------------------------------------
    # CATEGORY C: OIL PAINTS, SOLVENTS & VARNISHES (ROYAL TALENS VAN GOGH)
    # -------------------------------------------------------------
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Van Gogh Oil Colour: Titanium White (200 ml Tube)",
        "item_az": "Van Gogh Yağlı Boya: Titan Ağ (200 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 3,
        "unit": "tube",
        "unit_eur": 12.80,
        "est_weight_kg": 1.1,
        "notes": "Primary white for figurative flesh, saline shores, and waves"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Van Gogh Oil Colour: Zinc White (200 ml Tube)",
        "item_az": "Van Gogh Yağlı Boya: Sink Ağ (200 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 1,
        "unit": "tube",
        "unit_eur": 12.80,
        "est_weight_kg": 0.4,
        "notes": "Transparent glazing white for delicate skin undertones"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Van Gogh Oil Colour: Ivory Black (200 ml Tube)",
        "item_az": "Van Gogh Yağlı Boya: Fil Dişi Qara (200 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 2,
        "unit": "tube",
        "unit_eur": 12.80,
        "est_weight_kg": 0.7,
        "notes": "For intense dark connected eyebrows, pupils, and derrick scaffolding"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Van Gogh Oil Colour: Earth Master Palette (200 ml Tubes x 5)",
        "item_az": "Van Gogh Yağlı Boya: Torpaq Tonları Dəsti (200 ml x 5)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 1,
        "unit": "set of 5",
        "unit_eur": 58.00,
        "est_weight_kg": 1.8,
        "notes": "Raw Umber, Burnt Umber, Yellow Ochre, Raw Sienna, Burnt Sienna"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Van Gogh Oil Colour: Caspian Maritime Palette (60 ml Tubes x 6)",
        "item_az": "Van Gogh Yağlı Boya: Xəzər Su Tonları Dəsti (60 ml x 6)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 1,
        "unit": "set of 6",
        "unit_eur": 32.50,
        "est_weight_kg": 0.7,
        "notes": "Phthalo Turquoise, Cobalt Blue, Prussian Blue, Viridian, Olive Green, Cerulean"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Van Gogh Oil Colour: Accent Glazes (60 ml Tubes x 4)",
        "item_az": "Van Gogh Yağlı Boya: İntensiv Qırmızı/Bənövşəyi (60 ml x 4)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 1,
        "unit": "set of 4",
        "unit_eur": 24.00,
        "est_weight_kg": 0.5,
        "notes": "Alizarin Crimson, Carmine, Cadmium Red Medium Hue, Dioxazine Mauve"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Talens Odorless White Spirit (1000 ml Bottle)",
        "item_az": "Talens Qoxusuz Həlledici / Ağ Spirt (1000 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 2,
        "unit": "bottle",
        "unit_eur": 14.50,
        "est_weight_kg": 2.0,
        "notes": "Solvent for bitumen dissolution (Recipe D) and brush washing"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Talens Stand Oil (500 ml Bottle)",
        "item_az": "Talens Qatı Kətan Yağı / Stand Oil (500 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 1,
        "unit": "bottle",
        "unit_eur": 15.50,
        "est_weight_kg": 0.6,
        "notes": "Enamel-like leveling and glass-sheen glazes for bitumen & marine shad scales"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Talens Dammar Varnish Gloss (250 ml Bottle)",
        "item_az": "Talens Dammar Lakı (250 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 1,
        "unit": "bottle",
        "unit_eur": 11.50,
        "est_weight_kg": 0.35,
        "notes": "Luminous traditional resin additive for bitumen glaze depth"
    },
    {
        "category": "C. Oil Paints & Archival Varnishes",
        "item_en": "Talens Picture Varnish UV Matt / Satin Spray (400 ml Cans)",
        "item_az": "Talens UV Qoruyucu Rəsm Lakı Sprey (400 ml)",
        "source": "NL Online (Royal Talens / Van Beek)",
        "qty": 4,
        "unit": "can",
        "unit_eur": 13.50,
        "est_weight_kg": 1.8,
        "notes": "Critical for Recipe B: Non-aqueous misting over Masazir salt & mineral craquelure"
    },

    # -------------------------------------------------------------
    # CATEGORY D: STUDIO HARDWARE, TROWELS, SGRAFFITO & PPE (NL ONLINE)
    # -------------------------------------------------------------
    {
        "category": "D. Hardware & Application Tools",
        "item_en": "Stainless Steel Palette Knives & Painter Spatula Set (10 Pcs)",
        "item_az": "Paslanmaz Polad Mastixin və Spatula Dəsti (10 ədəd)",
        "source": "NL Online (Amazon.nl / Van Beek)",
        "qty": 1,
        "unit": "set",
        "unit_eur": 22.00,
        "est_weight_kg": 0.6,
        "notes": "Essential for thick geological impasto knifing and mud manipulation"
    },
    {
        "category": "D. Hardware & Application Tools",
        "item_en": "Masonry Plastering Trowel & Notched Scraper (Flexible Japanese Steel)",
        "item_az": "Yüngül Qurucu Mala və Dişli Qazıyıcı",
        "source": "NL Online (Hornbach / Gamma NL)",
        "qty": 2,
        "unit": "pcs",
        "unit_eur": 9.50,
        "est_weight_kg": 0.7,
        "notes": "For spreading Recipe A mineral gesso across 185x120 and 180x180 canvases"
    },
    {
        "category": "D. Hardware & Application Tools",
        "item_en": "Steel Sgraffito Etching Needles & Dental Modeling Picks (6 Pcs)",
        "item_az": "Polad Sqqaffito Oyma İynələri və Qələmlər Dəsti (6 ədəd)",
        "source": "NL Online (Amazon.nl)",
        "qty": 1,
        "unit": "set",
        "unit_eur": 14.00,
        "est_weight_kg": 0.25,
        "notes": "For incising sharp geometric Shebeke grids and petroglyphs into wet mineral ground"
    },
    {
        "category": "D. Hardware & Application Tools",
        "item_en": "Heavy-Duty Hand Tacker / Staple Gun + 5,000 Heavy Staples",
        "item_az": "Ağır İş Üçün Mebel Stepleri və 5,000 Paslanmaz Ştift",
        "source": "NL Online (Gamma / Hornbach NL)",
        "qty": 1,
        "unit": "set",
        "unit_eur": 29.50,
        "est_weight_kg": 1.4,
        "notes": "Double-stapling heavy canvas onto modular stretchers"
    },
    {
        "category": "D. Hardware & Application Tools",
        "item_en": "Professional Wide Canvas Stretching Pliers",
        "item_az": "Peşəkar Kətan Dartma Qısqacı (Geniş Ağızlı)",
        "source": "NL Online (Van Beek)",
        "qty": 1,
        "unit": "pcs",
        "unit_eur": 18.00,
        "est_weight_kg": 0.5,
        "notes": "Provides drum-tight tension on 420+ gsm heavy canvas"
    },
    {
        "category": "D. Hardware & Application Tools",
        "item_en": "Hog Bristle & Synthetic Flat Brushes Assortment (15 Pcs)",
        "item_az": "Donuz Qılı və Sintetik Fırça Dəsti (15 ədəd)",
        "source": "NL Online (Van Beek)",
        "qty": 1,
        "unit": "set",
        "unit_eur": 28.00,
        "est_weight_kg": 0.5,
        "notes": "For glazes, underpainting, and delicate portrait details"
    },
    {
        "category": "D. Hardware & Application Tools",
        "item_en": "Personal Protective Equipment: FFP3 Respirators (Box of 10) & Nitrile Gloves (Box of 100)",
        "item_az": "Fərdi Mühafizə: FFP3 Respiratorlar və Nitril Əlcəklər",
        "source": "NL Online (Amazon.nl)",
        "qty": 1,
        "unit": "kit",
        "unit_eur": 25.00,
        "est_weight_kg": 0.8,
        "notes": "Protection during limestone dust sifting, solvent mixing, and bitumen handling"
    },

    # -------------------------------------------------------------
    # CATEGORY E: INTERNATIONAL CARGO & SHIPPING (NL TO BAKU)
    # -------------------------------------------------------------
    {
        "category": "E. International Cargo Logistics",
        "item_en": "Air Cargo Freight Consolidated Shipment (Amsterdam Schiphol to Baku GYD, ~55 kg)",
        "item_az": "Hava Yükü Konsolidasiya Daşınması (Amsterdam-Bakı, ~55 kq)",
        "source": "Cargo Express (Silk Way / Camex / Limak / DHL Freight)",
        "qty": 1,
        "unit": "shipment",
        "unit_eur": 195.00,
        "est_weight_kg": 55.0,
        "notes": "Consolidated package for all stretcher bars, canvas rolls, paints & tools"
    },
    {
        "category": "E. International Cargo Logistics",
        "item_en": "Baku Airport Terminal Handling & Customs Declaration Fee",
        "item_az": "Bakı Terminal İdarəetmə və Gömrük Bəyannamə Xərci",
        "source": "Baku Cargo Terminal (GYD)",
        "qty": 1,
        "unit": "fee",
        "unit_eur": 35.00,
        "est_weight_kg": 0.0,
        "notes": "Standard clearance fee for personal studio supplies"
    },

    # -------------------------------------------------------------
    # CATEGORY F: LOCAL ABSHERON WILD FIELD SOURCING EXPEDITIONS
    # -------------------------------------------------------------
    {
        "category": "F. Local Field Expeditions",
        "item_en": "4WD Vehicle Rental & Fuel for 2-Day Absheron Geological Expedition",
        "item_az": "2 Günlük Abşeron Ekspedisiyası üçün 4x4 Avtomobil və Yanacaq",
        "source": "Local Baku Rental & SOCAR Gas",
        "qty": 1,
        "unit": "2 days",
        "unit_eur": 95.00,
        "est_weight_kg": 0.0,
        "notes": "Route: Masazır Lake -> Lökbatan Mud Volcano -> Binaqədi Tar Pits -> Türkan/Bilgəh coast"
    },
    {
        "category": "F. Local Field Expeditions",
        "item_en": "Airtight Heavy-Duty Buckets (10L x 6) & Geological Sampling Trowels",
        "item_az": "Qapaqlı Hava Keçirməyən Vedrələr (10L x 6) və Nümunə Qabları",
        "source": "Baku Sədərək / Binə Bazar or Local Hardware",
        "qty": 1,
        "unit": "kit",
        "unit_eur": 18.00,
        "est_weight_kg": 2.0,
        "notes": "For transporting wet volcanic clay, raw Masazir salt, and coastal sand"
    },
    {
        "category": "F. Local Field Expeditions",
        "item_en": "Field Supplies: Hydrogen Peroxide (30%), Disinfectant & Lab Sifting Sieves",
        "item_az": "Hidrogen Peroksid (30%), Ələklər və Təmizləyici Vasitələr",
        "source": "Baku Local Pharmacy / Hardware",
        "qty": 1,
        "unit": "kit",
        "unit_eur": 15.00,
        "est_weight_kg": 1.5,
        "notes": "For Didacna shell bleaching and mechanical limestone dust sifting"
    },
    {
        "category": "F. Local Field Expeditions",
        "item_en": "Pyrite Ore Specimens (Brassy Mineral Aggregates) from Local Collectors",
        "item_az": "Təbii Pirit Filizi Nümunələri (Yerli Kolleksiyaçılardan)",
        "source": "Nizami Street Mineral Stalls / Dashgil Field Find",
        "qty": 1,
        "unit": "lot (~500g)",
        "unit_eur": 20.00,
        "est_weight_kg": 0.5,
        "notes": "Golden fool's gold sulfide nodules to crush into 1-4 mm aggregates"
    },

    # -------------------------------------------------------------
    # CATEGORY G: CONCRETE / STONE SUPPLIERS (BACKUP BULK OPTION)
    # -------------------------------------------------------------
    {
        "category": "G. Concrete & Stone Yards (Backup Bulk)",
        "item_en": "Fine Sifted Absheron Limestone Powder (Əhəng tozu, 25 kg bag)",
        "item_az": "Abşeron Əhəngdaşı Tozu / Gülbax Tozu (25 kq kisə)",
        "source": "Dərnəgül / Binəqədi Daş Bazarı (Stone Yards)",
        "qty": 1,
        "unit": "25kg bag",
        "unit_eur": 6.50,
        "est_weight_kg": 25.0,
        "notes": "Ultra-cheap local commercial source for limestone gesso ground filler"
    },
    {
        "category": "G. Concrete & Stone Yards (Backup Bulk)",
        "item_en": "Crushed Absheron Coquina Limestone Aggregate (Balıqqulağı qırıntısı, 20 kg bag)",
        "item_az": "Xırdalanmış Balıqqulağı Daşı / Coquina Qırıntısı (20 kq kisə)",
        "source": "Qaradağ / Şüvəlan Daş Sexi (Stone Carvers)",
        "qty": 1,
        "unit": "20kg bag",
        "unit_eur": 5.50,
        "est_weight_kg": 20.0,
        "notes": "Porous fossil-rich aggregate for sculptural 3D relief texture"
    },
    {
        "category": "G. Concrete & Stone Yards (Backup Bulk)",
        "item_en": "Washed Quartz Coastal Dune Sand (Yuyulmuş Dəniz Qumu, 20 kg bag)",
        "item_az": "Yuyulmuş Sahil Qumu (20 kq kisə)",
        "source": "Local Baku Building Materials Yard",
        "qty": 1,
        "unit": "20kg bag",
        "unit_eur": 4.50,
        "est_weight_kg": 20.0,
        "notes": "Pre-washed salt-free mineral grit for tooth and traction in gesso"
    }
]

def calculate_budget():
    categories = {}
    total_eur = 0.0
    total_azn = 0.0
    total_cargo_weight_kg = 0.0

    for item in ITEMS:
        qty = item["qty"]
        unit_eur = item["unit_eur"]
        line_eur = qty * unit_eur
        line_azn = line_eur * EUR_TO_AZN
        weight = item["est_weight_kg"] * (qty if item["unit"] not in ["set", "kit", "shipment"] else 1)

        item["line_eur"] = line_eur
        item["line_azn"] = line_azn

        cat = item["category"]
        if cat not in categories:
            categories[cat] = {
                "items": [],
                "subtotal_eur": 0.0,
                "subtotal_azn": 0.0,
                "weight_kg": 0.0
            }

        categories[cat]["items"].append(item)
        categories[cat]["subtotal_eur"] += line_eur
        categories[cat]["subtotal_azn"] += line_azn
        categories[cat]["weight_kg"] += weight

        total_eur += line_eur
        total_azn += line_azn

        # Cargo weight tracking for NL to Baku shipment
        if cat in ["A. Substrates & Stretcher Bars", "B. Acrylic Mediums & Grounds",
                   "C. Oil Paints & Archival Varnishes", "D. Hardware & Application Tools"]:
            total_cargo_weight_kg += weight

    # Add 10% contingency buffer
    contingency_rate = 0.10
    contingency_eur = total_eur * contingency_rate
    contingency_azn = total_azn * contingency_rate

    grand_total_eur = total_eur + contingency_eur
    grand_total_azn = total_azn + contingency_azn

    return {
        "categories": categories,
        "total_eur": total_eur,
        "total_azn": total_azn,
        "contingency_eur": contingency_eur,
        "contingency_azn": contingency_azn,
        "grand_total_eur": grand_total_eur,
        "grand_total_azn": grand_total_azn,
        "total_cargo_weight_kg": total_cargo_weight_kg,
        "rate": EUR_TO_AZN
    }

def export_csv(budget_data, output_filepath):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Category",
            "Item Name (EN)",
            "Item Name (AZ)",
            "Supplier / Channel",
            "Quantity",
            "Unit",
            "Unit Price (EUR)",
            "Total Price (EUR)",
            "Total Price (AZN)",
            "Est. Weight (kg)",
            "Application & Strategic Notes"
        ])

        for cat_name, cat_data in budget_data["categories"].items():
            for it in cat_data["items"]:
                writer.writerow([
                    cat_name,
                    it["item_en"],
                    it["item_az"],
                    it["source"],
                    it["qty"],
                    it["unit"],
                    f"{it['unit_eur']:.2f}",
                    f"{it['line_eur']:.2f}",
                    f"{it['line_azn']:.2f}",
                    f"{it['est_weight_kg']:.1f}",
                    it["notes"]
                ])
            # Category subtotal row
            writer.writerow([
                f"SUBTOTAL: {cat_name}",
                "", "", "", "", "",
                "",
                f"{cat_data['subtotal_eur']:.2f}",
                f"{cat_data['subtotal_azn']:.2f}",
                f"{cat_data['weight_kg']:.1f}",
                ""
            ])

        # Contingency row
        writer.writerow([])
        writer.writerow([
            "CONTINGENCY BUFFER (10%)",
            "Emergency Replenishment & Price Variance Buffer",
            "Gözlənilməz Xərclər Ehtiyatı (10%)",
            "Studio Contingency Fund",
            "1", "buffer",
            f"{budget_data['contingency_eur']:.2f}",
            f"{budget_data['contingency_eur']:.2f}",
            f"{budget_data['contingency_azn']:.2f}",
            "0.0",
            "Covers minor price fluctuations, express fees, and extra solvent/varnish"
        ])

        # Grand Total
        writer.writerow([
            "GRAND TOTAL (AZN / EUR)",
            "Complete 5-Artwork Commission Procurement Budget",
            "5 Əsər Üçün Tam Təchizat Büdcəsi",
            "All Channels (NL Cargo + Baku Local)",
            "", "",
            "",
            f"{budget_data['grand_total_eur']:.2f}",
            f"{budget_data['grand_total_azn']:.2f}",
            f"{budget_data['total_cargo_weight_kg']:.1f} (Cargo)",
            f"Converted at 1 EUR = {budget_data['rate']:.2f} AZN"
        ])

def print_summary(budget_data):
    print("=" * 75)
    print("  MIRGASIM ART STUDIO | GAZELLI ART COMMISSION PROCUREMENT BUDGET")
    print(f"  Exchange Benchmark: 1 EUR = {budget_data['rate']:.2f} AZN")
    print("=" * 75)
    for cat_name, cat_data in budget_data["categories"].items():
        print(f"\n[{cat_name}]")
        print(f"  Subtotal: €{cat_data['subtotal_eur']:>8.2f}  |  ₼{cat_data['subtotal_azn']:>8.2f} AZN")
        for it in cat_data["items"]:
            print(f"   • {it['item_en'][:45]:<45} : €{it['line_eur']:>6.2f} (₼{it['line_azn']:>6.2f})")

    print("\n" + "-" * 75)
    print(f"BASE ESTIMATE TOTAL      : €{budget_data['total_eur']:>8.2f}  |  ₼{budget_data['total_azn']:>8.2f} AZN")
    print(f"CONTINGENCY BUFFER (10%) : €{budget_data['contingency_eur']:>8.2f}  |  ₼{budget_data['contingency_azn']:>8.2f} AZN")
    print("=" * 75)
    print(f"GRAND TOTAL ESTIMATE     : €{budget_data['grand_total_eur']:>8.2f}  |  ₼{budget_data['grand_total_azn']:>8.2f} AZN")
    print(f"EST. CARGO WEIGHT (NL)   : ~{budget_data['total_cargo_weight_kg']:.1f} kg")
    print("=" * 75)

if __name__ == "__main__":
    budget = calculate_budget()
    print_summary(budget)
    csv_path = os.path.join(os.path.dirname(__file__), "..", "docs", "procurement", "procurement_budget_azn_eur.csv")
    export_csv(budget, csv_path)
    print(f"\n[OK] CSV exported to: {os.path.abspath(csv_path)}")
