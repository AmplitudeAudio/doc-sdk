---
title: AmplimixLayer
description: A single layer in the mixer.
generator: doxide
---


# AmplimixLayer

**class  AmplimixLayer**


A single layer in the mixer.

A mixer layer is a container for audio data and associated properties. Each layer is linked
to a single `SoundInstance`, and manage its life cycle inside `Amplimix`.


:material-eye-outline: **See**
:    [SoundInstance](../../engine/SoundInstance/index.md), [Amplimix](../Amplimix/index.md)


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~AmplimixLayer](#_u007eAmplimixLayer) | Default destructor.  |
| [GetId](#GetId) | Gets the unique identifier of the layer. |
| [GetStartPosition](#GetStartPosition) | Gets the start position of the audio data in the layer. |
| [GetEndPosition](#GetEndPosition) | Gets the end position of the audio data in the layer. |
| [GetCurrentPosition](#GetCurrentPosition) | Gets the current position of the audio data in the layer. |
| [GetGain](#GetGain) | Gets the final gain of the audio data in the layer. |
| [GetStereoPan](#GetStereoPan) | Gets the stereo pan of the audio data in the layer. |
| [GetPitch](#GetPitch) | Gets the pitch of the audio data in the layer. |
| [GetObstruction](#GetObstruction) | Gets the obstruction amount of the audio data in the layer. |
| [GetOcclusion](#GetOcclusion) | Gets the occlusion amount of the audio data in the layer. |
| [GetPlaySpeed](#GetPlaySpeed) | Gets the play speed of the audio data in the layer. |
| [GetLocation](#GetLocation) | Gets the location of the audio data in the layer. |
| [GetEntity](#GetEntity) | Gets the entity associated with the audio data in the layer. |
| [GetListener](#GetListener) | Gets the listener currently rendering the audio data in the layer. |
| [GetRoom](#GetRoom) | Gets the room in which the audio data in the layer is currently located. |
| [GetChannel](#GetChannel) | Gets the channel managing the audio data in the layer. |
| [GetBus](#GetBus) | Gets the bus on which the audio data in the layer is playing. |
| [GetSoundFormat](#GetSoundFormat) | Gets the sound format of the audio data in the layer. |
| [GetSpatialization](#GetSpatialization) | Gets the spatialization mode of the audio data in the layer. |
| [IsLoopEnabled](#IsLoopEnabled) | Checks if the audio data in the layer is looping. |
| [IsStreamEnabled](#IsStreamEnabled) | Checks if the audio data in the layer is streaming from the file system. |
| [GetSound](#GetSound) | Gets the sound associated with the audio data in the layer. |
| [GetEffect](#GetEffect) | Gets the effect associated with the audio data in the layer. |
| [GetAttenuation](#GetAttenuation) | Gets the attenuation associated with the audio data in the layer. |
| [GetSampleRate](#GetSampleRate) | Gets the current sample rate of the audio data in the layer. |

## Function Details

### GetAttenuation<a name="GetAttenuation"></a>
!!! function "&#42; GetAttenuation() const"

    
    Gets the attenuation associated with the audio data in the layer.
    
    
    :material-keyboard-return: **Return**
    :    The attenuation associated with the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [Attenuation](../../assets/Attenuation/index.md)
            
    

### GetBus<a name="GetBus"></a>
!!! function "virtual Bus GetBus() const = 0"

    
    Gets the bus on which the audio data in the layer is playing.
    
    
    :material-keyboard-return: **Return**
    :    The bus on which the audio data in the layer is playing.
    
    
    :material-eye-outline: **See**
    :    [Bus](../../engine/Bus/index.md)
            
    

### GetChannel<a name="GetChannel"></a>
!!! function "virtual Channel GetChannel() const = 0"

    
    Gets the channel managing the audio data in the layer.
    
    Multiple layers can be linked to the same `Channel`.
    
    
    :material-keyboard-return: **Return**
    :    The channel managing the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [Channel](../../engine/Channel/index.md)
            
    

### GetCurrentPosition<a name="GetCurrentPosition"></a>
!!! function "virtual AmUInt64 GetCurrentPosition() const = 0"

    
    Gets the current position of the audio data in the layer.
    
    This position is in samples, not bytes. It represents the current offset from the start of the
    linked sound data, where the mixer is currently playing audio.
    
    
    :material-keyboard-return: **Return**
    :    The current playback position of the audio data in the layer.
            
    

### GetEffect<a name="GetEffect"></a>
!!! function "&#42; GetEffect() const"

    
    Gets the effect associated with the audio data in the layer.
    
    
    :material-keyboard-return: **Return**
    :    The effect associated with the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [EffectInstance](../../engine/EffectInstance/index.md), [Effect](../../assets/Effect/index.md)
            
    

### GetEndPosition<a name="GetEndPosition"></a>
!!! function "virtual AmUInt64 GetEndPosition() const = 0"

    
    Gets the end position of the audio data in the layer.
    
    This position is in samples, not bytes. It represents the offset from the start of the
    linked sound data, where the mixer should stop playing audio.
    
    
    :material-keyboard-return: **Return**
    :    The end position of the audio data in the layer.
            
    

### GetEntity<a name="GetEntity"></a>
!!! function "virtual Entity GetEntity() const = 0"

    
    Gets the entity associated with the audio data in the layer.
    
    
    :material-keyboard-return: **Return**
    :    The entity associated with the audio data in the layer. If the layer is not associated with
    an `Entity`, an invalid entity is returned.
    
    
    :material-eye-outline: **See**
    :    [Entity](../../engine/Entity/index.md)
            
    

### GetGain<a name="GetGain"></a>
!!! function "virtual AmReal32 GetGain() const = 0"

    
    Gets the final gain of the audio data in the layer.
    
    
    :material-keyboard-return: **Return**
    :    The final gain of the audio data in the layer.
            
    

### GetId<a name="GetId"></a>
!!! function "virtual AmUInt32 GetId() const = 0"

    
    Gets the unique identifier of the layer.
    
    
    :material-keyboard-return: **Return**
    :    The unique identifier of the layer.
            
    

### GetListener<a name="GetListener"></a>
!!! function "virtual Listener GetListener() const = 0"

    
    Gets the listener currently rendering the audio data in the layer.
    
    
    :material-keyboard-return: **Return**
    :    The listener currently rendering the audio data in the layer. If the layer is not associated with
    a `Listener`, an invalid listener is returned.
    
    
    :material-eye-outline: **See**
    :    [Listener](../../engine/Listener/index.md)
            
    

### GetLocation<a name="GetLocation"></a>
!!! function "virtual AmVec3 GetLocation() const = 0"

    
    Gets the location of the audio data in the layer.
    
    The location is expressed as a 3D vector in the global space. For sound instances linked
    to an `Entity`, the location of that entity is returned instead.
    
    
    :material-keyboard-return: **Return**
    :    The location of the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [Entity](../../engine/Entity/index.md)
            
    

### GetObstruction<a name="GetObstruction"></a>
!!! function "virtual AmReal32 GetObstruction() const = 0"

    
    Gets the obstruction amount of the audio data in the layer.
    
    This value is useful only when the layer is associated with a sound instance that has spatialization enabled. You
    can update this value using the `SetObstruction` method from the `Entity` this layer is associated with.
    
    
    :material-keyboard-return: **Return**
    :    The obstruction amount of the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [Entity](../../engine/Entity/index.md)
            
    

### GetOcclusion<a name="GetOcclusion"></a>
!!! function "virtual AmReal32 GetOcclusion() const = 0"

    
    Gets the occlusion amount of the audio data in the layer.
    
    This value is useful only when the layer is associated with a sound instance that has spatialization enabled. You
    can update this value using the `SetOcclusion` method from the `Entity` this layer is associated with.
    
    
    :material-keyboard-return: **Return**
    :    The occlusion amount of the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [Entity](../../engine/Entity/index.md)
            
    

### GetPitch<a name="GetPitch"></a>
!!! function "virtual AmReal32 GetPitch() const = 0"

    
    Gets the pitch of the audio data in the layer.
    
    This value is affected by the Doppler effect. A value of 1.0 will play the audio data at its original pitch,
    while any value greater than 1.0 will increase the pitch, and any value less than 1.0 will decrease the pitch.
    
    
    :material-keyboard-return: **Return**
    :    The pitch of the audio data in the layer.
            
    

### GetPlaySpeed<a name="GetPlaySpeed"></a>
!!! function "virtual AmReal32 GetPlaySpeed() const = 0"

    
    Gets the play speed of the audio data in the layer.
    
    This values affects the final [pitch.](#GetPitch)
    
    
    :material-keyboard-return: **Return**
    :    The play speed of the audio data in the layer.
            
    

### GetRoom<a name="GetRoom"></a>
!!! function "virtual Room GetRoom() const = 0"

    
    Gets the room in which the audio data in the layer is currently located.
    
    
    :material-keyboard-return: **Return**
    :    The room in which the audio data in the layer is currently located. If the layer is not located
    in a `Room`, an invalid room is returned.
    
    
    :material-eye-outline: **See**
    :    [Room](../../engine/Room/index.md)
            
    

### GetSampleRate<a name="GetSampleRate"></a>
!!! function "virtual AmUInt32 GetSampleRate() const = 0"

    
    Gets the current sample rate of the audio data in the layer.
    
    The current sample rate of the audio data in the layer can be different from the original sample rate
    stored in the sound format. Its value may change due to the Doppler effect, or due to an internal
    sample rate conversion to match the one specified in the loaded engine configuration.
    
    
    :material-keyboard-return: **Return**
    :    The current sample rate of the audio data in the layer.
            
    

### GetSound<a name="GetSound"></a>
!!! function "&#42; GetSound() const"

    
    Gets the sound associated with the audio data in the layer.
    
    
    :material-keyboard-return: **Return**
    :    The sound associated with the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [Sound](../../assets/Sound/index.md)
            
    

### GetSoundFormat<a name="GetSoundFormat"></a>
!!! function "virtual SoundFormat GetSoundFormat() const = 0"

    
    Gets the sound format of the audio data in the layer.
    
    The sound format specifies the number of channels, sample rate, and other audio properties. It is
    filled by the `Codec` that handled the decoding of the audio data.
    
    
    :material-keyboard-return: **Return**
    :    The sound format of the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [SoundFormat](../../core/SoundFormat/index.md), [Codec](../../engine/Codec/index.md)
            
    

### GetSpatialization<a name="GetSpatialization"></a>
!!! function "virtual eSpatialization GetSpatialization() const = 0"

    
    Gets the spatialization mode of the audio data in the layer.
    
    The spatialization mode determines how the audio data in the layer is processed to produce a stereoscopic
    sound. This value must be set in the asset file of the sound object.
    
    
    :material-keyboard-return: **Return**
    :    The spatialization mode of the audio data in the layer.
    
    
    :material-eye-outline: **See**
    :    [eSpatialization](../../core/eSpatialization/index.md)
            
    

### GetStartPosition<a name="GetStartPosition"></a>
!!! function "virtual AmUInt64 GetStartPosition() const = 0"

    
    Gets the start position of the audio data in the layer.
    
    This position is in samples, not bytes. It represents the offset from the start of the
    linked sound data, where the mixer should start playing audio.
    
    
    :material-keyboard-return: **Return**
    :    The start position of the audio data in the layer.
            
    

### GetStereoPan<a name="GetStereoPan"></a>
!!! function "virtual AmReal32 GetStereoPan() const = 0"

    
    Gets the stereo pan of the audio data in the layer.
    
    The stereo pan of the audio data in the layer is a value between -1.0 (left) and 1.0 (right). A
    value of -1.0 will render the audio data to the left speaker, a value of 1.0 will render the audio data
    to the right speaker, and a value of 0.0 will render the audio data to the center speaker.
    
    
    :material-keyboard-return: **Return**
    :    The stereo pan of the audio data in the layer.
            
    

### IsLoopEnabled<a name="IsLoopEnabled"></a>
!!! function "virtual bool IsLoopEnabled() const = 0"

    
    Checks if the audio data in the layer is looping.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the audio data in the layer is looping, `false` otherwise.
            
    

### IsStreamEnabled<a name="IsStreamEnabled"></a>
!!! function "virtual bool IsStreamEnabled() const = 0"

    
    Checks if the audio data in the layer is streaming from the file system.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the audio data in the layer is streaming from the file system, `false` otherwise.
            
    

### ~AmplimixLayer<a name="_u007eAmplimixLayer"></a>
!!! function "virtual ~AmplimixLayer() = default"

    
    Default destructor.
             
    
    
    

