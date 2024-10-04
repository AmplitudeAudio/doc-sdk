---
title: ConeShape
description: A cone shape, defined by a radius and an height.
generator: doxide
---


# ConeShape

**class  ConeShape : public Shape**


A cone shape, defined by a radius and an height.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Create](#Create) | Creates a new ConeShape from a definition. |
| [ConeShape](#ConeShape) | Constructs a new `ConeShape`. |
| [GetRadius](#GetRadius) | Gets the radius of the cone shape. |
| [GetDiameter](#GetDiameter) | Gets the diameter of the cone shape. |
| [GetHeight](#GetHeight) | Gets the height of the cone shape. |
| [SetRadius](#SetRadius) | Sets the radius of the cone shape. |
| [SetHeight](#SetHeight) | Sets the height of the cone shape. |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Gets the shortest distance to the edge of this shape. |
| [Contains](#Contains) | Checks if the given position is contained in this shape. |

## Function Details

### ConeShape<a name="ConeShape"></a>
!!! function "explicit ConeShape(AmReal32 radius, AmReal32 height)"

    
    Constructs a new `ConeShape`.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The radius of the cone's base.
        
    :material-location-enter: **Parameter** `height`
    :    The height of the cone.
                
    

### Contains<a name="Contains"></a>
!!! function "[[nodiscard]] bool Contains(const AmVec3&amp; location) final"

    
    Checks if the given position is contained in this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The 3D position to check.
    
    
    :material-keyboard-return: **Return**
    :    true if the shape contains the given position, false otherwise.
            
    

### Create<a name="Create"></a>
!!! function "static ConeShape&#42; Create(const ConeShapeDefinition&#42; definition)"

    
    Creates a new ConeShape from a definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The definition of the shape generated
        from a flatbuffer binary.
    
    
    !!! warning
         This method is intended for internal usage only.
                
    

### GetDiameter<a name="GetDiameter"></a>
!!! function "[[nodiscard]] AmReal32 GetDiameter() const"

    
    Gets the diameter of the cone shape.
    
    
    :material-keyboard-return: **Return**
    :    The cone base's diameter.
            
    

### GetHeight<a name="GetHeight"></a>
!!! function "[[nodiscard]] AmReal32 GetHeight() const"

    
    Gets the height of the cone shape.
    
    
    :material-keyboard-return: **Return**
    :    The cone's height.
            
    

### GetRadius<a name="GetRadius"></a>
!!! function "[[nodiscard]] AmReal32 GetRadius() const"

    
    Gets the radius of the cone shape.
    
    
    :material-keyboard-return: **Return**
    :    The cone base's radius.
            
    

### GetShortestDistanceToEdge<a name="GetShortestDistanceToEdge"></a>
!!! function "[[nodiscard]] AmReal32 GetShortestDistanceToEdge(const AmVec3&amp; location) final"

    
    Gets the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the location to the edge
    of this shape. If negative, the given location in outside the shape.
            
    

### SetHeight<a name="SetHeight"></a>
!!! function "void SetHeight(AmReal32 height)"

    
    Sets the height of the cone shape.
    
    
    :material-location-enter: **Parameter** `height`
    :    The cone's height.
                
    

### SetRadius<a name="SetRadius"></a>
!!! function "void SetRadius(AmReal32 radius)"

    
    Sets the radius of the cone shape.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The cone base's radius.
                
    

