---
title: eChannelPlaybackState
description: Enumerates the playback states for a `Channel`.
generator: doxide
---


# eChannelPlaybackState

**enum eChannelPlaybackState : AmUInt8**


Enumerates the playback states for a `Channel`.


    


**eChannelPlaybackState_Stopped = 0**
:   
The channel is stopped and not rendering audio.
         




**eChannelPlaybackState_Playing = 1**
:   
The channel is playing audio.
         




**eChannelPlaybackState_FadingIn = 2**
:   
The channel has just been played or resumed and is fading in to the `Playing` state.
         




**eChannelPlaybackState_FadingOut = 3**
:   
The channel has just been stopped or paused and is fading out to the `Stopped` or `Paused` state.
         




**eChannelPlaybackState_SwitchingState = 4**
:   
The channel is updating the value of his linked switch state.
         




**eChannelPlaybackState_Paused = 5**
:   
The channel is playing audio but in a paused state.
         





