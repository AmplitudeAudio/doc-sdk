---
title: EffectInstance
description: An instance of an `Effect` asset.
generator: doxide
---


# EffectInstance

**class EffectInstance**


An instance of an `Effect` asset.

The effect instance is the real place where the filter is applied to only one sound object
at a time. Each effect instance has its own state, and that state is not shared across sound objects.


:material-eye-outline: **See**
:    [Effect](../../assets/Effect/index.md), [FilterInstance](../../dsp/FilterInstance/index.md)


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~EffectInstance](#_u007eEffectInstance) | Default destructor.  |
| [GetFilter](#GetFilter) | Gets the filter instance wrapped by this effect. |

## Function Details

### GetFilter<a name="GetFilter"></a>
!!! function "&#42; GetFilter() const"

    
    Gets the filter instance wrapped by this effect.
    
    
    :material-keyboard-return: **Return**
    :    The filter instance.
            
    

### ~EffectInstance<a name="_u007eEffectInstance"></a>
!!! function "virtual ~EffectInstance() = default"

    
    Default destructor.
             
    
    
    

