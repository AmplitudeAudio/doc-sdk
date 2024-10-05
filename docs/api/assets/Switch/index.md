---
title: Switch
description: Amplitude Switch Asset.
generator: doxide
---


# Switch

**class  Switch : public Asset&lt;AmSwitchID&gt;**


Amplitude Switch Asset.

A switch is a collection of states which can change the sounds played from a `SwitchContainer`.

For example, you can have a switch named `SurfaceType` which have `wood`, `grass`, `metal` and `water` as states. A
`SwitchContainer` using this switch can group sounds per switch states, so when a state is active, all the sounds of
that state are played. Changing the state of a `Switch` will updated ALL the `SwitchContainer` objects that use this `Switch`.

The `Switch` is a shared object between sound sources. They are used only by `SwitchContainer` objects.


:material-eye-outline: **See**
:    [SwitchState](../../engine/SwitchState/index.md), [SwitchContainer](../../assets/SwitchContainer/index.md)


    


## Functions

| Name | Description |
| ---- | ----------- |
| [GetState](#GetState) | Gets the current state of the switch. |
| [SetState](#SetState) | Sets the current state of the switch. |
| [SetState](#SetState) | Sets the current state of the switch using the state ID. |
| [SetState](#SetState) | Sets the current state of the switch using the state name. |
| [GetSwitchStates](#GetSwitchStates) | Gets the list of available SwitchStates in this Switch. |

## Function Details

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] virtual const SwitchState&amp; GetState() const = 0"

    
    Gets the current state of the switch.
    
    
    :material-keyboard-return: **Return**
    :    The current state of the switch.
            
    

### GetSwitchStates<a name="GetSwitchStates"></a>
!!! function "[[nodiscard]] virtual const std::vector&lt;SwitchState&gt;&amp; GetSwitchStates() const = 0"

    
    Gets the list of available SwitchStates in this Switch.
    
    
    :material-keyboard-return: **Return**
    :    The list of available SwitchStates.
            
    

### SetState<a name="SetState"></a>
!!! function "virtual void SetState(const SwitchState&amp; state) = 0"

    
    Sets the current state of the switch.
    
    
    !!! note
         Changing the state of a `Switch` will updated ALL the `SwitchContainer` objects that use this `Switch`.
    
    
    :material-location-enter: **Parameter** `state`
    :    The state to apply to the switch.
                
    

!!! function "virtual void SetState(AmObjectID id) = 0"

    
    Sets the current state of the switch using the state ID.
    
    
    !!! note
         Changing the state of a `Switch` will updated ALL the `SwitchContainer` objects that use this `Switch`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the state to apply. This ID should exist in the list
        of registered switch states.
                
    

!!! function "virtual void SetState(const AmString&amp; name) = 0"

    
    Sets the current state of the switch using the state name.
    
    
    !!! note
         Changing the state of a `Switch` will updated ALL the `SwitchContainer` objects that use this `Switch`.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the state to apply. This name should exist in the
        list of registered switch states.
                
    

