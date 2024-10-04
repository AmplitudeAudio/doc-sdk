---
title: Curve
description: A Curve which describe the variation of a value (on the Y-axis) according to another (on the X-axis). 
generator: doxide
---


# Curve

**class  Curve**


A Curve which describe the variation of a value (on the Y-axis) according to another (on the X-axis).
     




## Functions

| Name | Description |
| ---- | ----------- |
| [Initialize](#Initialize) | Initializes curve parts from the given definition. |
| [Get](#Get) | Get the curve value corresponding to the given X value. |

## Function Details

### Get<a name="Get"></a>
!!! function "[[nodiscard]] float Get(double x) const"

    
    Get the curve value corresponding to the given X value.
    
    
    :material-location-enter: **Parameter** `x`
    :    The X value.
    
    
    :material-keyboard-return: **Return**
    :    The curve value.
            
    

### Initialize<a name="Initialize"></a>
!!! function "void Initialize(const CurveDefinition&#42; definition)"

    
    Initializes curve parts from the given definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The curve definition data.
                
    

