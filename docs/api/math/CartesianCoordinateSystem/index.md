---
title: CartesianCoordinateSystem
description: A class representing a cartesian coordinate system.
generator: doxide
---


# CartesianCoordinateSystem

**class  CartesianCoordinateSystem**


A class representing a cartesian coordinate system.

It's used to know which direction is positive along each axis, and also allows
Amplitude to convert incoming data to the internal coordinate system.


    


## Types

| Name | Description |
| ---- | ----------- |
| [Axis](Axis/index.md) | Enumerates the axes of the cartesian coordinate system.  |
| [Converter](Converter/index.md) | Converts values from one cartesian coordinate system to another.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Default](#Default) | Creates a cartesian coordinate system which match the one used in Amplitude. |
| [AmbiX](#AmbiX) | Creates a cartesian coordinate system suitable for the AmbiX ambisonics format. |
| [RightHandedYUp](#RightHandedYUp) | Creates a right-handed, Y-up cartesian coordinate system. |
| [LeftHandedYUp](#LeftHandedYUp) | Creates a left-handed, Y-up cartesian coordinate system. |
| [RightHandedZUp](#RightHandedZUp) | Creates a right-handed, Z-up cartesian coordinate system. |
| [LeftHandedZUp](#LeftHandedZUp) | Creates a left-handed, Z-up cartesian coordinate system. |
| [Convert](#Convert) | Converts a vector from one coordinate system to another. |
| [ConvertToDefault](#ConvertToDefault) | Converts a vector from one coordinate system to the default coordinate system. |
| [GetVector](#GetVector) | Gets a vector corresponding to the given axis. |
| [CartesianCoordinateSystem](#CartesianCoordinateSystem) | Creates a new cartesian coordinate system with the given axes. |
| [GetRightVector](#GetRightVector) | Gets the vector corresponding to the coordinate system's right axis. * @return The coordinate system's right vector.  |
| [GetForwardVector](#GetForwardVector) | Gets the vector corresponding to the coordinate system's forward axis. * @return The coordinate system's forward vector.  |
| [GetUpVector](#GetUpVector) | Gets the vector corresponding to the coordinate system's up axis. * @return The coordinate system's up vector.  |
| [Convert](#Convert) | Converts a vector from one coordinate system to the current one. |
| [Convert](#Convert) | Converts a quaternion from one coordinate system to the current one. |
| [Convert](#Convert) | Converts a scalar from one coordinate system to the current one. |

## Function Details

### AmbiX<a name="AmbiX"></a>
!!! function "static CartesianCoordinateSystem AmbiX()"

    
    Creates a cartesian coordinate system suitable for the AmbiX ambisonics format.
    
    
    :material-keyboard-return: **Return**
    :    AmbiX format's cartesian coordinate system.
            
    

### CartesianCoordinateSystem<a name="CartesianCoordinateSystem"></a>
!!! function "CartesianCoordinateSystem(Axis right, Axis forward, Axis up)"

    
    Creates a new cartesian coordinate system with the given axes.
    
    
    :material-location-enter: **Parameter** `right`
    :    The right axis of the new coordinate system.
        
    :material-location-enter: **Parameter** `forward`
    :    The forward axis of the new coordinate system.
        
    :material-location-enter: **Parameter** `up`
    :    The up axis of the new coordinate system.
                
    

### Convert<a name="Convert"></a>
!!! function "static AmVec3 Convert(const AmVec3&amp; vector, const CartesianCoordinateSystem&amp; from, const CartesianCoordinateSystem&amp; to)"

    
    Converts a vector from one coordinate system to another.
    
    
    :material-location-enter: **Parameter** `vector`
    :    The vector to convert.
        
    :material-location-enter: **Parameter** `from`
    :    The source coordinate system.
        
    :material-location-enter: **Parameter** `to`
    :    The destination coordinate system.
    
    
    :material-keyboard-return: **Return**
    :    The converted vector.
            
    

!!! function "[[nodiscard]] AmVec3 Convert(const AmVec3&amp; vector, const CartesianCoordinateSystem&amp; from) const"

    
    Converts a vector from one coordinate system to the current one.
    
    
    :material-location-enter: **Parameter** `vector`
    :    The vector to convert.
        
    :material-location-enter: **Parameter** `from`
    :    The original coordinate system of the vector.
    
    
    :material-keyboard-return: **Return**
    :    The converted vector in the current coordinate system.
            
    

!!! function "[[nodiscard]] AmQuat Convert(const AmQuat&amp; quaternion, const CartesianCoordinateSystem&amp; from) const"

    
    Converts a quaternion from one coordinate system to the current one.
    
    
    :material-location-enter: **Parameter** `quaternion`
    :    The quaternion to convert.
        
    :material-location-enter: **Parameter** `from`
    :    The original coordinate system of the quaternion.
    
    
    :material-keyboard-return: **Return**
    :    The converted quaternion in the current coordinate system.
            
    

!!! function "[[nodiscard]] AmReal32 Convert(const AmReal32&amp; scalar, const CartesianCoordinateSystem&amp; from) const"

    
    Converts a scalar from one coordinate system to the current one.
    
    
    :material-location-enter: **Parameter** `scalar`
    :    The scalar to convert.
        
    :material-location-enter: **Parameter** `from`
    :    The original coordinate system of the scalar.
    
    
    :material-keyboard-return: **Return**
    :    The converted scalar in the current coordinate system.
            
    

### ConvertToDefault<a name="ConvertToDefault"></a>
!!! function "static AmVec3 ConvertToDefault(const AmVec3&amp; vector, const CartesianCoordinateSystem&amp; from)"

    
    Converts a vector from one coordinate system to the default coordinate system.
    
    
    :material-location-enter: **Parameter** `vector`
    :    The vector to convert.
        
    :material-location-enter: **Parameter** `from`
    :    The source coordinate system.
    
    
    :material-keyboard-return: **Return**
    :    The converted vector.
            
    

### Default<a name="Default"></a>
!!! function "static CartesianCoordinateSystem Default()"

    
    Creates a cartesian coordinate system which match the one used in Amplitude.
    
    
    :material-keyboard-return: **Return**
    :    Amplitude's internal coordinate system for right-handed, Z-up cartesian coordinate system.
            
    

### GetForwardVector<a name="GetForwardVector"></a>
!!! function "[[nodiscard]] inline AmVec3 GetForwardVector() const"

    
    Gets the vector corresponding to the coordinate system's forward axis.
             * @return The coordinate system's forward vector.
             
    
    
    

### GetRightVector<a name="GetRightVector"></a>
!!! function "[[nodiscard]] inline AmVec3 GetRightVector() const"

    
    Gets the vector corresponding to the coordinate system's right axis.
             * @return The coordinate system's right vector.
             
    
    
    

### GetUpVector<a name="GetUpVector"></a>
!!! function "[[nodiscard]] inline AmVec3 GetUpVector() const"

    
    Gets the vector corresponding to the coordinate system's up axis.
             * @return The coordinate system's up vector.
             
    
    
    

### GetVector<a name="GetVector"></a>
!!! function "[[nodiscard]] static AmVec3 GetVector(Axis axis)"

    
    Gets a vector corresponding to the given axis.
    
    
    :material-location-enter: **Parameter** `axis`
    :    The axis to get the vector for.
    
    
    :material-keyboard-return: **Return**
    :    A vector corresponding to the given axis.
            
    

### LeftHandedYUp<a name="LeftHandedYUp"></a>
!!! function "static CartesianCoordinateSystem LeftHandedYUp()"

    
    Creates a left-handed, Y-up cartesian coordinate system.
    
    
    :material-keyboard-return: **Return**
    :    A left-handed, Y-up cartesian coordinate system.
            
    

### LeftHandedZUp<a name="LeftHandedZUp"></a>
!!! function "static CartesianCoordinateSystem LeftHandedZUp()"

    
    Creates a left-handed, Z-up cartesian coordinate system.
    
    
    :material-keyboard-return: **Return**
    :    A left-handed, Z-up cartesian coordinate system.
            
    

### RightHandedYUp<a name="RightHandedYUp"></a>
!!! function "static CartesianCoordinateSystem RightHandedYUp()"

    
    Creates a right-handed, Y-up cartesian coordinate system.
    
    
    :material-keyboard-return: **Return**
    :    A right-handed, Y-up cartesian coordinate system.
            
    

### RightHandedZUp<a name="RightHandedZUp"></a>
!!! function "static CartesianCoordinateSystem RightHandedZUp()"

    
    Creates a right-handed, Z-up cartesian coordinate system.
    
    
    :material-keyboard-return: **Return**
    :    A right-handed, Z-up cartesian coordinate system.
            
    

