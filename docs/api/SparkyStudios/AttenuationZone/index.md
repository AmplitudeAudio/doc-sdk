---
title: AttenuationZone
description: The propagation shape for positional sounds.
generator: doxide
---


# AttenuationZone

**class  AttenuationZone**


The propagation shape for positional sounds.

This allows to increase the attenuation according to the shape of
the sound propagation.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [GetAttenuationFactor](#GetAttenuationFactor) | Returns the attenuation factor. |
| [GetAttenuationFactor](#GetAttenuationFactor) | Returns the attenuation factor. |

## Function Details

### GetAttenuationFactor<a name="GetAttenuationFactor"></a>
!!! function "virtual AmReal32 GetAttenuationFactor(const Attenuation&#42; attenuation, const AmVec3&amp; soundLocation, const Listener&amp; listener) = 0"

    
    Returns the attenuation factor.
    
    This method is used only for position based sound sources.
    
    
    :material-location-enter: **Parameter** `attenuation`
    :    The Attenuator object to use for distance attenuation.
        
    :material-location-enter: **Parameter** `soundLocation`
    :    The location of the sound source.
        
    :material-location-enter: **Parameter** `listener`
    :    The listener for which compute the attenuation.
    
    
    :material-keyboard-return: **Return**
    :    The attenuation factor.
            
    

!!! function "virtual AmReal32 GetAttenuationFactor(const Attenuation&#42; attenuation, const Entity&amp; entity, const Listener&amp; listener) = 0"

    
    Returns the attenuation factor.
    
    This method is used by position and orientation based sound sources.
    
    
    :material-location-enter: **Parameter** `attenuation`
    :    The Attenuator object to use for distance attenuation.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity which emits the sound.
        
    :material-location-enter: **Parameter** `listener`
    :    The listener for which compute the attenuation.
    
    
    :material-keyboard-return: **Return**
    :    The attenuation factor.
            
    

