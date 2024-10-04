---
title: Switch
description: Amplitude Switch.
generator: doxide
---


# Switch

**class  Switch : public Asset&lt;AmSwitchID&gt;**


Amplitude Switch.

A switch is a collection of states which can change the sound played from a SwitchContainer.

For example, you can have a switch named "SurfaceType" which have "wood", "grass", "metal" and "water" as states. A
SwitchContainer using this switch can group sounds per switch states, so when a state is active, all the sounds of
that state are played.

The Switch is a shared object between sound sources. They are used only by SwitchContainer objects.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [GetState](#GetState) | Get the current state of the switch. |
| [SetState](#SetState) | Set the current state of the switch. |
| [SetState](#SetState) | Set the current state of the switch using the state ID. |
| [SetState](#SetState) | Set the current state of the switch using the state name. |
| [GetSwitchStates](#GetSwitchStates) | Get the list of available SwitchStates in this Switch. |

## Function Details

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] virtual const SwitchState&amp; GetState() const = 0"

    
    Get the current state of the switch.
    
    
    :material-keyboard-return: **Return**
    :    The current state of the switch.
            
    

### GetSwitchStates<a name="GetSwitchStates"></a>
!!! function "[[nodiscard]] virtual const std::vector&lt;SwitchState&gt;&amp; GetSwitchStates() const = 0"

    
    Get the list of available SwitchStates in this Switch.
    
    
    :material-keyboard-return: **Return**
    :    The list of available SwitchStates.
            
    

### SetState<a name="SetState"></a>
!!! function "virtual void SetState(const SwitchState&amp; state) = 0"

    
    Set the current state of the switch.
    
    
    :material-location-enter: **Parameter** `state`
    :    The state to apply to the switch.
                
    

!!! function "virtual void SetState(AmObjectID id) = 0"

    
    Set the current state of the switch using the state ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the state to apply. This ID should exist in the list
        of switch states.
                
    

!!! function "virtual void SetState(const AmString&amp; name) = 0"

    
    Set the current state of the switch using the state name.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the state to apply. This name should exist in the
        list of switch states.
                
    

