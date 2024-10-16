---
title: RoomMaterial
description: Represents the material of a `Room` wall.
generator: doxide
---


# RoomMaterial

**struct  RoomMaterial**


Represents the material of a `Room` wall.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_type](#m_type) | The type of the material.  |

## Operators

| Name | Description |
| ---- | ----------- |
| [operator==](#operator_u003d_u003d) | The absorption coefficients of the material. Checks if two `RoomMaterial` objects are equal. |
| [operator!=](#operator_u0021_u003d) | Checks if two `RoomMaterial` objects are not equal. |

## Functions

| Name | Description |
| ---- | ----------- |
| [RoomMaterial](#RoomMaterial) | Constructs a new `RoomMaterial`. |
| [RoomMaterial](#RoomMaterial) | Constructs a new predefined `RoomMaterial`. |

## Variable Details

### m_type<a name="m_type"></a>

!!! variable "RoomMaterialType m_type"

    
    The type of the material.
             
    
    
    

## Operator Details

### operator!=<a name="operator_u0021_u003d"></a>

!!! function "bool operator!=(const RoomMaterial&amp; other) const"

    
    Checks if two `RoomMaterial` objects are not equal.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other `RoomMaterial` to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the materials are not equal, `false` otherwise.
            
    

### operator==<a name="operator_u003d_u003d"></a>

!!! function "bool operator==(const RoomMaterial&amp; other) const"

    
    The absorption coefficients of the material.
             
    
    
    
    Checks if two `RoomMaterial` objects are equal.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other `RoomMaterial` to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the materials are equal, `false` otherwise.
            
    

## Function Details

### RoomMaterial<a name="RoomMaterial"></a>
!!! function "RoomMaterial()"

    
    Constructs a new `RoomMaterial`.
    
    
    !!! note
         This constructor initializes a `RoomMaterialType::Custom` material.
                
    

!!! function "explicit RoomMaterial(RoomMaterialType type)"

    
    Constructs a new predefined `RoomMaterial`.
    
    
    :material-location-enter: **Parameter** `type`
    :    The type of the material.
                
    

