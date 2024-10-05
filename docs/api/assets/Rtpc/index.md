---
title: Rtpc
description: Amplitude Real-Time Parameter Control Asset.
generator: doxide
---


# Rtpc

**class  Rtpc : public Asset&lt;AmRtpcID&gt;**


Amplitude Real-Time Parameter Control Asset.

A RTPC is a value that is updated by the game. Any update to the RTPC is
listened by the engine to propagate the changes to other parameters linked to it.

A Rtpc object is shared between any objects and values linked to it.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Update](#Update) | Updates the value of the RTPC. |
| [GetMinValue](#GetMinValue) | Gets the minimum value of this RTPC. |
| [GetMaxValue](#GetMaxValue) | Gets the maximum value of this RTPC. |
| [GetValue](#GetValue) | Gets the current value of this RTPC. |
| [SetValue](#SetValue) | Sets the current value of this RTPC. |
| [GetDefaultValue](#GetDefaultValue) | Gets the default value of this RTPC. |
| [Reset](#Reset) | Resets the current RTPC value to the default value.  |

## Function Details

### GetDefaultValue<a name="GetDefaultValue"></a>
!!! function "[[nodiscard]] virtual AmReal64 GetDefaultValue() const = 0"

    
    Gets the default value of this RTPC.
    
    
    :material-keyboard-return: **Return**
    :    The default RTPC value.
            
    

### GetMaxValue<a name="GetMaxValue"></a>
!!! function "[[nodiscard]] virtual AmReal64 GetMaxValue() const = 0"

    
    Gets the maximum value of this RTPC.
    
    
    :material-keyboard-return: **Return**
    :    The RTPC maximum value.
            
    

### GetMinValue<a name="GetMinValue"></a>
!!! function "[[nodiscard]] virtual AmReal64 GetMinValue() const = 0"

    
    Gets the minimum value of this RTPC.
    
    
    :material-keyboard-return: **Return**
    :    The RTPC minimum value.
            
    

### GetValue<a name="GetValue"></a>
!!! function "[[nodiscard]] virtual AmReal64 GetValue() const = 0"

    
    Gets the current value of this RTPC.
    
    
    :material-keyboard-return: **Return**
    :    The current RTPC value.
            
    

### Reset<a name="Reset"></a>
!!! function "virtual void Reset() = 0"

    
    Resets the current RTPC value to the default value.
             
    
    
    

### SetValue<a name="SetValue"></a>
!!! function "virtual void SetValue(AmReal64 value) = 0"

    
    Sets the current value of this RTPC.
    
    
    :material-location-enter: **Parameter** `value`
    :    The value to set.
                
    

### Update<a name="Update"></a>
!!! function "virtual void Update(AmTime deltaTime) = 0"

    
    Updates the value of the RTPC.
    
    This method is useful only for RTPCs that are using a curve to update their value.
    
    
    :material-location-enter: **Parameter** `deltaTime`
    :    The time elapsed since the last update.
                
    

