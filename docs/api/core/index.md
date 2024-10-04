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
| [AmThreadHandle](AmThreadHandle/index.md) | The AmThreadFunction signature is used to create threads. |
| [AudioBuffer](AudioBuffer/index.md) | Represents an audio buffer containing multiple channels. |
| [AudioBufferChannel](AudioBufferChannel/index.md) | Represents a view to a single channel in an `AudioBuffer`. |
| [AwaitablePoolTask](AwaitablePoolTask/index.md) | A pool task that allows a thread to wait until it finishes. |
| [ConsoleLogger](ConsoleLogger/index.md) | The console logger class. |
| [HRIRSphere](HRIRSphere/index.md) | A 3D sphere of HRIR data. |
| [HRIRSphereDatasetModel](HRIRSphereDatasetModel/index.md) | The model of the HRIR sphere dataset. |
| [HRIRSphereFileHeaderDescription](HRIRSphereFileHeaderDescription/index.md) | Provides metadata about an HRIR sphere file. |
| [HRIRSphereVertex](HRIRSphereVertex/index.md) | A vertex of the HRIR sphere. |
| [Logger](Logger/index.md) | The logger class. |
| [Pool](Pool/index.md) | Pool tasks scheduler class. |
| [PoolTask](PoolTask/index.md) | Base class for pool tasks. |
| [RefCounter](RefCounter/index.md) | Holds the number of references to an object. |
| [SoundFormat](SoundFormat/index.md) | Describe the format of an audio sample. |
| [Version](Version/index.md) | A structure containing the version number of the library. |
| [Version](Version/index.md) | Returns the version. |
| [eAudioSampleFormat](eAudioSampleFormat/index.md) | Enumerates the list of possible sample formats handled by Amplitude. |
| [eErrorCode](eErrorCode/index.md) | Enumerates the list of possible errors encountered by the library. |
| [eHRIRSphereSamplingMode](eHRIRSphereSamplingMode/index.md) | Defines how the HRIR sphere is sampled when doing Ambisonics binauralization. |
| [eLogMessageLevel](eLogMessageLevel/index.md) | The level of a log message. |
| [ePanningMode](ePanningMode/index.md) | Enumerates the list of available panning modes. |
| [eSpatialization](eSpatialization/index.md) | Enumerates the list of available spatialization modes. |

## Macros

| Name | Description |
| ---- | ----------- |
| [AM_CALLBACK](#AM_CALLBACK) | Declare a callback function type |
| [AM_UNUSED](#AM_UNUSED) | Helps to avoid compiler warnings about unused values. |
| [amLog](#amLog) | Logs a message with the given level. |
| [amLogCritical](#amLogCritical) | Logs a critical message. |
| [amLogDebug](#amLogDebug) | Logs a debug message. |
| [amLogError](#amLogError) | Logs an error message. |
| [amLogInfo](#amLogInfo) | Logs an informational message. |
| [amLogWarning](#amLogWarning) | Logs a warning message. |
| [amLogger](#amLogger) | The global logger instance. |

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

## Functions

| Name | Description |
| ---- | ----------- |
| [CreateMutex](#CreateMutex) | Creates a mutex object. |
| [CreateThread](#CreateThread) | Creates a new thread. |
| [DestroyMutex](#DestroyMutex) | Destroys a mutex object. |
| [GetCurrentThreadId](#GetCurrentThreadId) | Gets the handle of the calling thread. |
| [GetTimeMillis](#GetTimeMillis) | Gets the total execution time in milliseconds for the calling thread. |
| [LockMutex](#LockMutex) | Takes ownership of a mutex. |
| [Release](#Release) | Manually stops a thread execution. |
| [Sleep](#Sleep) | Makes the calling thread sleep for the given amount of milliseconds. |
| [UnlockMutex](#UnlockMutex) | Releases ownership of a mutex. |
| [Wait](#Wait) | Waits for the given thread to stop. |

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
    
    
    
    

### amLog<a name="amLog"></a>

!!! macro "#define amLog(_level_, _message_, ...)                                                                                                     \"

    
    Logs a message with the given level.
    
    
    :material-location-enter: **Parameter** `_level_`
    :    The level of the log message.
        
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
    
    
    
    

### amLogCritical<a name="amLogCritical"></a>

!!! macro "#define amLogCritical(_message_, ...)"

    
    Logs a critical message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
    
    
    
    

### amLogDebug<a name="amLogDebug"></a>

!!! macro "#define amLogDebug(_message_, ...)"

    
    Logs a debug message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
    
    
    
    

### amLogError<a name="amLogError"></a>

!!! macro "#define amLogError(_message_, ...)"

    
    Logs an error message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
    
    
    
    

### amLogInfo<a name="amLogInfo"></a>

!!! macro "#define amLogInfo(_message_, ...)"

    
    Logs an informational message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
    
    
    
    

### amLogWarning<a name="amLogWarning"></a>

!!! macro "#define amLogWarning(_message_, ...)"

    
    Logs a warning message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
    
    
    
    

### amLogger<a name="amLogger"></a>

!!! macro "#define amLogger"

    
    The global logger instance.
    
    
    
    

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
    
    
        
    

## Function Details

### CreateMutex<a name="CreateMutex"></a>
!!! function "AmMutexHandle CreateMutex(AmUInt64 spinCount = 100)"

    
    Creates a mutex object.
    
    A mutex is an object that a thread can acquire, preventing other
    threads from acquiring it.
    
    To acquire the mutex ownership, you should use [`LockMutex()`](#LockMutex) with
    the mutex handle as parameter. To release the ownership, use [`UnlockMutex()`](#UnlockMutex)
    with the mutex handle as parameter.
    
    
    :material-location-enter: **Parameter** `spinCount`
    :    The number of times the mutex should spin before checking if it's available.
    
    
            
    

### CreateThread<a name="CreateThread"></a>
!!! function "AmThreadHandle CreateThread(AmThreadFunction threadFunction, AmVoidPtr parameter = nullptr)"

    
    Creates a new thread.
    
    
    :material-location-enter: **Parameter** `threadFunction`
    :    The function to run in the thread.
        
    :material-location-enter: **Parameter** `parameter`
    :    An optional shared data to pass to the thread
    
    
            
    

### DestroyMutex<a name="DestroyMutex"></a>
!!! function "void DestroyMutex(AmMutexHandle handle)"

    
    Destroys a mutex object.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The mutex object handle.
    
    
            
    

### GetCurrentThreadId<a name="GetCurrentThreadId"></a>
!!! function "AmThreadID GetCurrentThreadId()"

    
    Gets the handle of the calling thread.
    
    
            
    

### GetTimeMillis<a name="GetTimeMillis"></a>
!!! function "AmUInt64 GetTimeMillis()"

    
    Gets the total execution time in milliseconds for the calling thread.
    
    
            
    

### LockMutex<a name="LockMutex"></a>
!!! function "void LockMutex(AmMutexHandle handle)"

    
    Takes ownership of a mutex.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The mutex object handle.
    
    
            
    

### Release<a name="Release"></a>
!!! function "void Release(AmThreadHandle&amp; thread)"

    
    Manually stops a thread execution.
    
    
    :material-location-enter: **Parameter** `thread`
    :    The handle of the thread to stop.
    
    
            
    

### Sleep<a name="Sleep"></a>
!!! function "void Sleep(AmInt32 milliseconds)"

    
    Makes the calling thread sleep for the given amount of milliseconds.
    
    
    :material-location-enter: **Parameter** `milliseconds`
    :    The amount of time the calling thread should sleep.
    
    
            
    

### UnlockMutex<a name="UnlockMutex"></a>
!!! function "void UnlockMutex(AmMutexHandle handle)"

    
    Releases ownership of a mutex.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The mutex object handle.
    
    
            
    

### Wait<a name="Wait"></a>
!!! function "void Wait(AmThreadHandle thread)"

    
    Waits for the given thread to stop.
    
    
    :material-location-enter: **Parameter** `thread`
    :    The handle of the thread to wait.
    
    
            
    

