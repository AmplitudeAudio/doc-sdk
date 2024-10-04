---
title: EventCanceler
description: An helper class used to cancel a running `Event`.
generator: doxide
---


# EventCanceler

**class  EventCanceler**


An helper class used to cancel a running `Event`.


:material-eye-outline: **See**
:    Event


    


## Functions

| Name | Description |
| ---- | ----------- |
| [EventCanceler](#EventCanceler) | Creates an uninitialized `EventCanceler`. |
| [EventCanceler](#EventCanceler) | Creates an `EventCanceler` which will abort * the given event once cancelled. |
| [~EventCanceler](#_u007eEventCanceler) | Destroys the event canceller and releases * the wrapped event instance.  |
| [Valid](#Valid) | Checks whether this `EventCanceler` has been initialized. |
| [Cancel](#Cancel) | Cancels and abort the wrapped `Event`.  |
| [GetEvent](#GetEvent) | Returns the `Event` wrapped by this `EventCanceler`. |

## Function Details

### Cancel<a name="Cancel"></a>
!!! function "void Cancel() const"

    
    Cancels and abort the wrapped `Event`.
             
    
    
    

### EventCanceler<a name="EventCanceler"></a>
!!! function "EventCanceler()"

    
    Creates an uninitialized `EventCanceler`.
    
    An uninitialized `EventCanceler` cannot be canceled.
            
    

!!! function "explicit EventCanceler(EventInstance&#42; event)"

    
    Creates an `EventCanceler` which will abort
             * the given event once cancelled.
    
    
    :material-location-enter: **Parameter** `event`
    :    The event instance to cancel.
                
    

### GetEvent<a name="GetEvent"></a>
!!! function "[[nodiscard]] EventInstance&#42; GetEvent() const"

    
    Returns the `Event` wrapped by this `EventCanceler`.
    
    
    :material-keyboard-return: **Return**
    :    The `Event` wrapped by this `EventCanceler`.
            
    

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this `EventCanceler` has been initialized.
    
    
    :material-keyboard-return: **Return**
    :    `true` if this `EventCanceler` has been initialized, `false` otherwise.
            
    

### ~EventCanceler<a name="_u007eEventCanceler"></a>
!!! function "~EventCanceler()"

    
    Destroys the event canceller and releases
             * the wrapped event instance.
             
    
    
    

