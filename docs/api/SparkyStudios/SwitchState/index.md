---
title: SwitchState
description: A switch state. 
generator: doxide
---


# SwitchState

**struct  SwitchState**


A switch state.
     




## Variables

| Name | Description |
| ---- | ----------- |
| [m_id](#m_id) | The ID of this switch state. |
| [m_name](#m_name) | The name of this switch state.  |

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
             
    
    
    

## Function Details

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this switch state is valid.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the switch state is valid, `false` otherwise.
            
    

