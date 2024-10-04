---
title: Core
description: Core functionalities of the SDK
generator: doxide
---


# Core

Core functionalities of the SDK

## Types

| Name | Description |
| ---- | ----------- |
| [AmAlignedReal32Buffer](AmAlignedReal32Buffer/index.md) | Class that handles aligned allocations to support vectorized operations. |
| [AudioBuffer](AudioBuffer/index.md) | Represents an audio buffer containing multiple channels. |
| [AudioBufferChannel](AudioBufferChannel/index.md) | Represents a view to a single channel in an `AudioBuffer`. |
| [HRIRSphere](HRIRSphere/index.md) | A 3D sphere of HRIR data. |
| [HRIRSphereDatasetModel](HRIRSphereDatasetModel/index.md) | The model of the HRIR sphere dataset. |
| [HRIRSphereFileHeaderDescription](HRIRSphereFileHeaderDescription/index.md) | Provides metadata about an HRIR sphere file. |
| [HRIRSphereVertex](HRIRSphereVertex/index.md) | A vertex of the HRIR sphere. |
| [SoundFormat](SoundFormat/index.md) | Describe the format of an audio sample. |
| [Version](Version/index.md) | A structure containing the version number of the library. |
| [Version](Version/index.md) | Returns the version. |
| [eAudioSampleFormat](eAudioSampleFormat/index.md) | Enumerates the list of possible sample formats handled by Amplitude. |
| [eErrorCode](eErrorCode/index.md) | Enumerates the list of possible errors encountered by the library. |
| [eHRIRSphereSamplingMode](eHRIRSphereSamplingMode/index.md) | Defines how the HRIR sphere is sampled when doing Ambisonics binauralization. |
| [ePanningMode](ePanningMode/index.md) | Enumerates the list of available panning modes. |
| [eSpatialization](eSpatialization/index.md) | Enumerates the list of available spatialization modes. |

## Macros

| Name | Description |
| ---- | ----------- |
| [AM_CALLBACK](#AM_CALLBACK) | Declare a callback function type |
| [AM_UNUSED](#AM_UNUSED) | Helps to avoid compiler warnings about unused values. |

## Variables

| Name | Description |
| ---- | ----------- |
| [kAm51SurroundChannelCount](#kAm51SurroundChannelCount) | The number of channels in a 5.1 surround audio source. |
| [kAm71SurroundChannelCount](#kAm71SurroundChannelCount) | The number of channels in a 7.1 surround audio source. |
| [kAmAirAbsorptionBandCount](#kAmAirAbsorptionBandCount) | The number of air absorption bands for attenuation models. |
| [kAmFirstOrderAmbisonicChannelCount](#kAmFirstOrderAmbisonicChannelCount) | The number of channels in first-order ambisonic source. |
| [kAmFixedPointBits](#kAmFixedPointBits) | The number of bits to shift when processing audio data with floating point values. |
| [kAmFixedPointMask](#kAmFixedPointMask) | Used to mask the bits when processing audio data with fixed-point values. |
| [kAmFixedPointUnit](#kAmFixedPointUnit) | The unit value for a 32-bit fixed-point audio sample.. |
| [kAmInvalidObjectId](#kAmInvalidObjectId) | Invalid Amplitude object ID. |
| [kAmMasterBusId](#kAmMasterBusId) | Specifies the value of the "master" bus ID. |
| [kAmMaxSupportedAmbisonicOrder](#kAmMaxSupportedAmbisonicOrder) | The maximum supported ambisonic order. |
| [kAmMaxSupportedChannelCount](#kAmMaxSupportedChannelCount) | The maximum supported channel count for an ambisonic source. |
| [kAmMaxSupportedFrameCount](#kAmMaxSupportedFrameCount) | The maximum number of frames that can be processed at once. |
| [kAmMonoChannelCount](#kAmMonoChannelCount) | The number of channels in a mono audio source. |
| [kAmRoomSurfaceCount](#kAmRoomSurfaceCount) | The number of surfaces in a room. |
| [kAmSecond](#kAmSecond) | The number of milliseconds in one second. |
| [kAmSecondOrderAmbisonicChannelCount](#kAmSecondOrderAmbisonicChannelCount) | The number of channels in second-order ambisonic source. |
| [kAmStereoChannelCount](#kAmStereoChannelCount) | The number of channels in a stereo audio source. |
| [kAmThirdOrderAmbisonicChannelCount](#kAmThirdOrderAmbisonicChannelCount) | The number of channels in third-order ambisonic source. |
| [kEpsilon](#kEpsilon) | Minimum value where values lower than this are considered to be 0. |
| [kMinFadeDuration](#kMinFadeDuration) | The minimum fade duration in milliseconds. |

## Macro Details

### AM_CALLBACK<a name="AM_CALLBACK"></a>

!!! macro "#define AM_CALLBACK(_type_, _name_)"

    
    Declare a callback function type
    
    
    :material-location-enter: **Parameter** `_type_`
    :    Return type of the function
        
    :material-location-enter: **Parameter** `_name_`
    :    Name of the function
    
    
    !!! note
         This must be followed by the parentheses containing the function arguments declaration
    
    
    
    

### AM_UNUSED<a name="AM_UNUSED"></a>

!!! macro "#define AM_UNUSED(x)"

    
    Helps to avoid compiler warnings about unused values.
    
    
    :material-location-enter: **Parameter** `x`
    :    The statement where the return value is not used.
    
    
    
    

## Variable Details

### kAm51SurroundChannelCount<a name="kAm51SurroundChannelCount"></a>

!!! variable "constexpr AmSize kAm51SurroundChannelCount"

    
    The number of channels in a 5.1 surround audio source.
    
    
        
    

### kAm71SurroundChannelCount<a name="kAm71SurroundChannelCount"></a>

!!! variable "constexpr AmSize kAm71SurroundChannelCount"

    
    The number of channels in a 7.1 surround audio source.
    
    
        
    

### kAmAirAbsorptionBandCount<a name="kAmAirAbsorptionBandCount"></a>

!!! variable "constexpr AmUInt32 kAmAirAbsorptionBandCount"

    
    The number of air absorption bands for attenuation models.
    
    
        
    

### kAmFirstOrderAmbisonicChannelCount<a name="kAmFirstOrderAmbisonicChannelCount"></a>

!!! variable "constexpr AmSize kAmFirstOrderAmbisonicChannelCount"

    
    The number of channels in first-order ambisonic source.
    
    
        
    

### kAmFixedPointBits<a name="kAmFixedPointBits"></a>

!!! variable "constexpr AmInt32 kAmFixedPointBits"

    
    The number of bits to shift when processing audio data with floating point values.
    
    
        
    

### kAmFixedPointMask<a name="kAmFixedPointMask"></a>

!!! variable "constexpr AmInt32 kAmFixedPointMask"

    
    Used to mask the bits when processing audio data with fixed-point values.
    
    
        
    

### kAmFixedPointUnit<a name="kAmFixedPointUnit"></a>

!!! variable "constexpr AmInt32 kAmFixedPointUnit"

    
    The unit value for a 32-bit fixed-point audio sample..
    
    
        
    

### kAmInvalidObjectId<a name="kAmInvalidObjectId"></a>

!!! variable "constexpr AmObjectID kAmInvalidObjectId"

    
    Invalid Amplitude object ID.
    
    
        
    

### kAmMasterBusId<a name="kAmMasterBusId"></a>

!!! variable "constexpr AmBusID kAmMasterBusId"

    
    Specifies the value of the "master" bus ID.
    
    
        
    

### kAmMaxSupportedAmbisonicOrder<a name="kAmMaxSupportedAmbisonicOrder"></a>

!!! variable "constexpr AmUInt32 kAmMaxSupportedAmbisonicOrder"

    
    The maximum supported ambisonic order.
    
    
        
    

### kAmMaxSupportedChannelCount<a name="kAmMaxSupportedChannelCount"></a>

!!! variable "constexpr AmUInt32 kAmMaxSupportedChannelCount"

    
    The maximum supported channel count for an ambisonic source.
    
    
        
    

### kAmMaxSupportedFrameCount<a name="kAmMaxSupportedFrameCount"></a>

!!! variable "constexpr AmUInt64 kAmMaxSupportedFrameCount"

    
    The maximum number of frames that can be processed at once.
    
    
        
    

### kAmMonoChannelCount<a name="kAmMonoChannelCount"></a>

!!! variable "constexpr AmSize kAmMonoChannelCount"

    
    The number of channels in a mono audio source.
    
    
        
    

### kAmRoomSurfaceCount<a name="kAmRoomSurfaceCount"></a>

!!! variable "constexpr AmSize kAmRoomSurfaceCount"

    
    The number of surfaces in a room.
    
    
    !!! warning
         Only cube-shaped rooms are supported.
    
    
        
    

### kAmSecond<a name="kAmSecond"></a>

!!! variable "constexpr AmTime kAmSecond"

    
    The number of milliseconds in one second.
    
    
        
    

### kAmSecondOrderAmbisonicChannelCount<a name="kAmSecondOrderAmbisonicChannelCount"></a>

!!! variable "constexpr AmSize kAmSecondOrderAmbisonicChannelCount"

    
    The number of channels in second-order ambisonic source.
    
    
        
    

### kAmStereoChannelCount<a name="kAmStereoChannelCount"></a>

!!! variable "constexpr AmSize kAmStereoChannelCount"

    
    The number of channels in a stereo audio source.
    
    
        
    

### kAmThirdOrderAmbisonicChannelCount<a name="kAmThirdOrderAmbisonicChannelCount"></a>

!!! variable "constexpr AmSize kAmThirdOrderAmbisonicChannelCount"

    
    The number of channels in third-order ambisonic source.
    
    
        
    

### kEpsilon<a name="kEpsilon"></a>

!!! variable "constexpr AmReal32 kEpsilon"

    
    Minimum value where values lower than this are considered to be 0.
    
    
        
    

### kMinFadeDuration<a name="kMinFadeDuration"></a>

!!! variable "constexpr AmTime kMinFadeDuration"

    
    The minimum fade duration in milliseconds.
    
    
        
    

