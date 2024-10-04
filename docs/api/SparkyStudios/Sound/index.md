---
title: Sound
description: Amplitude Sound.
generator: doxide
---


# Sound

**class  Sound : public SoundObject , public Resource , public Asset&lt;AmSoundID&gt;**


Amplitude Sound.

A Sound is the most basic sound object in Amplitude. It can be used to directly play an audio file,
or can be contained in a *SwitchContainer* or a *Collection* for a fine-grained control.

Effects can be attached to a Sound, which will be applied to all instances of the sound in the EffectProcessor
of the Amplimix pipeline.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [IsStream](#IsStream) | Checks streaming is enabled for this Sound. |
| [IsLoop](#IsLoop) | Checks if looping is enabled for this Sound. |
| [GetNearFieldGain](#GetNearFieldGain) | Gets the near field effect gain of the sound object. |

## Function Details

### GetNearFieldGain<a name="GetNearFieldGain"></a>
!!! function "[[nodiscard]] virtual const RtpcValue&amp; GetNearFieldGain() const = 0"

    
    Gets the near field effect gain of the sound object.
    
    
    :material-keyboard-return: **Return**
    :    The sound object near field effect gain.
            
    

### IsLoop<a name="IsLoop"></a>
!!! function "[[nodiscard]] virtual bool IsLoop() const = 0"

    
    Checks if looping is enabled for this Sound.
    
    
    :material-keyboard-return: **Return**
    :    true if looping is enabled, false otherwise.
            
    

### IsStream<a name="IsStream"></a>
!!! function "[[nodiscard]] virtual bool IsStream() const = 0"

    
    Checks streaming is enabled for this Sound.
    
    
    :material-keyboard-return: **Return**
    :    true if streaming is enabled, false otherwise.
            
    

