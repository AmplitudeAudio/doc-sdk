---
title: CapsuleZone
description: A `Zone` built with an inner `CapsuleShape` and an outer `CapsuleShape`.
generator: doxide
---


# CapsuleZone

**class  CapsuleZone : public Zone**


A `Zone` built with an inner `CapsuleShape` and an outer `CapsuleShape`.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [CapsuleZone](#CapsuleZone) | Constructs a new `CapsuleZone`. |
| [GetFactor](#GetFactor) |  @inherit  |

## Function Details

### CapsuleZone<a name="CapsuleZone"></a>
!!! function "CapsuleZone(std::shared_ptr&lt;CapsuleShape&gt; inner, std::shared_ptr&lt;CapsuleShape&gt; outer)"

    
    Constructs a new `CapsuleZone`.
    
    
    :material-location-enter: **Parameter** `inner`
    :    The inner `CapsuleShape`.
        
    :material-location-enter: **Parameter** `outer`
    :    The outer `CapsuleShape`.
                
    

### GetFactor<a name="GetFactor"></a>
!!! function "[[nodiscard]] AmReal32 GetFactor(const AmVec3&amp; position) final"

    
    @inherit
            
    

