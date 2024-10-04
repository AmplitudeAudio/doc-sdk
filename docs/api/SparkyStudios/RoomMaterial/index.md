---
title: RoomMaterial
description: Represents the material of a @c Room wall. 
generator: doxide
---


# RoomMaterial

**struct  RoomMaterial**


Represents the material of a @c Room wall.
     




## Variables

| Name | Description |
| ---- | ----------- |
| [m_type](#m_type) | The type of the material.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [RoomMaterial](#RoomMaterial) | Constructs a new @c RoomMaterial. |
| [RoomMaterial](#RoomMaterial) | Constructs a new predefined @c RoomMaterial. |

## Variable Details

### m_type<a name="m_type"></a>

!!! variable "RoomMaterialType m_type"

    
    The type of the material.
             
    
    
    

## Function Details

### RoomMaterial<a name="RoomMaterial"></a>
!!! function "RoomMaterial()"

    
    Constructs a new @c RoomMaterial.
    
    
    !!! note
         This constructor initializes a `RoomMaterialType::Custom` material.
                
    

!!! function "explicit RoomMaterial(RoomMaterialType type)"

    
    Constructs a new predefined @c RoomMaterial.
    
    
    :material-location-enter: **Parameter** `type`
    :    The type of the material.
                
    

