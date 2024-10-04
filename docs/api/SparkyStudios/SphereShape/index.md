---
title: SphereShape
description: A sphere shape, defined by a radius. 
generator: doxide
---


# SphereShape

**class  SphereShape : public Shape**


A sphere shape, defined by a radius.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [Create](#Create) | Creates a new SphereShape from a definition. |
| [SphereShape](#SphereShape) | Construct a new Sphere Shape. |
| [GetRadius](#GetRadius) | Get the radius of the sphere shape. |
| [GetDiameter](#GetDiameter) | Get the diameter of the sphere shape. |
| [SetRadius](#SetRadius) | Set the radius of the sphere shape. |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Get the shortest distance to the edge of this shape. |
| [Contains](#Contains) | Checks if the given position is contained in this shape. |

## Function Details

### Contains<a name="Contains"></a>
!!! function "[[nodiscard]] bool Contains(const AmVec3&amp; location) final"

    
    Checks if the given position is contained in this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The 3D position to check.
    
    
    :material-keyboard-return: **Return**
    :    true if the shape contains the given position, false otherwise.
            
    

### Create<a name="Create"></a>
!!! function "static SphereShape&#42; Create(const SphereShapeDefinition&#42; definition)"

    
    Creates a new SphereShape from a definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The definition of the sphere shape generated
                          from a flatbuffer binary.
                
    

### GetDiameter<a name="GetDiameter"></a>
!!! function "[[nodiscard]] AmReal32 GetDiameter() const"

    
    Get the diameter of the sphere shape.
    
    
    :material-keyboard-return: **Return**
    :    The sphere's diameter.
            
    

### GetRadius<a name="GetRadius"></a>
!!! function "[[nodiscard]] AmReal32 GetRadius() const"

    
    Get the radius of the sphere shape.
    
    
    :material-keyboard-return: **Return**
    :    The sphere's radius.
            
    

### GetShortestDistanceToEdge<a name="GetShortestDistanceToEdge"></a>
!!! function "[[nodiscard]] AmReal32 GetShortestDistanceToEdge(const AmVec3&amp; location) final"

    
    Get the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the location to the edge
    of this shape. If negative, the given location in outside the shape.
            
    

### SetRadius<a name="SetRadius"></a>
!!! function "void SetRadius(AmReal32 radius)"

    
    Set the radius of the sphere shape.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The sphere's radius.
                
    

### SphereShape<a name="SphereShape"></a>
!!! function "explicit SphereShape(AmReal32 radius)"

    
    Construct a new Sphere Shape.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The sphere's radius.
                
    

