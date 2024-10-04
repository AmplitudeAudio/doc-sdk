---
title: EffectInstance
description: An instance of an Effect asset.
generator: doxide
---


# EffectInstance

**class EffectInstance**


An instance of an Effect asset.

The effect instance is the real filter applied to only one sound object
at a time. It is used to not share the same state between multiple sound
objects.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [~EffectInstance](#_u007eEffectInstance) | Destroys the EffectInstance.  |
| [GetFilter](#GetFilter) | Get the filter instance wrapped by this effect. |

## Function Details

### GetFilter<a name="GetFilter"></a>
!!! function "&#42; GetFilter() const"

    
    Get the filter instance wrapped by this effect.
    
    
    :material-keyboard-return: **Return**
    :    The filter instance.
            
    

### ~EffectInstance<a name="_u007eEffectInstance"></a>
!!! function "virtual ~EffectInstance() = default"

    
    Destroys the EffectInstance.
             
    
    
    

