---
title: Converter
description: Converts values from one cartesian coordinate system to another. 
generator: doxide
---


# Converter

**class  Converter**


Converts values from one cartesian coordinate system to another.
         




## Functions

| Name | Description |
| ---- | ----------- |
| [Converter](#Converter) | Constructs a converter from two cartesian coordinate systems. |
| [Forward](#Forward) | Converts a vector from the source coordinate system to the target coordinate system. |
| [Forward](#Forward) | Converts a quaternion from the source coordinate system to the target coordinate system. |
| [Forward](#Forward) | Converts a scalar from the source coordinate system to the target coordinate system. |
| [Backward](#Backward) | Converts a vector from the target coordinate system to the source coordinate system. |
| [Backward](#Backward) | Converts a quaternion from the target coordinate system to the source coordinate system. |
| [Backward](#Backward) | Converts a scalar from the target coordinate system to the source coordinate system. |

## Function Details

### Backward<a name="Backward"></a>
!!! function "[[nodiscard]] AmVec3 Backward(const AmVec3&amp; vector) const"

    
    Converts a vector from the target coordinate system to the source coordinate system.
    
    
    :material-location-enter: **Parameter** `vector`
    :    The vector to convert.
    
    
    :material-keyboard-return: **Return**
    :    A vector in the source coordinate system.
                
    

!!! function "[[nodiscard]] AmQuat Backward(const AmQuat&amp; quaternion) const"

    
    Converts a quaternion from the target coordinate system to the source coordinate system.
    
    
    :material-location-enter: **Parameter** `quaternion`
    :    The quaternion to convert.
    
    
    :material-keyboard-return: **Return**
    :    A quaternion in the source coordinate system.
                
    

!!! function "[[nodiscard]] AmReal32 Backward(const AmReal32&amp; scalar) const"

    
    Converts a scalar from the target coordinate system to the source coordinate system.
    
    
    :material-location-enter: **Parameter** `scalar`
    :    The scalar to convert.
    
    
    :material-keyboard-return: **Return**
    :    A scalar in the source coordinate system.
                
    

### Converter<a name="Converter"></a>
!!! function "Converter(const CartesianCoordinateSystem&amp; from, const CartesianCoordinateSystem&amp; to)"

    
    Constructs a converter from two cartesian coordinate systems.
    
    
    :material-location-enter: **Parameter** `from`
    :    The source cartesian coordinate system.
        
    :material-location-enter: **Parameter** `to`
    :    The target cartesian coordinate system.
                    
    

### Forward<a name="Forward"></a>
!!! function "[[nodiscard]] AmVec3 Forward(const AmVec3&amp; vector) const"

    
    Converts a vector from the source coordinate system to the target coordinate system.
    
    
    :material-location-enter: **Parameter** `vector`
    :    The vector to convert.
    
    
    :material-keyboard-return: **Return**
    :    A vector in the target coordinate system.
                
    

!!! function "[[nodiscard]] AmQuat Forward(const AmQuat&amp; quaternion) const"

    
    Converts a quaternion from the source coordinate system to the target coordinate system.
    
    
    :material-location-enter: **Parameter** `quaternion`
    :    The quaternion to convert.
    
    
    :material-keyboard-return: **Return**
    :    A quaternion in the target coordinate system.
                
    

!!! function "[[nodiscard]] AmReal32 Forward(const AmReal32&amp; scalar) const"

    
    Converts a scalar from the source coordinate system to the target coordinate system.
    
    
    :material-location-enter: **Parameter** `scalar`
    :    The scalar to convert.
    
    
    :material-keyboard-return: **Return**
    :    A scalar in the target coordinate system.
                
    

