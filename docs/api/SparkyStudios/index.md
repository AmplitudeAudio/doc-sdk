---
title: SparkyStudios
description: 
generator: doxide
---


# SparkyStudios



:material-package: [Thread](Thread/index.md)
:   

## Types

| Name | Description |
| ---- | ----------- |
| [AmThreadHandle](AmThreadHandle/index.md) | The AmThreadFunction signature is used to create threads.  |
| [Amplimix](Amplimix/index.md) | Amplitude Audio Mixer. |
| [AmplimixLayer](AmplimixLayer/index.md) | Called just before the mixer process audio data. Called just after the mixer process audio data.  |
| [Attenuation](Attenuation/index.md) | Amplitude Attenuation. |
| [AttenuationZone](AttenuationZone/index.md) | The propagation shape for positional sounds. |
| [AudioConverter](AudioConverter/index.md) | Allow converting audio buffers between different sample rates and channel counts. |
| [BarycentricCoordinates](BarycentricCoordinates/index.md) | Represents barycentric coordinates between a point and 3 vertices of a triangle.  |
| [BoxShape](BoxShape/index.md) | A box shape, defined by a width, an height, and a depth.  |
| [CapsuleShape](CapsuleShape/index.md) | A capsule shape, defined by a radius and an height.  |
| [CartesianCoordinateSystem](CartesianCoordinateSystem/index.md) | A class representing a cartesian coordinate system. |
| [Collection](Collection/index.md) | Amplitude Collection. |
| [ConeShape](ConeShape/index.md) | A cone shape, defined by a radius and an height.  |
| [ConsoleLogger](ConsoleLogger/index.md) | The console logger class. |
| [ConsumerNodeInstance](ConsumerNodeInstance/index.md) | Interface for Amplimix pipeline nodes that can consume * audio data from an input buffer.  |
| [Curve](Curve/index.md) | A Curve which describe the variation of a value (on the Y-axis) according to another (on the X-axis).  |
| [CurvePart](CurvePart/index.md) | A part of a Curve. |
| [CurvePoint](CurvePoint/index.md) | A single point in a Curve.  |
| [DiskFile](DiskFile/index.md) | A File implementation that reads and writes a file on disk.  |
| [DiskFileSystem](DiskFileSystem/index.md) | A FileSystem implementation that reads and write files * from disk.  |
| [Edge](Edge/index.md) | Represents an edge.  |
| [Effect](Effect/index.md) | Amplitude Effect. |
| [EffectInstance](EffectInstance/index.md) | An instance of an Effect asset. |
| [Entity](Entity/index.md) | An Entity represent an object in the game. |
| [Environment](Environment/index.md) | An Environment is a zone where every spatialized audio playing inside him got * applied a specific effect. |
| [Event](Event/index.md) | An event is mainly used to apply a set of actions at a given time in game. |
| [EventCanceler](EventCanceler/index.md) | A class which can cancel a triggered Event.  |
| [EventInstance](EventInstance/index.md) | A triggered event. |
| [FFT](FFT/index.md) | The Fast Fourier Transform (FFT) class. |
| [Face](Face/index.md) | Represents a triangulated face.  |
| [Fader](Fader/index.md) | Helper class to process faders. |
| [FaderInstance](FaderInstance/index.md) | A Fader instance. An object of this class will be created each time a `Fader` is requested.  |
| [File](File/index.md) | Base class for a file in a FileSystem.  |
| [FileOpenKind](FileOpenKind/index.md) | The type of file being opened.  |
| [FileOpenMode](FileOpenMode/index.md) | Describes the mode in which open the file.  |
| [FileSeekOrigin](FileSeekOrigin/index.md) | Defines from where to seek in the file.  |
| [FileSystem](FileSystem/index.md) | Base class for files and resources loaders. |
| [Filter](Filter/index.md) | Helper class to manage filters. |
| [FilterInstance](FilterInstance/index.md) | A Filter instance. |
| [InputNodeInstance](InputNodeInstance/index.md) | Class used to marks the input of the pipeline. |
| [Listener](Listener/index.md) | An object whose distance from sounds determines their gain. |
| [LogMessageLevel](LogMessageLevel/index.md) | The level of a log message. |
| [Logger](Logger/index.md) | The logger class. |
| [MemoryFile](MemoryFile/index.md) | A File implementation that reads and writes a memory buffer.  |
| [MemoryManager](MemoryManager/index.md) | Manages memory allocations inside the engine.  |
| [MemoryManagerConfig](MemoryManagerConfig/index.md) | Configures the memory management system.  |
| [MemoryPoolKind](MemoryPoolKind/index.md) | Available memory pools.  |
| [MemoryPoolStats](MemoryPoolStats/index.md) | Collects the statistics about the memory allocations * for a specific pool  |
| [MixerNodeInstance](MixerNodeInstance/index.md) | Base class for Amplimix pipeline nodes that can mix * audio data from multiple input buffers, and outputs the result * of the mix.  |
| [Node](Node/index.md) | Base class for Amplimix pipeline nodes. |
| [NodeInstance](NodeInstance/index.md) | An instance of an Amplimix pipeline node. |
| [Orientation](Orientation/index.md) | Represents an orientation in 3D space. |
| [OutputNodeInstance](OutputNodeInstance/index.md) | Class used to marks the output of the pipeline. |
| [PackageFileCompressionAlgorithm](PackageFileCompressionAlgorithm/index.md) | Defines the compression algorithms a package file can be compressed with.  |
| [PackageFileHeaderDescription](PackageFileHeaderDescription/index.md) | Provides metadata about the package file.  |
| [PackageFileItemDescription](PackageFileItemDescription/index.md) | Describes an item in the package file. |
| [PackageFileSystem](PackageFileSystem/index.md) | A FileSystem implementation that provides access * to an Amplitude package file.  |
| [PackageItemFile](PackageItemFile/index.md) | A File implementation that provides access to an item in an * Amplitude package file.  |
| [Pipeline](Pipeline/index.md) | A pipeline assembles a set of nodes to process audio data. |
| [ProcessorNodeInstance](ProcessorNodeInstance/index.md) | Base class for Amplimix pipeline nodes that can process * audio data in-place.  |
| [ProviderNodeInstance](ProviderNodeInstance/index.md) | Interface for Amplimix pipeline nodes that can provide * audio data to an output buffer.  |
| [RefCounter](RefCounter/index.md) | Holds the number of references to an object.  |
| [ResamplerInstance](ResamplerInstance/index.md) | A Resampler instance. |
| [Resource](Resource/index.md) | An Amplitude resource in a FileSystem. |
| [Room](Room/index.md) | The absorption coefficients of the material. Represents a physical space where sound waves can propagate. Any sound source within the room will be affected * by the room's properties, and got applied early reflections and reverberation effects. |
| [RoomMaterial](RoomMaterial/index.md) | Represents the material of a @c Room wall.  |
| [RoomMaterialType](RoomMaterialType/index.md) | Defines the material type of a @c Room wall. |
| [RoomWall](RoomWall/index.md) | Enumerates the walls of a @c Room.  |
| [Rtpc](Rtpc/index.md) | Amplitude Real-Time Parameter Control. |
| [RtpcValue](RtpcValue/index.md) | A RTPC compatible value is used as a wrapper to hold propertiy values * that can be linked to RTPCs. |
| [ScopedMemoryAllocation](ScopedMemoryAllocation/index.md) | Allocates a block of memory with the given size in the given pool. |
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
| [FindGCD](#FindGCD) | Finds the greatest common divisor (GCD) of two integers. |
| [GetRelativeDirection](#GetRelativeDirection) | Returns a direction vector relative to a given position and rotation. |
| [IntegerPow](#IntegerPow) | Computes the value base^exp using the squared exponentiation method. |
| [NextPowerOf2](#NextPowerOf2) | Returns the next power of 2 of a given number. |

## Function Details

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
        
    

