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
| [Collection](Collection/index.md) | Amplitude Collection. |
| [ConsumerNodeInstance](ConsumerNodeInstance/index.md) | Interface for Amplimix pipeline nodes that can consume * audio data from an input buffer.  |
| [Effect](Effect/index.md) | Amplitude Effect. |
| [EffectInstance](EffectInstance/index.md) | An instance of an Effect asset. |
| [InputNodeInstance](InputNodeInstance/index.md) | Class used to marks the input of the pipeline. |
| [MixerNodeInstance](MixerNodeInstance/index.md) | Base class for Amplimix pipeline nodes that can mix * audio data from multiple input buffers, and outputs the result * of the mix.  |
| [Node](Node/index.md) | Base class for Amplimix pipeline nodes. |
| [NodeInstance](NodeInstance/index.md) | An instance of an Amplimix pipeline node. |
| [OutputNodeInstance](OutputNodeInstance/index.md) | Class used to marks the output of the pipeline. |
| [Pipeline](Pipeline/index.md) | A pipeline assembles a set of nodes to process audio data. |
| [ProcessorNodeInstance](ProcessorNodeInstance/index.md) | Base class for Amplimix pipeline nodes that can process * audio data in-place.  |
| [ProviderNodeInstance](ProviderNodeInstance/index.md) | Interface for Amplimix pipeline nodes that can provide * audio data to an output buffer.  |
| [Rtpc](Rtpc/index.md) | Amplitude Real-Time Parameter Control. |
| [RtpcValue](RtpcValue/index.md) | A RTPC compatible value is used as a wrapper to hold propertiy values * that can be linked to RTPCs. |
| [Sound](Sound/index.md) | Amplitude Sound. |
| [SoundBank](SoundBank/index.md) | Amplitude Sound Bank |
| [SoundObject](SoundObject/index.md) | The SoundObject class is the base class for all sound objects.  |
| [SplitComplex](SplitComplex/index.md) | Buffer for split-complex representation of FFT results. |
| [Switch](Switch/index.md) | Amplitude Switch. |
| [SwitchContainer](SwitchContainer/index.md) | Amplitude Switch Container. |
| [SwitchContainerItem](SwitchContainerItem/index.md) | Describes a single item within a SwitchContainer.  |
| [SwitchState](SwitchState/index.md) | A switch state.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [AM_CALLBACK](#AM_CALLBACK) | Called just before the mixer process audio data.  |
| [AM_CALLBACK](#AM_CALLBACK) | Called just after the mixer process audio data.  |
| [GetRelativeDirection](#GetRelativeDirection) | Returns a direction vector relative to a given position and rotation. |

## Function Details

### AM_CALLBACK<a name="AM_CALLBACK"></a>
!!! function "AM_CALLBACK(void, BeforeMixCallback)(Amplimix&#42; mixer, AmVoidPtr buffer, AmUInt32 frames)"

    
    Called just before the mixer process audio data.
         
    
    
    

!!! function "AM_CALLBACK(void, AfterMixCallback)(Amplimix&#42; mixer, AmVoidPtr buffer, AmUInt32 frames)"

    
    Called just after the mixer process audio data.
         
    
    
    

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
        
    

