# The Watcher - Enhanced Edition (Web)

Play in your browser: https://akashgaur.itch.io/thekeeper

## What's New in This Version

### 🌐 Now Playable in the Browser
- The game is converted to run in the browser using **Pygbag** (Python and Pygame CE compiled to WebAssembly)
- Published on itch.io as an HTML5 game, so there is nothing to download or install
- The main loop is asynchronous (`asyncio`) as the browser requires
- Fullscreen is handled by the itch.io fullscreen button instead of the desktop `F11` display-mode cycle

### 🐍 Python Compatibility
- Web build runs on **Python 3.12** through Pygbag
- Desktop version still supports Python 3.10 through 3.20 (including 3.15.2)
- Improved pygame version detection with error handling
- Future-proofed for upcoming Python releases

### 🎨 Enhanced Visual Effects
- **Particle System**: Red dust, electrical sparks, and steam effects
- **Dynamic Lighting**: Pulsing glows, spotlight effects, and lighthouse beam with progressive dimming
- **Screen Shake**: Dramatic camera shake for earthquakes and critical moments
- **Weather System**: Progressive red rain that intensifies with the Nightfall
- **Atmospheric Effects**: Enhanced sky transitions with more color gradations

### 📖 Expanded Story Content
- **Deeper Lore**: More detailed opening narration establishing three generations of watchers
- **Extended Dialogue**: Richer conversations with the Fisherman and Scientist
- **Character Development**: NPCs now express more fear, doubt, and emotional depth
- **Environmental Storytelling**: More detailed internal monologue reflecting the watcher's deteriorating situation
- **Daily Progression**: Each day now has unique atmospheric descriptions and thought patterns

### 🎮 Enhanced Gameplay Features

#### New Visual Feedback
- Particle effects trigger during minigames (sparks on breaker switches, steam from pressure valves)
- Dynamic lighting shows equipment status
- Weather intensity reflects game progression

#### Improved Immersion
- Extended opening sequence with more historical context
- More visceral descriptions of the red dust phenomenon
- Enhanced day-night transitions with atmospheric effects
- Progressive equipment degradation reflected in visuals

## Story Enhancements by Day

### Day 1
- Establishes family legacy (grandfather built in 1847, father served 43 years)
- Introduces the watcher's philosophy and sense of duty
- Subtle foreshadowing of coming events

### Day 2-4
- Growing unease reflected in extended internal thoughts
- More detailed observations of environmental changes
- Pressure readings become a recurring anxiety point

### Day 5
- Scientist provides more scientific context about the phenomenon
- Explicit mention of government involvement
- Discussion of exponential daylight shrinkage

### Day 6-7
- Red dust becomes a physical presence affecting everything
- Fisherman's departure is more emotionally charged
- Isolation becomes concrete and irreversible

### Day 8-9
- Equipment failure descriptions are more visceral
- Physical toll on the watcher is emphasized
- Desperation and determination intensify

### Day 10
- Apocalyptic finale with earthquake effects
- Final affirmation of duty over survival
- Grandfather's legacy fulfilled

## Technical Improvements

### New Core Systems
- `core/visual_effects.py`: Comprehensive particle and lighting system
- Enhanced rendering pipeline with blend modes
- Optimized particle management for performance
- Browser-ready async game loop for the web build

### Visual Effects Classes
- **Particle**: Individual particle with physics
- **ParticleSystem**: Manages multiple particle types
- **LightingEffect**: Dynamic lighting and glow effects
- **ScreenShake**: Camera shake for dramatic moments
- **WeatherEffect**: Atmospheric weather progression

## Playing the Game

### Play online (recommended)

1. Open https://akashgaur.itch.io/the-watcher
2. Wait for the game to load. The first load can take up to a minute.
3. Click inside the game window and press any key to enable audio.
4. Use the fullscreen button below the game for the best experience.

### Build and test the web version locally

```powershell
pip install -r requirements.txt
pip install pygbag
python -m pygbag --build .
```

Pygbag 0.9.3 can generate an `index.html` with a broken BrowserFS URL. After every build, replace this URL in `build/web/index.html`:

```
https://pygame-web.github.io/cdn/0.9.3//browserfs.min.js
```

with:

```
https://cdn.jsdelivr.net/npm/browserfs@1.4.3/dist/browserfs.min.js
```

Then serve the build folder and open `http://127.0.0.1:8765` in a fresh or Incognito Chrome window:

```powershell
cd build/web
python -m http.server 8765
```

Do not run `pygbag --port 8765 .` after applying the fix, because that rebuilds the game and overwrites it.

### Publish to itch.io

1. Copy the contents of `build/web/` into a clean `release/itch-web/` folder.
2. ZIP the contents so that `index.html` is at the root of the ZIP (itch.io allows at most 1,000 files per browser ZIP).
3. Upload the ZIP on itch.io and tick **This file will be played in the browser**.
4. Set the viewport to 1280 x 720, enable fullscreen, and test as Draft before making it Public.

### Run the desktop version (optional)

```bash
# Install dependencies (works with Python 3.10-3.20)
pip install -r requirements.txt

# Run the enhanced game
python run_game.py
```

## Compatibility Notes

- **Web build**: Python 3.12, Pygame CE and Pygbag 0.9.3
- **Desktop**: Python 3.10 through 3.20 (including 3.15.2)
- **pygame**: Requires 2.1.0 or later (graceful handling of version detection)
- **pytmx**: No changes required
- **Performance**: Visual effects are optimized for 60 FPS gameplay on desktop. Browser performance depends on your device and browser.
- **Audio**: Browsers block audio until you click or press a key in the game window.
- **Saves**: In the browser, save data is kept in your browser's storage, so clearing site data erases it.

## Visual Effect Controls

Visual effects are automatically integrated into gameplay:
- Equipment failures trigger sparks
- Pressure releases emit steam
- Red dust falls progressively after Day 6
- Lighthouse beam dims and reddens over time
- Screen shake during Day 10 earthquake

## Story Changes Summary

| Day | Original Lines | Enhanced Lines | New Elements |
|-----|---------------|----------------|--------------|
| Opening | 6 lines | 10 lines | Family history, dates, covenant |
| Day 1 | 5 lines | 7 lines | Philosophy, neglect warning |
| Days 2-10 | ~3 lines/day | ~5-7 lines/day | Visceral details, emotional depth |
| NPCs | ~3-5 lines | ~7-12 lines | Context, fear, relationships |

## Credits

**Enhanced Edition by**: Claude Sonnet 4.5
**Web conversion and itch.io release by**: Akash Gaur
**Original Game by**: MXRV Team (PyWeek 41 Winner)
- ved-in (developer/team leader)
- X3r0Day (developer)
- RudyDaBot (sound design and assets)
- xodo2fast4u (original concept and storyline)
- omnimistic (assets)

## License

Maintains original GNU GPL v3 License
