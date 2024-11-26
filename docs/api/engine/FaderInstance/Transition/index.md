---
title: Transition
description: Create an animation transition function using * a one-dimensional cubic Bézier curve.
generator: doxide
---


# Transition

**struct Transition**


Create an animation transition function using
         * a one-dimensional cubic Bézier curve.

This use the exact same algorithm as in CSS. The first and last
control points of the cubic Bézier curve are fixed to (0,0)
and (1,1) respectively.
        


## Variables

| Name | Description |
| ---- | ----------- |
| [m_controlPoints](#m_controlPoints) | The control points.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Transition](#Transition) | Constructs a new Transition curve. |
| [Transition](#Transition) | Constructs a new Transition curve. |
| [Ease](#Ease) | Given an animation duration percentage (in the range [0, 1]), * it calculates the animation progression percentage from the configured curve. |

## Variable Details

### m_controlPoints<a name="m_controlPoints"></a>

!!! variable "BezierCurveControlPoints m_controlPoints"

    
    The control points.
                 
    
    
    

## Function Details

### Ease<a name="Ease"></a>
!!! function "[[nodiscard]] AmTime Ease(AmTime t) const"

    
    Given an animation duration percentage (in the range [0, 1]),
                 * it calculates the animation progression percentage from the configured curve.
    
    
    :material-location-enter: **Parameter** `t`
    :    The animation duration percentage (in the range [0, 1]).
    
    
    :material-keyboard-return: **Return**
    :    The animation progress percentage (in the range [0, 1]).
                
    

### Transition<a name="Transition"></a>
!!! function "Transition(AmReal32 x1, AmReal32 y1, AmReal32 x2, AmReal32 y2)"

    
    Constructs a new Transition curve.
    
    
    :material-location-enter: **Parameter** `x1`
    :    The x coordinate of the second control point.
        
    :material-location-enter: **Parameter** `y1`
    :    The y coordinate of the second control point.
        
    :material-location-enter: **Parameter** `x2`
    :    The x coordinate of the third control point.
        
    :material-location-enter: **Parameter** `y2`
    :    The y coordinate of the third control point.
                    
    

!!! function "Transition(const BezierCurveControlPoints&amp; controlPoints)"

    
    Constructs a new Transition curve.
    
    
    :material-location-enter: **Parameter** `controlPoints`
    :    The control points of the curve.
                    
    

