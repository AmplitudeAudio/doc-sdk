---
title: FaderInstance
description: A Fader instance. An object of this class will be created each time a `Fader` is requested. 
generator: doxide
---


# FaderInstance

**class  FaderInstance**


A Fader instance. An object of this class will be created each time a `Fader` is requested.
     




## Types

| Name | Description |
| ---- | ----------- |
| [Transition](Transition/index.md) | Create an animation transition function using * a one-dimensional cubic bezier curve. |

## Functions

| Name | Description |
| ---- | ----------- |
| [FaderInstance](#FaderInstance) | Construct a new FaderInstance object. |
| [Set](#Set) | Set up fader. |
| [Set](#Set) | Set up fader. |
| [SetDuration](#SetDuration) | Set the duration of the transition. |
| [GetFromTime](#GetFromTime) | Get the current fading value. |
| [GetFromPercentage](#GetFromPercentage) | Get the current fading value. |
| [GetState](#GetState) | Get the state of this Fader. |
| [SetState](#SetState) | Set the state of this Fader. |
| [Start](#Start) | Sets the fading start time. |

## Function Details

### FaderInstance<a name="FaderInstance"></a>
!!! function "FaderInstance()"

    
    Construct a new FaderInstance object.
    
    This will initialize the fader instance state to default values.
            
    

### GetFromPercentage<a name="GetFromPercentage"></a>
!!! function "virtual AmReal64 GetFromPercentage(AmReal64 percentage)"

    
    Get the current fading value.
    
    
    :material-location-enter: **Parameter** `percentage`
    :    The percentage of time elapsed. This should be in the range [0, 1].
    
    
    :material-keyboard-return: **Return**
    :    The current value.
            
    

### GetFromTime<a name="GetFromTime"></a>
!!! function "virtual AmReal64 GetFromTime(AmTime time)"

    
    Get the current fading value.
    
    To use this method you firstly need to define the fading start time using
    <code>Fader::Start()</code>.
    
    
    :material-location-enter: **Parameter** `time`
    :    The time at which the value should be calculated.
    
    
    :material-keyboard-return: **Return**
    :    The current value.
            
    

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] inline eFaderState GetState() const"

    
    Get the state of this Fader.
    
    
    :material-keyboard-return: **Return**
    :    The Fader state.
            
    

### Set<a name="Set"></a>
!!! function "void Set(AmReal64 from, AmReal64 to, AmTime duration)"

    
    Set up fader.
    
    
    :material-location-enter: **Parameter** `from`
    :    The start value.
        
    :material-location-enter: **Parameter** `to`
    :    The target value.
        
    :material-location-enter: **Parameter** `duration`
    :    The duration of transition.
                
    

!!! function "void Set(AmReal64 from, AmReal64 to)"

    
    Set up fader.
    
    
    :material-location-enter: **Parameter** `from`
    :    The start value.
        
    :material-location-enter: **Parameter** `to`
    :    The target value.
                
    

### SetDuration<a name="SetDuration"></a>
!!! function "void SetDuration(AmTime duration)"

    
    Set the duration of the transition.
    
    
    :material-location-enter: **Parameter** `duration`
    :    The transition duration.
                
    

### SetState<a name="SetState"></a>
!!! function "inline void SetState(eFaderState state)"

    
    Set the state of this Fader.
    
    
    :material-location-enter: **Parameter** `state`
    :    The state to set.
                
    

### Start<a name="Start"></a>
!!! function "void Start(AmTime time = 0.0)"

    
    Sets the fading start time.
    
    
    :material-location-enter: **Parameter** `time`
    :    The fading start time.
                
    

