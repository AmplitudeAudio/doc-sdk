---
title: Sample Project Walkthrough
description: A step-by-step walkthrough of building and running the Amplitude sample projects.
diataxis: tutorial

---

This tutorial walks you through building, configuring, and running the Amplitude Audio SDK sample projects from scratch. By the end, you will understand the complete workflow from project setup to hearing spatialized audio.

## Prerequisites

Before starting, ensure you have:

- Amplitude Audio SDK source code cloned
- XMake installed (see [Installation](../getting-started/installation.md))
- A C++ compiler (GCC, Clang, MSVC, or Xcode)
- SDL2 installed (for Sample 02 only)

## Step 1: Clone and Configure the SDK

```bash
git clone https://github.com/AmplitudeAudio/sdk.git
cd sdk

# Configure with samples and tools enabled
xmake config --build_samples=y --build_tools=y
```

## Step 2: Build the Sample Project Assets

The sample project in `sample_project/` contains JSON configuration files and raw audio assets. These must be compiled into binary FlatBuffers files before the engine can load them:

```bash
xmake build_sample_project
```

This generates:

- `sample_project/.amproject` — Project metadata
- Binary `.amsound`, `.amcollection`, `.ambank`, etc. files
- Compiled engine config and bus files

## Step 3: Build the Samples

```bash
xmake
```

This builds:

- `build/[platform]/[arch]/[mode]/sample_01`
- `build/[platform]/[arch]/[mode]/sample_02`

## Step 4: Run Sample 01 (Console Demo)

Sample 01 is a command-line demo that plays sounds and prints information:

```bash
./build/linux/x86_64/release/sample_01 ./sample_project/
```

You should see:

```
[Info] Amplitude Audio SDK v1.0.0
[Info] Loaded sound bank: master
[Info] Playing collection: footsteps
[Info] Sound finished playing!
[Info] Memory stats - Engine: 2048 bytes, SoundData: 1048576 bytes
```

### What Sample 01 Demonstrates

1. **Engine initialization**: Creates the memory manager, file system, and engine.
2. **Bank loading**: Loads `master.ambank` from the sample project.
3. **Collection playback**: Randomly selects and plays footstep sounds.
4. **Switch container**: Changes footstep sounds based on surface type.
5. **Event triggering**: Plays a sequence of sounds via an event.
6. **Callbacks**: Logs when sounds start and finish.
7. **Cleanup**: Unloads banks and shuts down the engine.

## Step 5: Run Sample 02 (Interactive SDL2 Demo)

Sample 02 is a graphical application that lets you experiment with spatial audio:

```bash
./build/linux/x86_64/release/sample_02 ./sample_project/
```

A window will open showing a top-down view of a 2D world.

### Controls

| Input | Action |
|-------|--------|
| Move mouse | Control the sound source (entity) position |
| Left click | Trigger a sound at the cursor location |
| Right click | Move the listener position |
| `1`–`4` | Set bus gain presets |
| `Space` | Toggle between single listener and multi-listener modes |

### What Sample 02 Demonstrates

1. **Spatial audio**: Sounds pan and attenuate based on distance and direction.
2. **Attenuation zones**: Visual circles show where sounds begin to fade.
3. **Dynamic plugins**: Loads Vorbis and FLAC codecs at runtime.
4. **Bus control**: Adjusts SFX and music bus gains in real time.
5. **Device notifications**: Detects when headphones are plugged/unplugged.
6. **Multi-listener**: Simulates split-screen with two independent listeners.

## Step 6: Explore the Sample Project Structure

Open `sample_project/` in your editor:

```
sample_project/
├── pc.config.json          # Engine config (driver, mixer, HRTF)
├── pc.buses.json           # Bus hierarchy
├── attenuators/            # Distance attenuation models
├── collections/            # Sound collections (footsteps, impacts)
├── effects/                # DSP effects (reverb, EQ)
├── events/                 # Triggerable events
├── pipelines/              # Audio processing graphs
├── rtpc/                   # Real-time parameter controls
├── soundbanks/             # Sound bank definitions
├── sounds/                 # Individual sound assets
├── switch_containers/      # State-driven switches
└── switches/               # Switch state definitions
```

Each JSON file corresponds to a FlatBuffers schema in `schemas/`. The `build_project.py` script compiles these JSON files into binary assets.

## Step 7: Modify and Rebuild

Try making a small change:

1. Open `sample_project/sounds/ambient_wind.json`.
2. Change the `gain` value from `1.0` to `0.5`.
3. Rebuild the project assets:

```bash
xmake build_sample_project
```

4. Run Sample 01 again and notice the quieter wind sound.

## Step 8: Add Your Own Sound

1. Copy a WAV file into `sample_project/sounds/`.
2. Create a new JSON file:

```json
{
  "id": 999,
  "name": "my_sound",
  "path": "sounds/my_sound.wav",
  "gain": 1.0
}
```

3. Add it to a sound bank in `sample_project/soundbanks/master.json`:

```json
{
  "id": 1,
  "name": "master",
  "sounds": [1, 2, 3, 999]
}
```

4. Rebuild and run:

```bash
xmake build_sample_project
./build/linux/x86_64/release/sample_01 ./sample_project/
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `sample_01` crashes on startup | Verify the sample project path is correct and assets are built. |
| No audio in `sample_02` | Check that your default audio device is working. |
| SDL2 not found | Install SDL2 development libraries (`libsdl2-dev` on Ubuntu). |
| Build errors | Ensure you are using a supported compiler and XMake version. |

## Next Steps

- Read the [Quick Start](../getting-started/quick-start.md) to integrate Amplitude into your own game.
- Explore the [Project Reference](../project/index.md) to understand all asset types.
- Learn how to write [custom effects](../tutorials/custom-effect.md) or [codecs](../tutorials/custom-codec.md).
