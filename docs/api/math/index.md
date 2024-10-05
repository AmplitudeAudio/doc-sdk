---
title: Math
description: Math libraries and utilities
generator: doxide
---


# Math

Math libraries and utilities

## Types

| Name | Description |
| ---- | ----------- |
| [BarycentricCoordinates](BarycentricCoordinates/index.md) | Represents barycentric coordinates between a point and 3 vertices of a triangle. |
| [BeizerCurveControlPoints](BeizerCurveControlPoints/index.md) | A structure containing control points for a Bezier curve. |
| [BoxShape](BoxShape/index.md) | A box shape, defined by a width, an height, and a depth. |
| [BoxZone](BoxZone/index.md) | A `Zone` built with an inner `BoxShape` and an outer `BoxShape`. |
| [CapsuleShape](CapsuleShape/index.md) | A capsule shape, defined by a radius and an height. |
| [CapsuleZone](CapsuleZone/index.md) | A `Zone` built with an inner `CapsuleShape` and an outer `CapsuleShape`. |
| [CartesianCoordinateSystem](CartesianCoordinateSystem/index.md) | A class representing a cartesian coordinate system. |
| [ConeShape](ConeShape/index.md) | A cone shape, defined by a radius and an height. |
| [ConeZone](ConeZone/index.md) | A `Zone` built with an inner `ConeShape` and an outer `ConeShape`. |
| [Curve](Curve/index.md) | A `Curve` which describe the variation of a value (on the Y-axis) according to another (on the X-axis). |
| [CurvePart](CurvePart/index.md) | A segment of a `Curve`. |
| [CurvePoint](CurvePoint/index.md) | A single point in a Curve. |
| [Edge](Edge/index.md) | Represents an edge. |
| [Face](Face/index.md) | Represents a triangulated face. |
| [Orientation](Orientation/index.md) | Represents an orientation in 3D space. |
| [Shape](Shape/index.md) | A geometrical closed 3D shape. |
| [SphereShape](SphereShape/index.md) | A sphere shape, defined by a radius. |
| [SphereZone](SphereZone/index.md) | A `Zone` built with an inner `SphereShape` and an outer `SphereShape`. |
| [SphericalPosition](SphericalPosition/index.md) | Spherical coordinates representation. |
| [Zone](Zone/index.md) | A tuple of shapes that represents a zone in the world. |

## Macros

| Name | Description |
| ---- | ----------- |
| [AM_BETWEEN](#AM_BETWEEN) | Checks if a value is between a and b. |
| [AM_CLAMP](#AM_CLAMP) | Clamps a value between a and b. |

## Functions

| Name | Description |
| ---- | ----------- |
| [AmDitherReal32](#AmDitherReal32) | Generates a random number between `ditherMin` and `ditherMax`. |
| [AmFloatToFixedPoint](#AmFloatToFixedPoint) | Converts a 32-bit floating-point audio sample to a fixed-point representation. |
| [AmInt16ToReal32](#AmInt16ToReal32) | Converts a 16-bit signed integer audio sample to a 32-bit floating-point representation. |
| [AmInt32ToReal32](#AmInt32ToReal32) | Converts a 32-bit signed integer audio sample to a 32-bit floating-point representation. |
| [AmReal32ToInt16](#AmReal32ToInt16) | Converts a 32-bit floating-point audio sample to a 16-bit signed integer representation. |
| [CatmullRom](#CatmullRom) | Computes the Catmull-Rom interpolation value at a given time `t` between four points. |
| [ComputeDopplerFactor](#ComputeDopplerFactor) | Computes the Doppler factor for a sound source at a given location. |
| [FindGCD](#FindGCD) | Finds the greatest common divisor (GCD) of two integers. |
| [IntegerPow](#IntegerPow) | Computes the value base^exp using the squared exponentiation method. |
| [NextPowerOf2](#NextPowerOf2) | Returns the next power of 2 of a given number. |

## Macro Details

### AM_BETWEEN<a name="AM_BETWEEN"></a>

!!! macro "#define AM_BETWEEN(v, a, b)"

    
    Checks if a value is between a and b.
    
    
    :material-location-enter: **Parameter** `v`
    :    The value to check
        
    :material-location-enter: **Parameter** `a`
    :    The minimum value
        
    :material-location-enter: **Parameter** `b`
    :    The maximum value
    
    
    :material-keyboard-return: **Return**
    :    `true` if the value is between a and b, `false` otherwise.
    
    
    
    

### AM_CLAMP<a name="AM_CLAMP"></a>

!!! macro "#define AM_CLAMP(v, a, b)"

    
    Clamps a value between a and b.
    
    
    :material-location-enter: **Parameter** `v`
    :    The value to clamp
        
    :material-location-enter: **Parameter** `a`
    :    The minimum value
        
    :material-location-enter: **Parameter** `b`
    :    The maximum value
    
    
    :material-keyboard-return: **Return**
    :    The clamped value
    
    
    
    

## Function Details

### AmDitherReal32<a name="AmDitherReal32"></a>
!!! function "inline AmReal32 AmDitherReal32(const AmReal32 ditherMin, const AmReal32 ditherMax)"

    
    Generates a random number between `ditherMin` and `ditherMax`.
    
    
    :material-location-enter: **Parameter** `ditherMin`
    :    The minimum value for the random number.
        
    :material-location-enter: **Parameter** `ditherMax`
    :    The maximum value for the random number.
    
    
    :material-keyboard-return: **Return**
    :    A random number between `ditherMin` and `ditherMax`.
    
    
        
    

### AmFloatToFixedPoint<a name="AmFloatToFixedPoint"></a>
!!! function "inline AmInt32 AmFloatToFixedPoint(const AmReal32 x)"

    
    Converts a 32-bit floating-point audio sample to a fixed-point representation.
    
    
    :material-location-enter: **Parameter** `x`
    :    The 32-bit floating-point audio sample to convert.
    
    
    :material-keyboard-return: **Return**
    :    The fixed-point representation of the input 32-bit floating-point audio sample.
    
    
        
    

### AmInt16ToReal32<a name="AmInt16ToReal32"></a>
!!! function "inline AmReal32 AmInt16ToReal32(const AmInt16 x)"

    
    Converts a 16-bit signed integer audio sample to a 32-bit floating-point representation.
    
    
    :material-location-enter: **Parameter** `x`
    :    The 16-bit signed integer audio sample to convert.
    
    
    :material-keyboard-return: **Return**
    :    The 32-bit floating-point representation of the input 16-bit signed integer audio sample.
    
    
    !!! tip
         For more accurate conversion, the SDK should be compiled with the `AM_ACCURATE_CONVERSION`
        macro defined.
    
    
        
    

### AmInt32ToReal32<a name="AmInt32ToReal32"></a>
!!! function "inline AmReal32 AmInt32ToReal32(const AmInt32 x)"

    
    Converts a 32-bit signed integer audio sample to a 32-bit floating-point representation.
    
    
    :material-location-enter: **Parameter** `x`
    :    The 32-bit signed integer audio sample to convert.
    
    
    :material-keyboard-return: **Return**
    :    The 32-bit floating-point representation of the input 32-bit signed integer audio sample.
    
    
    !!! tip
         For more accurate conversion, the SDK should be compiled with the `AM_ACCURATE_CONVERSION`
        macro defined.
    
    
        
    

### AmReal32ToInt16<a name="AmReal32ToInt16"></a>
!!! function "inline AmInt16 AmReal32ToInt16(const AmReal32 x, bool dithering = false)"

    
    Converts a 32-bit floating-point audio sample to a 16-bit signed integer representation.
    
    
    :material-location-enter: **Parameter** `x`
    :    The 32-bit floating-point audio sample to convert.
        
    :material-location-enter: **Parameter** `dithering`
    :    If `true`, adds a dithering noise to the output.
    
    
    :material-keyboard-return: **Return**
    :    The 16-bit signed integer representation of the input 32-bit floating-point audio sample.
    
    
    !!! tip
         For more accurate conversion, the SDK should be compiled with the `AM_ACCURATE_CONVERSION`
        macro defined.
    
    
        
    

### CatmullRom<a name="CatmullRom"></a>
!!! function "inline AmReal32 CatmullRom(const AmReal32 t, const AmReal32 p0, const AmReal32 p1, const AmReal32 p2, const AmReal32 p3)"

    
    Computes the Catmull-Rom interpolation value at a given time `t` between four points.
    
    
    :material-location-enter: **Parameter** `t`
    :    The time value between 0 and 1.
        
    :material-location-enter: **Parameter** `p0`
    :    The first point.
        
    :material-location-enter: **Parameter** `p1`
    :    The second point.
        
    :material-location-enter: **Parameter** `p2`
    :    The third point.
        
    :material-location-enter: **Parameter** `p3`
    :    The fourth point.
    
    
    :material-keyboard-return: **Return**
    :    The Catmull-Rom interpolation value at the given time `t`.
    
    
        
    

### ComputeDopplerFactor<a name="ComputeDopplerFactor"></a>
!!! function "inline AmReal32 ComputeDopplerFactor( const AmVec3&amp; locationDelta, const AmVec3&amp; sourceVelocity, const AmVec3&amp; listenerVelocity, const AmReal32 soundSpeed, const AmReal32 dopplerFactor)"

    
    Computes the Doppler factor for a sound source at a given location.
    
    
    :material-location-enter: **Parameter** `locationDelta`
    :    The distance vector from the listener to the sound source.
        
    :material-location-enter: **Parameter** `sourceVelocity`
    :    The velocity of the sound source.
        
    :material-location-enter: **Parameter** `listenerVelocity`
    :    The velocity of the listener.
        
    :material-location-enter: **Parameter** `soundSpeed`
    :    The speed of sound.
        
    :material-location-enter: **Parameter** `dopplerFactor`
    :    The Doppler factor.
    
    
    :material-keyboard-return: **Return**
    :    The computed Doppler factor.
    
    
        
    

### FindGCD<a name="FindGCD"></a>
!!! function "inline AmInt64 FindGCD(AmInt64 a, AmInt64 b)"

    
    Finds the greatest common divisor (GCD) of two integers.
    
    
    :material-location-enter: **Parameter** `a`
    :    First integer.
        
    :material-location-enter: **Parameter** `b`
    :    Second integer.
    
    
    :material-keyboard-return: **Return**
    :    The greatest common divisor of a and b.
    
    
        
    

### IntegerPow<a name="IntegerPow"></a>
!!! function "template&lt;typename T&gt; inline T IntegerPow(T base, AmInt32 exp)"

    
    Computes the value base^exp using the squared exponentiation method.
    
    
    :material-code-tags: **Template parameter** `T`
    :    An integer type, a floating-point type, or a any other type where operator *= is defined.
    
    
    :material-location-enter: **Parameter** `base`
    :    Input of the power function.
        
    :material-location-enter: **Parameter** `exp`
    :    The exponent of the power function. Must be non-negative.
    
    
    :material-keyboard-return: **Return**
    :    The result of raising the base to the power of the exponent.
    
    
        
    

### NextPowerOf2<a name="NextPowerOf2"></a>
!!! function "template&lt;typename T&gt; inline T NextPowerOf2(const T&amp; val)"

    
    Returns the next power of 2 of a given number.
    
    
    :material-code-tags: **Template parameter** `T`
    :    An integer type, a floating-point type, or a any other type where operator *= is defined.
    
    
    :material-location-enter: **Parameter** `val`
    :    The number.
    
    
    :material-keyboard-return: **Return**
    :    The next power of 2.
    
    
        
    

