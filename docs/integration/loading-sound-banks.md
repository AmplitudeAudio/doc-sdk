---
title: Loading sound banks
description: Sound banks are units storing the data your game will need to play audio. The page will show you how to load soundbanks from an Amplitude project.
---

!!! danger Incomplete Documentation
    This documentation page is WIP and not yet complete. You can have a complete demo on how to interact with the engine through the official [sample projects](https://github.com/AmplitudeAudio/sdk/blob/develop/samples).

When the engine is [fully initialized](./initializing-the-engine.md), you have to load a [sound bank](../project/sound-bank.md) to be able to play any sound or interact with your Amplitude project at runtime.

By loading a sound bank, the engine will also load all the associated data (effects, attenuation, events, etc.).

```cpp
AmBankID bankId = kAmInvalidObjectId;

if (!amEngine->LoadSoundBank(AM_OS_STRING("init.ambank"), bankId))
  return 1;
```

At this point, the engine has only preloaded sound objects associated to the sound bank. The process of loading sound files is done manually, in another thread, so the main thread is ensured to not hang during this time.

During this process, only sound files with streaming disabled will be read and stored in memory. Other sound files will read from the file system on playback.

```cpp
// Load audio files
amEngine->StartLoadSoundFiles();
while (!m_pEngine->TryFinalizeLoadSoundFiles())
  Thread::Sleep(1);
```

Audio data loaded in memory are shared across every sound instances.
