/**
 * MIRGASIM ART STUDIO | Curatorial Commission Data
 * Series: Absheron Tectonics: Primordial Matter & Geological Strata
 * Commissioning Body: Gazelli Art House (London / Baku)
 */

const GALLERY_DATA = [
  {
    id: "plate-01",
    number: "01",
    roman: "I",
    title: "Luminescence of Masazir Dawn",
    azTitle: "Masazır Şəfəqi: Çəhrayı Duz Gölü",
    genre: "Pure Mineral Abstraction / Lacustrine Strata Painting",
    widthCm: 185,
    heightCm: 120,
    dimensions: "185 × 120 cm (72.8 × 47.2 in)",
    orientation: "horizontal",
    niche: "Executive Boardroom / Presidential Suite / Coastal Wellness Reception",
    endemicFocus: "Absheron Lacustrine Strata (Pure geological meditation; zero figures, zero fauna, zero carpets)",
    scientificTaxonomy: "Artemia salina / Saline micro-algal Dunaliella salina mineral salts",
    minerals: [
      {
        name: "Masazir Pink Lake Salt",
        description: "Genuine crystalline lake salt encrustations integrated directly into the heavy impasto ground, catching natural daylight with subtle prismatic sparkle."
      },
      {
        name: "Absheron Limestone & Alabaster Plaster",
        description: "Porous cream-and-ochre ground scored with delicate geometric sgraffito lines."
      }
    ],
    curatorialNarrative: "An ethereal, meditative abstract landscape capturing the tranquil morning horizon over Lake Masazir. Where misted pastel-pink saline waters meet white crystalline shores, thick palette-knife impasto sculpts the organic coastline, embedded with coarse pink-and-white mineral crystals that glisten naturally in ambient light. Scored with delicate geometric sgraffito fissures in the mineral foreground, this composition embodies pure lacustrine serenity.",
    turnkeySpecs: {
      chassis: "Cross-braced Finnish pine with aluminum cradle",
      weight: "14.5 kg",
      mounting: "Dual continuous aluminum French cleats (Z-bars)",
      edgeFinish: "Continuous mineral gallery-wrap (45mm profile)",
      lighting: "2700K warm-white recessed ceiling wash lighting (CRI 95+)"
    },
    images: {
      clean: "docs/output/latest/_clean/01_luminescence_of_masazir_salt_dawn.jpg",
      insitu: "docs/output/latest/_insitu/insitu_plate_01_masazir_dawn.jpg",
      plate: "docs/output/latest/_exhibition_plates/plate_01_luminescence_of_masazir_salt_dawn.jpg"
    },
    hotspots: [
      { x: 32, y: 48, label: "Masazir Pink Salt Crystals", desc: "Genuine crystallized halite clusters embedded in thick oil impasto." },
      { x: 68, y: 35, label: "Atmospheric Saline Gradient", desc: "Glazed blush and dawn-rose pigments evoking geothermal lake reflections." },
      { x: 45, y: 78, label: "Incised Sgraffito Fissures", desc: "Razor-carved directional strata lines exposing the coquina limestone primer." }
    ]
  },
  {
    id: "plate-02",
    number: "02",
    roman: "II",
    title: "The Shebeke Reliquary: Fossil Didacna in Absheron Stone",
    azTitle: "Şəbəkə Qalığı: Qədim Didakna və Daş Pəncərə",
    genre: "Mixed-Media Painting on Canvas / Tactile Stone Relief",
    widthCm: 40,
    heightCm: 60,
    dimensions: "40 × 60 cm (15.7 × 23.6 in)",
    orientation: "vertical",
    niche: "VIP Elevator Vestibule / Intimate Gallery Corridor / Private Dining Alcove",
    endemicFocus: "Caspian Cockles (Didacna trigonoides & Didacna pyramidata)",
    scientificTaxonomy: "Didacna trigonoides (Pall.) & Didacna pyramidata (Grimm)",
    minerals: [
      {
        name: "Absheron Limestone & Coquina Primer",
        description: "Fine quarry coquina and porous limestone powder integrated into gesso ground for authentic masonry tooth."
      },
      {
        name: "Natural Caspian Didacna Accents",
        description: "Genuine small Didacna bivalve shells embedded in low-relief into the impasto crust."
      },
      {
        name: "Absheron Coastal Beach Sand",
        description: "Natural quartz-shell sand blended into knife impasto for tactile friction."
      }
    ],
    curatorialNarrative: "Celebrating Absheron's ancient stone-carving heritage (daş yonma), this intimate vertical painting on canvas captures a weather-worn Shebeke window lattice rendered in thick palette-knife impasto and porous mineral grounds. Behind the painted geometric tracery glow luminous glazes of Caspian turquoise and deep lapis lazuli. The painted surface is enriched with subtle low-relief physical accents—authentic small Didacna cockle shells embedded into the impasto crust—while an elongated painted hand rests against the window aperture, bridging human craftsmanship and deep geological time.",
    turnkeySpecs: {
      chassis: "Solid reinforced wood cradle",
      weight: "3.2 kg",
      mounting: "Single aluminum Z-bar cleat with locking pin",
      edgeFinish: "Gallery-wrapped coquina primer edges (38mm profile)",
      lighting: "2700K–3000K accent spotlight with narrow 15° beam"
    },
    images: {
      clean: "docs/output/latest/_clean/02_the_weaver_of_sunken_shells_didacna.jpg",
      insitu: "docs/output/latest/_insitu/insitu_plate_02_shebeke_reliquary.jpg",
      plate: "docs/output/latest/_exhibition_plates/plate_02_the_weaver_of_sunken_shells_didacna.jpg"
    },
    hotspots: [
      { x: 50, y: 25, label: "Carved Shebeke Lattice", desc: "Geometric architectural stone tracery inspired by Palace of the Shirvanshahs." },
      { x: 38, y: 70, label: "Fossil Didacna Cockles", desc: "Prehistoric Caspian bivalve fossils anchored into mineral plaster." },
      { x: 62, y: 55, label: "Turquoise & Lapis Glaze", desc: "Translucent Caspian deep-water hues glowing behind masonry fretwork." }
    ]
  },
  {
    id: "plate-03",
    number: "03",
    roman: "III",
    title: "The Binagadi Derrick: Hydrocarbon Strata & Pyrite Shad",
    azTitle: "Binaqədi Buruğu: Qara Qızıl və Pirit Şad",
    genre: "Industrial-Geological Abstraction / Hydrocarbon Matter Painting",
    widthCm: 80,
    heightCm: 100,
    dimensions: "80 × 100 cm (31.5 × 39.4 in)",
    orientation: "vertical",
    niche: "High-Traffic Transition Corridor / Executive Wall / Aviation VIP Lounge",
    endemicFocus: "Caspian Marine Shad / Brazhnikov’s Shad (Alosa braschnikowi)",
    scientificTaxonomy: "Alosa braschnikowi (Borodin, 1904)",
    minerals: [
      {
        name: "Natural Absheron Bitumen (Binagadi & Fatmai)",
        description: "Pure unrefined asphaltite applied in thick, viscous knife-strokes, curing to a deep matte-gloss hydrocarbon black."
      },
      {
        name: "Pyrite Mineral Aggregates (FeS₂)",
        description: "Irregular metallic brassy-gold sulfide crystals embedded into the fish scales, catching ambient gallery lighting."
      },
      {
        name: "Absheron Limestone Powder",
        description: "Chalky white contrast scored across the black bitumen field."
      }
    ],
    curatorialNarrative: "Confronting Baku's historic role as the pioneer of world petroleum, minimal structural scaffolding beams inspired by historic wooden oil derricks slice across visceral slabs of pitch-black Binagadi bitumen. Leaping through the dark matrix is an armored Caspian marine shad adorned with metallic golden pyrite ore, set above the eternal subterranean gas flame (Yanar Dağ / Ateshgah), synthesizing Baku's hydrocarbon heritage with natural marine vitality.",
    turnkeySpecs: {
      chassis: "Solid cross-braced Finnish pine with aluminum cradle",
      weight: "6.8 kg",
      mounting: "Heavy-duty aluminum French cleat (Z-bar)",
      edgeFinish: "Polymerized bitumen continuous edge (45mm profile)",
      lighting: "3000K museum track lighting to catch pyrite metallic facets"
    },
    images: {
      clean: "docs/output/latest/_clean/03_keeper_of_the_cold_depths_caspian_shad.jpg",
      insitu: "docs/output/latest/_insitu/insitu_plate_03_binagadi_derrick.jpg",
      plate: "docs/output/latest/_exhibition_plates/plate_03_keeper_of_the_cold_depths_caspian_shad.jpg"
    },
    hotspots: [
      { x: 42, y: 22, label: "Derrick Structural Beams", desc: "Minimalist geometric scaffolding echoing early Absheron oil derricks." },
      { x: 55, y: 52, label: "Pyrite-Studded Caspian Shad", desc: "Natural brassy pyrite flakes encrusted on Alosa braschnikowi scales." },
      { x: 48, y: 85, label: "Viscous Binagadi Bitumen", desc: "Subterranean heavy asphaltite matrix cured with archival beeswax." }
    ]
  },
  {
    id: "plate-04",
    number: "04",
    roman: "IV",
    title: "Breath of Lokbatan: Volcanic Crater and Armored Goby",
    azTitle: "Lökbatan Nəfəsi: Palçıq Vulkanı və Zirehli Qobi",
    genre: "Earth-Art Vortex / Geothermal Mineral Painting",
    widthCm: 180,
    heightCm: 180,
    dimensions: "180 × 180 cm (70.9 × 70.9 in)",
    orientation: "square",
    niche: "Grand Central Atrium / Double-Height Salon / Wellness Mezzanine Feature Wall",
    endemicFocus: "Armored Caspian Tadpole Goby (Benthophilus spp.)",
    scientificTaxonomy: "Benthophilus macrocephalus / Benthophilus baeri",
    minerals: [
      {
        name: "Subterranean Lokbatan Mud-Volcano Clay",
        description: "Authentic mineral clay harvested from Lokbatan crater ejecta, curing into rich 3D craquelure fissures."
      },
      {
        name: "Caspian Mineral Glazes",
        description: "Luminous celadon, seafoam green, and verdigris pigments evoking thermal spring luminescence."
      },
      {
        name: "Metallic Pyrite Infiltration",
        description: "Genuine pyrite mineral grains accenting the prehistoric armor plates of the goby."
      }
    ],
    curatorialNarrative: "A monumental square statement uniting subterranean geothermal energy with aquatic serenity. An aerial vortex of an active mud-volcano crater rendered in thick palette-knife impasto and authentic mud clay craquelure fissures opens into luminous, flowing glazes of Caspian celadon and seafoam green. Gliding through the geothermal currents, an armored Caspian tadpole goby (Benthophilus) gleams with metallic pyrite veins, harmonizing primordial geological power with tranquil ecological resilience.",
    turnkeySpecs: {
      chassis: "Dual-aluminum cross-braced cradled chassis",
      weight: "19.5 kg",
      mounting: "Triple heavy-duty aircraft-grade aluminum French cleats",
      edgeFinish: "Continuous volcanic craquelure wrap (50mm profile)",
      lighting: "High-CRI (98) wall wash lighting grazing from above to accent deep craquelure shadows"
    },
    images: {
      clean: "docs/output/latest/_clean/04_breath_of_lokbatan_tadpole_goby.jpg",
      insitu: "docs/output/latest/_insitu/insitu_plate_04_breath_of_lokbatan.jpg",
      plate: "docs/output/latest/_exhibition_plates/plate_04_breath_of_lokbatan_tadpole_goby.jpg"
    },
    hotspots: [
      { x: 50, y: 50, label: "Geothermal Crater Vortex", desc: "Concentric impasto vortex evoking the pulsating throat of Lokbatan mud volcano." },
      { x: 65, y: 62, label: "Armored Benthophilus Goby", desc: "Archaic armored benthic fish adorned with raw metallic pyrite crystals." },
      { x: 28, y: 34, label: "Volcanic Clay Craquelure", desc: "Authentic mud clay dried into deep geological fractures and tactile fissures." }
    ]
  },
  {
    id: "plate-05",
    number: "05",
    roman: "V",
    title: "The Gobustan Solar Oracle: Ouroboros Lamprey",
    azTitle: "Qobustan Günəşi: İlanbalığı və Qədim Qaya Təsvirləri",
    genre: "Mythological Contemporary Altar Piece / Archaeological Totem",
    widthCm: 120,
    heightCm: 100,
    dimensions: "120 × 100 cm (47.2 × 39.4 in)",
    orientation: "horizontal",
    niche: "Ceremonial Foyer / Executive Reception / Gallery Altar Niche",
    endemicFocus: "Caspian Lamprey (Caspiomyzon wagneri)",
    scientificTaxonomy: "Caspiomyzon wagneri (Kessler, 1870)",
    minerals: [
      {
        name: "Gobustan Limestone & Bone Plaster",
        description: "Sgraffito incisions depicting prehistoric petroglyphs (reed boats, hunters, and sacred solar bulls)."
      },
      {
        name: "Absheron Coastal Beach Sand",
        description: "Concentric rings textured with coarse raw beach sand and quartz grit."
      },
      {
        name: "Masazir Lake Salt Clusters",
        description: "Saline crystals embedded along the cyan-blue outer orbital halo."
      }
    ],
    curatorialNarrative: "A transcendental contemporary altar piece uniting prehistoric rock art with ecological mystery. The ancient Caspian lamprey coils into an Ouroboros circle of eternity around a concentric sand-and-salt mandala. Carved directly into the limestone ground are Gobustan petroglyphs (reed boats, hunters, and sacred solar bulls), immortalizing Absheron's ancient rock art heritage within deep cosmological time.",
    turnkeySpecs: {
      chassis: "Anti-warp aluminum-cradled stretcher",
      weight: "8.2 kg",
      mounting: "Dual aluminum Z-bar cleat set",
      edgeFinish: "Mineral-plaster gallery edge (45mm profile)",
      lighting: "Dedicated 2700K framing projector or adjustable gimbal spotlight"
    },
    images: {
      clean: "docs/output/latest/_clean/05_the_lampreys_vigil_caspian_lamprey.jpg",
      insitu: "docs/output/latest/_insitu/insitu_plate_05_gobustan_oracle.jpg",
      plate: "docs/output/latest/_exhibition_plates/plate_05_the_lampreys_vigil_caspian_lamprey.jpg"
    },
    hotspots: [
      { x: 50, y: 46, label: "Solar Mandala & Ouroboros", desc: "The ancient Caspian lamprey coiled into an eternal cosmic solar wheel." },
      { x: 48, y: 76, label: "Gobustan Petroglyph Sgraffito", desc: "Carved reed boat and ritual dancer figures incised in porous stone plaster." },
      { x: 26, y: 38, label: "Caspian Cyan Orbital Ring", desc: "Vibrant azure and salt mineral halo radiating from the ancient sun disk." }
    ]
  },
  {
    id: "study-01",
    number: "06",
    roman: "Archive",
    title: "The Muse of Masazir: Caspian Seal Study",
    azTitle: "Masazır Pərisi: Xəzər Suiti və Duz Qayası",
    genre: "Figurative Mineral Portraiture / Geological Matter Painting",
    widthCm: 100,
    heightCm: 150,
    dimensions: "100 × 150 cm (39.4 × 59.1 in)",
    orientation: "vertical",
    niche: "Private VIP Wellness Suite / Executive Lounge / Presidential Antechamber",
    endemicFocus: "Caspian Seal (Pusa caspica)",
    scientificTaxonomy: "Pusa caspica (Gmelin, 1788)",
    minerals: [
      {
        name: "Genuine Masazir Pink Lake Salt",
        description: "Encrustations glistening in ambient light across the warm ochre impasto ground."
      },
      {
        name: "Absheron Limestone Plaster",
        description: "Porous tactile masonry ground scored with delicate geometric sgraffito incisions."
      }
    ],
    curatorialNarrative: "Synthesizing Mirgasim’s iconic visual hallmarks—a melancholic, statuesque Azerbaijani muse with connected dark brows, sculpted hands, and intense gaze—with the raw geological matter of Absheron. Cradled tenderly in her arms is a gentle Caspian seal pup (Pusa caspica), its silver-grey mottled coat glistening against modern draped plum-burgundy fabric. The background is a thick, sculptural palette-knife impasto ground in warm ochres and blush tones, embedded with authentic sparkling crystalline clusters of raw pink-and-white Masazir lake salt and incised with delicate geometric sgraffito lines.",
    turnkeySpecs: {
      chassis: "Reinforced wood and aluminum chassis",
      weight: "10.8 kg",
      mounting: "Dual aluminum Z-bars",
      edgeFinish: "Gallery-wrapped blush limestone edges (40mm profile)",
      lighting: "2700K intimate warm wash lighting"
    },
    images: {
      clean: "docs/output/latest/_studies/the_muse_of_masazir_caspian_seal_study.jpg",
      insitu: "docs/output/latest/_studies/the_muse_of_masazir_caspian_seal_study.jpg",
      plate: "docs/output/latest/_studies/the_muse_of_masazir_caspian_seal_study.jpg"
    },
    hotspots: [
      { x: 50, y: 30, label: "Sculpted Absheron Muse", desc: "Iconic Mirgasim features: statuesque gaze, connected dark brows, timeless nobility." },
      { x: 52, y: 64, label: "Caspian Seal Pup (Pusa caspica)", desc: "Endemic Caspian marine sentinel cradled with profound tenderness." },
      { x: 78, y: 40, label: "Masazir Halite Crystals", desc: "Pure pink lake salt aggregates glistening along the warm ochre ground." }
    ]
  }
];

// Architectural wall surface options
const WALL_SURFACES = [
  {
    id: "limestone",
    name: "Absheron Coquina Limestone",
    subtitle: "Warm, tactile, porous quarry plaster",
    bgClass: "wall-limestone",
    ambientLight: "rgba(255, 238, 215, 0.12)"
  },
  {
    id: "white-cube",
    name: "Curatorial White Cube",
    subtitle: "Pristine warm-neutral museum off-white",
    bgClass: "wall-white-cube",
    ambientLight: "rgba(255, 255, 255, 0.18)"
  },
  {
    id: "anthracite",
    name: "Anthracite Architectural Concrete",
    subtitle: "Moody dark gallery with high drama",
    bgClass: "wall-anthracite",
    ambientLight: "rgba(215, 225, 240, 0.08)"
  },
  {
    id: "travertine",
    name: "Warm Travertine Stone",
    subtitle: "Geological golden vein texture",
    bgClass: "wall-travertine",
    ambientLight: "rgba(240, 220, 190, 0.14)"
  }
];

// Framing options
const FRAME_STYLES = [
  {
    id: "floater-walnut",
    name: "Matte Walnut Floater",
    description: "10mm recessed shadow-line reveal with dark American walnut edge",
    class: "frame-floater-walnut"
  },
  {
    id: "museum-edge",
    name: "Museum Edge (Unframed)",
    description: "45mm continuous mineral impasto gallery wrap",
    class: "frame-museum-edge"
  },
  {
    id: "floater-steel",
    name: "Blackened Steel Floater",
    description: "Razor-thin industrial anthracite floater profile",
    class: "frame-floater-steel"
  },
  {
    id: "floater-brass",
    name: "Aged Champagne Brass",
    description: "Warm burnished metallic profile catching spotlight facets",
    class: "frame-floater-brass"
  },
  {
    id: "passe-partout",
    name: "Museum Mat & Glass",
    description: "Archival cotton rag passe-partout with natural oak box frame",
    class: "frame-passe-partout"
  }
];
