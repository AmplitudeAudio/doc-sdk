---
title: CurvePart
description: A segment of a `Curve`.
generator: doxide
---


# CurvePart

**class  CurvePart**


A segment of a `Curve`.

A `CurvePart` allows a curve to have different fading algorithms at the same time.
Each `CurvePart` has a start and end point, and the fading algorithm which moves the value
from the start point to the end point.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [CurvePart](#CurvePart) | Creates an empty `CurvePart`.  |
| [~CurvePart](#_u007eCurvePart) | Destroys this `CurvePart`.  |
| [Initialize](#Initialize) | Initializes this `CurvePart` from a definition. |
| [GetStart](#GetStart) | Returns the start point of this `CurvePart`. |
| [SetStart](#SetStart) | Sets the start point of this `CurvePart`. |
| [GetEnd](#GetEnd) | Returns the end point of this `CurvePart`. |
| [SetEnd](#SetEnd) | Sets the end point of this `CurvePart`. |
| [GetFader](#GetFader) | Returns the Fader of this `CurvePart`. |
| [SetFader](#SetFader) | Sets the fader of this `CurvePart`. |
| [Get](#Get) | Gets the Y coordinates of a point given its coordinates over the X axis. |

## Function Details

### CurvePart<a name="CurvePart"></a>
!!! function "CurvePart()"

    
    Creates an empty `CurvePart`.
             
    
    
    

### Get<a name="Get"></a>
!!! function "[[nodiscard]] AmReal32 Get(AmReal64 x) const"

    
    Gets the Y coordinates of a point given its coordinates over the X axis.
    
    
    :material-location-enter: **Parameter** `x`
    :    The coordinates of the point over the X axis.
    
    
    :material-keyboard-return: **Return**
    :    The Y coordinates of the point.
            
    

### GetEnd<a name="GetEnd"></a>
!!! function "[[nodiscard]] const CurvePoint&amp; GetEnd() const"

    
    Returns the end point of this `CurvePart`.
    
    
    :material-keyboard-return: **Return**
    :    The end point of this `CurvePart`.
            
    

### GetFader<a name="GetFader"></a>
!!! function "[[nodiscard]] FaderInstance&#42; GetFader() const"

    
    Returns the Fader of this `CurvePart`.
    
    
    :material-keyboard-return: **Return**
    :    The `FaderInstance` of this `CurvePart`.
            
    

### GetStart<a name="GetStart"></a>
!!! function "[[nodiscard]] const CurvePoint&amp; GetStart() const"

    
    Returns the start point of this `CurvePart`.
    
    
    :material-keyboard-return: **Return**
    :    The start point of this `CurvePart`.
            
    

### Initialize<a name="Initialize"></a>
!!! function "void Initialize(const CurvePartDefinition&#42; definition)"

    
    Initializes this `CurvePart` from a definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The definition of the curve part generated
        from a flatbuffer binary.
                
    

### SetEnd<a name="SetEnd"></a>
!!! function "void SetEnd(const CurvePoint&amp; end)"

    
    Sets the end point of this `CurvePart`.
    
    
    :material-location-enter: **Parameter** `end`
    :    The new end point.
                
    

### SetFader<a name="SetFader"></a>
!!! function "void SetFader(const AmString&amp; fader)"

    
    Sets the fader of this `CurvePart`.
    
    
    :material-location-enter: **Parameter** `fader`
    :    The name of the `Fader` to set.
                
    

### SetStart<a name="SetStart"></a>
!!! function "void SetStart(const CurvePoint&amp; start)"

    
    Sets the start point of this `CurvePart`.
    
    
    :material-location-enter: **Parameter** `start`
    :    The new start point.
                
    

### ~CurvePart<a name="_u007eCurvePart"></a>
!!! function "~CurvePart()"

    
    Destroys this `CurvePart`.
             
    
    
    

