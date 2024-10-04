---
title: EventInstance
description: A triggered event.
generator: doxide
---


# EventInstance

**class  EventInstance**


A triggered event.

EventInstance are created when an Event is effectively triggered. They represent
the lifetime of that event at that particular time.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [AdvanceFrame](#AdvanceFrame) | Applies a frame update on this Event. |
| [IsRunning](#IsRunning) | Returns whether thisEvent is running. |
| [Abort](#Abort) | Aborts the execution of this Event.  |

## Function Details

### Abort<a name="Abort"></a>
!!! function "virtual void Abort() = 0"

    
    Aborts the execution of this Event.
             
    
    
    

### AdvanceFrame<a name="AdvanceFrame"></a>
!!! function "virtual void AdvanceFrame(AmTime deltaTime) = 0"

    
    Applies a frame update on this Event.
    
    
    :material-location-enter: **Parameter** `deltaTime`
    :    The time elapsed since the last frame.
                
    

### IsRunning<a name="IsRunning"></a>
!!! function "[[nodiscard]] virtual bool IsRunning() const = 0"

    
    Returns whether thisEvent is running.
    
    
    :material-keyboard-return: **Return**
    :    true if the event is running, false otherwise.
            
    

