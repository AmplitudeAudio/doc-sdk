---
title: Zone
description: A tuple of shapes that represents a zone in the world.
generator: doxide
---


# Zone

**class  Zone**


A tuple of shapes that represents a zone in the world.

This shape is mainly used by attenuations and environments. It's composed of an inner `Shape` and an outer `Shape`.
The inner shape is the place where the [factor](#GetFactor) is equal to one all the time. The outer shape is the place where the
[factor](#GetFactor) increase or decrease according to the shortest distance of the game object from the outer edge.

If the game object is outside the outer shape (thus, outside the zone), the [factor](#GetFactor) is zero.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_innerShape](#m_innerShape) | The inner shape of the zone.  |
| [m_outerShape](#m_outerShape) | The outer shape of the zone.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Zone](#Zone) | Creates a new `Zone` from the given inner and outer shapes. |
| [~Zone](#_u007eZone) | Default destructor.  |
| [GetFactor](#GetFactor) | Gets the factor according to the position of the given entity in the zone. |
| [GetFactor](#GetFactor) | Gets the factor according to the position of the given listener in the zone. |
| [GetFactor](#GetFactor) | Gets the factor according to the given position in the zone. |
| [SetLocation](#SetLocation) | Sets the location of this zone in the 3D environment. |
| [GetLocation](#GetLocation) | Gets the current location of this zone. |
| [SetOrientation](#SetOrientation) | Sets the orientation of this zone. |
| [GetOrientation](#GetOrientation) | Gets the orientation of this zone. |
| [GetDirection](#GetDirection) | Gets the direction vector of the zone. |
| [GetUp](#GetUp) | Gets the up vector of the zone. |

## Variable Details

### m_innerShape<a name="m_innerShape"></a>

!!! variable "Shape&#42; m_innerShape"

    
    The inner shape of the zone.
             
    
    
    

### m_outerShape<a name="m_outerShape"></a>

!!! variable "Shape&#42; m_outerShape"

    
    The outer shape of the zone.
             
    
    
    

## Function Details

### GetDirection<a name="GetDirection"></a>
!!! function "[[nodiscard]] AmVec3 GetDirection() const"

    
    Gets the direction vector of the zone.
    
    
    :material-keyboard-return: **Return**
    :    The direction vector.
            
    

### GetFactor<a name="GetFactor"></a>
!!! function "[[nodiscard]] virtual inline AmReal32 GetFactor(const Entity&amp; entity)"

    
    Gets the factor according to the position of the given entity in the zone.
    
    
    :material-location-enter: **Parameter** `entity`
    :    The entity to get the factor for.
    
    
    :material-keyboard-return: **Return**
    :    The factor.
    
    
    !!! note
         The factor is a value in the range [0, 1].
                
    

!!! function "[[nodiscard]] virtual inline AmReal32 GetFactor(const Listener&amp; listener)"

    
    Gets the factor according to the position of the given listener in the zone.
    
    
    :material-location-enter: **Parameter** `listener`
    :    The listener to get the factor for.
    
    
    :material-keyboard-return: **Return**
    :    The factor.
    
    
    !!! note
         The factor is a value in the range [0, 1].
                
    

!!! function "[[nodiscard]] virtual AmReal32 GetFactor(const AmVec3&amp; position) = 0"

    
    Gets the factor according to the given position in the zone.
    
    
    :material-location-enter: **Parameter** `position`
    :    The position in the zone to get the factor for.
    
    
    :material-keyboard-return: **Return**
    :    The factor.
    
    
    !!! note
         The factor is a value in the range [0, 1].
                
    

### GetLocation<a name="GetLocation"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetLocation() const"

    
    Gets the current location of this zone.
    
    
    :material-keyboard-return: **Return**
    :    The current location of this zone.
            
    

### GetOrientation<a name="GetOrientation"></a>
!!! function "[[nodiscard]] const Orientation&amp; GetOrientation() const"

    
    Gets the orientation of this zone.
    
    
    :material-keyboard-return: **Return**
    :    The orientation of this zone.
            
    

### GetUp<a name="GetUp"></a>
!!! function "[[nodiscard]] AmVec3 GetUp() const"

    
    Gets the up vector of the zone.
    
    
    :material-keyboard-return: **Return**
    :    The up vector.
            
    

### SetLocation<a name="SetLocation"></a>
!!! function "void SetLocation(const AmVec3&amp; location)"

    
    Sets the location of this zone in the 3D environment.
    
    
    :material-location-enter: **Parameter** `location`
    :    The zone location.
                
    

### SetOrientation<a name="SetOrientation"></a>
!!! function "void SetOrientation(const Orientation&amp; orientation)"

    
    Sets the orientation of this zone.
    
    
    :material-location-enter: **Parameter** `orientation`
    :    The new orientation.
                
    

### Zone<a name="Zone"></a>
!!! function "explicit Zone(Shape&#42; inner, Shape&#42; outer)"

    
    Creates a new `Zone` from the given inner and outer shapes.
    
    
    :material-location-enter: **Parameter** `inner`
    :    The inner shape.
        
    :material-location-enter: **Parameter** `outer`
    :    The outer shape.
                
    

### ~Zone<a name="_u007eZone"></a>
!!! function "virtual ~Zone() = default"

    
    Default destructor.
             
    
    
    

