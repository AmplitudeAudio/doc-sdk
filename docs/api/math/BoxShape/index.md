---
title: BoxShape
description: A box shape, defined by a width, an height, and a depth.
generator: doxide
---


# BoxShape

**class  BoxShape : public Shape**


A box shape, defined by a width, an height, and a depth.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Create](#Create) | Creates a new `BoxShape` from a definition. |
| [BoxShape](#BoxShape) | Constructs a new `BoxShape`. |
| [BoxShape](#BoxShape) | Constructs a new `BoxShape`. |
| [GetHalfWidth](#GetHalfWidth) | Gets the half width of the `BoxShape`. |
| [GetHalfHeight](#GetHalfHeight) | Gets the half height of the `BoxShape`. |
| [GetHalfDepth](#GetHalfDepth) | Gets the half depth of the `BoxShape`. |
| [GetWidth](#GetWidth) | Gets the width of the `BoxShape`. |
| [GetHeight](#GetHeight) | Gets the height of the `BoxShape`. |
| [GetDepth](#GetDepth) | Gets the depth of the `BoxShape`. |
| [SetHalfWidth](#SetHalfWidth) | Sets the half width of the `BoxShape`. |
| [SetHalfHeight](#SetHalfHeight) | Sets the half height of the `BoxShape`. |
| [SetHalfDepth](#SetHalfDepth) | Sets the half depth of the `BoxShape`. |
| [GetShortestDistanceToEdge](#GetShortestDistanceToEdge) | Gets the shortest distance to the edge of this shape. |
| [Contains](#Contains) | Checks if the given position is contained in this shape. |
| [GetClosestPoint](#GetClosestPoint) | Gets the closest point to the given location. |

## Function Details

### BoxShape<a name="BoxShape"></a>
!!! function "explicit BoxShape(AmReal32 halfWidth, AmReal32 halfHeight, AmReal32 halfDepth)"

    
    Constructs a new `BoxShape`.
    
    
    :material-location-enter: **Parameter** `halfWidth`
    :    The half width of the box shape.
        
    :material-location-enter: **Parameter** `halfHeight`
    :    The half height of the box shape.
        
    :material-location-enter: **Parameter** `halfDepth`
    :    The half depth of the box shape.
                
    

!!! function "explicit BoxShape(const AmVec3&amp; position, const AmVec3&amp; dimensions)"

    
    Constructs a new `BoxShape`.
    
    
    :material-location-enter: **Parameter** `position`
    :    The position of the box shape.
        
    :material-location-enter: **Parameter** `dimensions`
    :    The dimensions of the box shape.
                
    

### Contains<a name="Contains"></a>
!!! function "[[nodiscard]] bool Contains(const AmVec3&amp; location) final"

    
    Checks if the given position is contained in this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The 3D position to check.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the shape contains the given position, `false` otherwise.
            
    

### Create<a name="Create"></a>
!!! function "static BoxShape&#42; Create(const BoxShapeDefinition&#42; definition)"

    
    Creates a new `BoxShape` from a definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The definition of the shape generated
        from a flatbuffer binary.
    
    
    !!! warning
         This method is intended for internal usage only.
                
    

### GetClosestPoint<a name="GetClosestPoint"></a>
!!! function "[[nodiscard]] AmVec3 GetClosestPoint(const AmVec3&amp; location) const"

    
    Gets the closest point to the given location.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location to get the closest point for.
    
    
    :material-keyboard-return: **Return**
    :    The closest point to the given location.
            
    

### GetDepth<a name="GetDepth"></a>
!!! function "[[nodiscard]] AmReal32 GetDepth() const"

    
    Gets the depth of the `BoxShape`.
    
    
    :material-keyboard-return: **Return**
    :    The box shape's depth.
            
    

### GetHalfDepth<a name="GetHalfDepth"></a>
!!! function "[[nodiscard]] AmReal32 GetHalfDepth() const"

    
    Gets the half depth of the `BoxShape`.
    
    
    :material-keyboard-return: **Return**
    :    The box shape's half depth.
            
    

### GetHalfHeight<a name="GetHalfHeight"></a>
!!! function "[[nodiscard]] AmReal32 GetHalfHeight() const"

    
    Gets the half height of the `BoxShape`.
    
    
    :material-keyboard-return: **Return**
    :    The box shape's half height.
            
    

### GetHalfWidth<a name="GetHalfWidth"></a>
!!! function "[[nodiscard]] AmReal32 GetHalfWidth() const"

    
    Gets the half width of the `BoxShape`.
    
    
    :material-keyboard-return: **Return**
    :    The box shape's half width.
            
    

### GetHeight<a name="GetHeight"></a>
!!! function "[[nodiscard]] AmReal32 GetHeight() const"

    
    Gets the height of the `BoxShape`.
    
    
    :material-keyboard-return: **Return**
    :    The box shape's height.
            
    

### GetShortestDistanceToEdge<a name="GetShortestDistanceToEdge"></a>
!!! function "[[nodiscard]] AmReal32 GetShortestDistanceToEdge(const AmVec3&amp; location) final"

    
    Gets the shortest distance to the edge of this shape.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location from which calculate the distance.
    
    
    :material-keyboard-return: **Return**
    :    The shortest distance from the location to the edge
    of this shape. If negative, the given location in outside the shape.
            
    

### GetWidth<a name="GetWidth"></a>
!!! function "[[nodiscard]] AmReal32 GetWidth() const"

    
    Gets the width of the `BoxShape`.
    
    
    :material-keyboard-return: **Return**
    :    The box shape's width.
            
    

### SetHalfDepth<a name="SetHalfDepth"></a>
!!! function "void SetHalfDepth(AmReal32 halfDepth)"

    
    Sets the half depth of the `BoxShape`.
    
    
    :material-location-enter: **Parameter** `halfDepth`
    :    The new box shape's half depth.
                
    

### SetHalfHeight<a name="SetHalfHeight"></a>
!!! function "void SetHalfHeight(AmReal32 halfHeight)"

    
    Sets the half height of the `BoxShape`.
    
    
    :material-location-enter: **Parameter** `halfHeight`
    :    The new box shape's half height.
                
    

### SetHalfWidth<a name="SetHalfWidth"></a>
!!! function "void SetHalfWidth(AmReal32 halfWidth)"

    
    Sets the half width of the `BoxShape`.
    
    
    :material-location-enter: **Parameter** `halfWidth`
    :    The new box shape's half width.
                
    

