---
title: Sample Projects
description: Overview of the sample projects included with the Amplitude Audio SDK.
---

The Amplitude Audio SDK includes two sample projects that demonstrate different aspects of the engine. This document explains what each sample covers and how to run them.

## Building the Samples

Enable sample builds in the XMake configuration:

```bash
xmake config --build_samples=y
xmake
```

This also builds the sample assets (`build_assets=y` is implied).

---

## Sample 01 — Console Demo

A command-line application that demonstrates core engine features without graphical dependencies.

### Location

`samples/sample_01/`

### Features Demonstrated

| Feature | Description |
|---------|-------------|
| **Engine initialization** | Full init sequence including memory manager, file system, and plugin registration. |
| **Sound bank loading** | Loading and unloading `.ambank` files. |
| **Collections** | Playing randomized sound collections (e.g., footstep variations). |
| **Switch containers** | State-driven audio switching (e.g., surface types). |
| **Events** | Triggering events with multiple actions. |
| **Channel callbacks** | Registering callbacks for playback events (Begin, End, Loop). |
| **Memory stats** | Querying and printing memory pool usage. |

### Running

```bash
./sample_01 /path/to/sample_project/
```

The sample expects a compiled Amplitude project directory as its argument.

### Code Highlights

```cpp
// Load a sound bank
amEngine->LoadSoundBank("sample_project/soundbanks/master.ambank");

// Play a collection
auto collection = amEngine->GetCollection("footsteps");
Channel ch = amEngine->Play(collection);

// Register a callback
ch.On(ChannelEvent::End, [](ChannelEventInfo info) {
    amLogInfo("Sound finished playing!");
});

// Print memory stats
auto stats = amMemory->GetStats();
amLogInfo("Engine pool: %zu bytes", stats.GetPoolStats(eMemoryPoolKind_Engine).mUsed);
```

---

## Sample 02 — SDL2 Interactive Demo

A graphical application that demonstrates spatial audio, plugin loading, and real-time interaction.

### Location

`samples/sample_02/`

### Dependencies

- SDL2 (for windowing and input)
- OpenGL or similar (for simple rendering)

### Features Demonstrated

| Feature | Description |
|---------|-------------|
| **2D spatial audio** | Mouse-controlled entities and listeners in a 2D plane. |
| **Plugin loading** | Dynamic loading of Vorbis and FLAC plugins at runtime. |
| **Device notifications** | Handling audio device connect/disconnect events. |
| **Bus gain control** | Real-time adjustment of bus volumes via UI. |
| **Multi-listener** | Switching between different listener perspectives. |
| **Attenuation visualization** | Visual display of attenuation zones. |

### Running

```bash
./sample_02 /path/to/sample_project/
```

### Controls

| Input | Action |
|-------|--------|
| Mouse move | Control entity position |
| Left click | Play a sound at the cursor position |
| Right click | Move the listener |
| Number keys 1-4 | Switch between bus gain presets |
| Space | Toggle between listener modes |

### Code Highlights

```cpp
// Load dynamic plugins
Engine::AddPluginSearchPath(AM_OS_STRING("./plugins"));
Engine::LoadPlugin(AM_OS_STRING("vorbis_plugin"));
Engine::LoadPlugin(AM_OS_STRING("flac_plugin"));

// Handle device notifications
Engine::SetDeviceNotificationCallback([](eDeviceNotification notification, const DeviceDescription& device) {
    switch (notification)
    {
        case eDeviceNotification_Rerouted:
            amLogInfo("Audio device rerouted to: %s", device.mName.c_str());
            break;
        // ...
    }
});

// Real-time bus control
Bus sfxBus = amEngine->GetBus("sfx");
sfxBus.SetGain(0.7f);
```

---

## Sample Project Data

Both samples load assets from the `sample_project/` directory at the SDK root. This directory contains a complete Amplitude project with:

- Engine configuration (`pc.config.json`)
- Bus configuration (`pc.buses.json`)
- Sound banks, collections, switch containers
- Effects, attenuation models, RTPCs
- Sample audio files

To build the sample project assets:

```bash
xmake build_sample_project
```

This compiles all JSON assets into binary FlatBuffers files ready for runtime loading.

## Next Steps

- Follow the [Quick Start](../getting-started/quick-start.md) to build your own application.
- Learn how to [compile Amplitude projects](../integration/compiling-amplitude-project.md).
- Explore the [Sample Project Walkthrough](../tutorials/sample-project-walkthrough.md) for a line-by-line guide.
