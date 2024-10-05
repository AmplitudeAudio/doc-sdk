---
title: SoundObject
description: Base class for Amplitude sound objects.
generator: doxide
---


# SoundObject

**class  SoundObject**


Base class for Amplitude sound objects.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~SoundObject](#_u007eSoundObject) | Default destructor.  |
| [GetGain](#GetGain) | Gets the linear gain of the sound object. |
| [GetPitch](#GetPitch) | Gets the actual pitch of the sound object. |
| [GetPriority](#GetPriority) | Gets the actual priority of the sound object. |
| [GetEffect](#GetEffect) | Gets the Effect object associated with this sound object. |
| [GetAttenuation](#GetAttenuation) | Gets the Attenuation object associated with this sound object. |
| [GetBus](#GetBus) | Returns the bus this sound object will play on. |

## Function Details

### GetAttenuation<a name="GetAttenuation"></a>
!!! function "&#42; GetAttenuation() const"

    
    Gets the Attenuation object associated with this sound object.
    
    
    :material-keyboard-return: **Return**
    :    The Attenuation object.
            
    

### GetBus<a name="GetBus"></a>
!!! function "[[nodiscard]] virtual Bus GetBus() const = 0"

    
    Returns the bus this sound object will play on.
    
    
    :material-keyboard-return: **Return**
    :    The bus this sound object will play on.
            
    

### GetEffect<a name="GetEffect"></a>
!!! function "&#42; GetEffect() const"

    
    Gets the Effect object associated with this sound object.
    
    
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
            
    

### ~SoundObject<a name="_u007eSoundObject"></a>
!!! function "virtual ~SoundObject() = default"

    
    Default destructor.
             
    
    
    

