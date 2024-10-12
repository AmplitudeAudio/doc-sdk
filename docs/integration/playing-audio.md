---
title: Playing audio
description: Use the Channel API to play and manage sound sources. You also have the ability to listen to playback events and run actions in realtime.
---

## Handles

Handles represent an instance to specific sound object. There are many handle types, each of them corresponding to a [sound object] type.

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
SoundObjectHandle handle = amEngine->GetSoundObjectHandle("dialogue_01");
```

!!! note
    When using the `GetSoundObjectHandle()` method, Amplitude will scan your assets in this order: **Sounds**, then **Collections**, and then **Switch Containers**.

It's always safe to check if your handle is valid before using it. Once you get your handle, you can check for its validity by comparing it to the [`AM_INVALID_HANDLE`](../api/engine/index.md#AM_INVALID_HANDLE) macro, or by directly using the [`AM_IS_VALID_HANDLE()`](../api/engine/index.md#AM_IS_VALID_HANDLE) macro function.

```cpp
// Get an handle
auto handle = amEngine->GetSoundHandle("footsteps"); // This is instead a switch container, but we are querying it as a sound, which will return an invalid handle

if (handle == AM_INVALID_HANDLE)
    amLogError("The returned handle is invalid");

// Same as doing
if (!AM_IS_VALID_HANDLE(handle))
    amLogError("The returned handle is invalid");
```

## Channels

Each time you play a [sound object], you have a [Channel] that will help you manage the playback of that sound object.

To play an audio, you need either its name, its ID, or a [handle](#handles) to its sound object instance, and then use any overrides of the [`Play()`](../api/engine/Engine/index.md#Play) method in the `Engine`

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
    Playing a sound object using a handle is always faster than using its name or its ID. Thus, it's recommended to prefer using handles for sound objects you plan to frequently play.

When you obtain a Channel for a sound object, it's recommended to check if the returned Channel is valid before using it.

```cpp
// Get a channel
Channel sound = amEngine->Play(1234);

// Check if the channel is valid
if (sound.Valid())
    amLogError("The returned channel is not valid");
```

!!! info
    Amplitude may return an invalid Channel when the maximum number of channels is exceeded, or the requested sound object was not found in any loaded sound bank.

Using a Channel, you can manage the playback state and other sound object properties:

```cpp
// Check whether the sound object in the channel is currently playing
bool isPlaying = channel.Playing();

// Stop the playback
channel.Stop();

// Pause the playback
channel.Pause();

// Resume the playback
channel.Resume();

// Get the current location of the sound object
AmVec3 location = channel.GetLocation();

// Set the sound object location
channel.SetLocation(newLocation);

// Get the current playback state of the channel
ChannelPlaybackState state = channel.GetPlaybackState(); // Either Playing, Paused, Stopped, FadingIn, or FadingOut
```

!!! tip "API Reference available"
    Check out the [API Reference](../api/engine/Channel/index.md) to see the complete list of methods you can use with a Channel.

## Playback Events

Amplitude allows you to register callbacks for notable playback events within a Channel:

```cpp
// Add a callback when the playback has started
channel.On(ChannelEvent::Begin, [](ChannelEventInfo info) {
    amLogDebug("Playback started");
});

// Add a callback when the playback is paused
channel.On(ChannelEvent::Pause, [](ChannelEventInfo info) {
    amLogDebug("Playback paused");
});

// Add a callback when the playback is resumed
channel.On(ChannelEvent::Resume, [](ChannelEventInfo info) {
    amLogDebug("Playback resumed");
});

// Add a callback when the playback is stopped
channel.On(ChannelEvent::Stop, [](ChannelEventInfo info) {
    amLogDebug("Playback stopped");
});

// Add a callback when the playback has looped
channel.On(ChannelEvent::Loop, [](ChannelEventInfo info) {
    amLogDebug("Playback looped");
});

// Add a callback when the playback has ended
channel.On(ChannelEvent::End, [](ChannelEventInfo info) {
    amLogDebug("Playback ended");
});
```

!!! tip "API Reference available"
    You can also pass arbitrary data to the method and access it in the callback using the event `info`. Check out the [Channel API Reference](../api/engine/Channel/index.md#on) and the [ChannelEventInfo API Reference](../api/engine/ChannelEventInfo/index.md) to lean more.

[sound object]: ../project/sound-object.md
[Channel]: ../getting-started/concepts.md#channels