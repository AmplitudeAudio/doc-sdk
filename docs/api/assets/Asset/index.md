---
title: Asset
description: Amplitude Asset.
generator: doxide
---


# Asset

**template&lt;typename Id&gt; class  Asset**


Amplitude Asset.

This is the base class for all Amplitude assets. An Amplitude asset is a
`.json` file with a specific format (definition) specified by the corresponding
asset's flatbuffer schema.


:material-code-tags: **Template parameter** `Id`
:    The type of the asset id.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~Asset](#_u007eAsset) | Destroys the asset and all related resources.  |
| [GetId](#GetId) | Returns the unique ID of this asset. |
| [GetName](#GetName) | Gets the name of this asset. |

## Function Details

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] virtual Id GetId() const = 0"

    
    Returns the unique ID of this asset.
    
    
    :material-keyboard-return: **Return**
    :    The asset unique ID.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] virtual const AmString&amp; GetName() const = 0"

    
    Gets the name of this asset.
    
    
    :material-keyboard-return: **Return**
    :    The asset name.
            
    

### ~Asset<a name="_u007eAsset"></a>
!!! function "virtual ~Asset() = default"

    
    Destroys the asset and all related resources.
             
    
    
    

