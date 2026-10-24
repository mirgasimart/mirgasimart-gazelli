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
    title: "Pink Moon",
    azTitle: "Çəhrayı Ay",
    ruTitle: "Розовая Луна",
    genre: "Pure Mineral Abstraction / Lacustrine Strata Painting",
    widthCm: 130,
    heightCm: 100,
    dimensions: "130 × 100 cm (51.2 × 39.4 in)",
    orientation: "horizontal",
    niche: "Executive Boardroom / Presidential Suite / Coastal Wellness Reception",
    endemicFocus: "Absheron Lacustrine Strata (Pure geological meditation; zero figures, zero fauna, zero carpets)",
    scientificTaxonomy: "Artemia salina / Saline micro-algal Dunaliella salina mineral salts",
    minerals: [
      {
        name: "Genuine Masazir Pink Lake Salt",
        description: "Raw crystalline lake salt encrustations embedded directly into the impasto ground, catching ambient light."
      },
      {
        name: "Textured Paste & Heavy Impasto",
        description: "High-relief textural modeling sculpted with palette knife."
      },
      {
        name: "Oil Paint on Canvas",
        description: "Translucent layered oil glazes creating delicate atmospheric gradients."
      }
    ],
    curatorialNarrative: "Where saline water turns to rose mist at dawn. Thick crystalline salt sculpted by the palette knife, holding the silent breath of an ancient Caspian morning before humankind had a name for time.",
    azCuratorial: "Səhər şəfəqində duzlu suların çəhrayı dumana çevrildiyi məkan. İnsan hələ zamana ad verməmişdən əvvəl qədim Xəzər sübhünün səssiz nəfəsini saxlayan, palitrası ilə yonulmuş Masazır gölünün qalın kristalları.",
    ruCuratorial: "Там, где соленая вода на рассвете обращается в розовый туман. Кристаллы соли Масазыра, вылепленные мастихином, хранят дыхание древнего Каспийского утра до того, как человек дал имя времени.",
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
    ],
    variations: [
      {
        index: 0,
        number: "1",
        label: "Primary Master",
        azLabel: "Əsas Əsər",
        ruLabel: "Основной Шедевр",
        subtitle: "Atmospheric Saline Dawn • Lacustrine Gradient",
        image: "docs/output/latest/_clean/01_luminescence_of_masazir_salt_dawn.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_01_masazir_dawn.jpg",
        plate: "docs/output/latest/_exhibition_plates/plate_01_luminescence_of_masazir_salt_dawn.jpg",
        desc: "Where saline water turns to rose mist at dawn. Thick crystalline salt sculpted by the palette knife, holding the silent breath of an ancient Caspian morning.",
        hotspots: [
          { x: 32, y: 48, label: "Masazir Pink Salt Crystals", desc: "Genuine crystallized halite clusters embedded in thick oil impasto." },
          { x: 68, y: 35, label: "Atmospheric Saline Gradient", desc: "Glazed blush and dawn-rose pigments evoking geothermal lake reflections." },
          { x: 45, y: 78, label: "Incised Sgraffito Fissures", desc: "Razor-carved directional strata lines exposing the coquina limestone primer." }
        ]
      },
      {
        index: 1,
        number: "2",
        label: "Evaporite Strata",
        azLabel: "Buxarlanma Qatları",
        ruLabel: "Слои Эвапоритов",
        subtitle: "Sedimentary Salt Terraces • Sgraffito Chalk Ridge",
        image: "docs/output/latest/_studies/plate_01_variation_2_lacustrine_strata.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_01_masazir_dawn.jpg",
        plate: "docs/output/latest/_studies/plate_01_variation_2_lacustrine_strata.jpg",
        desc: "Horizontal geological sedimentary bands of Masazir lake salt and compressed coquina limestone, scored with deep razor sgraffito lines.",
        hotspots: [
          { x: 50, y: 35, label: "Horizontal Evaporite Ridge", desc: "Layered geological salt bands cured with heavy palette knife impasto." },
          { x: 25, y: 65, label: "Chalk Sgraffito Groove", desc: "Incised tectonic lines exposing the Absheron coquina limestone foundation." },
          { x: 75, y: 55, label: "Saline Blush Glaze", desc: "Dunaliella salina micro-algae organic pigments locked in cold wax medium." }
        ]
      },
      {
        index: 2,
        number: "3",
        label: "Halite Crust",
        azLabel: "Qalit Qabığı",
        ruLabel: "Галитовая Корка",
        subtitle: "Heavy Sculptural Relief • High-Texture Encrustation",
        image: "docs/output/latest/_studies/plate_01_variation_3_halite_crystallization.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_01_masazir_dawn.jpg",
        plate: "docs/output/latest/_studies/plate_01_variation_3_halite_crystallization.jpg",
        desc: "Monumental clusters of genuine crystallized halite mineral encrusted directly into heavy textured impasto paste catching ambient gallery lighting.",
        hotspots: [
          { x: 40, y: 50, label: "Macro Halite Clusters", desc: "Sculptural crystalline lake salt encrustations projecting 8mm off canvas." },
          { x: 65, y: 30, label: "Saline Craquelure Bed", desc: "Dry lake-bed contraction cracks formed during natural solar evaporation." },
          { x: 30, y: 75, label: "Rose Quartz Impasto", desc: "Coarse Absheron beach quartz sand blended into dawn-tinted oil paste." }
        ]
      }
    ]
  },
  {
    id: "plate-02",
    number: "02",
    roman: "II",
    title: "Across the Universe",
    azTitle: "Kainat Boyu",
    ruTitle: "Сквозь Вселенную",
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
        name: "Crystalline Masazir Pink Lake Salt",
        description: "Genuine crystallized halite clusters embedded directly into the impasto crust."
      },
      {
        name: "Fine Absheron Beach Sand",
        description: "Natural quartz-shell beach sand blended into impasto for tactile friction."
      },
      {
        name: "Oil Paints & Canvas",
        description: "Artist-grade professional oil colors on stretched linen canvas."
      }
    ],
    curatorialNarrative: "Centuries of tides carved into sacred stone Shebeke geometry. Concentric rings of fossilized Caspian cockles radiate from a saline core—a celestial calendar measuring eternity in mother-of-pearl.",
    azCuratorial: "Müqəddəs daş Şəbəkə həndəsəsinə həkk olunmuş əsrlərin qabarmaları. Duzlu mərkəzdən şüalanan fosilləşmiş Didakna qabıqlarının konsentrik halqaları — sədəf içində əbədiyyəti ölçən səma təqvimi.",
    ruCuratorial: "Века приливов, запечатленные в сакральной геометрии Шебеке. Концентрические кольца ископаемых раковин Дидакна лучатся от соляного ядра — небесный календарь, отмеряющий вечность в перламутре.",
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
    ],
    variations: [
      {
        index: 0,
        number: "1",
        label: "Primary Master",
        azLabel: "Əsas Əsər",
        ruLabel: "Основной Шедевр",
        subtitle: "Sacred Stone Shebeke • Concentric Cockle Halo",
        image: "docs/output/latest/_clean/02_the_weaver_of_sunken_shells_didacna.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_02_shebeke_reliquary.jpg",
        plate: "docs/output/latest/_exhibition_plates/plate_02_the_weaver_of_sunken_shells_didacna.jpg",
        desc: "Concentric rings of fossilized Caspian cockles (Didacna) radiating from a crystalline saline core—a celestial calendar measuring eternity in mother-of-pearl.",
        hotspots: [
          { x: 50, y: 45, label: "Concentric Shebeke Reliquary", desc: "Sacred Islamic architectural stone tracery rendered in fossilized Caspian cockles." },
          { x: 35, y: 68, label: "Didacna Shell Clusters", desc: "Endemic Caspian bivalves (Didacna trigonoides) set in deep mineral relief." },
          { x: 65, y: 25, label: "Crystalline Halite Halo", desc: "Masazir lake salt encrustations catching grazing accent lighting." }
        ]
      },
      {
        index: 1,
        number: "2",
        label: "Coastal Mosaic",
        azLabel: "Sahil Mozaikası",
        ruLabel: "Прибрежная Мозаика",
        subtitle: "Radial Didacna Cluster • Beach Quartz Grit",
        image: "docs/output/latest/_studies/plate_02_variation_2_coastal_mosaic.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_02_shebeke_reliquary.jpg",
        plate: "docs/output/latest/_studies/plate_02_variation_2_coastal_mosaic.jpg",
        desc: "Dense tactile mosaic of fossilized Caspian cockles embedded in heavy Absheron beach sand and warm quarry plaster.",
        hotspots: [
          { x: 48, y: 40, label: "Fossil Shell Radial Field", desc: "Concentric rings of weathered marine cockles bound in chalk paste." },
          { x: 28, y: 60, label: "Absheron Quartz Grit", desc: "Unrefined coastal sand creating high-friction matte surface texture." },
          { x: 70, y: 50, label: "Mother-of-Pearl Aperture", desc: "Abraded nacre reflections catching ambient illumination." }
        ]
      },
      {
        index: 2,
        number: "3",
        label: "Shell Monolith",
        azLabel: "Qabıq Monoliti",
        ruLabel: "Монолит Раковин",
        subtitle: "Vertical Quarry Strata • Scored Nacre Relief",
        image: "docs/output/latest/_studies/plate_02_variation_3_shell_monolith.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_02_shebeke_reliquary.jpg",
        plate: "docs/output/latest/_studies/plate_02_variation_3_shell_monolith.jpg",
        desc: "A solitary vertical limestone stele bearing scored geometric apertures, iridescent shell fragments, and fine quartz sand impasto.",
        hotspots: [
          { x: 50, y: 35, label: "Monolithic Vertical Axis", desc: "Carved coquina stone relief evoking an ancient Baku portal stela." },
          { x: 40, y: 65, label: "Embedded Didacna Valves", desc: "Submerged marine shell valves fossilized into limestone matrix." },
          { x: 60, y: 55, label: "Scored Sgraffito Tracery", desc: "Deep geometric Shebeke fretwork incised with sculptor's chisel." }
        ]
      }
    ]
  },
  {
    id: "plate-03",
    number: "03",
    roman: "III",
    title: "Paint It Black",
    azTitle: "Qara Qızıl",
    ruTitle: "Черное Золото",
    subtitle: "Black Gold / Qara Qızıl",
    genre: "Industrial-Geological Abstraction / Hydrocarbon Matter Painting",
    widthCm: 80,
    heightCm: 100,
    dimensions: "80 × 100 cm (31.5 × 39.4 in)",
    orientation: "vertical",
    niche: "High-Traffic Transition Corridor / Executive Wall / Aviation VIP Lounge",
    endemicFocus: "Caspian Marine Shad (Alosa braschnikowi) & Sturgeon",
    scientificTaxonomy: "Alosa braschnikowi (Borodin, 1904) / Acipenser gueldenstaedtii",
    minerals: [
      {
        name: "Natural Absheron Bitumen (Binagadi & Fatmai)",
        description: "Pure unrefined asphaltite applied in viscous palette-knife impasto ridges, curing to an obsidian hydrocarbon crust."
      },
      {
        name: "Pyrite Mineral Aggregates (FeS₂)",
        description: "Irregular metallic brassy-gold sulfide crystals embedded into the dorsal scutes, catching ambient gallery lighting."
      },
      {
        name: "Oxidized 24k Gold Leaf & Limestone Ground",
        description: "Abraded precious leaf and Absheron chalk scored into the bitumen field, evoking metallurgical antiquity."
      }
    ],
    curatorialNarrative: "The earth bleeding memory. Charred derrick scaffolding drowned in raw Binagadi bitumen, where an armored marine shad gleams with subterranean pyrite above eternal gas fire. Three iterations of an unfinished industrial reckoning.",
    azCuratorial: "Yaddaşı qanayan torpaq. Qatran qara Binaqədi bitumunda batmış kömürləşmiş buruq qülləsi, burada zirehli dəniz siyənəyi əbədi qaz alovu üzərində yeraltı piritlə parıldayır. Bitməmiş sənaye hesablaşmasının üç təkrarlanması.",
    ruCuratorial: "Земля, истекающая памятью. Обугленные леса буровых вышек в вязком бинагадинском битуме, где чешуя каспийской сельди сияет золотым пиритом над вечным огнем недр. Три итерации незавершенного индустриального расплаты.",
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
    variations: [
      {
        index: 0,
        number: "1",
        label: "Primary Master",
        subtitle: "Scaffolding & Visceral Bitumen Matrix",
        image: "docs/output/latest/_clean/03_keeper_of_the_cold_depths_caspian_shad.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_03_binagadi_derrick.jpg",
        plate: "docs/output/latest/_exhibition_plates/plate_03_keeper_of_the_cold_depths_caspian_shad.jpg",
        desc: "Historic wooden oil derrick scaffolding beams slicing across visceral slabs of pitch-black Binagadi bitumen, with a golden pyrite-studded marine shad leaping above eternal subterranean gas fire.",
        hotspots: [
          { x: 42, y: 22, label: "Derrick Structural Beams", desc: "Minimalist geometric scaffolding echoing early Absheron oil derricks." },
          { x: 55, y: 52, label: "Pyrite-Studded Caspian Shad", desc: "Natural brassy pyrite flakes encrusted on Alosa braschnikowi scales." },
          { x: 48, y: 85, label: "Viscous Binagadi Bitumen", desc: "Subterranean heavy asphaltite matrix cured with archival beeswax." }
        ]
      },
      {
        index: 1,
        number: "2",
        label: "Industrial Cretti",
        subtitle: "Alberto Burri Lineage • Fault-Line Matter Painting",
        image: "docs/output/latest/_studies/plate_03_variation_2_industrial_cretti.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_03_binagadi_derrick.jpg",
        plate: "docs/output/latest/_studies/plate_03_variation_2_industrial_cretti.jpg",
        desc: "A monumental expanse of deeply cracked Lokbatan volcanic mud craquelure on raw linen, cleft by a vertical fault line of viscous, deep-relief black bitumen and embedded rusted iron plates.",
        hotspots: [
          { x: 50, y: 50, label: "Bitumen Fault Chasm", desc: "Pure deep-relief obsidian asphaltite dividing continental earth." },
          { x: 28, y: 35, label: "Volcanic Mud Cretti", desc: "Authentic shrinkage craquelure forming deep physical fissures." },
          { x: 68, y: 20, label: "Oxidized Gold Seam", desc: "Delicate veins of flaked 24k gold leaf abraded across the rift." }
        ]
      },
      {
        index: 2,
        number: "3",
        label: "Tectonic Obliteration",
        subtitle: "Anselm Kiefer Lineage • Excavated Archaeological Relic",
        image: "docs/output/latest/_studies/plate_03_variation_1_tectonic_obliteration.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_03_binagadi_derrick.jpg",
        plate: "docs/output/latest/_studies/plate_03_variation_1_tectonic_obliteration.jpg",
        desc: "Charred, splintered wooden derrick timbers and rusted iron angle-trusses crushed into the asphalt earth like an ancient industrial skeleton, with fossilized sturgeon scutes in heavy relief.",
        hotspots: [
          { x: 62, y: 30, label: "Charred Derrick Timber", desc: "Splintered wooden structural scaffolding swallowed by the earth." },
          { x: 48, y: 68, label: "Fossilized Armored Sturgeon", desc: "Prehistoric Caspian sturgeon scutes encrusted with pyrite and gold leaf." },
          { x: 22, y: 38, label: "Submerged Rig Truss", desc: "Historic wooden lattice frame sinking into the bitumen bed." }
        ]
      }
    ],
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
    title: "A Hard Day's Night",
    azTitle: "Ağır Bir Günün Gecəsi",
    ruTitle: "Вечер Трудного Дня",
    genre: "Earth-Art Vortex / Geothermal Mineral Painting",
    widthCm: 145,
    heightCm: 145,
    dimensions: "145 × 145 cm (57.1 × 57.1 in)",
    orientation: "square",
    niche: "Grand Central Atrium / Double-Height Salon / Wellness Mezzanine Feature Wall",
    endemicFocus: "Armored Caspian Tadpole Goby (Benthophilus spp.)",
    scientificTaxonomy: "Benthophilus macrocephalus / Benthophilus baeri",
    minerals: [
      {
        name: "Mud Volcano",
        description: "Authentic mud volcano clay curing into rich tactile craquelure fissures."
      },
      {
        name: "Oil Paint & Canvas",
        description: "Masterwork oil pigments and mineral glazes on heavy linen canvas."
      }
    ],
    curatorialNarrative: "The quiet exhaustion of a planet. Millions of years of subterranean pressure exhaled onto canvas—cracked volcanic clay and geothermal celadon resting in the dark stillness after eruption.",
    azCuratorial: "Bir planetin sakit yorğunluğu. Kətana sovrulmuş milyonlarla illik yeraltı təzyiq — püskürmədən sonrakı qaranlıq sükutda dincələn çatlamış vulkan gil və geotermal seladon.",
    ruCuratorial: "Тихое истощение планеты. Миллионы лет подземного давления выдохнуты на холст — потрескавшаяся глина вулкана Локбатан и геотермальный селадон в темном безмолвии после извержения.",
    turnkeySpecs: {
      chassis: "Dual-aluminum cross-braced cradled chassis",
      weight: "12.5 kg",
      mounting: "Dual heavy-duty aircraft-grade aluminum French cleats",
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
    ],
    variations: [
      {
        index: 0,
        number: "1",
        label: "Primary Master",
        azLabel: "Əsas Əsər",
        ruLabel: "Основной Шедевр",
        subtitle: "Geothermal Crater Vortex • Armored Tadpole Goby",
        image: "docs/output/latest/_clean/04_breath_of_lokbatan_tadpole_goby.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_04_breath_of_lokbatan.jpg",
        plate: "docs/output/latest/_exhibition_plates/plate_04_breath_of_lokbatan_tadpole_goby.jpg",
        desc: "The quiet exhaustion of a planet. Cracked volcanic clay and geothermal celadon swirling around the pulsating vent of Lokbatan mud volcano.",
        hotspots: [
          { x: 50, y: 50, label: "Geothermal Crater Vortex", desc: "Concentric impasto vortex evoking the pulsating throat of Lokbatan mud volcano." },
          { x: 65, y: 62, label: "Armored Benthophilus Goby", desc: "Archaic armored benthic fish adorned with raw metallic pyrite crystals." },
          { x: 28, y: 34, label: "Volcanic Clay Craquelure", desc: "Authentic mud clay dried into deep geological fractures and tactile fissures." }
        ]
      },
      {
        index: 1,
        number: "2",
        label: "Celadon Caldera",
        azLabel: "Seladon Kalderası",
        ruLabel: "Селадоновая Кальдера",
        subtitle: "Concentric Clay Eruption • Pale Celadon Mineral Glaze",
        image: "docs/output/latest/_studies/plate_04_variation_2_celadon_caldera.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_04_breath_of_lokbatan.jpg",
        plate: "docs/output/latest/_studies/plate_04_variation_2_celadon_caldera.jpg",
        desc: "Rhythmic concentric rings of drying geothermal mud and pale celadon pigment expanding outwards from the central vent.",
        hotspots: [
          { x: 48, y: 48, label: "Caldera Vent Core", desc: "Subterranean pressure epicentre modeled in thick volcanic clay." },
          { x: 72, y: 35, label: "Celadon Glaze Wash", desc: "Rare copper-iron mineral silicate washes layered over raw linen." },
          { x: 30, y: 68, label: "Desiccation Fissures", desc: "Natural evaporative shrinkage craquelure forming organic radial fractures." }
        ]
      },
      {
        index: 2,
        number: "3",
        label: "Abyssal Eruption",
        azLabel: "Abissal Püskürmə",
        ruLabel: "Абиссальное Извержение",
        subtitle: "Deep Emerald & Volcanic Ash • High-Relief Craquelure",
        image: "docs/output/latest/_studies/plate_04_variation_3_abyssal_caldera.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_04_breath_of_lokbatan.jpg",
        plate: "docs/output/latest/_studies/plate_04_variation_3_abyssal_caldera.jpg",
        desc: "Deep tectonic fissures and abyssal emerald-charcoal craquelure documenting the cooling tectonic earth in heavy tactile relief.",
        hotspots: [
          { x: 55, y: 45, label: "Tectonic Fractures", desc: "Profound 12mm deep relief fissures sculpted in polymerized mud slurry." },
          { x: 35, y: 30, label: "Volcanic Ash Glaze", desc: "Mineral ash and charcoal grounds creating dramatic light absorption." },
          { x: 60, y: 70, label: "Pyrite Inclusions", desc: "Subterranean brassy sulfide crystals gleaming amidst dark earth." }
        ]
      }
    ]
  },
  {
    id: "plate-05",
    number: "05",
    roman: "V",
    title: "Here Comes the Sun",
    azTitle: "Günəş Doğur",
    ruTitle: "Всходит Солнце",
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
        name: "Absheron Coastal Beach Sand",
        description: "Concentric rings textured with coarse raw beach sand and quartz grit."
      },
      {
        name: "Masazir Lake Salt Clusters",
        description: "Saline crystals embedded along the cyan-blue outer orbital halo."
      },
      {
        name: "Oil & Bone Plaster on Linen",
        description: "Layered artist-grade oil pigments and archival mineral plaster."
      }
    ],
    curatorialNarrative: "Twelve thousand years ago, hunters etched a boat carrying the sun across rock. An archaic Caspian lamprey loops through gold dust and beach sand, completing an eternal circle of return.",
    azCuratorial: "On iki min il əvvəl ovçular daş üzərində günəşi daşıyan qayıq həkk etdilər. Qədim Xəzər ilanbalığı qızıl tozu və çimərlik qumundan keçərək əbədi qayıdış dövrəsini tamamlayır.",
    ruCuratorial: "Двенадцать тысяч лет назад охотники высекли в скале лодку, несущую солнце. Древняя каспийская минога огибает солнечный диск из золотой пыли и песка, замыкая вечный круг возвращения.",
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
    ],
    variations: [
      {
        index: 0,
        number: "1",
        label: "Primary Master",
        azLabel: "Əsas Əsər",
        ruLabel: "Основной Шедевр",
        subtitle: "Solar Mandala & Ouroboros • Caspian Lamprey",
        image: "docs/output/latest/_clean/05_the_lampreys_vigil_caspian_lamprey.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_05_gobustan_oracle.jpg",
        plate: "docs/output/latest/_exhibition_plates/plate_05_the_lampreys_vigil_caspian_lamprey.jpg",
        desc: "Twelve thousand years ago, hunters etched a boat carrying the sun across rock. An archaic Caspian lamprey loops through gold dust and beach sand, completing an eternal circle of return.",
        hotspots: [
          { x: 50, y: 46, label: "Solar Mandala & Ouroboros", desc: "The ancient Caspian lamprey coiled into an eternal cosmic solar wheel." },
          { x: 48, y: 76, label: "Gobustan Petroglyph Sgraffito", desc: "Carved reed boat and ritual dancer figures incised in porous stone plaster." },
          { x: 26, y: 38, label: "Caspian Cyan Orbital Ring", desc: "Vibrant azure and salt mineral halo radiating from the ancient sun disk." }
        ]
      },
      {
        index: 1,
        number: "2",
        label: "Gobustan Solar Disc",
        azLabel: "Qobustan Günəş Diski",
        ruLabel: "Гобустанский Солнечный Диск",
        subtitle: "Petroglyphic Sgraffito • Cyan Orbital Halo",
        image: "docs/output/latest/_studies/plate_05_variation_2_gobustan_disc.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_05_gobustan_oracle.jpg",
        plate: "docs/output/latest/_studies/plate_05_variation_2_gobustan_disc.jpg",
        desc: "Archaic reed boat petroglyphs carved into bone plaster, surrounded by a luminous cyan-salt halo and gold dust orbit.",
        hotspots: [
          { x: 48, y: 42, label: "Solar Disc Center", desc: "Brushed 24k gold leaf and Masazir salt forming a radiant solar core." },
          { x: 68, y: 58, label: "Sgraffito Reed Boat", desc: "Ancient petroglyph silhouettes scored deeply into coarse limestone plaster." },
          { x: 30, y: 65, label: "Azure Saline Orbital", desc: "Concentric cyan-blue mineral halo reflecting Caspian seawater." }
        ]
      },
      {
        index: 2,
        number: "3",
        label: "Cosmic Wheel Totem",
        azLabel: "Kosmik Çarx Totemi",
        ruLabel: "Тотем Космического Колеса",
        subtitle: "Prehistoric Altar Stele • Concentric Sand Halos",
        image: "docs/output/latest/_studies/plate_05_variation_3_cosmic_wheel.jpg",
        insitu: "docs/output/latest/_insitu/insitu_plate_05_gobustan_oracle.jpg",
        plate: "docs/output/latest/_studies/plate_05_variation_3_cosmic_wheel.jpg",
        desc: "Deeply textured coarse beach sand and quartz grit arranged in monumental concentric solar rings around an ancient Caspian totem.",
        hotspots: [
          { x: 50, y: 48, label: "Concentric Quartz Rings", desc: "Textured beach sand bands sculpted in high relief around the central axis." },
          { x: 35, y: 32, label: "Bone Plaster Ground", desc: "Porous Absheron coquina and chalk primer cured with archival beeswax." },
          { x: 65, y: 68, label: "Archaic Totem Loop", desc: "Prehistoric Caspian aquatic totem coiled in eternal astronomical return." }
        ]
      }
    ]
  }
];

// Architectural wall surface options (Canonical 3)
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
  }
];

// Turnkey Framing options (Canonical 3)
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
  }
];

// Trilingual Dictionary (Canonical 3: English Default, Azerbaijani, Russian)
const I18N = {
  en: {
    langCode: "EN",
    langName: "English",
    brandTitle: "Absheron Tectonics",
    brandSub: "Gazelli Art House Curatorial Commission Suite",
    modes: {
      gallery: "Stage",
      panoramic: "Walk",
      macro: "Loupe"
    },
    actions: {
      scale: "Scale",
      finishes: "Finishes",
      minerals: "Minerals",
      dossier: "Dossier",
      more: "More"
    },
    placard: {
      artist: "Mirgasim Art Studio",
      year: "2026",
      dossierLink: "Curatorial Dossier & Specs ↗",
      variation: "Variation"
    },
    drawer: {
      title: "Curatorial & Technical Dossier",
      statement: "Curatorial Statement",
      anatomy: "Absheron Geological Mineral Anatomy",
      specs: "Turnkey Architectural Specifications",
      chassis: "Chassis",
      weight: "Weight",
      mounting: "Mounting",
      edgeFinish: "Edge Finish",
      lighting: "Lighting",
      niche: "Architectural Placement",
      endemic: "Endemic Ecology & Lineage",
      paletteBoxPrompt: "Physical Material Palette Box (15 × 15 cm cured plaques) available upon formal curatorial request."
    },
    popover: {
      title: "Curatorial Environment",
      intensity: "Spotlight Intensity",
      temp: "Color Temperature",
      followBeam: "Interactive Follow-Beam",
      soundscape: "Caspian Soundscape",
      soundscapeSub: "Synthesized geological atmosphere",
      insitu: "In-Situ Interior Room",
      insituSub: "Architectural placement view",
      downloadPdf: "Download Curatorial Proposal (PDF)"
    },
    finishes: {
      title: "Wall Plaster & Turnkey Framing",
      wallSurface: "Wall Plaster Surface",
      framing: "Turnkey Framing",
      variations: "Curatorial Variations",
      paletteBox: "Curatorial Material Palette Box"
    }
  },
  az: {
    langCode: "AZ",
    langName: "Azərbaycan",
    brandTitle: "Abşeron Tektonikası",
    brandSub: "Gazelli Art House Kuratorluq Sifarişi Süitası",
    modes: {
      gallery: "Səhnə",
      panoramic: "Gəzinti",
      macro: "Böyüdücü"
    },
    actions: {
      scale: "Miqyas",
      finishes: "Tərtibat",
      minerals: "Minerallar",
      dossier: "Dosye",
      more: "Daha Çox"
    },
    placard: {
      artist: "Mirqasım İncəsənət Emalatxanası",
      year: "2026",
      dossierLink: "Kurator Dosyesi və Spesifikasiyalar ↗",
      variation: "Variasiya"
    },
    drawer: {
      title: "Kurator və Texniki Dosye",
      statement: "Kurator Bəyanatı",
      anatomy: "Abşeron Geoloji Mineral Anatomiyası",
      specs: "Memarlıq və Quraşdırma Spesifikasiyaları",
      chassis: "Şassi",
      weight: "Çəki",
      mounting: "Montaj",
      edgeFinish: "Kənar Tərtibatı",
      lighting: "İşıqlandırma",
      niche: "Memarlıq Məkanı",
      endemic: "Endemik Ekologiya və İrs",
      paletteBoxPrompt: "Fiziki Material Qutusu (15 × 15 sm nümunə lövhələri) rəsmi kurator sorğusu ilə təqdim olunur."
    },
    popover: {
      title: "Mühit Tənzimləmələri",
      intensity: "Projektor İntensivliyi",
      temp: "Rəng Hərarəti",
      followBeam: "İnteraktiv İşıq Şüası",
      soundscape: "Xəzər Səs Mənzərəsi",
      soundscapeSub: "Sintez edilmiş geoloji atmosfer",
      insitu: "İnteryer Baxışı",
      insituSub: "Memarlıq yerləşdirmə görünüşü",
      downloadPdf: "Təklif Kataloqunu Yüklə (PDF)"
    },
    finishes: {
      title: "Divar Suvağı və Çərçivə Tərtibatı",
      wallSurface: "Divar Səthi",
      framing: "Çərçivə",
      variations: "Müəllif Variasiyaları",
      paletteBox: "Fiziki Material Nümunələri"
    }
  },
  ru: {
    langCode: "RU",
    langName: "Русский",
    brandTitle: "Тектоника Апшерона",
    brandSub: "Кураторская Сюита для Gazelli Art House",
    modes: {
      gallery: "Сцена",
      panoramic: "Галерея",
      macro: "Лупа"
    },
    actions: {
      scale: "Масштаб",
      finishes: "Отделка",
      minerals: "Минералы",
      dossier: "Досье",
      more: "Еще"
    },
    placard: {
      artist: "Арт-Студия Миргасим",
      year: "2026",
      dossierLink: "Кураторское Досье и Спецификации ↗",
      variation: "Вариация"
    },
    drawer: {
      title: "Кураторское и Техническое Досье",
      statement: "Кураторское Описание",
      anatomy: "Геологическая Анатомия Минералов",
      specs: "Архитектурные Спецификации Под Ключ",
      chassis: "Подрамник",
      weight: "Вес",
      mounting: "Крепление",
      edgeFinish: "Обработка Края",
      lighting: "Освещение",
      niche: "Архитектурное Размещение",
      endemic: "Эндемическая Экология и Линия",
      paletteBoxPrompt: "Физический бокс с образцами минералов (плитки 15 × 15 см) доступен по кураторскому запросу."
    },
    popover: {
      title: "Кураторская Среда",
      intensity: "Яркость Спотлайта",
      temp: "Цветовая Температура",
      followBeam: "Интерактивный Луч",
      soundscape: "Звуки Каспия",
      soundscapeSub: "Синтезированная геологическая атмосфера",
      insitu: "Интерьер In-Situ",
      insituSub: "Архитектурное размещение",
      downloadPdf: "Скачать Каталог Предложения (PDF)"
    },
    finishes: {
      title: "Штукатурка Стен и Обрамление",
      wallSurface: "Поверхность Стены",
      framing: "Обрамление",
      variations: "Кураторские Вариации",
      paletteBox: "Бокс с Образцами Материалов"
    }
  }
};

window.GALLERY_DATA = GALLERY_DATA;
window.WALL_SURFACES = WALL_SURFACES;
window.FRAME_STYLES = FRAME_STYLES;
window.I18N = I18N;
