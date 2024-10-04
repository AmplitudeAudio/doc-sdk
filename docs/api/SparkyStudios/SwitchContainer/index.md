---
title: SwitchContainer
description: Amplitude Switch Container.
generator: doxide
---


# SwitchContainer

**class  SwitchContainer : public SoundObject , public Asset&lt;AmSwitchContainerID&gt;**


Amplitude Switch Container.

A switch container is a container sound object where sounds and collections can be registered on
one or multiple switches. Only one switch can be active at a time in a switch container. When a
switch is active, all the sounds and collections that are registered on it will be played.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [GetSwitch](#GetSwitch) | Returns the switch attached to this SwitchContainer. |
| [GetFaderIn](#GetFaderIn) | Get the fade in Fader for the given sound object ID. |
| [GetFaderOut](#GetFaderOut) | Get the fade out Fader for the given sound object ID. |
| [GetSoundObjects](#GetSoundObjects) | Returns the list of sound objects referenced in this SwitchContainer for the given state. |

## Function Details

### GetFaderIn<a name="GetFaderIn"></a>
!!! function "&#42; GetFaderIn(AmObjectID id) const"

    
    Get the fade in Fader for the given sound object ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the sound object.
    
    
    :material-keyboard-return: **Return**
    :    The fade in Fader.
            
    

### GetFaderOut<a name="GetFaderOut"></a>
!!! function "&#42; GetFaderOut(AmObjectID id) const"

    
    Get the fade out Fader for the given sound object ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the sound object.
    
    
    :material-keyboard-return: **Return**
    :    The fade out Fader.
            
    

### GetSoundObjects<a name="GetSoundObjects"></a>
!!! function "[[nodiscard]] virtual const std::vector&lt;SwitchContainerItem&gt;&amp; GetSoundObjects(AmObjectID stateId) const = 0"

    
    Returns the list of sound objects referenced in this SwitchContainer for the given state.
    
    
    :material-location-enter: **Parameter** `stateId`
    :    The switch state to get the objects for.
    
    
    :material-keyboard-return: **Return**
    :    The list of sound object IDs registered to the given state.
            
    

### GetSwitch<a name="GetSwitch"></a>
!!! function "&#42; GetSwitch() const"

    
    Returns the switch attached to this SwitchContainer.
    
    
    :material-keyboard-return: **Return**
    :    The switch of this SwitchContainer if available or nullptr.
            
    

