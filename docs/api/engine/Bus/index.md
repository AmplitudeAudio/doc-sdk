---
title: Bus
description: An object representing one node in the tree of buses. Buses are used to adjust a set of channel gains in tandem.
generator: doxide
---


# Bus

**class  Bus**


An object representing one node in the tree of buses. Buses are used to adjust a set of channel gains in tandem.

The `Bus` class is a lightweight reference to a `BusInternalState` object which
is managed by the Engine. There is always at least one bus, the **master** bus,
and any number of additional buses may be defined as well. Each bus can be
thought as a node in the tree. The gain on a `Bus` is applied to all child buses as well.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Bus](#Bus) | Creates an uninitialized `Bus`. |
| [Bus](#Bus) | Creates a wrapper instance over the provided state. |
| [Clear](#Clear) | Uninitializes this `Bus`. |
| [Valid](#Valid) | Checks whether this `Bus` has been initialized. |
| [GetId](#GetId) | Gets the unique ID of this `Bus`. |
| [GetName](#GetName) | Gets the name of this `Bus`. |
| [SetGain](#SetGain) | Sets the gain of this `Bus`. |
| [GetGain](#GetGain) | Returns the user specified gain on this `Bus`. |
| [FadeTo](#FadeTo) | Fades to `gain` over `duration` milliseconds. |
| [GetFinalGain](#GetFinalGain) | Returns the final calculated gain on this `Bus`. |
| [SetMute](#SetMute) | Sets the muted state of this `Bus`. |
| [IsMuted](#IsMuted) | Returns whether this `Bus` is muted. |
| [GetState](#GetState) | Returns the internal state of this `Bus`. |

## Function Details

### Bus<a name="Bus"></a>
!!! function "Bus()"

    
    Creates an uninitialized `Bus`.
    
    An uninitialized Bus cannot set or get any of it's fields.
            
    

!!! function "explicit Bus(BusInternalState&#42; state)"

    
    Creates a wrapper instance over the provided state.
    
    
    :material-location-enter: **Parameter** `state`
    :    The internal state to wrap.
    
    
    !!! warning
         This constructor is for internal usage only.
                
    

### Clear<a name="Clear"></a>
!!! function "void Clear()"

    
    Uninitializes this `Bus`.
    
    Note that this does not destroy the internal state it references,
    it just removes this reference to it.
            
    

### FadeTo<a name="FadeTo"></a>
!!! function "void FadeTo(AmReal32 gain, AmTime duration) const"

    
    Fades to `gain` over `duration` milliseconds.
    
    
    :material-location-enter: **Parameter** `gain`
    :    The gain value to fade to.
        
    :material-location-enter: **Parameter** `duration`
    :    The amount of time in milliseconds to take to reach the desired gain.
                
    

### GetFinalGain<a name="GetFinalGain"></a>
!!! function "[[nodiscard]] AmReal32 GetFinalGain() const"

    
    Returns the final calculated gain on this `Bus`.
    
    
    !!! note
         The final gain of a bus is the product of the gain specified in the bus
        definition file, with the gain specified by the user, and with the final gain
        of the parent bus.
    
    
    :material-keyboard-return: **Return**
    :    The final calculated gain.
            
    

### GetGain<a name="GetGain"></a>
!!! function "[[nodiscard]] AmReal32 GetGain() const"

    
    Returns the user specified gain on this `Bus`.
    
    
    :material-keyboard-return: **Return**
    :    The user specified gain.
            
    

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmBusID GetId() const"

    
    Gets the unique ID of this `Bus`.
    
    
    :material-keyboard-return: **Return**
    :    The bus unique ID.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Gets the name of this `Bus`.
    
    
    :material-keyboard-return: **Return**
    :    The bus name.
            
    

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] BusInternalState&#42; GetState() const"

    
    Returns the internal state of this `Bus`.
    
    
    !!! warning
         This method is only for internal usage.
    
    
    :material-keyboard-return: **Return**
    :    The bus internal state.
            
    

### IsMuted<a name="IsMuted"></a>
!!! function "[[nodiscard]] bool IsMuted() const"

    
    Returns whether this `Bus` is muted.
    
    
    :material-keyboard-return: **Return**
    :    `true` if this Bus is muted, `false` otherwise.
            
    

### SetGain<a name="SetGain"></a>
!!! function "void SetGain(AmReal32 gain) const"

    
    Sets the gain of this `Bus`.
    
    
    :material-location-enter: **Parameter** `gain`
    :    The new gain value.
                
    

### SetMute<a name="SetMute"></a>
!!! function "void SetMute(bool mute) const"

    
    Sets the muted state of this `Bus`.
    
    
    :material-location-enter: **Parameter** `mute`
    :    The muted state.
                
    

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this `Bus` has been initialized.
    
    
    :material-keyboard-return: **Return**
    :    `true` if this `Bus` has been initialized.
            
    

