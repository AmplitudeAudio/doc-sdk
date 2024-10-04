---
title: ChannelEventInfo
description: The event info passed to the channel event listener.
generator: doxide
---


# ChannelEventInfo

**struct ChannelEventInfo**


The event info passed to the channel event listener.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_source](#m_source) | The event source.  |
| [m_userData](#m_userData) | Additional user data passed to the event listener.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [ChannelEventInfo](#ChannelEventInfo) | Constructor. |

## Variable Details

### m_source<a name="m_source"></a>

!!! variable "ChannelInternalState&#42; m_source"

    
    The event source.
             
    
    
    

### m_userData<a name="m_userData"></a>

!!! variable "void&#42; m_userData"

    
    Additional user data passed to the event listener.
             
    
    
    

## Function Details

### ChannelEventInfo<a name="ChannelEventInfo"></a>
!!! function "explicit ChannelEventInfo(ChannelInternalState&#42; source)"

    
    Constructor.
    
    
    :material-location-enter: **Parameter** `source`
    :    The source of the event.
    
    
    !!! warning
         This constructor is for internal usage only.
                
    

