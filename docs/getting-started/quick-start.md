---
title: Quick Start
description: Get up and running with Amplitude Audio SDK in your game project. This guide walks you through the essential steps to initialize the engine and play your first sound.
diataxis: tutorial

---

This guide walks you through the essential steps to initialize the Amplitude engine, load a sound bank, and play your first sound. By the end, you'll have a working audio loop integrated into your game.

!!! note "Prerequisites"
    Before following this guide, make sure you have:

    - [Built and installed](installation.md) the Amplitude SDK
    - Set up an [Amplitude project](../project/project-architecture.md) with at least one sound bank
    - Compiled your project assets using the `build_project.py` script

## Step 1: Include the SDK

A single header gives you access to the entire Amplitude API:

```cpp
#include <SparkyStudios/Audio/Amplitude/Amplitude.h>

using namespace SparkyStudios::Audio::Amplitude;
```

## Step 2: Initialize Core Systems

Before using the engine, initialize the **memory manager** and optionally set up a **logger**:

```cpp
// Set up logging (optional, but recommended for debugging)
ConsoleLogger logger(true); // true enables verbose output
Logger::SetLogger(&logger);

// Initialize the memory manager (required, must be first)
MemoryManager::Initialize();
```

The memory manager must be initialized before any other Amplitude calls, as it handles all internal allocations. See [Initializing the Engine](../integration/initializing-the-engine.md#memory-manager) for custom allocator configurations.

## Step 3: Set Up the File System

Amplitude needs a file system to locate your compiled project assets:

```cpp
// Create a file system pointing to your compiled project directory
auto fileSystem = AmSharedPtr<DiskFileSystem, eMemoryPoolKind_IO>::Make();
fileSystem->SetBasePath(AM_OS_STRING("./my_project"));

amEngine->SetFileSystem(fileSystem);

// Open the file system (may load asynchronously)
amEngine->StartOpenFileSystem();
while (!amEngine->TryFinalizeOpenFileSystem())
    Thread::Sleep(1);
```

## Step 4: Register Extensions and Initialize

Register the built-in extensions (codecs, filters, pipeline nodes, etc.) and then initialize the engine with your configuration file:

```cpp
// Register all default extensions shipped with the engine
Engine::RegisterDefaultExtensions();

// Initialize the engine with your project configuration
if (!amEngine->Initialize(AM_OS_STRING("pc.config.amconfig")))
{
    // Handle initialization failure
    return 1;
}
```

!!! tip
    The configuration file path is relative to the base path of the file system you set in Step 3.

## Step 5: Load a Sound Bank

[Sound banks](../project/sound-bank.md) contain references to all your audio assets. Load one to make its sounds available:

```cpp
// Load a sound bank (synchronous — returns true on success)
if (!amEngine->LoadSoundBank(AM_OS_STRING("my_soundbank.ambank")))
{
    // Handle loading failure
    return 1;
}

// Start loading the actual sound file data (asynchronous)
amEngine->StartLoadSoundFiles();

// Wait for sound files to finish loading
while (!amEngine->TryFinalizeLoadSoundFiles())
    Thread::Sleep(1);
```

`LoadSoundBank()` loads the bank metadata synchronously and returns `true` on success. The actual audio data is loaded separately via `StartLoadSoundFiles()`, which runs on a background thread. See [Loading Sound Banks](../integration/loading-sound-banks.md) for details.

## Step 6: Set Up a Listener

A [listener](../integration/managing-game-objects.md#listeners) represents the player's ears in the game world. You need at least one for spatial audio to work:

```cpp
// Create a listener (ID must be unique)
Listener listener = amEngine->AddListener(1);
listener.SetLocation({ 0.0f, 0.0f, 0.0f });
listener.SetOrientation(Orientation({ 0.0f, 0.0f, -1.0f }, { 0.0f, 1.0f, 0.0f }));

// Set it as the default listener
amEngine->SetDefaultListener(&listener);
```

## Step 7: Play a Sound

You can play a sound by name, by ID, or by handle:

```cpp
// Play by name (simplest, but requires an internal lookup)
Channel channel = amEngine->Play("my_sound");

// Play by handle (faster for frequently played sounds)
SoundHandle handle = amEngine->GetSoundHandle("my_sound");
Channel channel = amEngine->Play(handle);
```

The returned `Channel` lets you control playback:

```cpp
if (channel.Valid())
{
    // Check playback state
    bool playing = channel.Playing();

    // Pause and resume
    channel.Pause();
    channel.Resume();

    // Stop playback
    channel.Stop();
}
```

See [Playing Audio](../integration/playing-audio.md) for the full Channel API, including playback events.

## Step 8: Run the Game Loop

Call `AdvanceFrame()` every frame to keep the audio engine in sync with your game:

```cpp
while (running)
{
    // ... update game logic, physics, positions ...

    // Advance the audio engine (delta is in seconds)
    amEngine->AdvanceFrame(deltaTime);
}
```

See [The Rendering Loop](../integration/the-rendering-loop.md) for the recommended update order and threading considerations.

## Step 9: Shut Down

Clean up in reverse order when your game exits:

```cpp
// Deinitialize the engine
amEngine->Deinitialize();

// Close the file system
amEngine->StartCloseFileSystem();
while (!amEngine->TryFinalizeCloseFileSystem())
    Thread::Sleep(1);

// Unregister extensions
Engine::UnregisterDefaultExtensions();

// Destroy the engine singleton
Engine::DestroyInstance();

// Deinitialize the memory manager (must be last)
MemoryManager::Deinitialize();
```

## Complete Example

Here is a minimal but complete program that initializes Amplitude, plays a sound, runs for a few seconds, and shuts down:

```cpp
#include <SparkyStudios/Audio/Amplitude/Amplitude.h>

using namespace SparkyStudios::Audio::Amplitude;

int main(int argc, char* argv[])
{
    // --- Core systems ---
    ConsoleLogger logger(true);
    Logger::SetLogger(&logger);
    MemoryManager::Initialize();

    // --- File system ---
    auto fileSystem = AmSharedPtr<DiskFileSystem, eMemoryPoolKind_IO>::Make();
    fileSystem->SetBasePath(AM_OS_STRING("./my_project"));
    amEngine->SetFileSystem(fileSystem);

    amEngine->StartOpenFileSystem();
    while (!amEngine->TryFinalizeOpenFileSystem())
        Thread::Sleep(1);

    // --- Extensions and engine ---
    Engine::RegisterDefaultExtensions();

    if (!amEngine->Initialize(AM_OS_STRING("pc.config.amconfig")))
    {
        amLogError("Failed to initialize the engine");
        return 1;
    }

    // --- Sound bank ---
    if (!amEngine->LoadSoundBank(AM_OS_STRING("my_soundbank.ambank")))
    {
        amLogError("Failed to load sound bank");
        return 1;
    }

    amEngine->StartLoadSoundFiles();
    while (!amEngine->TryFinalizeLoadSoundFiles())
        Thread::Sleep(1);

    // --- Listener ---
    Listener listener = amEngine->AddListener(1);
    listener.SetLocation({ 0.0f, 0.0f, 0.0f });
    listener.SetOrientation(Orientation({ 0.0f, 0.0f, -1.0f }, { 0.0f, 1.0f, 0.0f }));
    amEngine->SetDefaultListener(&listener);

    // --- Play a sound ---
    Channel channel = amEngine->Play("my_sound");

    // --- Game loop ---
    constexpr AmTime kFrameRate = 1.0 / 60.0;

    for (int frame = 0; frame < 300; ++frame) // Run for ~5 seconds at 60 FPS
    {
        amEngine->AdvanceFrame(kFrameRate);
        Thread::Sleep(static_cast<AmInt32>(kFrameRate * kAmSecond));
    }

    // --- Shutdown ---
    channel.Stop();

    amEngine->Deinitialize();

    amEngine->StartCloseFileSystem();
    while (!amEngine->TryFinalizeCloseFileSystem())
        Thread::Sleep(1);

    Engine::UnregisterDefaultExtensions();
    Engine::DestroyInstance();

    MemoryManager::Deinitialize();

    return 0;
}
```

## Next Steps

Now that you have audio playing, explore these topics to build a complete audio experience:

- **[Managing Game Objects](../integration/managing-game-objects.md)** — Add entities, environments, and rooms for spatial audio
- **[Playing Audio](../integration/playing-audio.md)** — Master the Channel API and playback events
- **[The Rendering Loop](../integration/the-rendering-loop.md)** — Optimize your game loop integration
- **[Project Reference](../project/index.md)** — Configure sounds, effects, attenuations, and more
- **[Pipeline](../project/pipeline.md)** — Customize the audio processing pipeline
