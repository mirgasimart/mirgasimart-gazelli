/**
 * MIRGASIM ART STUDIO | Interactive Curatorial Gallery Logic
 * Powers the museum hanging view, lighting physics, framing, scale visualizer,
 * in-situ interior cross-fade, and macro mineral inspection loupe.
 */

class GazelliCuratorialGallery {
  constructor() {
    this.artworks = GALLERY_DATA;
    this.currentIndex = 0;
    this.currentMode = 'gallery'; // 'gallery' | 'insitu' | 'plate' | 'macro'
    this.currentWall = 'limestone';
    this.currentFrame = 'floater-walnut';
    this.showHumanScale = true;
    this.mouseSpotlight = true;
    this.spotlightIntensity = 0.85;
    this.spotlightTemp = 2700; // Kelvin
    this.audioPlaying = false;
    this.audioCtx = null;
    this.audioOscillators = [];

    this.cacheDOM();
    this.initAudioEngine();
    this.bindEvents();
    this.renderThumbnails();
    this.initPanoramicPromenade();
    this.updateArtwork(0);
  }

  cacheDOM() {
    this.dom = {
      stage: document.getElementById('galleryStage'),
      wallBg: document.getElementById('galleryWallBg'),
      artworkMount: document.getElementById('artworkMount'),
      frameWrapper: document.getElementById('frameWrapper'),
      canvasInner: document.getElementById('canvasInner'),
      artworkImg: document.getElementById('artworkImg'),
      labelCard: document.getElementById('labelCard'),
      humanScaleFigure: document.getElementById('humanScaleFigure'),
      figureSvg: document.getElementById('figureSvg'),
      hotspotContainer: document.getElementById('hotspotContainer'),
      macroLoupe: document.getElementById('macroLoupe'),
      
      // Fullscreen alternative views
      insituView: document.getElementById('insituView'),
      insituImg: document.getElementById('insituImg'),
      insituBadge: document.getElementById('insituBadge'),
      plateView: document.getElementById('plateView'),
      plateImg: document.getElementById('plateImg'),

      // Widescreen Curatorial Wings
      triptychContainer: document.getElementById('triptychContainer'),
      wingLeft: document.getElementById('wingLeft'),
      wingRight: document.getElementById('wingRight'),
      wingInsituBtn: document.getElementById('wingInsituBtn'),
      wingInsituThumb: document.getElementById('wingInsituThumb'),
      wingNicheTag: document.getElementById('wingNicheTag'),
      wingNicheDesc: document.getElementById('wingNicheDesc'),
      wingDimension: document.getElementById('wingDimension'),
      wingLighting: document.getElementById('wingLighting'),
      wingMineralsList: document.getElementById('wingMineralsList'),
      wingChassis: document.getElementById('wingChassis'),
      wingWeight: document.getElementById('wingWeight'),
      wingCleats: document.getElementById('wingCleats'),

      // Panoramic Promenade
      panoramicPromenade: document.getElementById('panoramicPromenade'),
      panoramicTrack: document.getElementById('panoramicTrack'),
      
      // Bottom & Controls
      thumbnailStrip: document.getElementById('thumbnailStrip'),
      prevBtn: document.getElementById('prevBtn'),
      nextBtn: document.getElementById('nextBtn'),
      drawer: document.getElementById('curatorialDrawer'),
      drawerOpenBtn: document.getElementById('drawerOpenBtn'),
      drawerCloseBtn: document.getElementById('drawerCloseBtn'),
      lightingPopover: document.getElementById('lightingPopover'),
      lightingToggleBtn: document.getElementById('lightingToggleBtn'),
      audioToggleBtn: document.getElementById('audioToggleBtn'),
      scaleToggleBtn: document.getElementById('scaleToggleBtn'),
      
      // Sliders & inputs
      intensitySlider: document.getElementById('intensitySlider'),
      tempSlider: document.getElementById('tempSlider'),
      mouseSpotToggle: document.getElementById('mouseSpotToggle'),
      spotlightLayer: document.getElementById('spotlightLayer')
    };
  }

  bindEvents() {
    // Mode tabs
    document.querySelectorAll('.mode-tab').forEach(tab => {
      tab.addEventListener('click', (e) => {
        const mode = tab.dataset.mode;
        this.setMode(mode);
      });
    });

    // Navigation arrows
    this.dom.prevBtn.addEventListener('click', () => this.navigate(-1));
    this.dom.nextBtn.addEventListener('click', () => this.navigate(1));

    // Drawer toggle
    this.dom.drawerOpenBtn.addEventListener('click', () => this.toggleDrawer(true));
    this.dom.drawerCloseBtn.addEventListener('click', () => this.toggleDrawer(false));

    // Popover
    this.dom.lightingToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      this.dom.lightingPopover.classList.toggle('open');
    });

    document.addEventListener('click', (e) => {
      if (!this.dom.lightingPopover.contains(e.target) && e.target !== this.dom.lightingToggleBtn) {
        this.dom.lightingPopover.classList.remove('open');
      }
    });

    // Human scale toggle
    this.dom.scaleToggleBtn.addEventListener('click', () => {
      this.showHumanScale = !this.showHumanScale;
      this.dom.scaleToggleBtn.classList.toggle('active', this.showHumanScale);
      this.dom.humanScaleFigure.classList.toggle('visible', this.showHumanScale);
    });

    // Audio atmosphere toggle
    this.dom.audioToggleBtn.addEventListener('click', () => {
      this.toggleAudioAtmosphere();
    });

    // Lighting controls
    this.dom.intensitySlider.addEventListener('input', (e) => {
      this.spotlightIntensity = parseFloat(e.target.value);
      this.updateLightingPhysics();
    });

    this.dom.tempSlider.addEventListener('input', (e) => {
      this.spotlightTemp = parseInt(e.target.value);
      this.updateLightingPhysics();
    });

    this.dom.mouseSpotToggle.addEventListener('change', (e) => {
      this.mouseSpotlight = e.target.checked;
    });

    // Interactive mouse move for spotlight and loupe
    this.dom.stage.addEventListener('mousemove', (e) => this.handleMouseMove(e));
    this.dom.stage.addEventListener('mouseleave', () => this.handleMouseLeave());

    // Wall texture buttons
    document.querySelectorAll('[data-wall]').forEach(btn => {
      btn.addEventListener('click', () => {
        this.setWall(btn.dataset.wall);
        document.querySelectorAll('[data-wall]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });

    // Frame style buttons
    document.querySelectorAll('[data-frame]').forEach(btn => {
      btn.addEventListener('click', () => {
        this.setFrame(btn.dataset.frame);
        document.querySelectorAll('[data-frame]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => this.handleKeyboard(e));

    // In-situ preview button in left wing
    if (this.dom.wingInsituBtn) {
      this.dom.wingInsituBtn.addEventListener('click', () => this.setMode('insitu'));
    }

    // Resize handler to recalculate real-world scale
    window.addEventListener('resize', () => this.applyProportionalDimensions());
  }

  renderThumbnails() {
    this.dom.thumbnailStrip.innerHTML = '';
    this.artworks.forEach((art, index) => {
      const item = document.createElement('div');
      item.className = `thumb-item ${index === this.currentIndex ? 'active' : ''}`;
      item.dataset.index = index;
      item.innerHTML = `
        <img src="${art.images.clean}" alt="${art.title}" loading="lazy">
        <span class="thumb-number">${art.number}</span>
      `;
      item.addEventListener('click', () => this.updateArtwork(index));
      this.dom.thumbnailStrip.appendChild(item);
    });
  }

  updateArtwork(index) {
    this.currentIndex = index;
    const art = this.artworks[index];

    // Highlight thumbnail
    document.querySelectorAll('.thumb-item').forEach((thumb, i) => {
      thumb.classList.toggle('active', i === index);
    });

    // Scroll thumbnail into view
    const activeThumb = this.dom.thumbnailStrip.children[index];
    if (activeThumb) {
      activeThumb.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }

    // Update main image with smooth fade
    this.dom.artworkMount.style.opacity = '0';
    setTimeout(() => {
      this.dom.artworkImg.src = art.images.clean;
      this.dom.insituImg.src = art.images.insitu;
      this.dom.plateImg.src = art.images.plate;
      this.dom.insituBadge.textContent = `Architectural Placement: ${art.niche}`;

      this.applyProportionalDimensions();
      this.updatePlacardLabel();
      this.updateWidescreenWings(art);
      this.renderHotspots();
      this.updateDrawerContent();

      this.dom.artworkMount.style.opacity = '1';
    }, 200);
  }

  updateWidescreenWings(art) {
    if (!this.dom.wingLeft || !this.dom.wingRight) return;

    // Update Left Wing (Architectural Niche Context)
    this.dom.wingNicheTag.textContent = `Plate ${art.number}`;
    this.dom.wingInsituThumb.src = art.images.insitu;
    this.dom.wingNicheDesc.textContent = art.niche;
    this.dom.wingDimension.textContent = art.dimensions;
    this.dom.wingLighting.textContent = art.turnkeySpecs.lighting.split('(')[0].trim();

    // Update Right Wing (Absheron Geological Minerals & Specs)
    this.dom.wingMineralsList.innerHTML = '';
    art.minerals.forEach(min => {
      const item = document.createElement('div');
      item.className = 'wing-mineral-item';
      item.innerHTML = `
        <div class="wing-mineral-name">${min.name}</div>
        <div class="wing-mineral-sub">${min.description.slice(0, 85)}...</div>
      `;
      this.dom.wingMineralsList.appendChild(item);
    });

    this.dom.wingChassis.textContent = art.turnkeySpecs.chassis.split('with')[0].trim();
    this.dom.wingWeight.textContent = art.turnkeySpecs.weight;
    this.dom.wingCleats.textContent = art.turnkeySpecs.mounting.split('(')[0].trim();
  }

  initPanoramicPromenade() {
    if (!this.dom.panoramicTrack) return;
    this.dom.panoramicTrack.innerHTML = '';

    // Standard human scale figure in panoramic promenade
    const baseHeight = 360; // px reference for tall works

    this.artworks.forEach((art, index) => {
      const station = document.createElement('div');
      station.className = `promenade-station ${index === this.currentIndex ? 'active' : ''}`;
      station.dataset.index = index;

      // Real scale proportional height & width for panoramic promenade
      const pxPerCm = 1.9;
      const w = Math.round(art.widthCm * pxPerCm);
      const h = Math.round(art.heightCm * pxPerCm);

      station.innerHTML = `
        <div class="promenade-light-cone"></div>
        <div class="promenade-frame frame-floater-walnut">
          <img src="${art.images.clean}" alt="${art.title}" style="width: ${w}px; height: ${h}px; object-fit: cover; display: block;">
        </div>
        <div class="promenade-label">
          <div class="promenade-title">${art.title}</div>
          <div class="promenade-meta">${art.genre}</div>
          <div class="promenade-dim">${art.dimensions}</div>
        </div>
      `;

      station.addEventListener('click', () => {
        this.updateArtwork(index);
        this.setMode('gallery');
      });

      this.dom.panoramicTrack.appendChild(station);
    });

    // Horizontal wheel scroll support
    this.dom.panoramicPromenade.addEventListener('wheel', (e) => {
      if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
        this.dom.panoramicPromenade.scrollLeft += e.deltaY;
        e.preventDefault();
      }
    }, { passive: false });
  }

  applyProportionalDimensions() {
    const art = this.artworks[this.currentIndex];
    
    // Scale reference: map cm to screen pixels proportionally
    // Maximum canvas bounds based on stage height/width
    const stageH = this.dom.stage.clientHeight - 190; // room for track light and floor
    const stageW = this.dom.stage.clientWidth - 320; // room for placard & scale figure

    // Physical reference: Largest artwork is Plate 03 (200cm tall) or Plate 01 (185cm wide)
    // Scale factor: pixels per cm
    const scaleFactorByHeight = Math.min(stageH / 210, 2.7);
    const scaleFactorByWidth = Math.min(stageW / 210, 2.7);
    const pxPerCm = Math.max(Math.min(scaleFactorByHeight, scaleFactorByWidth), 1.6);

    const targetWidth = Math.round(art.widthCm * pxPerCm);
    const targetHeight = Math.round(art.heightCm * pxPerCm);

    this.dom.canvasInner.style.width = `${targetWidth}px`;
    this.dom.canvasInner.style.height = `${targetHeight}px`;

    // Position & Scale the 175cm Human Figure
    const humanHeightPx = Math.round(175 * pxPerCm);
    this.dom.figureSvg.style.height = `${humanHeightPx}px`;
    this.dom.figureSvg.style.width = 'auto';

    // Position human silhouette standing on floor slightly to the left of the artwork
    const figureOffsetX = -(targetWidth / 2 + 75);
    this.dom.humanScaleFigure.style.transform = `translateX(${figureOffsetX}px)`;
    this.dom.humanScaleFigure.classList.toggle('visible', this.showHumanScale);

    // Position Placard card to the bottom right of the canvas
    const placardOffsetX = (targetWidth / 2 + 30);
    this.dom.labelCard.style.right = `${-placardOffsetX}px`;
  }

  updatePlacardLabel() {
    const art = this.artworks[this.currentIndex];
    this.dom.labelCard.innerHTML = `
      <div class="label-artist">Mirgasim Art Studio</div>
      <div class="label-title">${art.title}</div>
      <div class="label-meta">${art.genre}</div>
      <div class="label-meta">${art.minerals[0].name} on Canvas</div>
      <div class="label-dim">${art.dimensions}</div>
    `;
  }

  renderHotspots() {
    this.dom.hotspotContainer.innerHTML = '';
    const art = this.artworks[this.currentIndex];

    if (!art.hotspots || this.currentMode !== 'gallery') return;

    art.hotspots.forEach(spot => {
      const el = document.createElement('div');
      el.className = 'tactile-hotspot';
      el.style.left = `${spot.x}%`;
      el.style.top = `${spot.y}%`;
      el.innerHTML = `
        <div class="hotspot-pulse"></div>
        <div class="hotspot-dot"></div>
        <div class="hotspot-tooltip">
          <div class="tooltip-title">${spot.label}</div>
          <div class="tooltip-desc">${spot.desc}</div>
        </div>
      `;
      this.dom.hotspotContainer.appendChild(el);
    });
  }

  setMode(mode) {
    this.currentMode = mode;

    document.querySelectorAll('.mode-tab').forEach(tab => {
      tab.classList.toggle('active', tab.dataset.mode === mode);
    });

    // Reset views
    if (this.dom.triptychContainer) this.dom.triptychContainer.style.display = 'none';
    this.dom.artworkMount.style.display = 'none';
    if (this.dom.humanScaleFigure) this.dom.humanScaleFigure.style.display = 'none';
    this.dom.insituView.classList.remove('active');
    this.dom.plateView.classList.remove('active');
    this.dom.macroLoupe.style.display = 'none';
    if (this.dom.panoramicPromenade) {
      this.dom.panoramicPromenade.classList.remove('active');
    }

    if (mode === 'gallery') {
      if (this.dom.triptychContainer) this.dom.triptychContainer.style.display = 'flex';
      this.dom.artworkMount.style.display = 'flex';
      if (this.dom.humanScaleFigure) this.dom.humanScaleFigure.style.display = 'flex';
      this.renderHotspots();
    } else if (mode === 'panoramic') {
      if (this.dom.panoramicPromenade) {
        this.dom.panoramicPromenade.classList.add('active');
      }
    } else if (mode === 'insitu') {
      this.dom.insituView.classList.add('active');
    } else if (mode === 'plate') {
      this.dom.plateView.classList.add('active');
    } else if (mode === 'macro') {
      if (this.dom.triptychContainer) this.dom.triptychContainer.style.display = 'flex';
      this.dom.artworkMount.style.display = 'flex';
      this.dom.hotspotContainer.innerHTML = ''; // clear hotspots in loupe mode
    }
  }

  setWall(wallId) {
    this.currentWall = wallId;
    const surface = WALL_SURFACES.find(w => w.id === wallId);
    if (!surface) return;

    this.dom.wallBg.className = `gallery-wall-bg ${surface.bgClass}`;
    this.updateLightingPhysics();
  }

  setFrame(frameId) {
    this.currentFrame = frameId;
    const style = FRAME_STYLES.find(f => f.id === frameId);
    if (!style) return;

    this.dom.frameWrapper.className = `frame-wrapper ${style.class}`;
  }

  navigate(dir) {
    let newIndex = this.currentIndex + dir;
    if (newIndex < 0) newIndex = this.artworks.length - 1;
    if (newIndex >= this.artworks.length) newIndex = 0;
    this.updateArtwork(newIndex);
  }

  toggleDrawer(open) {
    this.dom.drawer.classList.toggle('open', open);
  }

  updateDrawerContent() {
    const art = this.artworks[this.currentIndex];

    document.getElementById('drawerNumber').textContent = `PLATE ${art.number} OF ${this.artworks.length}`;
    document.getElementById('drawerTitle').textContent = art.title;
    document.getElementById('drawerAzTitle').textContent = art.azTitle;
    document.getElementById('drawerDimensions').textContent = art.dimensions;
    document.getElementById('drawerNiche').textContent = art.niche;
    document.getElementById('drawerCuratorial').textContent = art.curatorialNarrative;
    document.getElementById('drawerTaxonomy').textContent = `${art.endemicFocus} — ${art.scientificTaxonomy}`;

    // Minerals cards
    const mineralsContainer = document.getElementById('drawerMinerals');
    mineralsContainer.innerHTML = '';
    art.minerals.forEach(min => {
      const card = document.createElement('div');
      card.className = 'mineral-card';
      card.innerHTML = `
        <div class="mineral-title">${min.name}</div>
        <div class="mineral-desc">${min.description}</div>
      `;
      mineralsContainer.appendChild(card);
    });

    // Specifications
    document.getElementById('specWeight').textContent = art.turnkeySpecs.weight;
    document.getElementById('specChassis').textContent = art.turnkeySpecs.chassis;
    document.getElementById('specMounting').textContent = art.turnkeySpecs.mounting;
    document.getElementById('specLighting').textContent = art.turnkeySpecs.lighting;
    document.getElementById('specEdge').textContent = art.turnkeySpecs.edgeFinish;
  }

  handleMouseMove(e) {
    const stageRect = this.dom.stage.getBoundingClientRect();
    const mouseX = e.clientX - stageRect.left;
    const mouseY = e.clientY - stageRect.top;

    // Dynamic Spotlight following cursor
    if (this.mouseSpotlight && this.currentMode === 'gallery') {
      const pctX = ((mouseX / stageRect.width) * 100).toFixed(1);
      const pctY = ((mouseY / stageRect.height) * 100).toFixed(1);
      document.documentElement.style.setProperty('--spotlight-x', `${pctX}%`);
      document.documentElement.style.setProperty('--spotlight-y', `${pctY}%`);
    }

    // Macro Loupe Magnifier
    if (this.currentMode === 'macro') {
      const canvasRect = this.dom.canvasInner.getBoundingClientRect();
      const inCanvas = (
        e.clientX >= canvasRect.left &&
        e.clientX <= canvasRect.right &&
        e.clientY >= canvasRect.top &&
        e.clientY <= canvasRect.bottom
      );

      if (inCanvas) {
        this.dom.macroLoupe.style.display = 'block';
        this.dom.macroLoupe.style.left = `${e.clientX - 100}px`;
        this.dom.macroLoupe.style.top = `${e.clientY - 100}px`;

        const relX = (e.clientX - canvasRect.left) / canvasRect.width;
        const relY = (e.clientY - canvasRect.top) / canvasRect.height;
        const art = this.artworks[this.currentIndex];

        this.dom.macroLoupe.style.backgroundImage = `url("${art.images.clean}")`;
        const zoom = 2.6;
        this.dom.macroLoupe.style.backgroundSize = `${canvasRect.width * zoom}px ${canvasRect.height * zoom}px`;
        this.dom.macroLoupe.style.backgroundPosition = `${-((relX * canvasRect.width * zoom) - 100)}px ${-((relY * canvasRect.height * zoom) - 100)}px`;
      } else {
        this.dom.macroLoupe.style.display = 'none';
      }
    }
  }

  handleMouseLeave() {
    if (this.dom.macroLoupe) {
      this.dom.macroLoupe.style.display = 'none';
    }
    // Return spotlight to center artwork position
    document.documentElement.style.setProperty('--spotlight-x', `50%`);
    document.documentElement.style.setProperty('--spotlight-y', `38%`);
  }

  updateLightingPhysics() {
    document.documentElement.style.setProperty('--spotlight-intensity', this.spotlightIntensity);

    // Kelvin to RGB conversion approximation
    let colorHex = '#fff4e6';
    if (this.spotlightTemp <= 2800) {
      colorHex = '#ffdfba'; // Warm Tungsten 2700K
    } else if (this.spotlightTemp <= 3400) {
      colorHex = '#fff1e0'; // Warm White 3000K
    } else {
      colorHex = '#f0f5ff'; // Daylight 4500K
    }
    document.documentElement.style.setProperty('--spotlight-temp', colorHex);
  }

  initAudioEngine() {
    // Generates procedural subtle gallery acoustics and low Caspian mineral drone via Web Audio API
    // Zero external audio files required!
  }

  toggleAudioAtmosphere() {
    if (!this.audioCtx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.audioCtx = new AudioCtx();
    }

    if (this.audioPlaying) {
      // Mute / stop
      if (this.audioGain) {
        this.audioGain.gain.exponentialRampToValueAtTime(0.0001, this.audioCtx.currentTime + 0.8);
      }
      this.audioPlaying = false;
      this.dom.audioToggleBtn.classList.remove('active');
    } else {
      // Resume / start sound
      if (this.audioCtx.state === 'suspended') {
        this.audioCtx.resume();
      }

      this.audioGain = this.audioCtx.createGain();
      this.audioGain.gain.setValueAtTime(0.001, this.audioCtx.currentTime);
      this.audioGain.gain.exponentialRampToValueAtTime(0.04, this.audioCtx.currentTime + 1.2);
      this.audioGain.connect(this.audioCtx.destination);

      // Low Caspian depth drone (55 Hz fundamental + 110 Hz harmonic with subtle beating)
      const osc1 = this.audioCtx.createOscillator();
      const osc2 = this.audioCtx.createOscillator();
      osc1.type = 'sine';
      osc1.frequency.setValueAtTime(55, this.audioCtx.currentTime);
      osc2.type = 'sine';
      osc2.frequency.setValueAtTime(110.4, this.audioCtx.currentTime);

      const filter = this.audioCtx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(180, this.audioCtx.currentTime);

      osc1.connect(filter);
      osc2.connect(filter);
      filter.connect(this.audioGain);

      osc1.start();
      osc2.start();

      this.audioOscillators = [osc1, osc2];
      this.audioPlaying = true;
      this.dom.audioToggleBtn.classList.add('active');
    }
  }

  handleKeyboard(e) {
    if (e.target.tagName === 'INPUT') return;

    switch (e.key) {
      case 'ArrowLeft':
        this.navigate(-1);
        break;
      case 'ArrowRight':
        this.navigate(1);
        break;
      case 's':
      case 'S':
        this.dom.scaleToggleBtn.click();
        break;
      case 'i':
      case 'I':
        this.toggleDrawer(!this.dom.drawer.classList.contains('open'));
        break;
      case 'm':
      case 'M':
        this.setMode(this.currentMode === 'macro' ? 'gallery' : 'macro');
        break;
      case 'f':
      case 'F':
        // Cycle frame
        const nextFrameIdx = (FRAME_STYLES.findIndex(f => f.id === this.currentFrame) + 1) % FRAME_STYLES.length;
        const nextFrame = FRAME_STYLES[nextFrameIdx].id;
        this.setFrame(nextFrame);
        document.querySelectorAll('[data-frame]').forEach(b => b.classList.toggle('active', b.dataset.frame === nextFrame));
        break;
      case 'w':
      case 'W':
        // Cycle wall
        const nextWallIdx = (WALL_SURFACES.findIndex(w => w.id === this.currentWall) + 1) % WALL_SURFACES.length;
        const nextWall = WALL_SURFACES[nextWallIdx].id;
        this.setWall(nextWall);
        document.querySelectorAll('[data-wall]').forEach(b => b.classList.toggle('active', b.dataset.wall === nextWall));
        break;
      case '1':
      case '2':
      case '3':
      case '4':
      case '5':
      case '6':
        const num = parseInt(e.key) - 1;
        if (num >= 0 && num < this.artworks.length) {
          this.updateArtwork(num);
        }
        break;
      case 'Escape':
        this.toggleDrawer(false);
        this.dom.lightingPopover.classList.remove('open');
        break;
    }
  }
}

// Initialize gallery on window load
window.addEventListener('DOMContentLoaded', () => {
  window.gallery = new GazelliCuratorialGallery();
});
