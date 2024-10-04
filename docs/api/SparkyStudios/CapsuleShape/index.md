---
title: CapsuleShape
description: A capsule shape, defined by a radius and an height. 
generator: doxide
---


# CapsuleShape

**class  CapsuleShape : public Shape**


A capsule shape, defined by a radius and an height.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [Create](#Create) | Creates a new CapsuleShape from a definition. |
| [CapsuleShape](#CapsuleShape) | Construct a new Capsule Shape. |
| [GetRadius](#GetRadius) | Get the radius of the capsule shape. |
| [GetHalfHeight](#GetHalfHeight) | Get the half height of the capsule shape. |
| [GetDiameter](#GetDiameter) | Get the diameter of the capsule shape. |
| [GetHeight](#GetHeight) | Get the height of the capsule shape. |
| [SetRadius](#SetRadius) | Set the radius of the capsule shape. |
| [SetHalfHeight](#SetHalfHeight) | Set the half height of the capsule shape. |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Get the shortest distance to the edge of this shape. |
| [Contains](#Contains) | Checks if the given position is contained in this shape. |

## Function Details

### CapsuleShape<a name="CapsuleShape"></a>
!!! function "explicit CapsuleShape(AmReal32 radius, AmReal32 halfHeight)"

    
    Construct a new Capsule Shape.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The capsule radius.
        
    :material-location-enter: **Parameter** `halfHeight`
    :    The capsule half height.
                
    

### Contains<a name="Contains"></a>
!!! function "[[nodiscard]] bool Contains(const AmVec3&amp; location) final"

    
    Checks if the given position is contained in this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The 3D position to check.
    
    
    :material-keyboard-return: **Return**
    :    true if the shape contains the given position, false otherwise.
            
    

### Create<a name="Create"></a>
!!! function "static CapsuleShape&#42; Create(const CapsuleShapeDefinition&#42; definition)"

    
    Creates a new CapsuleShape from a definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The definition of the capsule shape generated
                          from a flatbuffer binary.
                
    

### GetDiameter<a name="GetDiameter"></a>
!!! function "[[nodiscard]] AmReal32 GetDiameter() const"

    
    Get the diameter of the capsule shape.
    
    
    :material-keyboard-return: **Return**
    :    The capsule's diameter.
            
    

### GetHalfHeight<a name="GetHalfHeight"></a>
!!! function "[[nodiscard]] AmReal32 GetHalfHeight() const"

    
    Get the half height of the capsule shape.
    
    
    :material-keyboard-return: **Return**
    :    The capsule's half height.
            
    

### GetHeight<a name="GetHeight"></a>
!!! function "[[nodiscard]] AmReal32 GetHeight() const"

    
    Get the height of the capsule shape.
    
    
    :material-keyboard-return: **Return**
    :    The capsule's height.
            
    

### GetRadius<a name="GetRadius"></a>
!!! function "[[nodiscard]] AmReal32 GetRadius() const"

    
    Get the radius of the capsule shape.
    
    
    :material-keyboard-return: **Return**
    :    The capsule's radius.
            
    

### GetShortestDistanceToEdge<a name="GetShortestDistanceToEdge"></a>
!!! function "[[nodiscard]] AmReal32 GetShortestDistanceToEdge(const AmVec3&amp; location) final"

    
    Get the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the location to the edge
    of this shape. If negative, the given location in outside the shape.
            
    

### SetHalfHeight<a name="SetHalfHeight"></a>
!!! function "void SetHalfHeight(AmReal32 halfHeight)"

    
    Set the half height of the capsule shape.
    
    
    :material-location-enter: **Parameter** `halfHeight`
    :    The capsule's half height.
                
    

### SetRadius<a name="SetRadius"></a>
!!! function "void SetRadius(AmReal32 radius)"

    
    Set the radius of the capsule shape.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The capsule's radius.
                
    

