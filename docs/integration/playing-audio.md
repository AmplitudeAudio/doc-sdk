---
title: Playing audio
description: Use the Channel API to play and manage sound sources. You can listen to playback events to run actions in realtime
---

!!! danger "Incomplete Documentation"
    This documentation page is WIP and not yet complete. You can have a complete demo on how to interact with the engine through the official [sample projects](https://github.com/AmplitudeAudio/sdk/blob/develop/samples).

Each time you play a [sound object], you have a [Channel](../getting-started/concepts.md#channels) that will help you manage the playback of that sound object.

To play an audio, you need either its name, its id, or an handle to its sound object instance, and then use any overrides of the [`Play()`](../api/engine/Engine/index.md#Play) method in the `Engine`

```cpp
// Using the name
Channel sound = amEngine->Play("dialogue_01");

// Using the ID
Channel sound = amEngine->Play(1234);

// Using an handle
SoundHandle handle = amEngine->GetSoundHandle(1234); // or amEngine->GetSoundHandle("dialogue_01")
Channel sound = amEngine->Play(handle);
```

!!! tip
    Playing a sound object using an handle is always faster than using its name or its ID. Thus, it's recommended to prefer using handles for sound objects you plan to frequently play.

## Handles

There are many handle types, each corresponding to a specific [sound object].

```cpp
// Sounds
SoundHandle backgroundSound = amEngine->GetSoundHandle("bg_forest");

// Collections
CollectionHandle gunFires = amEngine->GetCollectionHandle("ak47_gunfires");

// Switch Containers
SwitchContainerHandle footsteps = amEngine->GetSwitchContainerHandle("footsteps");
```

In the case you don't care about your sound object type and want a generic sound object handle, you can do it by using the [`GetSoundObjectHandle()`](../api/engine/Engine/index.md#GetSoundObjectHandle) method. The returned handle will be one of the previous ones, according to the type of sound object you are querying.

```cpp
// Get a generic sound handle
SoundObjectHandle handle = amEnigne->GetSoundObjectHandle("dialogue_01");
```

!!! note
    When using the `GetSoundObjectHandle()` method, Amplitude will scan your assets in this order: **Sounds**, then **Collections**, and then **Switch Containers**.

It's always safe to check if your handle is valid before using it. Once you get your handle, you can check for its validity by comparing it to the [`AM_INVALID_HANDLE`](../api/engine/index.md#AM_INVALID_HANDLE) macro, or by directly using the [`AM_IS_VALID_HANDLE`](../api/engine/index.md#AM_IS_VALID_HANDLE) macro function.

```cpp
// Get an handle
auto handle = amEngine->GetSoundHandle("footsteps"); // This is instead a switch container, but we are querying it as a sound, which will return an invalid handle

if (handle == AM_INVALID_HANDLE)
    amLogError("The returned handle is invalid");

// Same as doing
if (AM_IS_VALID_HANDLE(handle))
    amLogError("The returned handle is invalid");
```

[sound object]: ../project/sound-object.md