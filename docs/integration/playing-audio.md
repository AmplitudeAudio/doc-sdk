---
title: Playing audio
description: Use the Channel API to play and manage sound sources. You can listen to playback events to run actions in realtime
---

!!! danger "Incomplete Documentation"
    This documentation page is WIP and not yet complete. You can have a complete demo on how to interact with the engine through the official [sample projects](https://github.com/AmplitudeAudio/sdk/blob/develop/samples).

Each time you play a [sound object](../project/sound-object.md), you have a [Channel](../getting-started/concepts.md#channels) that will help you manage the playback of that sound object.

To play an audio, you need either its name, its id, or an handle to its sound object instance, and then use any overrides of the [`Play()`](../api/engine/Engine/index.md#playa-nameplaya) method in the `Engine`

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
