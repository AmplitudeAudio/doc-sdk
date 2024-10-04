---
title: SparkyStudios
description: 
generator: doxide
---


# SparkyStudios



## Types

| Name | Description |
| ---- | ----------- |
| [Amplimix](Amplimix/index.md) | Amplitude Audio Mixer. |
| [Attenuation](Attenuation/index.md) | Amplitude Attenuation. |
| [AttenuationZone](AttenuationZone/index.md) | The propagation shape for positional sounds. |
| [BarycentricCoordinates](BarycentricCoordinates/index.md) | Represents barycentric coordinates between a point and 3 vertices of a triangle.  |
| [BoxShape](BoxShape/index.md) | A box shape, defined by a width, an height, and a depth.  |
| [CapsuleShape](CapsuleShape/index.md) | A capsule shape, defined by a radius and an height.  |
| [CartesianCoordinateSystem](CartesianCoordinateSystem/index.md) | A class representing a cartesian coordinate system. |
| [Collection](Collection/index.md) | Amplitude Collection. |
| [ConeShape](ConeShape/index.md) | A cone shape, defined by a radius and an height.  |
| [ConsumerNodeInstance](ConsumerNodeInstance/index.md) | Interface for Amplimix pipeline nodes that can consume * audio data from an input buffer.  |
| [Curve](Curve/index.md) | A Curve which describe the variation of a value (on the Y-axis) according to another (on the X-axis).  |
| [CurvePart](CurvePart/index.md) | A part of a Curve. |
| [CurvePoint](CurvePoint/index.md) | A single point in a Curve.  |
| [Edge](Edge/index.md) | Represents an edge.  |
| [Effect](Effect/index.md) | Amplitude Effect. |
| [EffectInstance](EffectInstance/index.md) | An instance of an Effect asset. |
| [FFT](FFT/index.md) | The Fast Fourier Transform (FFT) class. |
| [Face](Face/index.md) | Represents a triangulated face.  |
| [Fader](Fader/index.md) | Helper class to process faders. |
| [FaderInstance](FaderInstance/index.md) | A Fader instance. An object of this class will be created each time a `Fader` is requested.  |
| [InputNodeInstance](InputNodeInstance/index.md) | Class used to marks the input of the pipeline. |
| [MixerNodeInstance](MixerNodeInstance/index.md) | Base class for Amplimix pipeline nodes that can mix * audio data from multiple input buffers, and outputs the result * of the mix.  |
| [Node](Node/index.md) | Base class for Amplimix pipeline nodes. |
| [NodeInstance](NodeInstance/index.md) | An instance of an Amplimix pipeline node. |
| [Orientation](Orientation/index.md) | Represents an orientation in 3D space. |
| [OutputNodeInstance](OutputNodeInstance/index.md) | Class used to marks the output of the pipeline. |
| [Pipeline](Pipeline/index.md) | A pipeline assembles a set of nodes to process audio data. |
| [ProcessorNodeInstance](ProcessorNodeInstance/index.md) | Base class for Amplimix pipeline nodes that can process * audio data in-place.  |
| [ProviderNodeInstance](ProviderNodeInstance/index.md) | Interface for Amplimix pipeline nodes that can provide * audio data to an output buffer.  |
| [Rtpc](Rtpc/index.md) | Amplitude Real-Time Parameter Control. |
| [RtpcValue](RtpcValue/index.md) | A RTPC compatible value is used as a wrapper to hold propertiy values * that can be linked to RTPCs. |
| [Shape](Shape/index.md) | A Shape. |
| [Sound](Sound/index.md) | Amplitude Sound. |
| [SoundBank](SoundBank/index.md) | Amplitude Sound Bank |
| [SoundObject](SoundObject/index.md) | The SoundObject class is the base class for all sound objects.  |
| [SphereShape](SphereShape/index.md) | A sphere shape, defined by a radius.  |
| [SphericalPosition](SphericalPosition/index.md) | Describes the coordinates of a point on a sphere's surface, relative * to the center of that sphere.  |
| [SplitComplex](SplitComplex/index.md) | Buffer for split-complex representation of FFT results. |
| [Switch](Switch/index.md) | Amplitude Switch. |
| [SwitchContainer](SwitchContainer/index.md) | Amplitude Switch Container. |
| [SwitchContainerItem](SwitchContainerItem/index.md) | Describes a single item within a SwitchContainer.  |
| [SwitchState](SwitchState/index.md) | A switch state.  |
| [Zone](Zone/index.md) | A shape that represents a zone in the world. |

## Functions

| Name | Description |
| ---- | ----------- |
| [AM_CALLBACK](#AM_CALLBACK) | Called just before the mixer process audio data.  |
| [AM_CALLBACK](#AM_CALLBACK) | Called just after the mixer process audio data.  |
| [FindGCD](#FindGCD) | Finds the greatest common divisor (GCD) of two integers. |
| [GetRelativeDirection](#GetRelativeDirection) | Returns a direction vector relative to a given position and rotation. |
| [IntegerPow](#IntegerPow) | Computes the value base^exp using the squared exponentiation method. |
| [NextPowerOf2](#NextPowerOf2) | Returns the next power of 2 of a given number. |

## Function Details

### AM_CALLBACK<a name="AM_CALLBACK"></a>
!!! function "AM_CALLBACK(void, BeforeMixCallback)(Amplimix&#42; mixer, AmVoidPtr buffer, AmUInt32 frames)"

    
    Called just before the mixer process audio data.
         
    
    
    

!!! function "AM_CALLBACK(void, AfterMixCallback)(Amplimix&#42; mixer, AmVoidPtr buffer, AmUInt32 frames)"

    
    Called just after the mixer process audio data.
         
    
    
    

### FindGCD<a name="FindGCD"></a>
!!! function "inline AmInt64 FindGCD(AmInt64 a, AmInt64 b)"

    
    Finds the greatest common divisor (GCD) of two integers.
    
    
    :material-location-enter: **Parameter** `a`
    :    First integer.
        
    :material-location-enter: **Parameter** `b`
    :    Second integer.
    
    
    :material-keyboard-return: **Return**
    :    The greatest common divisor of a and b.
        
    

### GetRelativeDirection<a name="GetRelativeDirection"></a>
!!! function "inline AmVec3 GetRelativeDirection(const AmVec3&amp; originPosition, const AmQuat&amp; originRotation, const AmVec3&amp; position)"

    
    Returns a direction vector relative to a given position and rotation.
    
    
    :material-location-enter: **Parameter** `originPosition`
    :    Origin position of the direction.
        
    :material-location-enter: **Parameter** `originRotation`
    :    Origin rotation of the direction.
        
    :material-location-enter: **Parameter** `position`
    :    Target position of the direction.
    
    
    :material-keyboard-return: **Return**
    :    A relative direction vector (not normalized).
        
    

### IntegerPow<a name="IntegerPow"></a>
!!! function "template&lt;typename T&gt; inline T IntegerPow(T base, AmInt32 exp)"

    
    Computes the value base^exp using the squared exponentiation method.
    
    
    :material-code-tags: **Template parameter** `T`
    :    An integer type, a floating-point type, or a any other type where operatror *= is defined.
        
    :material-location-enter: **Parameter** `base`
    :    Input of the power function.
        
    :material-location-enter: **Parameter** `exp`
    :    The exponent of the power function. Must be non-negative.
    
    
    :material-keyboard-return: **Return**
    :    The result of raising the base to the power of the exponent.
        
    

### NextPowerOf2<a name="NextPowerOf2"></a>
!!! function "template&lt;typename T&gt; inline T NextPowerOf2(const T&amp; val)"

    
    Returns the next power of 2 of a given number.
    
    
    :material-location-enter: **Parameter** `val`
    :    The number.
    
    
    :material-keyboard-return: **Return**
    :    The next power of 2.
        
    

