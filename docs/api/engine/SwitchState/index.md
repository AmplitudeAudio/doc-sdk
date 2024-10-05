---
title: SwitchState
description: A switch state.
generator: doxide
---


# SwitchState

**struct  SwitchState**


A switch state.

A switch state is a single state that can be applied to a `SwitchContainer` to control which sounds are played.
Only one state can be active at a time in the same `Switch` asset.


:material-eye-outline: **See**
:    [Switch](../../assets/Switch/index.md), [SwitchContainer](../../assets/SwitchContainer/index.md)


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_id](#m_id) | The ID of this switch state. |
| [m_name](#m_name) | The name of this switch state.  |

## Operators

| Name | Description |
| ---- | ----------- |
| [operator==](#operator_u003d_u003d) | Compares this switch state with another one for equality. |
| [operator!=](#operator_u0021_u003d) | Compares this switch state with another one for inequality. |

## Functions

| Name | Description |
| ---- | ----------- |
| [Valid](#Valid) | Checks whether this switch state is valid. |

## Variable Details

### m_id<a name="m_id"></a>

!!! variable "AmObjectID m_id"

    
    The ID of this switch state.
    
    This ID is unique only in the parent switch.
            
    

### m_name<a name="m_name"></a>

!!! variable "AmString m_name"

    
    The name of this switch state.
             
    
    
    

## Operator Details

### operator!=<a name="operator_u0021_u003d"></a>

!!! function "bool operator!=(const SwitchState&amp; other) const"

    
    Compares this switch state with another one for inequality.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other switch state to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the switch states are not equal, `false` otherwise.
            
    

### operator==<a name="operator_u003d_u003d"></a>

!!! function "bool operator==(const SwitchState&amp; other) const"

    
    Compares this switch state with another one for equality.
    
    
    :material-location-enter: **Parameter** `[im]`
    :    other The other switch state to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the switch states are equal, `false` otherwise.
            
    

## Function Details

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this switch state is valid.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the switch state is valid, `false` otherwise.
            
    

