---
title: BarycentricCoordinates
description: Represents barycentric coordinates between a point and 3 vertices of a triangle. 
generator: doxide
---


# BarycentricCoordinates

**struct BarycentricCoordinates**


Represents barycentric coordinates between a point and 3 vertices of a triangle.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [RayTriangleIntersection](#RayTriangleIntersection) | Computes the barycentric coordinates of the intersection of a ray with a triangle. |
| [BarycentricCoordinates](#BarycentricCoordinates) | Default constructor.  |
| [BarycentricCoordinates](#BarycentricCoordinates) | Computes barycentric coordinates from a position and a triangle. |
| [IsValid](#IsValid) | Checks whether the coordinates are valid. |

## Function Details

### BarycentricCoordinates<a name="BarycentricCoordinates"></a>
!!! function "BarycentricCoordinates()"

    
    Default constructor.
             
    
    
    

!!! function "BarycentricCoordinates(const AmVec3&amp; position, const std::array&lt;AmVec3, 3&gt;&amp; triangle)"

    
    Computes barycentric coordinates from a position and a triangle.
    
    
    :material-location-enter: **Parameter** `position`
    :    The position of the intersection.
        
    :material-location-enter: **Parameter** `triangle`
    :    The triangle.
                
    

### IsValid<a name="IsValid"></a>
!!! function "[[nodiscard]] bool IsValid() const"

    
    Checks whether the coordinates are valid.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the coordinates are valid, `false` otherwise.
            
    

### RayTriangleIntersection<a name="RayTriangleIntersection"></a>
!!! function "static bool RayTriangleIntersection( const AmVec3&amp; rayOrigin, const AmVec3&amp; rayDirection, const std::array&lt;AmVec3, 3&gt;&amp; triangle, BarycentricCoordinates&amp; result)"

    
    Computes the barycentric coordinates of the intersection of a ray with a triangle.
    
    
    :material-location-enter: **Parameter** `rayOrigin`
    :    The origin of the ray.
        
    :material-location-enter: **Parameter** `rayDirection`
    :    The direction of the ray.
        
    :material-location-enter: **Parameter** `triangle`
    :    The vertices of the triangle.
        
    :material-location-enter: **Parameter** `result`
    :    The result of the intersection.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the ray intersects the triangle, `false` otherwise.
            
    

