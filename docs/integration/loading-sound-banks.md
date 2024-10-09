---
title: Loading sound banks
description: Sound banks are units storing the data your game will need to play audio. The page will show you how to load sound banks from an Amplitude project.
---

When the engine is [fully initialized](./initializing-the-engine.md), you have to load a [sound bank](../project/sound-bank.md) to be able to play any sound or interact with your Amplitude project at runtime.

## Loading a sound bank

By loading a sound bank, the engine will also load all the associated data (effects, attenuation, events, etc.).

The process of loading a sound bank is basicaly the following:

```cpp
AmBankID bankId = kAmInvalidObjectId;

// Load the sound bank 'init.ambank', and store its ID in 'bankId'
if (!amEngine->LoadSoundBank(AM_OS_STRING("init.ambank"), bankId))
  return 1;

// You can now use sound bank data
```

!!! info
    You can load as many sound bank as you want. If one of your asset (sound object, effects, attenuation, etc.) has been registered in more than one loaded sound bank, that asset will be loaded only once, and reference counted. The reference count will decrement each time you [unload sound banks](#unloading-a-sound-bank), and the asset's memory will be totally released once the last sound bank referencing it is unloaded.

## Loading sound files

At this point, the engine has only preloaded sound objects associated to the sound bank. The process of loading sound files is done manually, in another thread, so the main thread is ensured to not hang during this time.

During this process, only sound files with streaming disabled will be entirely read and stored in memory. Other sound files will read from the file system on playback.

```cpp
// Load sound files from sound objects registered in all loaded sound banks
amEngine->StartLoadSoundFiles();

// You can optionally wait for the loading to finish
while (!amEngine->TryFinalizeLoadSoundFiles())
  Thread::Sleep(1);

// You can now play sound objects
```

!!! note
    Audio data loaded in memory are shared across every [sound instances](../getting-started/concepts.md#sound-instances).

## Unloading sound banks

To unload a sound bank, you just need to call an `Engine` method with the name or the ID of the sound bank to unload.

```cpp
// Unload a sound bank with name
amEngine->UnloadSoundBank("init.ambank");

// Unload a sound bank with id
amEngine->UnloadSoundBank(1234);
```

Once the sound bank is unloaded, all the registered assets are released too. If one or more of these assets were loaded by more that one sound bank, their reference count will be decremented.