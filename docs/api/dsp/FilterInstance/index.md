---
title: FilterInstance
description: A Filter instance.
generator: doxide
---


# FilterInstance

**class  FilterInstance**


A Filter instance.

An object of this class will be created each time a `Filter` is requested.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_parent](#m_parent) | The parent filter object that created this instance.  |
| [m_numParams](#m_numParams) | The number of parameters available for this filter.  |
| [m_numParamsChanged](#m_numParamsChanged) | The number of parameters that have changed since the last frame.  |
| [m_parameters](#m_parameters) | The parameters buffer.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [FilterInstance](#FilterInstance) | Constructs a new `FilterInstance` object. |
| [~FilterInstance](#_u007eFilterInstance) | Destroys the `FilterInstance` object.  |
| [Initialize](#Initialize) | Initializes the filter instance with the provided number of parameters. |
| [AdvanceFrame](#AdvanceFrame) | Updates the filter instance state for the provided delta time. |
| [Process](#Process) | Executes the filter instance. |
| [GetParameter](#GetParameter) | Gets the current value of the parameter at the given index. |
| [SetParameter](#SetParameter) | Sets the value of the parameter at the given index. |
| [ProcessChannel](#ProcessChannel) | Executes the filter instance on a single channel of the given buffer. |
| [ProcessSample](#ProcessSample) | Executes the filter instance on a single sample of the given buffer. |

## Variable Details

### m_numParams<a name="m_numParams"></a>

!!! variable "AmUInt32 m_numParams"

    
    The number of parameters available for this filter.
             
    
    
    

### m_numParamsChanged<a name="m_numParamsChanged"></a>

!!! variable "AmUInt32 m_numParamsChanged"

    
    The number of parameters that have changed since the last frame.
             
    
    
    

### m_parameters<a name="m_parameters"></a>

!!! variable "AmReal32&#42; m_parameters"

    
    The parameters buffer.
             
    
    
    

### m_parent<a name="m_parent"></a>

!!! variable "Filter&#42; m_parent"

    
    The parent filter object that created this instance.
             
    
    
    

## Function Details

### AdvanceFrame<a name="AdvanceFrame"></a>
!!! function "virtual void AdvanceFrame(AmTime deltaTime)"

    
    Updates the filter instance state for the provided delta time.
    
    
    :material-location-enter: **Parameter** `deltaTime`
    :    The time in milliseconds since the last frame.
                
    

### FilterInstance<a name="FilterInstance"></a>
!!! function "explicit FilterInstance(Filter&#42; parent)"

    
    Constructs a new `FilterInstance` object.
    
    
    :material-location-enter: **Parameter** `parent`
    :    The parent `Filter` object that created this instance.
                
    

### GetParameter<a name="GetParameter"></a>
!!! function "virtual AmReal32 GetParameter(AmUInt32 parameterIndex)"

    
    Gets the current value of the parameter at the given index.
    
    
    :material-location-enter: **Parameter** `parameterIndex`
    :    The index of the parameter to retrieve.
    
    
    :material-keyboard-return: **Return**
    :    The current value of the parameter.
            
    

### Initialize<a name="Initialize"></a>
!!! function "AmResult Initialize(AmUInt32 paramCount)"

    
    Initializes the filter instance with the provided number of parameters.
    
    
    :material-location-enter: **Parameter** `paramCount`
    :    The number of parameters the filter will need.
                
    

### Process<a name="Process"></a>
!!! function "virtual void Process(const AudioBuffer&amp; in, AudioBuffer&amp; out, AmUInt64 frames, AmUInt32 sampleRate)"

    
    Executes the filter instance.
    
    
    :material-location-enter: **Parameter** `in`
    :    The input buffer on which the filter should be applied.
        
    :material-location-exit: **Parameter** `out`
    :    The output buffer where the filtered output will be stored.
        
    :material-location-enter: **Parameter** `frames`
    :    The number of frames to process.
        
    :material-location-enter: **Parameter** `sampleRate`
    :    The current sample rate of the `buffer`.
                
    

### ProcessChannel<a name="ProcessChannel"></a>
!!! function "virtual void ProcessChannel(const AudioBuffer&amp; in, AudioBuffer&amp; out, AmUInt16 channel, AmUInt64 frames, AmUInt32 sampleRate)"

    
    Executes the filter instance on a single channel of the given buffer.
    
    
    :material-location-enter: **Parameter** `in`
    :    The input buffer on which the filter should be applied.
        
    :material-location-exit: **Parameter** `out`
    :    The output buffer where the filtered output will be stored.
        
    :material-location-enter: **Parameter** `channel`
    :    The index of the channel to process.
        
    :material-location-enter: **Parameter** `frames`
    :    The number of frames to process.
        
    :material-location-enter: **Parameter** `sampleRate`
    :    The current sample rate of the `buffer`.
                
    

### ProcessSample<a name="ProcessSample"></a>
!!! function "virtual AmAudioSample ProcessSample(AmAudioSample sample, AmUInt16 channel, AmUInt32 sampleRate)"

    
    Executes the filter instance on a single sample of the given buffer.
    
    
    :material-location-enter: **Parameter** `sample`
    :    The audio sample to process.
        
    :material-location-enter: **Parameter** `channel`
    :    The index of the channel to process.
        
    :material-location-enter: **Parameter** `sampleRate`
    :    The current sample rate of the `buffer`.
                
    

### SetParameter<a name="SetParameter"></a>
!!! function "virtual void SetParameter(AmUInt32 parameterIndex, AmReal32 value)"

    
    Sets the value of the parameter at the given index.
    
    
    :material-location-enter: **Parameter** `parameterIndex`
    :    The index of the parameter to retrieve.
        
    :material-location-enter: **Parameter** `value`
    :    The value to set to the parameter.
                
    

### ~FilterInstance<a name="_u007eFilterInstance"></a>
!!! function "virtual ~FilterInstance()"

    
    Destroys the `FilterInstance` object.
             
    
    
    

