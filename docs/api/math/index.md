---
title: Math
description: Math libraries and utilities
generator: doxide
---


# Math

Math libraries and utilities

## Types

| Name | Description |
| ---- | ----------- |
| [eFaderState](eFaderState/index.md) | Enumerates the list of states in a fader. |

## Macros

| Name | Description |
| ---- | ----------- |
| [AM_BETWEEN](#AM_BETWEEN) | Checks if a value is between a and b. |
| [AM_CLAMP](#AM_CLAMP) | Clamps a value between a and b. |

## Macro Details

### AM_BETWEEN<a name="AM_BETWEEN"></a>

!!! macro "#define AM_BETWEEN(v, a, b)"

    
    Checks if a value is between a and b.
    
    
    :material-location-enter: **Parameter** `v`
    :    The value to check
        
    :material-location-enter: **Parameter** `a`
    :    The minimum value
        
    :material-location-enter: **Parameter** `b`
    :    The maximum value
    
    
    :material-keyboard-return: **Return**
    :    `true` if the value is between a and b, `false` otherwise.
    
    
    
    

### AM_CLAMP<a name="AM_CLAMP"></a>

!!! macro "#define AM_CLAMP(v, a, b)"

    
    Clamps a value between a and b.
    
    
    :material-location-enter: **Parameter** `v`
    :    The value to clamp
        
    :material-location-enter: **Parameter** `a`
    :    The minimum value
        
    :material-location-enter: **Parameter** `b`
    :    The maximum value
    
    
    :material-keyboard-return: **Return**
    :    The clamped value
    
    
    
    

