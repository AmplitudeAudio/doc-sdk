---
title: AudioConverter
description: Allow converting audio buffers between different sample rates and channel counts.
generator: doxide
---


# AudioConverter

**class AudioConverter final**


Allow converting audio buffers between different sample rates and channel counts.


!!! note
     This class uses the `Resampler` class to perform sample rate conversion.
    
!!! note
         Only mono to stereo or vice versa conversions are supported.
            


## Types

| Name | Description |
| ---- | ----------- |
| [Settings](Settings/index.md) | Store conversion settings for an @c AudioConverter instance.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [AudioConverter](#AudioConverter) | Default constructor.  |
| [Configure](#Configure) | Initializes the audio converter with the given conversion settings. |
| [Process](#Process) | Converts the audio buffer from the source sample rate and channel count to the target sample rate and channel count. |
| [SetSampleRate](#SetSampleRate) | Updates the source sample rate and target sample rate. |
| [GetRequiredInputFrameCount](#GetRequiredInputFrameCount) | Returns the required number of frames to have as input for the * given amount of output frames. |
| [GetExpectedOutputFrameCount](#GetExpectedOutputFrameCount) | Returns the expected number of frames to have as output for the * given amount of input frames. |
| [GetInputLatency](#GetInputLatency) | Returns the current input latency in frames. |
| [GetOutputLatency](#GetOutputLatency) | Returns the current output latency in frames. |
| [Reset](#Reset) | Resets the internal state of the converter.  |
| [ConvertStereoFromMono](#ConvertStereoFromMono) | Convert stereo audio to mono. |
| [ConvertMonoFromStereo](#ConvertMonoFromStereo) | Convert mono audio to stereo. |

## Function Details

### AudioConverter<a name="AudioConverter"></a>
!!! function "AudioConverter()"

    
    Default constructor.
             
    
    
    

### Configure<a name="Configure"></a>
!!! function "bool Configure(const Settings&amp; settings)"

    
    Initializes the audio converter with the given conversion settings.
    
    
    :material-location-enter: **Parameter** `settings`
    :    The conversion settings.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the initialization was successful, `false` otherwise.
            
    

### ConvertMonoFromStereo<a name="ConvertMonoFromStereo"></a>
!!! function "static void ConvertMonoFromStereo(const AudioBuffer&amp; input, AudioBuffer&amp; output)"

    
    Convert mono audio to stereo.
    
    
    :material-location-enter: **Parameter** `input`
    :    The input audio buffer.
        
    :material-location-enter: **Parameter** `output`
    :    The output audio buffer to store the converted audio.
                
    

### ConvertStereoFromMono<a name="ConvertStereoFromMono"></a>
!!! function "static void ConvertStereoFromMono(const AudioBuffer&amp; input, AudioBuffer&amp; output)"

    
    Convert stereo audio to mono.
    
    
    :material-location-enter: **Parameter** `input`
    :    The input audio buffer.
        
    :material-location-enter: **Parameter** `output`
    :    The output audio buffer to store the converted audio.
                
    

### GetExpectedOutputFrameCount<a name="GetExpectedOutputFrameCount"></a>
!!! function "[[nodiscard]] AmUInt64 GetExpectedOutputFrameCount(AmUInt64 inputFrameCount) const"

    
    Returns the expected number of frames to have as output for the
             * given amount of input frames.
    
    
    :material-location-enter: **Parameter** `inputFrameCount`
    :    The number of input frames.
    
    
    :material-keyboard-return: **Return**
    :    The expected number of output frames for the given input frame count.
            
    

### GetInputLatency<a name="GetInputLatency"></a>
!!! function "[[nodiscard]] AmUInt64 GetInputLatency() const"

    
    Returns the current input latency in frames.
    
    
    :material-keyboard-return: **Return**
    :    The current input latency in frames.
            
    

### GetOutputLatency<a name="GetOutputLatency"></a>
!!! function "[[nodiscard]] AmUInt64 GetOutputLatency() const"

    
    Returns the current output latency in frames.
    
    
    :material-keyboard-return: **Return**
    :    The current output latency in frames.
            
    

### GetRequiredInputFrameCount<a name="GetRequiredInputFrameCount"></a>
!!! function "[[nodiscard]] AmUInt64 GetRequiredInputFrameCount(AmUInt64 outputFrameCount) const"

    
    Returns the required number of frames to have as input for the
             * given amount of output frames.
    
    
    :material-location-enter: **Parameter** `outputFrameCount`
    :    The number of output frames.
    
    
    :material-keyboard-return: **Return**
    :    The input frame count needed to produce the given output frame count.
            
    

### Process<a name="Process"></a>
!!! function "void Process(const AudioBuffer&amp; input, AmUInt64&amp; inputFrames, AudioBuffer&amp; output, AmUInt64&amp; outputFrames)"

    
    Converts the audio buffer from the source sample rate and channel count to the target sample rate and channel count.
    
    
    :material-location-enter: **Parameter** `input`
    :    The source audio buffer.
        
    :material-location-enter: **Parameter** `inputFrames`
    :    The number of frames to process in the input audio buffer.
        
    :material-location-enter: **Parameter** `output`
    :    The target audio buffer to store the converted audio.
        
    :material-location-enter: **Parameter** `outputFrames`
    :    The number of frames to process in the target audio buffer.
                
    

### Reset<a name="Reset"></a>
!!! function "void Reset()"

    
    Resets the internal state of the converter.
             
    
    
    

### SetSampleRate<a name="SetSampleRate"></a>
!!! function "void SetSampleRate(AmUInt64 sourceSampleRate, AmUInt64 targetSampleRate)"

    
    Updates the source sample rate and target sample rate.
    
    
    :material-location-enter: **Parameter** `sourceSampleRate`
    :    The source sample rate.
        
    :material-location-enter: **Parameter** `targetSampleRate`
    :    The target sample rate.
                
    

