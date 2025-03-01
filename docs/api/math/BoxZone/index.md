---
title: BoxZone
description: A `Zone` built with an inner `BoxShape` and an outer `BoxShape`.
generator: doxide
---


# BoxZone

**class  BoxZone : public Zone**


A `Zone` built with an inner `BoxShape` and an outer `BoxShape`.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [BoxZone](#BoxZone) | Constructs a new `BoxZone`. |
| [GetFactor](#GetFactor) |  @inherit  |

## Function Details

### BoxZone<a name="BoxZone"></a>
!!! function "BoxZone(std::shared_ptr&lt;BoxShape&gt; inner, std::shared_ptr&lt;BoxShape&gt; outer)"

    
    Constructs a new `BoxZone`.
    
    
    :material-location-enter: **Parameter** `inner`
    :    The inner `BoxShape`.
        
    :material-location-enter: **Parameter** `outer`
    :    The outer `BoxShape`.
                
    

### GetFactor<a name="GetFactor"></a>
!!! function "[[nodiscard]] AmReal32 GetFactor(const AmVec3&amp; position) final"

    
    @inherit
            
    

