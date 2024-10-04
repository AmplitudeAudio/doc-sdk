---
title: Channel
description: An object that represents a single channel of audio.
generator: doxide
---


# Channel

**class  Channel**


An object that represents a single channel of audio.

The `Channel` class is a lightweight reference to a `ChannelInternalState` object
which is managed by the Engine. Multiple channels may point to the same
underlying data.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Channel](#Channel) | Construct an uninitialized `Channel`. |
| [Channel](#Channel) | Creates a wrapper instance over the provided state. |
| [Clear](#Clear) | Uninitializes this `Channel`. |
| [Valid](#Valid) | Checks whether this `Channel` has been initialized. |
| [GetId](#GetId) | Gets the ID of this `Channel`. |
| [Playing](#Playing) | Checks if the sound associated to this `Channel` is playing. |
| [Stop](#Stop) | Stops the `Channel`. |
| [Pause](#Pause) | Pauses the `Channel`. |
| [Resume](#Resume) | Resumes the `Channel`. |
| [GetLocation](#GetLocation) | Gets the location of this `Channel`. |
| [SetLocation](#SetLocation) | Sets the location of this `Channel`. |
| [SetGain](#SetGain) | Sets the gain on this `Channel`. |
| [GetGain](#GetGain) | Returns the gain on this `Channel`. |
| [GetPlaybackState](#GetPlaybackState) | Returns the playback state of this `Channel`. |
| [GetEntity](#GetEntity) | Returns the `Entity` associated with this `Channel`. |
| [GetListener](#GetListener) | Returns the `Listener` associated with this `Channel`. |
| [GetRoom](#GetRoom) | Returns the `Room` associated with this `Channel`. |
| [GetState](#GetState) | Returns the internal state of this Channel. |
| [On](#On) | Registers a callback for a channel event. |

## Function Details

### Channel<a name="Channel"></a>
!!! function "Channel()"

    
    Construct an uninitialized `Channel`.
    
    An uninitialized `Channel` cannot have its data set or queried.
            
    

!!! function "explicit Channel(ChannelInternalState&#42; state)"

    
    Creates a wrapper instance over the provided state.
    
    
    :material-location-enter: **Parameter** `state`
    :    The internal state to wrap.
    
    
    !!! warning
         This constructor is for internal usage only.
                
    

### Clear<a name="Clear"></a>
!!! function "void Clear()"

    
    Uninitializes this `Channel`.
    
    Note that this does not stop the audio or destroy the internal
    state it references, it just removes this reference to it.
            
    

### GetEntity<a name="GetEntity"></a>
!!! function "[[nodiscard]] Entity GetEntity() const"

    
    Returns the `Entity` associated with this `Channel`.
    
    
    !!! note
         If no `Entity` is associated with this `Channel`, this method will return an
        uninitialized `Entity` object. You should check if the entity is valid before using it.
    
    
    :material-keyboard-return: **Return**
    :    The entity associated with this `Channel`.
    
    
    :material-eye-outline: **See**
    :    Entity
            
    

### GetGain<a name="GetGain"></a>
!!! function "[[nodiscard]] AmReal32 GetGain() const"

    
    Returns the gain on this `Channel`.
    
    
    :material-keyboard-return: **Return**
    :    The channel's gain.
            
    

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmUInt64 GetId() const"

    
    Gets the ID of this `Channel`.
    
    
    :material-keyboard-return: **Return**
    :    The ID of this `Channel`.
            
    

### GetListener<a name="GetListener"></a>
!!! function "[[nodiscard]] Listener GetListener() const"

    
    Returns the `Listener` associated with this `Channel`.
    
    
    !!! note
         If no `Listener` is associated with this `Channel`, this method will return an
        uninitialized `Listener` object. You should check if the listener is valid before using it.
    
    
    :material-keyboard-return: **Return**
    :    The listener associated with this `Channel`.
    
    
    :material-eye-outline: **See**
    :    Listener
            
    

### GetLocation<a name="GetLocation"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetLocation() const"

    
    Gets the location of this `Channel`.
    
    If the audio on this channel is not set to be Positional, this method will
    return an invalid location.
    
    
    :material-keyboard-return: **Return**
    :    The location of this `Channel`.
            
    

### GetPlaybackState<a name="GetPlaybackState"></a>
!!! function "[[nodiscard]] ChannelPlaybackState GetPlaybackState() const"

    
    Returns the playback state of this `Channel`.
    
    
    :material-keyboard-return: **Return**
    :    A `ChannelPlaybackState` enumeration value representing the current state of the `Channel`.
            
    

### GetRoom<a name="GetRoom"></a>
!!! function "[[nodiscard]] Room GetRoom() const"

    
    Returns the `Room` associated with this `Channel`.
    
    
    !!! note
         If no `Room` is associated with this `Channel`, this method will return an
        uninitialized `Room` object. You should check if the room is valid before using it.
    
    
    :material-keyboard-return: **Return**
    :    The room associated with this Channel.
            
    

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] ChannelInternalState&#42; GetState() const"

    
    Returns the internal state of this Channel.
    
    
    :material-keyboard-return: **Return**
    :    The internal state of this Channel.
    
    
    !!! warning
         This method is for internal usage only.
                
    

### On<a name="On"></a>
!!! function "void On(ChannelEvent event, ChannelEventCallback callback, void&#42; userData = nullptr) const"

    
    Registers a callback for a channel event.
    
    
    :material-location-enter: **Parameter** `event`
    :    The channel event.
        
    :material-location-enter: **Parameter** `callback`
    :    The callback function.
        
    :material-location-enter: **Parameter** `userData`
    :    The user data to pass to the callback.
    
    
    :material-eye-outline: **See**
    :    ChannelEvent
    
    :material-eye-outline: **See**
    :    ChannelEventCallback
            
    

### Pause<a name="Pause"></a>
!!! function "void Pause(AmTime duration = kMinFadeDuration) const"

    
    Pauses the `Channel`.
    
    A paused channel may be resumed where it left off.
    
    
    :material-location-enter: **Parameter** `duration`
    :    The fade out duration before to pause the channel.
                
    

### Playing<a name="Playing"></a>
!!! function "[[nodiscard]] bool Playing() const"

    
    Checks if the sound associated to this `Channel` is playing.
    
    
    :material-keyboard-return: **Return**
    :    Whether the channel is currently playing.
            
    

### Resume<a name="Resume"></a>
!!! function "void Resume(AmTime duration = kMinFadeDuration) const"

    
    Resumes the `Channel`.
    
    If this channel was paused it will continue where it left off.
    
    
    :material-location-enter: **Parameter** `duration`
    :    The fade in duration after resuming the channel.
                
    

### SetGain<a name="SetGain"></a>
!!! function "void SetGain(AmReal32 gain) const"

    
    Sets the gain on this `Channel`.
    
    
    :material-location-enter: **Parameter** `gain`
    :    The new gain value.
                
    

### SetLocation<a name="SetLocation"></a>
!!! function "void SetLocation(const AmVec3&amp; location) const"

    
    Sets the location of this `Channel`.
    
    If the audio on this channel is not set to be Positional, this method
    does nothing.
    
    
    :material-location-enter: **Parameter** `location`
    :    The new location of the `Channel`.
                
    

### Stop<a name="Stop"></a>
!!! function "void Stop(AmTime duration = kMinFadeDuration) const"

    
    Stops the `Channel`.
    
    A sound will stop on its own if its not set to loop. Looped audio must be explicitly stopped.
    
    
    :material-location-enter: **Parameter** `duration`
    :    The fade out duration before to stop the channel.
                
    

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this `Channel` has been initialized.
    
    
    :material-keyboard-return: **Return**
    :    `true` if this `Channel` has been initialized.
            
    

