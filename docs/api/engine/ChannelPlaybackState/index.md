---
title: ChannelPlaybackState
description: Enumerates the playback states for a `Channel`.
generator: doxide
---


# ChannelPlaybackState

**enum class ChannelPlaybackState : AmUInt8**


Enumerates the playback states for a `Channel`.


    


**Stopped = 0**
:   The channel is stopped and not rendering audio.


**Playing = 1**
:   The channel is playing audio.


**FadingIn = 2**
:   The channel has just been played or resumed and is fading in to the `Playing` state.


**FadingOut = 3**
:   The channel has just been stopped or paused and is fading out to the `Stopped` or `Paused` state.


**SwitchingState = 4**
:   The channel is updating the value of his linked switch state.


**Paused = 5**
:   The channel is paused.



