---
title: Effect
description: Amplitude Effect Asset.
generator: doxide
---


# Effect

**class  Effect : public Asset&lt;AmEffectID&gt;**


Amplitude Effect Asset.

An effect is a sound filter applied to one or more sound objects
(sounds, collections, or switch containers) during playback.

Effects are customized using parameters and each parameters can be
updated at runtime using a `Rtpc`.


:material-eye-outline: **See**
:    [Rtpc](../Rtpc/index.md), [EffectInstance](../../engine/EffectInstance/index.md)


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Update](#Update) | Updates the effect parameters on each frames.  |
| [CreateInstance](#CreateInstance) | Creates an instance of this effect. |
| [DestroyInstance](#DestroyInstance) | Destroys an instance of this effect. |

## Function Details

### CreateInstance<a name="CreateInstance"></a>
!!! function "&#42; CreateInstance() const"

    
    Creates an instance of this effect.
    
    
    :material-keyboard-return: **Return**
    :    The effect instance.
            
    

### DestroyInstance<a name="DestroyInstance"></a>
!!! function "virtual void DestroyInstance(EffectInstance&#42; instance) const = 0"

    
    Destroys an instance of this effect.
    
    
    :material-location-enter: **Parameter** `instance`
    :    The effect instance to delete.
                
    

### Update<a name="Update"></a>
!!! function "virtual void Update() = 0"

    
    Updates the effect parameters on each frames.
             
    
    
    

