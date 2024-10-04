---
title: ChannelEventListener
description: Channel Event listener.
generator: doxide
---


# ChannelEventListener

**class  ChannelEventListener**


Channel Event listener.

Event handlers are registered to the event listener through a callback to receive
event notifications.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [ChannelEventListener](#ChannelEventListener) | Initializes a new channel event listener.  |
| [~ChannelEventListener](#_u007eChannelEventListener) | Destroys the channel event listener.  |
| [Add](#Add) | Registers a custom callback to this event listener. |
| [Call](#Call) | Executes the event by calling all the registered event handlers. |

## Function Details

### Add<a name="Add"></a>
!!! function "void Add(const ChannelEventCallback&amp; callback, void&#42; userData = nullptr)"

    
    Registers a custom callback to this event listener.
    
    
    :material-location-enter: **Parameter** `callback`
    :    The event callback.
        
    :material-location-enter: **Parameter** `userData`
    :    The additional data to pass to the handler when this listener receive the event.
                
    

### Call<a name="Call"></a>
!!! function "void Call(ChannelInternalState&#42; channel)"

    
    Executes the event by calling all the registered event handlers.
    
    
    :material-location-enter: **Parameter** `channel`
    :    The channel which have triggered the event.
    
    
    !!! warning
         This method is for internal usage only.
                
    

### ChannelEventListener<a name="ChannelEventListener"></a>
!!! function "ChannelEventListener()"

    
    Initializes a new channel event listener.
             
    
    
    

### ~ChannelEventListener<a name="_u007eChannelEventListener"></a>
!!! function "~ChannelEventListener()"

    
    Destroys the channel event listener.
             
    
    
    

