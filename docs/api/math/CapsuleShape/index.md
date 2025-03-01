---
title: CapsuleShape
description: A capsule shape, defined by a radius and an height.
generator: doxide
---


# CapsuleShape

**class  CapsuleShape : public Shape**


A capsule shape, defined by a radius and an height.


    


## Operators

| Name | Description |
| ---- | ----------- |
| [operator==](#operator_u003d_u003d) | Compares this shape with another shape for equality. |
| [operator!=](#operator_u0021_u003d) | Compares this shape with another shape for inequality. |

## Functions

| Name | Description |
| ---- | ----------- |
| [Create](#Create) | Creates a new `CapsuleShape` from a definition. |
| [CapsuleShape](#CapsuleShape) | Constructs a new `CapsuleShape`. |
| [GetRadius](#GetRadius) | Gets the radius of the capsule shape. |
| [GetHalfHeight](#GetHalfHeight) | Gets the half height of the capsule shape. |
| [GetDiameter](#GetDiameter) | Gets the diameter of the capsule shape. |
| [GetHeight](#GetHeight) | Gets the height of the capsule shape. |
| [SetRadius](#SetRadius) | Sets the radius of the capsule shape. |
| [SetHalfHeight](#SetHalfHeight) | Sets the half height of the capsule shape. |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Gets the shortest distance to the edge of this shape. |
| [Contains](#Contains) | Checks if the given position is contained in this shape. |

## Operator Details

### operator!=<a name="operator_u0021_u003d"></a>

!!! function "bool operator!=(const CapsuleShape&amp; other) const"

    
    Compares this shape with another shape for inequality.
    
    
    !!! note
         Shapes are equal if they have the same dimensions, the position, and the same orientation.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other shape to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `false` if the shapes are equal, `true` otherwise.
            
    

### operator==<a name="operator_u003d_u003d"></a>

!!! function "bool operator==(const CapsuleShape&amp; other) const"

    
    Compares this shape with another shape for equality.
    
    
    !!! note
         Shapes are equal if they have the same dimensions, the position, and the same orientation.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other shape to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the shapes are equal, `false` otherwise.
            
    

## Function Details

### CapsuleShape<a name="CapsuleShape"></a>
!!! function "explicit CapsuleShape(AmReal32 radius, AmReal32 halfHeight)"

    
    Constructs a new `CapsuleShape`.
    
    
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
    :    `true` if the shape contains the given position, `false` otherwise.
            
    

### Create<a name="Create"></a>
!!! function "static std::shared_ptr&lt;CapsuleShape&gt; Create(const CapsuleShapeDefinition&#42; definition)"

    
    Creates a new `CapsuleShape` from a definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The definition of the shape generated
        from a flatbuffer binary.
    
    
    !!! warning
         This method is intended for internal usage only.
                
    

### GetDiameter<a name="GetDiameter"></a>
!!! function "[[nodiscard]] AmReal32 GetDiameter() const"

    
    Gets the diameter of the capsule shape.
    
    
    :material-keyboard-return: **Return**
    :    The capsule's diameter.
            
    

### GetHalfHeight<a name="GetHalfHeight"></a>
!!! function "[[nodiscard]] AmReal32 GetHalfHeight() const"

    
    Gets the half height of the capsule shape.
    
    
    :material-keyboard-return: **Return**
    :    The capsule's half height.
            
    

### GetHeight<a name="GetHeight"></a>
!!! function "[[nodiscard]] AmReal32 GetHeight() const"

    
    Gets the height of the capsule shape.
    
    
    :material-keyboard-return: **Return**
    :    The capsule's height.
            
    

### GetRadius<a name="GetRadius"></a>
!!! function "[[nodiscard]] AmReal32 GetRadius() const"

    
    Gets the radius of the capsule shape.
    
    
    :material-keyboard-return: **Return**
    :    The capsule's radius.
            
    

### GetShortestDistanceToEdge<a name="GetShortestDistanceToEdge"></a>
!!! function "[[nodiscard]] AmReal32 GetShortestDistanceToEdge(const AmVec3&amp; location) final"

    
    Gets the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the location to the edge
    of this shape. If negative, the given location in outside the shape.
            
    

### SetHalfHeight<a name="SetHalfHeight"></a>
!!! function "void SetHalfHeight(AmReal32 halfHeight)"

    
    Sets the half height of the capsule shape.
    
    
    :material-location-enter: **Parameter** `halfHeight`
    :    The capsule's half height.
                
    

### SetRadius<a name="SetRadius"></a>
!!! function "void SetRadius(AmReal32 radius)"

    
    Sets the radius of the capsule shape.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The capsule's radius.
                
    

