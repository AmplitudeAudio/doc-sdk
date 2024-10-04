---
title: SoundObject
description: The SoundObject class is the base class for all sound objects. 
generator: doxide
---


# SoundObject

**class  SoundObject**


The SoundObject class is the base class for all sound objects.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [GetGain](#GetGain) | Gets the linear gain of the sound object. |
| [GetPitch](#GetPitch) | Gets the actual pitch of the sound object. |
| [GetPriority](#GetPriority) | Gets the actual priority of the sound object. |
| [GetEffect](#GetEffect) | Get the Effect object associated with this sound object. |
| [GetAttenuation](#GetAttenuation) | Get the Attenuation object associated with this sound object. |
| [GetBus](#GetBus) | Return the bus this sound object will play on. |

## Function Details

### GetAttenuation<a name="GetAttenuation"></a>
!!! function "&#42; GetAttenuation() const"

    
    Get the Attenuation object associated with this sound object.
    
    
    :material-keyboard-return: **Return**
    :    The Attenuation object.
            
    

### GetBus<a name="GetBus"></a>
!!! function "[[nodiscard]] virtual Bus GetBus() const = 0"

    
    Return the bus this sound object will play on.
    
    
    :material-keyboard-return: **Return**
    :    The bus this sound object will play on.
            
    

### GetEffect<a name="GetEffect"></a>
!!! function "&#42; GetEffect() const"

    
    Get the Effect object associated with this sound object.
    
    
    :material-keyboard-return: **Return**
    :    The Effect object.
            
    

### GetGain<a name="GetGain"></a>
!!! function "[[nodiscard]] virtual const RtpcValue&amp; GetGain() const = 0"

    
    Gets the linear gain of the sound object.
    
    
    :material-keyboard-return: **Return**
    :    The sound object linear gain.
            
    

### GetPitch<a name="GetPitch"></a>
!!! function "[[nodiscard]] virtual const RtpcValue&amp; GetPitch() const = 0"

    
    Gets the actual pitch of the sound object.
    
    
    :material-keyboard-return: **Return**
    :    The sound object pitch.
            
    

### GetPriority<a name="GetPriority"></a>
!!! function "[[nodiscard]] virtual const RtpcValue&amp; GetPriority() const = 0"

    
    Gets the actual priority of the sound object.
    
    
    :material-keyboard-return: **Return**
    :    The sound object priority.
            
    

