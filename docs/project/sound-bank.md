---
title: Sound Bank
description: Sound banks are units that bundle together all the audio assets your game needs to load and play at runtime.
---

A sound bank groups together references to all the assets your game needs at runtime — sounds, collections, switch containers, events, effects, attenuations, switches, and RTPCs. By loading a sound bank, the engine registers all its referenced assets and makes them available for playback.

!!! info
    The FlatBuffers schema of this file can be found [here](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/sound_bank_definition.fbs).

A sound bank file contains the following properties:

## id

`uint64` `required`

A unique identifier for the sound bank. This value is used to reference the sound bank at runtime when loading or unloading it. This value should be different from `0`.

## name

`string` `required`

A unique name for the sound bank. This can also be used at runtime to reference the sound bank.

## sounds

`string[]` `optional`

An array of [Sound](./sound.md) asset file names to include in this sound bank. Each entry is the compiled binary file name (`.amsound` extension).

## collections

`string[]` `optional`

An array of [Collection](./collection.md) asset file names to include in this sound bank.

## switch_containers

`string[]` `optional`

An array of [Switch Container](./switch-container.md) asset file names to include in this sound bank.

## events

`string[]` `optional`

An array of [Event](./event.md) asset file names to include in this sound bank.

## attenuators

`string[]` `optional`

An array of [Attenuation](./attenuation-model.md) asset file names to include in this sound bank.

## switches

`string[]` `optional`

An array of [Switch](./switch.md) asset file names to include in this sound bank.

## rtpc

`string[]` `optional`

An array of [RTPC](./rtpc.md) asset file names to include in this sound bank.

## effects

`string[]` `optional`

An array of [Effect](./effect.md) asset file names to include in this sound bank.

## Reference Counting

Assets are reference-counted across sound banks. If the same asset is referenced by multiple loaded sound banks, it is only loaded into memory once. Its reference count decrements each time a sound bank referencing it is unloaded, and the asset's memory is released when the last sound bank referencing it is unloaded.

This means you can organize your sound banks however best fits your game — by level, by category, or by feature — without worrying about duplicating memory for shared assets.

## Example

A sound bank that loads background music, footstep sounds with surface-type switching, and a set of effects:

```json
{
  "id": 1,
  "name": "init",
  "switch_containers": [
    "footsteps.amswitchcontainer"
  ],
  "collections": [
    "grass_footsteps.amcollection",
    "metal_footsteps.amcollection",
    "snow_footsteps.amcollection"
  ],
  "sounds": [
    "background/AMBForst_Forest.wav.amsound"
  ],
  "events": [
    "play_throw.amevent",
    "stop_throw.amevent"
  ],
  "attenuators": [
    "impact.amattenuation",
    "room.amattenuation"
  ],
  "switches": [
    "surface_type.amswitch"
  ],
  "rtpc": [
    "wind_force.amrtpc"
  ],
  "effects": [
    "delay.amfx",
    "equalizer.amfx"
  ]
}
```

!!! tip
    Each entry in the arrays uses the compiled binary file name, not the source JSON file name. [Compile your project](../integration/compiling-amplitude-project.md) to generate these binary assets from your JSON source files.

## Loading at Runtime

Once your sound bank is compiled, load it at runtime using the engine API:

```cpp
// Load the sound bank (synchronous — returns true on success)
AmBankID bankId = kAmInvalidObjectId;
if (!amEngine->LoadSoundBank(AM_OS_STRING("init.ambank"), bankId))
{
    amLogError("Failed to load sound bank");
}

// Start loading the actual audio data (asynchronous)
amEngine->StartLoadSoundFiles();
while (!amEngine->TryFinalizeLoadSoundFiles())
    Thread::Sleep(1);

// Unload when no longer needed
amEngine->UnloadSoundBank(bankId);
// Or by filename:
amEngine->UnloadSoundBank(AM_OS_STRING("init.ambank"));
```

See [Loading Sound Banks](../integration/loading-sound-banks.md) for the full loading workflow.
