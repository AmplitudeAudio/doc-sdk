---
title: RtpcValue
description: A RTPC compatible value is used as a wrapper to hold property values * that can be linked to RTPCs.
generator: doxide
---


# RtpcValue

**struct  RtpcValue**


A RTPC compatible value is used as a wrapper to hold property values
     * that can be linked to RTPCs.

A property value that can be linked to a RTPC can be either a single static value
that never updates, or a curve and an RTPC value that is updated by the game. The
curve is used here as a function that takes the current RTPC value and returns the
parameter value.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [RtpcValue](#RtpcValue) | Creates an uninitialized `RtpcValue` object. |
| [RtpcValue](#RtpcValue) | Creates a copy of the `RtpcValue` object. |
| [~RtpcValue](#_u007eRtpcValue) | Destroys the RtpcValue object.  |
| [Init](#Init) | Creates a `RtpcValue` object with a static value. |
| [Init](#Init) | Creates a `RtpcValue` object with a curve and an RTPC object. |
| [Init](#Init) | Creates a `RtpcValue` object from an asset definition. |
| [GetValue](#GetValue) | Gets the current RTPC value. For static values, this will always * return the value passed to the constructor or set from an asset definition. |
| [IsStatic](#IsStatic) | Checks if the RTPC value is static. |

## Function Details

### GetValue<a name="GetValue"></a>
!!! function "[[nodiscard]] AmReal32 GetValue() const"

    
    Gets the current RTPC value. For static values, this will always
             * return the value passed to the constructor or set from an asset definition.
    
    
    :material-keyboard-return: **Return**
    :    The current RTPC value.
            
    

### Init<a name="Init"></a>
!!! function "void Init(AmReal32 value)"

    
    Creates a `RtpcValue` object with a static value.
    
    
    :material-location-enter: **Parameter** `value`
    :    The static value to set.
                
    

!!! function "void Init(const Rtpc&#42; rtpc, Curve&#42; curve)"

    
    Creates a `RtpcValue` object with a curve and an RTPC object.
    
    
    :material-location-enter: **Parameter** `rtpc`
    :    The RTPC to link to.
        
    :material-location-enter: **Parameter** `curve`
    :    The curve to use.
                
    

!!! function "void Init(const RtpcCompatibleValue&#42; definition)"

    
    Creates a `RtpcValue` object from an asset definition.
    
    
    :material-location-enter: **Parameter** `definition`
    :    The RTPC-compatible value asset definition.
                
    

### IsStatic<a name="IsStatic"></a>
!!! function "[[nodiscard]] bool IsStatic() const"

    
    Checks if the RTPC value is static.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the RTPC value is static, `false` otherwise.
            
    

### RtpcValue<a name="RtpcValue"></a>
!!! function "RtpcValue()"

    
    Creates an uninitialized `RtpcValue` object.
    
    An uninitialized `RtpcValue` object cannot be used to update values.
            
    

!!! function "RtpcValue(const RtpcValue&amp; other)"

    
    Creates a copy of the `RtpcValue` object.
    
    
    :material-location-enter: **Parameter** `other`
    :    The `RtpcValue` object to copy.
                
    

### ~RtpcValue<a name="_u007eRtpcValue"></a>
!!! function "~RtpcValue()"

    
    Destroys the RtpcValue object.
             
    
    
    

