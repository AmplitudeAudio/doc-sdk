---
title: Orientation
description: Represents an orientation in 3D space.
generator: doxide
---


# Orientation

**struct  Orientation**


Represents an orientation in 3D space.

This class provides methods for converting between different coordinate systems and
manipulating orientations. The orientation can be built from yaw, pitch, and roll angles,
or from a forward and up vector. Once built, the orientation is stored in the ZYX representation
(yaw, pitch, roll), in the ZYZ representation, in the quaternion representation, and in forward-up
vectors representation.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Zero](#Zero) | Gets a zero Orientation instance. |
| [Orientation](#Orientation) | Constructs an Orientation instance with the given yaw, pitch, and roll angles. |
| [Orientation](#Orientation) | Constructs an Orientation instance from a forward and up vector. |
| [Orientation](#Orientation) | Constructs an Orientation instance from a quaternion. |
| [GetYaw](#GetYaw) | The angle of rotation around the Z-axis in radians following the ZYX convention.  |
| [GetPitch](#GetPitch) | The angle of rotation around the Y-axis in radians following the ZYX convention.  |
| [GetRoll](#GetRoll) | The angle of rotation around the X-axis in radians following the ZYX convention.  |
| [GetForward](#GetForward) | The forward vector of the orientation.  |
| [GetUp](#GetUp) | The up vector of the orientation.  |
| [GetAlpha](#GetAlpha) | The angle of rotation around the Z-axis in radians following the ZYZ convention.  |
| [GetBeta](#GetBeta) | The angle of rotation around the Y-axis in radians following the ZYZ convention.  |
| [GetGamma](#GetGamma) | The angle of rotation around the new Z-axis in radians following the ZYZ convention.  |
| [GetQuaternion](#GetQuaternion) | The quaternion representation of the orientation.  |
| [GetRotationMatrix](#GetRotationMatrix) | Converts the orientation to a rotation matrix. |
| [GetLookAtMatrix](#GetLookAtMatrix) | Converts the orientation to a look-at matrix. |

## Function Details

### GetAlpha<a name="GetAlpha"></a>
!!! function "[[nodiscard]] inline AmReal32 GetAlpha() const"

    
    The angle of rotation around the Z-axis in radians following the ZYZ convention.
             
    
    
    

### GetBeta<a name="GetBeta"></a>
!!! function "[[nodiscard]] inline AmReal32 GetBeta() const"

    
    The angle of rotation around the Y-axis in radians following the ZYZ convention.
             
    
    
    

### GetForward<a name="GetForward"></a>
!!! function "[[nodiscard]] inline AmVec3 GetForward() const"

    
    The forward vector of the orientation.
             
    
    
    

### GetGamma<a name="GetGamma"></a>
!!! function "[[nodiscard]] inline AmReal32 GetGamma() const"

    
    The angle of rotation around the new Z-axis in radians following the ZYZ convention.
             
    
    
    

### GetLookAtMatrix<a name="GetLookAtMatrix"></a>
!!! function "[[nodiscard]] AmMat4 GetLookAtMatrix(AmVec3 eye) const"

    
    Converts the orientation to a look-at matrix.
    
    
    :material-location-enter: **Parameter** `eye`
    :    The eye's location.
    
    
    :material-keyboard-return: **Return**
    :    A look-at matrix representing the current orientation, with the eye at the given location.
            
    

### GetPitch<a name="GetPitch"></a>
!!! function "[[nodiscard]] inline AmReal32 GetPitch() const"

    
    The angle of rotation around the Y-axis in radians following the ZYX convention.
             
    
    
    

### GetQuaternion<a name="GetQuaternion"></a>
!!! function "[[nodiscard]] inline AmQuat GetQuaternion() const"

    
    The quaternion representation of the orientation.
             
    
    
    

### GetRoll<a name="GetRoll"></a>
!!! function "[[nodiscard]] inline AmReal32 GetRoll() const"

    
    The angle of rotation around the X-axis in radians following the ZYX convention.
             
    
    
    

### GetRotationMatrix<a name="GetRotationMatrix"></a>
!!! function "[[nodiscard]] AmMat4 GetRotationMatrix() const"

    
    Converts the orientation to a rotation matrix.
    
    
    :material-keyboard-return: **Return**
    :    A rotation matrix representing the current orientation.
            
    

### GetUp<a name="GetUp"></a>
!!! function "[[nodiscard]] inline AmVec3 GetUp() const"

    
    The up vector of the orientation.
             
    
    
    

### GetYaw<a name="GetYaw"></a>
!!! function "[[nodiscard]] inline AmReal32 GetYaw() const"

    
    The angle of rotation around the Z-axis in radians following the ZYX convention.
             
    
    
    

### Orientation<a name="Orientation"></a>
!!! function "Orientation(AmReal32 yaw, AmReal32 pitch, AmReal32 roll)"

    
    Constructs an Orientation instance with the given yaw, pitch, and roll angles.
    
    
    :material-location-enter: **Parameter** `yaw`
    :    The angle of rotation around the X-axis in radians.
        
    :material-location-enter: **Parameter** `pitch`
    :    The angle of rotation around the Y-axis in radians.
        
    :material-location-enter: **Parameter** `roll`
    :    The angle of rotation around the Z-axis in radians.
                
    

!!! function "Orientation(AmVec3 forward, AmVec3 up)"

    
    Constructs an Orientation instance from a forward and up vector.
    
    
    :material-location-enter: **Parameter** `forward`
    :    The forward vector of the orientation.
        
    :material-location-enter: **Parameter** `up`
    :    The up vector of the orientation.
                
    

!!! function "Orientation(AmQuat quaternion)"

    
    Constructs an Orientation instance from a quaternion.
    
    
    :material-location-enter: **Parameter** `quaternion`
    :    The quaternion representing the orientation.
                
    

### Zero<a name="Zero"></a>
!!! function "static Orientation Zero()"

    
    Gets a zero Orientation instance.
    
    
    :material-keyboard-return: **Return**
    :    A zero Orientation instance. 0 for all angles.
            
    

