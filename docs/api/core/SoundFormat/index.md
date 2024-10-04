---
title: SoundFormat
description: Describe the format of an audio sample.
generator: doxide
---


# SoundFormat

**struct  SoundFormat**


Describe the format of an audio sample.

This data structure is mainly filled by a `Codec` during the initialization time.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [SetAll](#SetAll) | Sets all the properties of the sound format. |
| [GetSampleRate](#GetSampleRate) | Get the sample rate. |
| [GetNumChannels](#GetNumChannels) | Get the number of channels. |
| [GetBitsPerSample](#GetBitsPerSample) | Get the bits per sample. |
| [GetFramesCount](#GetFramesCount) | Get the number of frames. |
| [GetFrameSize](#GetFrameSize) | Get the frame size. |
| [GetSampleType](#GetSampleType) | Get the sample type. |

## Function Details

### GetBitsPerSample<a name="GetBitsPerSample"></a>
!!! function "[[nodiscard]] inline AmUInt32 GetBitsPerSample() const"

    
    Get the bits per sample.
    
    
    :material-keyboard-return: **Return**
    :    The number of bits per sample.
            
    

### GetFrameSize<a name="GetFrameSize"></a>
!!! function "[[nodiscard]] inline AmUInt32 GetFrameSize() const"

    
    Get the frame size.
    
    
    :material-keyboard-return: **Return**
    :    The size of each audio frame in bytes.
            
    

### GetFramesCount<a name="GetFramesCount"></a>
!!! function "[[nodiscard]] inline AmUInt64 GetFramesCount() const"

    
    Get the number of frames.
    
    
    :material-keyboard-return: **Return**
    :    The total number of audio frames.
            
    

### GetNumChannels<a name="GetNumChannels"></a>
!!! function "[[nodiscard]] inline AmUInt16 GetNumChannels() const"

    
    Get the number of channels.
    
    
    :material-keyboard-return: **Return**
    :    The number of audio channels.
            
    

### GetSampleRate<a name="GetSampleRate"></a>
!!! function "[[nodiscard]] inline AmUInt32 GetSampleRate() const"

    
    Get the sample rate.
    
    
    :material-keyboard-return: **Return**
    :    The sample rate of the audio.
            
    

### GetSampleType<a name="GetSampleType"></a>
!!! function "[[nodiscard]] inline eAudioSampleFormat GetSampleType() const"

    
    Get the sample type.
    
    
    :material-keyboard-return: **Return**
    :    The type of audio sample.
            
    

### SetAll<a name="SetAll"></a>
!!! function "void SetAll( AmUInt32 sampleRate, AmUInt16 numChannels, AmUInt32 bitsPerSample, AmUInt64 framesCount, AmUInt32 frameSize, eAudioSampleFormat sampleType)"

    
    Sets all the properties of the sound format.
    
    
    :material-location-enter: **Parameter** `sampleRate`
    :    The sample rate of the audio.
        
    :material-location-enter: **Parameter** `numChannels`
    :    The number of audio channels.
        
    :material-location-enter: **Parameter** `bitsPerSample`
    :    The number of bits per sample.
        
    :material-location-enter: **Parameter** `framesCount`
    :    The total number of audio frames.
        
    :material-location-enter: **Parameter** `frameSize`
    :    The size of each audio frame in bytes.
        
    :material-location-enter: **Parameter** `sampleType`
    :    The type of audio sample.
                
    

