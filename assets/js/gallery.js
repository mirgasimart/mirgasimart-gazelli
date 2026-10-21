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
    this.wingCollapsed = false;
    this.pullReady = false;

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

      // Mobile Pull-to-Refresh Indicator
      pullIndicator: document.getElementById('pullRefreshIndicator'),
      pullText: document.getElementById('pullRefreshText'),

      // Widescreen Curatorial Wings
      triptychContainer: document.getElementById('triptychContainer'),
      wingLeft: document.getElementById('wingLeft'),
      wingRight: document.getElementById('wingRight'),
      wingToggleBtn: document.getElementById('wingToggleBtn'),
      wingCollapseBtn: document.getElementById('wingCollapseBtn'),
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
      lightingCloseBtn: document.getElementById('lightingCloseBtn'),
      audioToggleBtn: document.getElementById('audioToggleBtn'),
      scaleToggleBtn: document.getElementById('scaleToggleBtn'),
      
      // Mobile Customizer Bottom Sheet
      mobileCustomizerTrigger: document.getElementById('mobileCustomizerTrigger'),
      mobileCustomizerSheet: document.getElementById('mobileCustomizerSheet'),
      customizerCloseBtn: document.getElementById('customizerCloseBtn'),
      customizerBackdrop: document.getElementById('customizerBackdrop'),
      mobileScaleSwitch: document.getElementById('mobileScaleSwitch'),
      mobileAudioSwitch: document.getElementById('mobileAudioSwitch'),
      mobileIntensitySlider: document.getElementById('mobileIntensitySlider'),
      mobileIntensityVal: document.getElementById('mobileIntensityVal'),
      mobileTempSlider: document.getElementById('mobileTempSlider'),
      mobileTempVal: document.getElementById('mobileTempVal'),

      // Sliders & inputs
      intensitySlider: document.getElementById('intensitySlider'),
      tempSlider: document.getElementById('tempSlider'),
      mouseSpotToggle: document.getElementById('mouseSpotToggle'),
      spotlightLayer: document.getElementById('spotlightLayer')
    };
  }

  bindEvents() {
    // Mode tabs (Desktop and Mobile)
    document.querySelectorAll('.mode-tab').forEach(tab => {
      tab.addEventListener('click', () => {
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

    // Popover toggle (Lighting controls)
    this.dom.lightingToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      this.dom.lightingPopover.classList.toggle('open');
    });

    if (this.dom.lightingCloseBtn) {
      this.dom.lightingCloseBtn.addEventListener('click', () => {
        this.dom.lightingPopover.classList.remove('open');
      });
    }

    document.addEventListener('click', (e) => {
      if (!this.dom.lightingPopover.contains(e.target) && e.target !== this.dom.lightingToggleBtn) {
        this.dom.lightingPopover.classList.remove('open');
      }
    });

    // Mobile Customizer Bottom Sheet events
    if (this.dom.mobileCustomizerTrigger) {
      this.dom.mobileCustomizerTrigger.addEventListener('click', () => {
        this.toggleMobileCustomizer(true);
      });
    }
    if (this.dom.customizerCloseBtn) {
      this.dom.customizerCloseBtn.addEventListener('click', () => {
        this.toggleMobileCustomizer(false);
      });
    }
    if (this.dom.customizerBackdrop) {
      this.dom.customizerBackdrop.addEventListener('click', () => {
        this.toggleMobileCustomizer(false);
      });
    }

    // Human scale toggle (desktop button)
    this.dom.scaleToggleBtn.addEventListener('click', () => {
      this.showHumanScale = !this.showHumanScale;
      this.dom.scaleToggleBtn.classList.toggle('active', this.showHumanScale);
      if (this.dom.mobileScaleSwitch) {
        this.dom.mobileScaleSwitch.classList.toggle('active', this.showHumanScale);
        this.dom.mobileScaleSwitch.textContent = this.showHumanScale ? 'ON' : 'OFF';
      }
      this.dom.humanScaleFigure.classList.toggle('visible', this.showHumanScale);
    });

    // Mobile Scale Switch
    if (this.dom.mobileScaleSwitch) {
      this.dom.mobileScaleSwitch.addEventListener('click', () => {
        this.showHumanScale = !this.showHumanScale;
        this.dom.mobileScaleSwitch.classList.toggle('active', this.showHumanScale);
        this.dom.mobileScaleSwitch.textContent = this.showHumanScale ? 'ON' : 'OFF';
        this.dom.scaleToggleBtn.classList.toggle('active', this.showHumanScale);
        this.dom.humanScaleFigure.classList.toggle('visible', this.showHumanScale);
      });
    }

    // Audio atmosphere toggle
    this.dom.audioToggleBtn.addEventListener('click', () => {
      this.toggleAudioAtmosphere();
      if (this.dom.mobileAudioSwitch) {
        this.dom.mobileAudioSwitch.classList.toggle('active', this.audioPlaying);
        this.dom.mobileAudioSwitch.textContent = this.audioPlaying ? 'ON' : 'OFF';
      }
    });

    if (this.dom.mobileAudioSwitch) {
      this.dom.mobileAudioSwitch.addEventListener('click', () => {
        this.toggleAudioAtmosphere();
        this.dom.mobileAudioSwitch.classList.toggle('active', this.audioPlaying);
        this.dom.mobileAudioSwitch.textContent = this.audioPlaying ? 'ON' : 'OFF';
      });
    }

    // Lighting controls (Desktop sliders)
    this.dom.intensitySlider.addEventListener('input', (e) => {
      this.spotlightIntensity = parseFloat(e.target.value);
      const pct = Math.round(this.spotlightIntensity * 100);
      document.getElementById('intensityVal').textContent = `${pct}%`;
      if (this.dom.mobileIntensityVal) this.dom.mobileIntensityVal.textContent = `${pct}%`;
      if (this.dom.mobileIntensitySlider) this.dom.mobileIntensitySlider.value = e.target.value;
      this.updateLightingPhysics();
    });

    this.dom.tempSlider.addEventListener('input', (e) => {
      this.spotlightTemp = parseInt(e.target.value);
      const label = this.spotlightTemp <= 2800 ? '2700K (Warm Gallery)' : this.spotlightTemp <= 3400 ? '3200K (Neutral White)' : '4200K (Cool Daylight)';
      document.getElementById('tempVal').textContent = label;
      if (this.dom.mobileTempVal) this.dom.mobileTempVal.textContent = label;
      if (this.dom.mobileTempSlider) this.dom.mobileTempSlider.value = e.target.value;
      this.updateLightingPhysics();
    });

    // Mobile sliders syncing with desktop
    if (this.dom.mobileIntensitySlider) {
      this.dom.mobileIntensitySlider.addEventListener('input', (e) => {
        this.spotlightIntensity = parseFloat(e.target.value);
        this.dom.intensitySlider.value = e.target.value;
        const pct = Math.round(this.spotlightIntensity * 100);
        document.getElementById('intensityVal').textContent = `${pct}%`;
        if (this.dom.mobileIntensityVal) this.dom.mobileIntensityVal.textContent = `${pct}%`;
        this.updateLightingPhysics();
      });
    }

    if (this.dom.mobileTempSlider) {
      this.dom.mobileTempSlider.addEventListener('input', (e) => {
        this.spotlightTemp = parseInt(e.target.value);
        this.dom.tempSlider.value = e.target.value;
        const label = this.spotlightTemp <= 2800 ? '2700K (Warm Gallery)' : this.spotlightTemp <= 3400 ? '3200K (Neutral White)' : '4200K (Cool Daylight)';
        document.getElementById('tempVal').textContent = label;
        if (this.dom.mobileTempVal) this.dom.mobileTempVal.textContent = label;
        this.updateLightingPhysics();
      });
    }

    this.dom.mouseSpotToggle.addEventListener('change', (e) => {
      this.mouseSpotlight = e.target.checked;
    });

    // Interactive mouse move for spotlight and loupe
    this.dom.stage.addEventListener('mousemove', (e) => this.handleMouseMove(e));
    this.dom.stage.addEventListener('mouseleave', () => this.handleMouseLeave());

    // Geological Anatomy Wing Toggle
    if (this.dom.wingToggleBtn) {
      this.dom.wingToggleBtn.addEventListener('click', () => this.toggleWing());
    }
    if (this.dom.wingCollapseBtn) {
      this.dom.wingCollapseBtn.addEventListener('click', () => this.toggleWing(true));
    }

    // Native Touch Gestures: Horizontal Artwork Swipe & Pull-to-Refresh
    let touchStartX = 0;
    let touchStartY = 0;
    let touchStartTime = 0;
    let isTouchActive = false;
    let isPullRefreshing = false;
    let lastTapTime = 0;

    // Double-tap on canvas to quickly toggle between Gallery and In-Situ Interior
    if (this.dom.canvasInner) {
      this.dom.canvasInner.addEventListener('touchend', (e) => {
        const currentTime = Date.now();
        const tapGap = currentTime - lastTapTime;
        if (tapGap < 320 && tapGap > 40) {
          this.setMode(this.currentMode === 'insitu' ? 'gallery' : 'insitu');
          e.preventDefault();
        }
        lastTapTime = currentTime;
      });
    }

    const appEl = document.querySelector('.app-container') || this.dom.stage;

    appEl.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        touchStartTime = Date.now();
        isTouchActive = true;
        isPullRefreshing = false;
        this.pullReady = false;

        if (this.currentMode === 'macro') {
          this.handleTouchLoupe(e.touches[0]);
        }
      }
    }, { passive: true });

    appEl.addEventListener('touchmove', (e) => {
      if (!isTouchActive || e.touches.length !== 1) return;
      if (this.currentMode === 'macro') {
        this.handleTouchLoupe(e.touches[0]);
        return;
      }

      // If drawer or customizer sheet is open, allow standard vertical scrolling inside them
      const isDrawerOpen = this.dom.drawer && this.dom.drawer.classList.contains('open');
      const isSheetOpen = this.dom.mobileCustomizerSheet && this.dom.mobileCustomizerSheet.classList.contains('open');
      if (isDrawerOpen || isSheetOpen) return;

      const deltaX = e.touches[0].clientX - touchStartX;
      const deltaY = e.touches[0].clientY - touchStartY;

      // 1. PULL-TO-REFRESH GESTURE (Dominant downward drag from upper area)
      if (deltaY > 12 && deltaY > Math.abs(deltaX) * 1.15 && touchStartY < window.innerHeight * 0.75) {
        isPullRefreshing = true;
        const pullDist = Math.min(deltaY * 0.44, 90);

        if (this.dom.pullIndicator) {
          this.dom.pullIndicator.classList.add('visible');
          this.dom.pullIndicator.classList.remove('transitioning');
          this.dom.pullIndicator.style.transform = `translate(-50%, ${pullDist - 46}px)`;

          const isPrimed = pullDist >= 52;
          if (isPrimed && !this.pullReady) {
            this.pullReady = true;
            this.dom.pullIndicator.classList.add('ready');
            if (this.dom.pullText) this.dom.pullText.textContent = 'Release to refresh';
            if (navigator.vibrate) navigator.vibrate(14);
          } else if (!isPrimed && this.pullReady) {
            this.pullReady = false;
            this.dom.pullIndicator.classList.remove('ready');
            if (this.dom.pullText) this.dom.pullText.textContent = 'Pull to refresh';
          }
        }
        return;
      }

      // 2. HORIZONTAL ARTWORK SWIPE (Dominant horizontal drag)
      if (this.currentMode === 'gallery' && !isPullRefreshing) {
        if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > 10) {
          const isScaleActive = this.dom.artworkMount.classList.contains('scale-active-mobile');
          const baseOffset = isScaleActive ? 24 : 0;
          this.dom.artworkMount.style.transform = `translateX(${baseOffset + (deltaX * 0.18)}px)`;
        }
      }
    }, { passive: true });

    appEl.addEventListener('touchend', (e) => {
      if (!isTouchActive) return;
      isTouchActive = false;

      // 1. PULL-TO-REFRESH RESOLUTION
      if (isPullRefreshing) {
        isPullRefreshing = false;
        if (this.pullReady) {
          if (this.dom.pullIndicator) {
            this.dom.pullIndicator.classList.add('refreshing');
            this.dom.pullIndicator.style.transform = 'translate(-50%, 18px)';
            if (this.dom.pullText) this.dom.pullText.textContent = 'Refreshing gallery...';
          }
          if (navigator.vibrate) navigator.vibrate([15, 35, 15]);
          setTimeout(() => {
            window.location.reload();
          }, 320);
          return;
        } else {
          // Cancelled pull
          if (this.dom.pullIndicator) {
            this.dom.pullIndicator.classList.add('transitioning');
            this.dom.pullIndicator.style.transform = 'translate(-50%, -100%)';
            setTimeout(() => {
              this.dom.pullIndicator.classList.remove('visible', 'ready', 'transitioning');
              this.pullReady = false;
            }, 350);
          }
        }
      }

      // Reset elastic horizontal drag transform
      if (this.currentMode === 'gallery') {
        const isScaleActive = this.dom.artworkMount.classList.contains('scale-active-mobile');
        const offset = (window.innerWidth <= 768 && isScaleActive) ? 'translateX(24px)' : (window.innerWidth <= 768 ? 'none' : this.dom.artworkMount.style.transform);
        this.dom.artworkMount.style.transform = offset;
      }

      if (this.currentMode === 'macro') {
        this.handleMouseLeave();
        return;
      }

      if (e.changedTouches.length === 1) {
        const deltaX = e.changedTouches[0].clientX - touchStartX;
        const deltaY = e.changedTouches[0].clientY - touchStartY;
        const deltaTime = Date.now() - touchStartTime;

        // Valid swipe: horizontal threshold 40px, predominantly horizontal, swift flick under 550ms
        if (Math.abs(deltaX) > 40 && Math.abs(deltaX) > Math.abs(deltaY) * 1.2 && deltaTime < 550) {
          if (deltaX < 0) {
            this.navigate(1); // Swipe left: next artwork
          } else {
            this.navigate(-1); // Swipe right: previous artwork
          }
        }
      }
    }, { passive: true });

    // Wall texture buttons (Desktop toolbar)
    document.querySelectorAll('[data-wall]').forEach(btn => {
      btn.addEventListener('click', () => {
        this.setWall(btn.dataset.wall);
        document.querySelectorAll('[data-wall]').forEach(b => b.classList.toggle('active', b.dataset.wall === btn.dataset.wall));
        document.querySelectorAll('#mobileWallOptions .sheet-pill').forEach(b => b.classList.toggle('active', b.dataset.wall === btn.dataset.wall));
      });
    });

    // Mobile Wall Plaster pills
    document.querySelectorAll('#mobileWallOptions .sheet-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        this.setWall(btn.dataset.wall);
        document.querySelectorAll('#mobileWallOptions .sheet-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        document.querySelectorAll('[data-wall]').forEach(b => b.classList.toggle('active', b.dataset.wall === btn.dataset.wall));
      });
    });

    // Frame style buttons (Desktop toolbar)
    document.querySelectorAll('[data-frame]').forEach(btn => {
      btn.addEventListener('click', () => {
        this.setFrame(btn.dataset.frame);
        document.querySelectorAll('[data-frame]').forEach(b => b.classList.toggle('active', b.dataset.frame === btn.dataset.frame));
        document.querySelectorAll('#mobileFrameOptions .sheet-pill').forEach(b => b.classList.toggle('active', b.dataset.frame === btn.dataset.frame));
      });
    });

    // Mobile Framing pills
    document.querySelectorAll('#mobileFrameOptions .sheet-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        this.setFrame(btn.dataset.frame);
        document.querySelectorAll('#mobileFrameOptions .sheet-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        document.querySelectorAll('[data-frame]').forEach(b => b.classList.toggle('active', b.dataset.frame === btn.dataset.frame));
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
    window.addEventListener('orientationchange', () => {
      setTimeout(() => this.applyProportionalDimensions(), 150);
    });
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
    // Update Left Wing (Architectural Niche Context) if present
    if (this.dom.wingLeft) {
      if (this.dom.wingNicheTag) this.dom.wingNicheTag.textContent = `Plate ${art.number}`;
      if (this.dom.wingInsituThumb) this.dom.wingInsituThumb.src = art.images.insitu;
      if (this.dom.wingNicheDesc) this.dom.wingNicheDesc.textContent = art.niche;
      if (this.dom.wingDimension) this.dom.wingDimension.textContent = art.dimensions;
      if (this.dom.wingLighting) this.dom.wingLighting.textContent = art.turnkeySpecs.lighting.split('(')[0].trim();
    }

    // Update Right Wing (Absheron Geological Minerals & Specs) if present
    if (this.dom.wingRight && this.dom.wingMineralsList) {
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

      if (this.dom.wingChassis) this.dom.wingChassis.textContent = art.turnkeySpecs.chassis.split('with')[0].trim();
      if (this.dom.wingWeight) this.dom.wingWeight.textContent = art.turnkeySpecs.weight;
      if (this.dom.wingCleats) this.dom.wingCleats.textContent = art.turnkeySpecs.mounting.split('(')[0].trim();
    }
  }

  toggleWing(forceCollapse) {
    if (typeof forceCollapse === 'boolean') {
      this.wingCollapsed = forceCollapse;
    } else {
      this.wingCollapsed = !this.wingCollapsed;
    }
    if (this.dom.wingRight) {
      this.dom.wingRight.classList.toggle('collapsed', this.wingCollapsed);
    }
    if (this.dom.wingToggleBtn) {
      this.dom.wingToggleBtn.classList.toggle('active', !this.wingCollapsed);
    }
    this.applyProportionalDimensions();
  }

  initPanoramicPromenade() {
    if (!this.dom.panoramicTrack) return;
    this.dom.panoramicTrack.innerHTML = '';

    const isMobile = window.innerWidth <= 768;
    const isWidescreen = window.innerWidth >= 1800;
    const pxPerCm = isMobile ? 1.15 : (isWidescreen ? 2.6 : 1.95);

    this.artworks.forEach((art, index) => {
      const station = document.createElement('div');
      station.className = `promenade-station ${index === this.currentIndex ? 'active' : ''}`;
      station.dataset.index = index;

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

    // Smooth mouse drag-to-scroll on desktop
    let isMouseDown = false;
    let startX = 0;
    let scrollStart = 0;

    this.dom.panoramicPromenade.addEventListener('mousedown', (e) => {
      isMouseDown = true;
      startX = e.pageX - this.dom.panoramicPromenade.offsetLeft;
      scrollStart = this.dom.panoramicPromenade.scrollLeft;
    });

    window.addEventListener('mouseup', () => {
      isMouseDown = false;
    });

    this.dom.panoramicPromenade.addEventListener('mousemove', (e) => {
      if (!isMouseDown) return;
      e.preventDefault();
      const x = e.pageX - this.dom.panoramicPromenade.offsetLeft;
      const walk = (x - startX) * 1.5;
      this.dom.panoramicPromenade.scrollLeft = scrollStart - walk;
    });
  }

  applyProportionalDimensions() {
    const art = this.artworks[this.currentIndex];
    const isMobile = window.innerWidth <= 768;
    const isLandscapeMobile = isMobile && window.innerHeight <= 520 && window.innerWidth > window.innerHeight;
    const isTablet = window.innerWidth > 768 && window.innerWidth <= 1100;
    const isWidescreen = window.innerWidth >= 1800;

    let targetWidth, targetHeight, pxPerCm;

    if (isLandscapeMobile) {
      // Landscape mobile phone: maximum canvas expansion
      const availH = Math.max(window.innerHeight - 98, 180);
      const availW = Math.max(window.innerWidth - 60, 240);
      pxPerCm = Math.min(availW / art.widthCm, availH / art.heightCm);

      targetWidth = Math.round(art.widthCm * pxPerCm);
      targetHeight = Math.round(art.heightCm * pxPerCm);

      this.dom.canvasInner.style.width = `${targetWidth}px`;
      this.dom.canvasInner.style.height = `${targetHeight}px`;

      this.dom.artworkMount.style.transform = 'none';
      this.dom.artworkMount.classList.remove('scale-active-mobile');
      this.dom.humanScaleFigure.classList.remove('visible');
      this.dom.labelCard.className = 'gallery-label-card placard-mobile';
    } else if (isMobile) {
      // Mobile portrait layout (iPhone, Android)
      const stageH = Math.max(window.innerHeight - 250, 200);

      this.dom.artworkMount.style.transform = this.showHumanScale ? 'translateX(24px)' : 'none';

      const availW = this.showHumanScale 
        ? Math.max(window.innerWidth - 80, 220) 
        : Math.max(window.innerWidth - 30, 250);

      const maxScaleW = availW / art.widthCm;
      const maxScaleH = stageH / art.heightCm;
      pxPerCm = Math.min(maxScaleW, maxScaleH);
      pxPerCm = Math.max(pxPerCm, 1.0);

      targetWidth = Math.round(art.widthCm * pxPerCm);
      targetHeight = Math.round(art.heightCm * pxPerCm);

      this.dom.canvasInner.style.width = `${targetWidth}px`;
      this.dom.canvasInner.style.height = `${targetHeight}px`;

      const humanHeightPx = Math.round(175 * pxPerCm);
      this.dom.figureSvg.style.height = `${Math.min(humanHeightPx, stageH * 0.95)}px`;
      this.dom.figureSvg.style.width = 'auto';

      this.dom.humanScaleFigure.style.transform = 'none';
      this.dom.humanScaleFigure.classList.toggle('visible', this.showHumanScale);

      this.dom.labelCard.className = 'gallery-label-card placard-mobile';
    } else {
      // Desktop / Laptop / 4K Ultrawide proportional scaling
      this.dom.artworkMount.classList.remove('scale-active-mobile');

      const stageH = this.dom.stage.clientHeight - (isTablet ? 150 : 190);
      const wingIsVisible = window.innerWidth >= 1101 && !this.wingCollapsed;
      const wingReserved = wingIsVisible ? (isWidescreen ? 420 : 340) : 60;
      const figureReserved = this.showHumanScale ? 160 : 60;
      const stageW = this.dom.stage.clientWidth - wingReserved - figureReserved;

      // Allow higher scaling on 1440p / 4K / ultrawide displays
      const maxScaleCeiling = isWidescreen ? 4.8 : (window.innerWidth >= 1440 ? 3.8 : 3.0);
      const scaleFactorByHeight = stageH / (art.heightCm + 25);
      const scaleFactorByWidth = stageW / (art.widthCm + 25);

      pxPerCm = Math.min(scaleFactorByHeight, scaleFactorByWidth);
      pxPerCm = Math.min(Math.max(pxPerCm, 1.6), maxScaleCeiling);

      targetWidth = Math.round(art.widthCm * pxPerCm);
      targetHeight = Math.round(art.heightCm * pxPerCm);

      this.dom.canvasInner.style.width = `${targetWidth}px`;
      this.dom.canvasInner.style.height = `${targetHeight}px`;

      const humanHeightPx = Math.round(175 * pxPerCm);
      this.dom.figureSvg.style.height = `${humanHeightPx}px`;
      this.dom.figureSvg.style.width = 'auto';

      // 1. TRUE WALL CENTERING:
      // Center the artwork in the unobstructed wall space between the left screen edge and the right wing
      const stageTotalWidth = this.dom.stage.clientWidth;
      const clearLeft = this.showHumanScale ? 140 : 40;
      const clearRight = stageTotalWidth - (wingIsVisible ? (isWidescreen ? 420 : 340) : 40);
      const wallCenter = (clearLeft + clearRight) / 2;
      const offsetFromCenter = Math.round(wallCenter - (stageTotalWidth / 2));

      this.dom.artworkMount.style.transform = `translateX(${offsetFromCenter}px)`;

      // Ground and align human silhouette relative to the artwork's left frame edge
      const figureOffsetFromArt = -(targetWidth / 2 + 75);
      const figureTotalX = offsetFromCenter + figureOffsetFromArt;
      this.dom.humanScaleFigure.style.transform = `translateX(${figureTotalX}px)`;
      this.dom.humanScaleFigure.classList.toggle('visible', this.showHumanScale);

      // 2. CURATORIAL PLACARD / TOMBSTONE PLACEMENT:
      // Calculate unobstructed space to the right and left of the artwork frame
      const artRightEdgeX = (stageTotalWidth / 2) + offsetFromCenter + (targetWidth / 2);
      const rightAvailable = clearRight - artRightEdgeX;
      const leftAvailable = (stageTotalWidth / 2) + offsetFromCenter - (targetWidth / 2) - clearLeft;

      this.dom.labelCard.className = 'gallery-label-card';

      if (rightAvailable >= 235) {
        // Primary Museum Position: Mounted to the right of the floater frame at eye-level
        this.dom.labelCard.classList.add('placard-side-right');
      } else if (!this.showHumanScale || leftAvailable >= 235) {
        // Secondary Museum Position: Mounted to the left of the floater frame
        this.dom.labelCard.classList.add('placard-side-left');
      } else {
        // Fallback for monumental width works on compact screens: Docked neatly under right corner of frame
        this.dom.labelCard.classList.add('placard-docked-bottom');
      }
    }
  }

  updatePlacardLabel() {
    const art = this.artworks[this.currentIndex];
    const mediumText = art.minerals && art.minerals.length > 0 
      ? art.minerals.map(m => m.name).slice(0, 2).join(' · ') 
      : (art.genre || 'Oil and Raw Absheron Minerals on Canvas');

    const placementNiche = art.niche ? art.niche.split('/')[0].trim() : 'Curatorial Commission';

    this.dom.labelCard.innerHTML = `
      <div class="placard-mount-dots">
        <span class="dot-tl"></span>
        <span class="dot-tr"></span>
        <span class="dot-bl"></span>
        <span class="dot-br"></span>
      </div>
      <div class="label-header-row">
        <span class="label-artist">Mirgasim Art Studio</span>
        <span class="label-year">2026</span>
      </div>
      <div class="label-title">${art.title}</div>
      <div class="label-az-title">${art.azTitle}</div>
      <div class="label-divider"></div>
      <div class="label-medium">${mediumText}</div>
      <div class="label-dim">${art.dimensions}</div>
      <div class="label-placement"><span class="placement-pip"></span>${placementNiche}</div>
      <button class="label-dossier-link" onclick="window.gallery.toggleDrawer(true)" title="Inspect Full Technical & Mineral Specifications">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
        <span>Curatorial Dossier & Specs ↗</span>
      </button>
      <div class="mobile-swipe-guide">← Swipe to explore Caspian suite →</div>
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
      
      // Tap toggle for mobile screens
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        const wasActive = el.classList.contains('active');
        document.querySelectorAll('.tactile-hotspot').forEach(h => h.classList.remove('active'));
        if (!wasActive) el.classList.add('active');
      });

      this.dom.hotspotContainer.appendChild(el);
    });

    document.addEventListener('click', () => {
      document.querySelectorAll('.tactile-hotspot').forEach(h => h.classList.remove('active'));
    });
  }

  toggleMobileCustomizer(open) {
    if (this.dom.mobileCustomizerSheet) {
      this.dom.mobileCustomizerSheet.classList.toggle('open', open);
    }
  }

  handleTouchLoupe(touch) {
    if (this.currentMode !== 'macro') return;
    const canvasRect = this.dom.canvasInner.getBoundingClientRect();
    const inCanvas = (
      touch.clientX >= canvasRect.left &&
      touch.clientX <= canvasRect.right &&
      touch.clientY >= canvasRect.top &&
      touch.clientY <= canvasRect.bottom
    );

    if (inCanvas) {
      this.dom.macroLoupe.style.display = 'block';
      const loupeRadius = window.innerWidth <= 768 ? 80 : 100;
      const loupeDiam = loupeRadius * 2;

      let targetX = touch.clientX - loupeRadius;
      let targetY = touch.clientY - loupeRadius - 40;

      // Safe viewport boundary clamping so loupe never clips off screen
      const minX = 10;
      const maxX = window.innerWidth - loupeDiam - 10;
      const minY = 60; // clear header
      const maxY = window.innerHeight - loupeDiam - 75; // clear footer

      targetX = Math.max(minX, Math.min(maxX, targetX));
      targetY = Math.max(minY, Math.min(maxY, targetY));

      this.dom.macroLoupe.style.left = `${targetX}px`;
      this.dom.macroLoupe.style.top = `${targetY}px`;

      const relX = (touch.clientX - canvasRect.left) / canvasRect.width;
      const relY = (touch.clientY - canvasRect.top) / canvasRect.height;
      const art = this.artworks[this.currentIndex];

      this.dom.macroLoupe.style.backgroundImage = `url("${art.images.clean}")`;
      const zoom = 2.6;
      this.dom.macroLoupe.style.backgroundSize = `${canvasRect.width * zoom}px ${canvasRect.height * zoom}px`;
      this.dom.macroLoupe.style.backgroundPosition = `${-((relX * canvasRect.width * zoom) - loupeRadius)}px ${-((relY * canvasRect.height * zoom) - loupeRadius)}px`;
    } else {
      this.dom.macroLoupe.style.display = 'none';
    }
  }

  setMode(mode) {
    this.currentMode = mode;

    document.querySelectorAll('.mode-tab').forEach(tab => {
      const isActive = tab.dataset.mode === mode;
      tab.classList.toggle('active', isActive);
      if (isActive && window.innerWidth <= 900) {
        tab.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
      }
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
      case 'e':
      case 'E':
        this.toggleWing();
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
