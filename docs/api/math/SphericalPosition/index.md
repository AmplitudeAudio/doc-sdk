---
title: SphericalPosition
description: Spherical coordinates representation.
generator: doxide
---


# SphericalPosition

**struct  SphericalPosition**


Spherical coordinates representation.

Describes the coordinates of a point on a sphere's surface, relative to
the center of that sphere.


    


## Operators

| Name | Description |
| ---- | ----------- |
| [operator==](#operator_u003d_u003d) | Compares two spherical positions for equality. |
| [operator!=](#operator_u0021_u003d) | Compares two spherical positions for inequality. |

## Functions

| Name | Description |
| ---- | ----------- |
| [FromWorldSpace](#FromWorldSpace) | Creates a spherical position from a 3D position in world space. |
| [ForHRTF](#ForHRTF) | Creates a spherical position from a 3D position in world space. |
| [FromDegrees](#FromDegrees) | Creates a spherical position from given azimuth and elevation in degrees. |
| [SphericalPosition](#SphericalPosition) | Creates a spherical position with default values (azimuth = 0, elevation = 0, radius = 1).  |
| [SphericalPosition](#SphericalPosition) | Creates a spherical position with given azimuth, elevation, and radius. |
| [FlipAzimuth](#FlipAzimuth) | Flips the azimuth of the spherical position and returns a new instance. |
| [Rotate](#Rotate) | Rotates the spherical position with the given rotation and returns a new instance. |
| [ToCartesian](#ToCartesian) | Converts the spherical position to a 3D position in world space. |
| [GetAzimuth](#GetAzimuth) | Gets the azimuth in radians of the spherical position. |
| [GetElevation](#GetElevation) | Gets the elevation in radians of the spherical position. |
| [GetRadius](#GetRadius) | Gets the distance from the center of the sphere to the point. |
| [SetAzimuth](#SetAzimuth) | Sets the azimuth in radians of the spherical position. |
| [SetElevation](#SetElevation) | Sets the elevation in radians of the spherical position. |
| [SetRadius](#SetRadius) | Sets the distance from the center of the sphere to the point. |

## Operator Details

### operator!=<a name="operator_u0021_u003d"></a>

!!! function "bool operator!=(const SphericalPosition&amp; other) const"

    
    Compares two spherical positions for inequality.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other spherical position to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the spherical positions are not equal, `false` otherwise.
            
    

### operator==<a name="operator_u003d_u003d"></a>

!!! function "bool operator==(const SphericalPosition&amp; other) const"

    
    Compares two spherical positions for equality.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other spherical position to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the spherical positions are equal, `false` otherwise.
            
    

## Function Details

### FlipAzimuth<a name="FlipAzimuth"></a>
!!! function "[[nodiscard]] SphericalPosition FlipAzimuth() const"

    
    Flips the azimuth of the spherical position and returns a new instance.
    
    
    :material-keyboard-return: **Return**
    :    A new spherical position with the azimuth flipped.
            
    

### ForHRTF<a name="ForHRTF"></a>
!!! function "static SphericalPosition ForHRTF(const AmVec3&amp; position)"

    
    Creates a spherical position from a 3D position in world space.
    
    This method is optimized for use in HRTF (Head-Related Transfer Function) space,
    where the azimuth is rotated 90 degrees around the z-axis.
    
    
    :material-location-enter: **Parameter** `position`
    :    The position in world space.
                
    

### FromDegrees<a name="FromDegrees"></a>
!!! function "static SphericalPosition FromDegrees(AmReal32 azimuthDegrees, AmReal32 elevationDegrees, AmReal32 radius = 1.0f)"

    
    Creates a spherical position from given azimuth and elevation in degrees.
    
    
    :material-location-enter: **Parameter** `azimuthDegrees`
    :    The azimuth in degrees.
        
    :material-location-enter: **Parameter** `elevationDegrees`
    :    The elevation in degrees.
        
    :material-location-enter: **Parameter** `radius`
    :    The distance from the center of the sphere to the point.
    
    
    :material-keyboard-return: **Return**
    :    A spherical position representing the given azimuth and elevation in degrees.
            
    

### FromWorldSpace<a name="FromWorldSpace"></a>
!!! function "static SphericalPosition FromWorldSpace(const AmVec3&amp; position)"

    
    Creates a spherical position from a 3D position in world space.
    
    
    :material-location-enter: **Parameter** `position`
    :    The position in world space.
                
    

### GetAzimuth<a name="GetAzimuth"></a>
!!! function "[[nodiscard]] inline AmReal32 GetAzimuth() const"

    
    Gets the azimuth in radians of the spherical position.
    
    
    :material-keyboard-return: **Return**
    :    The azimuth in radians of the spherical position.
            
    

### GetElevation<a name="GetElevation"></a>
!!! function "[[nodiscard]] inline AmReal32 GetElevation() const"

    
    Gets the elevation in radians of the spherical position.
    
    
    :material-keyboard-return: **Return**
    :    The elevation in radians of the spherical position.
            
    

### GetRadius<a name="GetRadius"></a>
!!! function "[[nodiscard]] inline AmReal32 GetRadius() const"

    
    Gets the distance from the center of the sphere to the point.
    
    
    :material-keyboard-return: **Return**
    :    The distance from the center of the sphere to the point.
            
    

### Rotate<a name="Rotate"></a>
!!! function "[[nodiscard]] SphericalPosition Rotate(AmQuat rotation) const"

    
    Rotates the spherical position with the given rotation and returns a new instance.
    
    
    :material-location-enter: **Parameter** `rotation`
    :    The rotation to apply to the spherical position.
    
    
    :material-keyboard-return: **Return**
    :    A rotated spherical position.
            
    

### SetAzimuth<a name="SetAzimuth"></a>
!!! function "inline void SetAzimuth(AmReal32 azimuth)"

    
    Sets the azimuth in radians of the spherical position.
    
    
    :material-location-enter: **Parameter** `azimuth`
    :    The new azimuth in radians.
                
    

### SetElevation<a name="SetElevation"></a>
!!! function "inline void SetElevation(AmReal32 elevation)"

    
    Sets the elevation in radians of the spherical position.
    
    
    :material-location-enter: **Parameter** `elevation`
    :    The new elevation in radians.
                
    

### SetRadius<a name="SetRadius"></a>
!!! function "inline void SetRadius(AmReal32 radius)"

    
    Sets the distance from the center of the sphere to the point.
    
    
    :material-location-enter: **Parameter** `radius`
    :    The new distance from the center of the sphere to the point.
                
    

### SphericalPosition<a name="SphericalPosition"></a>
!!! function "SphericalPosition() = default"

    
    Creates a spherical position with default values (azimuth = 0, elevation = 0, radius = 1).
             
    
    
    

!!! function "SphericalPosition(AmReal32 azimuth, AmReal32 elevation, AmReal32 radius = 1.0f)"

    
    Creates a spherical position with given azimuth, elevation, and radius.
    
    
    :material-location-enter: **Parameter** `azimuth`
    :    The rotation around the z-axis in radians.
        
    :material-location-enter: **Parameter** `elevation`
    :    The rotation around the x-axis in radians.
        
    :material-location-enter: **Parameter** `radius`
    :    The distance from the center of the sphere to the point.
                
    

### ToCartesian<a name="ToCartesian"></a>
!!! function "[[nodiscard]] AmVec3 ToCartesian() const"

    
    Converts the spherical position to a 3D position in world space.
    
    
    :material-keyboard-return: **Return**
    :    A 3D position in world space corresponding to the spherical position.
            
    

