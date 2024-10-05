---
title: SwitchContainerItem
description: Describes a single item within a `SwitchContainer`.
generator: doxide
---


# SwitchContainerItem

**struct SwitchContainerItem**


Describes a single item within a `SwitchContainer`.


:material-eye-outline: **See**
:    [SwitchContainer](../../assets/SwitchContainer/index.md)


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_id](#m_id) | The object ID of the item. |
| [m_continueBetweenStates](#m_continueBetweenStates) | Whether to continue playing this item when the `SwitchContainer` * changes its state between one of the values where this item is registered. |
| [m_fadeInDuration](#m_fadeInDuration) | The fade duration in milliseconds when this item starts playing.  |
| [m_fadeInAlgorithm](#m_fadeInAlgorithm) | The name of the fading algorithm to use when this item starts playing.  |
| [m_fadeOutDuration](#m_fadeOutDuration) | The fade duration in milliseconds when this item stops playing.  |
| [m_fadeOutAlgorithm](#m_fadeOutAlgorithm) | The name of the fading algorithm to use when this item stops playing.  |
| [m_gain](#m_gain) | The custom linear gain applied on this item. |
| [m_pitch](#m_pitch) | The custom pitch applied on this item. |

## Variable Details

### m_continueBetweenStates<a name="m_continueBetweenStates"></a>

!!! variable "bool m_continueBetweenStates"

    
    Whether to continue playing this item when the `SwitchContainer`
             * changes its state between one of the values where this item is registered.
    
    If this value is set to `false`, each sound will be stopped and played again
    from the beginning.
            
    

### m_fadeInAlgorithm<a name="m_fadeInAlgorithm"></a>

!!! variable "AmString m_fadeInAlgorithm"

    
    The name of the fading algorithm to use when this item starts playing.
             
    
    
    

### m_fadeInDuration<a name="m_fadeInDuration"></a>

!!! variable "AmTime m_fadeInDuration"

    
    The fade duration in milliseconds when this item starts playing.
             
    
    
    

### m_fadeOutAlgorithm<a name="m_fadeOutAlgorithm"></a>

!!! variable "AmString m_fadeOutAlgorithm"

    
    The name of the fading algorithm to use when this item stops playing.
             
    
    
    

### m_fadeOutDuration<a name="m_fadeOutDuration"></a>

!!! variable "AmTime m_fadeOutDuration"

    
    The fade duration in milliseconds when this item stops playing.
             
    
    
    

### m_gain<a name="m_gain"></a>

!!! variable "RtpcValue m_gain"

    
    The custom linear gain applied on this item.
    
    The final gain will be computed with this value multiplied with the gain of the
    attenuation model, if any.
            
    

### m_id<a name="m_id"></a>

!!! variable "AmObjectID m_id"

    
    The object ID of the item.
    
    May be a `AmSoundID` or a `AmCollectionID`.
            
    

### m_pitch<a name="m_pitch"></a>

!!! variable "RtpcValue m_pitch"

    
    The custom pitch applied on this item.
    
    The final pitch will be computed with this value multiplied with the pitch of the
    doppler effect, if this switch container's spatialization mode is set to position.
            
    

