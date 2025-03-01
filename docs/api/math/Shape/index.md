---
title: Shape
description: A geometrical closed 3D shape.
generator: doxide
---


# Shape

**class  Shape**


A geometrical closed 3D shape.

A `Shape` defines a zone in the world where game objects (listener, sound sources, entities, etc.) can
be localized. Shapes are used in many places of the engine, like to define a sound attenuation shape, or to build a room.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Create](#Create) | Creates a new `Shape` from a definition. |
| [Shape](#Shape) | Constructs a new `Shape`.  |
| [~Shape](#_u007eShape) | Default destructor.  |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Gets the shortest distance to the edge of this shape. |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Gets the shortest distance to the edge of this shape. |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Gets the shortest distance to the edge of this shape. |
| [Contains](#Contains) | Checks if the given entity is contained in this shape. |
| [Contains](#Contains) | Checks if the given listener is contained in this shape. |
| [Contains](#Contains) | Checks if the given position is contained in this shape. |
| [SetLocation](#SetLocation) | Sets the location of this shape in the 3D environment. |
| [SetOrientation](#SetOrientation) | Sets the orientation of this shape. |
| [GetOrientation](#GetOrientation) | Gets the orientation of this shape. |
| [GetLookAt](#GetLookAt) | Gets the LookAt transformation matrix for this shape. |
| [GetLocation](#GetLocation) | Gets the position of this shape in the 3D environment. |
| [GetDirection](#GetDirection) | Gets the position of this shape in the 3D environment. |
| [GetUp](#GetUp) | Gets the up vector of the zone. |

## Function Details

### Contains<a name="Contains"></a>
!!! function "[[nodiscard]] virtual bool Contains(const Entity&amp; entity)"

    
    Checks if the given entity is contained in this shape.
    
    
    :material-location-enter: **Parameter** `entity`
    :    The entity to check.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the shape contains the entity, `false` otherwise.
            
    

!!! function "[[nodiscard]] virtual bool Contains(const Listener&amp; listener)"

    
    Checks if the given listener is contained in this shape.
    
    
    :material-location-enter: **Parameter** `listener`
    :    The listener to check.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the shape contains the listener, `false` otherwise.
            
    

!!! function "[[nodiscard]] virtual bool Contains(const AmVec3&amp; location) = 0"

    
    Checks if the given position is contained in this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The 3D position to check.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the shape contains the given position, `false` otherwise.
            
    

### Create<a name="Create"></a>
!!! function "static std::shared_ptr&lt;Shape&gt; Create(const ShapeDefinition&#42; definition)"

    
    Creates a new `Shape` from a definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The definition of the shape generated
        from a flatbuffer binary.
    
    
    !!! warning
         This method is intended for internal usage only.
                
    

### GetDirection<a name="GetDirection"></a>
!!! function "[[nodiscard]] AmVec3 GetDirection() const"

    
    Gets the position of this shape in the 3D environment.
    
    
    :material-keyboard-return: **Return**
    :    The shape's position.
            
    

### GetLocation<a name="GetLocation"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetLocation() const"

    
    Gets the position of this shape in the 3D environment.
    
    
    :material-keyboard-return: **Return**
    :    The shape's position.
            
    

### GetLookAt<a name="GetLookAt"></a>
!!! function "[[nodiscard]] const AmMat4&amp; GetLookAt() const"

    
    Gets the LookAt transformation matrix for this shape.
    
    
    :material-keyboard-return: **Return**
    :    The look-at transformation matrix.
            
    

### GetOrientation<a name="GetOrientation"></a>
!!! function "[[nodiscard]] const Orientation&amp; GetOrientation() const"

    
    Gets the orientation of this shape.
    
    
    :material-keyboard-return: **Return**
    :    The orientation of this shape.
            
    

### GetShortestDistanceToEdge<a name="GetShortestDistanceToEdge"></a>
!!! function "[[nodiscard]] virtual AmReal32 GetShortestDistanceToEdge(const Entity&amp; entity)"

    
    Gets the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `entity`
    :    The entity from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the entity location to the edge
    of this shape. If negative, the given entity in outside the shape.
            
    

!!! function "[[nodiscard]] virtual AmReal32 GetShortestDistanceToEdge(const Listener&amp; listener)"

    
    Gets the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `listener`
    :    The listener from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the listener location to the edge
    of this shape. If negative, the given listener in outside the shape.
            
    

!!! function "[[nodiscard]] virtual AmReal32 GetShortestDistanceToEdge(const AmVec3&amp; location) = 0"

    
    Gets the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the location to the edge
    of this shape. If negative, the given location in outside the shape.
            
    

### GetUp<a name="GetUp"></a>
!!! function "[[nodiscard]] AmVec3 GetUp() const"

    
    Gets the up vector of the zone.
    
    
    :material-keyboard-return: **Return**
    :    The up vector.
            
    

### SetLocation<a name="SetLocation"></a>
!!! function "void SetLocation(const AmVec3&amp; location)"

    
    Sets the location of this shape in the 3D environment.
    
    
    :material-location-enter: **Parameter** `location`
    :    The shape location.
                
    

### SetOrientation<a name="SetOrientation"></a>
!!! function "void SetOrientation(const Orientation&amp; orientation)"

    
    Sets the orientation of this shape.
    
    
    :material-location-enter: **Parameter** `orientation`
    :    The new orientation.
                
    

### Shape<a name="Shape"></a>
!!! function "Shape()"

    
    Constructs a new `Shape`.
             
    
    
    

### ~Shape<a name="_u007eShape"></a>
!!! function "virtual ~Shape() = default"

    
    Default destructor.
             
    
    
    

