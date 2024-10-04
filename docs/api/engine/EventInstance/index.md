---
title: EventInstance
description: A triggered event.
generator: doxide
---


# EventInstance

**class  EventInstance**


A triggered event.

`EventInstance` objects are created when an `Event` is triggered. They represent
the lifetime of that event at that particular time.

The internal state of an `EventInstance` is owned by that `EventInstance`, that means
each time you trigger an `Event`, a new instance with its own state is created.


:material-eye-outline: **See**
:    Event


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~EventInstance](#_u007eEventInstance) | Default constructor.  |
| [AdvanceFrame](#AdvanceFrame) | Applies a frame update on this `Event`. |
| [IsRunning](#IsRunning) | Returns whether this `EventInstance` is running. |
| [Abort](#Abort) | Aborts the execution of this `Event`.  |

## Function Details

### Abort<a name="Abort"></a>
!!! function "virtual void Abort() = 0"

    
    Aborts the execution of this `Event`.
             
    
    
    

### AdvanceFrame<a name="AdvanceFrame"></a>
!!! function "virtual void AdvanceFrame(AmTime deltaTime) = 0"

    
    Applies a frame update on this `Event`.
    
    This method is called once per frame to update the event instance's state.
    
    
    :material-location-enter: **Parameter** `deltaTime`
    :    The time elapsed since the last frame.
    
    
    !!! warning
         This method is for internal usage only.
                
    

### IsRunning<a name="IsRunning"></a>
!!! function "[[nodiscard]] virtual bool IsRunning() const = 0"

    
    Returns whether this `EventInstance` is running.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the event is running, `false` otherwise.
            
    

### ~EventInstance<a name="_u007eEventInstance"></a>
!!! function "virtual ~EventInstance() = default"

    
    Default constructor.
             
    
    
    

