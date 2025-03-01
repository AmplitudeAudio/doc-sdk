---
title: SphereShape
description: A sphere shape, defined by a radius.
generator: doxide
---


# SphereShape

**class  SphereShape : public Shape**


A sphere shape, defined by a radius.


    


## Operators

| Name | Description |
| ---- | ----------- |
| [operator==](#operator_u003d_u003d) | Compares this shape with another shape for equality. |
| [operator!=](#operator_u0021_u003d) | Compares this shape with another shape for inequality. |

## Functions

| Name | Description |
| ---- | ----------- |
| [Create](#Create) | Creates a new SphereShape from a definition. |
| [SphereShape](#SphereShape) | Constructs a new `SphereShape`. |
| [GetRadius](#GetRadius) | Gets the radius of the sphere shape. |
| [GetDiameter](#GetDiameter) | Gets the diameter of the sphere shape. |
| [SetRadius](#SetRadius) | Sets the radius of the sphere shape. |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Gets the shortest distance to the edge of this shape. |
| [Contains](#Contains) | Checks if the given position is contained in this shape. |

## Operator Details

### operator!=<a name="operator_u0021_u003d"></a>

!!! function "bool operator!=(const SphereShape&amp; other) const"

    
    Compares this shape with another shape for inequality.
    
    
    !!! note
         Shapes are equal if they have the same dimensions, the position, and the same orientation.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other shape to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `false` if the shapes are equal, `true` otherwise.
            
    

### operator==<a name="operator_u003d_u003d"></a>

!!! function "bool operator==(const SphereShape&amp; other) const"

    
    Compares this shape with another shape for equality.
    
    
    !!! note
         Shapes are equal if they have the same dimensions, the position, and the same orientation.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other shape to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the shapes are equal, `false` otherwise.
            
    

## Function Details

### Contains<a name="Contains"></a>
!!! function "[[nodiscard]] bool Contains(const AmVec3&amp; location) final"

    
    Checks if the given position is contained in this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The 3D position to check.
    
    
    :material-keyboard-return: **Return**
    :    true if the shape contains the given position, false otherwise.
            
    

### Create<a name="Create"></a>
!!! function "static std::shared_ptr&lt;SphereShape&gt; Create(const SphereShapeDefinition&#42; definition)"

    
    Creates a new SphereShape from a definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The definition of the shape generated
        from a flatbuffer binary.
    
    
    !!! warning
         This method is intended for internal usage only.
                
    

### GetDiameter<a name="GetDiameter"></a>
!!! function "[[nodiscard]] AmReal32 GetDiameter() const"

    
    Gets the diameter of the sphere shape.
    
    
    :material-keyboard-return: **Return**
    :    The sphere's diameter.
            
    

### GetRadius<a name="GetRadius"></a>
!!! function "[[nodiscard]] AmReal32 GetRadius() const"

    
    Gets the radius of the sphere shape.
    
    
    :material-keyboard-return: **Return**
    :    The sphere's radius.
            
    

### GetShortestDistanceToEdge<a name="GetShortestDistanceToEdge"></a>
!!! function "[[nodiscard]] AmReal32 GetShortestDistanceToEdge(const AmVec3&amp; location) final"

    
    Gets the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the location to the edge
    of this shape. If negative, the given location in outside the shape.
            
    

### SetRadius<a name="SetRadius"></a>
!!! function "void SetRadius(AmReal32 radius)"

    
    Sets the radius of the sphere shape.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The sphere's radius.
                
    

### SphereShape<a name="SphereShape"></a>
!!! function "explicit SphereShape(AmReal32 radius)"

    
    Constructs a new `SphereShape`.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The sphere's radius.
                
    

