---
title: ResamplerInstance
description: A Resampler instance.
generator: doxide
---


# ResamplerInstance

**class  ResamplerInstance**


A Resampler instance.

An object of this class will be created each time a `Resampler` is requested.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [ResamplerInstance](#ResamplerInstance) | Constructs a new `ResamplerInstance` object. |
| [~ResamplerInstance](#_u007eResamplerInstance) | Default destructor.  |
| [Initialize](#Initialize) | Initializes a new instance of the resampler. |
| [Process](#Process) | Processes the audio data. |
| [SetSampleRate](#SetSampleRate) | Changes the input and output sample rate. |
| [GetSampleRateIn](#GetSampleRateIn) | Gets the current input sample rate. |
| [GetSampleRateOut](#GetSampleRateOut) | Gets the current output sample rate. |
| [GetChannelCount](#GetChannelCount) | Gets the current channels count. |
| [GetRequiredInputFrames](#GetRequiredInputFrames) | Returns the required number of frames to have as input for the given amount of output frames. |
| [GetExpectedOutputFrames](#GetExpectedOutputFrames) | Returns the expected number of frames to have as output for the given amount of input frames. |
| [GetInputLatency](#GetInputLatency) | Returns the current input latency in frames. |
| [GetOutputLatency](#GetOutputLatency) | Returns the current output latency in frames. |
| [Reset](#Reset) | Resets the internal resampler state.  |
| [Clear](#Clear) | Cleans up the internal resampler state and allocated data. |

## Function Details

### Clear<a name="Clear"></a>
!!! function "virtual void Clear() = 0"

    
    Cleans up the internal resampler state and allocated data.
    
    
    !!! note
         This method is called when the resampler is about to be destroyed.
                
    

### GetChannelCount<a name="GetChannelCount"></a>
!!! function "[[nodiscard]] virtual AmUInt16 GetChannelCount() const = 0"

    
    Gets the current channels count.
    
    
    :material-keyboard-return: **Return**
    :    The current channels count.
            
    

### GetExpectedOutputFrames<a name="GetExpectedOutputFrames"></a>
!!! function "[[nodiscard]] virtual AmUInt64 GetExpectedOutputFrames(AmUInt64 inputFrameCount) const = 0"

    
    Returns the expected number of frames to have as output for the given amount of input frames.
    
    
    :material-location-enter: **Parameter** `inputFrameCount`
    :    The number of input frames.
    
    
    :material-keyboard-return: **Return**
    :    The expected number of output frames for the given input frame count.
            
    

### GetInputLatency<a name="GetInputLatency"></a>
!!! function "[[nodiscard]] virtual AmUInt64 GetInputLatency() const = 0"

    
    Returns the current input latency in frames.
    
    
    :material-keyboard-return: **Return**
    :    The resampler's current input latency in frames.
            
    

### GetOutputLatency<a name="GetOutputLatency"></a>
!!! function "[[nodiscard]] virtual AmUInt64 GetOutputLatency() const = 0"

    
    Returns the current output latency in frames.
    
    
    :material-keyboard-return: **Return**
    :    The resampler's current output latency in frames.
            
    

### GetRequiredInputFrames<a name="GetRequiredInputFrames"></a>
!!! function "[[nodiscard]] virtual AmUInt64 GetRequiredInputFrames(AmUInt64 outputFrameCount) const = 0"

    
    Returns the required number of frames to have as input for the given amount of output frames.
    
    
    :material-location-enter: **Parameter** `outputFrameCount`
    :    The number of output frames.
    
    
    :material-keyboard-return: **Return**
    :    The input frame count needed to produce the given output frame count.
            
    

### GetSampleRateIn<a name="GetSampleRateIn"></a>
!!! function "[[nodiscard]] virtual AmUInt32 GetSampleRateIn() const = 0"

    
    Gets the current input sample rate.
    
    
    :material-keyboard-return: **Return**
    :    The current input sample rate.
            
    

### GetSampleRateOut<a name="GetSampleRateOut"></a>
!!! function "[[nodiscard]] virtual AmUInt32 GetSampleRateOut() const = 0"

    
    Gets the current output sample rate.
    
    
    :material-keyboard-return: **Return**
    :    The current output sample rate.
            
    

### Initialize<a name="Initialize"></a>
!!! function "virtual void Initialize(AmUInt16 channelCount, AmUInt32 sampleRateIn, AmUInt32 sampleRateOut) = 0"

    
    Initializes a new instance of the resampler.
    
    
    :material-location-enter: **Parameter** `channelCount`
    :    The number of channels in the audio data.
        
    :material-location-enter: **Parameter** `sampleRateIn`
    :    The input sample rate.
        
    :material-location-enter: **Parameter** `sampleRateOut`
    :    The output sample rate.
                
    

### Process<a name="Process"></a>
!!! function "virtual bool Process(const AudioBuffer&amp; input, AmUInt64&amp; inputFrames, AudioBuffer&amp; output, AmUInt64&amp; outputFrames) = 0"

    
    Processes the audio data.
    
    
    :material-location-enter: **Parameter** `input`
    :    The input audio data.
        
    :material-location-enter::material-location-exit: **Parameter** `inputFrames`
    :    The number of frames in the input buffer.
        
    :material-location-exit: **Parameter** `output`
    :    The output audio data.
        
    :material-location-enter::material-location-exit: **Parameter** `outputFrames`
    :    The number of frames in the output buffer.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the resampling was successful, `false` otherwise.
            
    

### ResamplerInstance<a name="ResamplerInstance"></a>
!!! function "ResamplerInstance() = default"

    
    Constructs a new `ResamplerInstance` object.
    
    This will initialize the resampler instance state to default values.
            
    

### Reset<a name="Reset"></a>
!!! function "virtual void Reset() = 0"

    
    Resets the internal resampler state.
             
    
    
    

### SetSampleRate<a name="SetSampleRate"></a>
!!! function "virtual void SetSampleRate(AmUInt32 sampleRateIn, AmUInt32 sampleRateOut) = 0"

    
    Changes the input and output sample rate.
    
    
    :material-location-enter: **Parameter** `sampleRateIn`
    :    The new input sample rate.
        
    :material-location-enter: **Parameter** `sampleRateOut`
    :    The new output sample rate.
                
    

### ~ResamplerInstance<a name="_u007eResamplerInstance"></a>
!!! function "virtual ~ResamplerInstance() = default"

    
    Default destructor.
             
    
    
    

