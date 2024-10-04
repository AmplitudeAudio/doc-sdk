---
title: Resource
description: An Amplitude resource in a FileSystem.
generator: doxide
---


# Resource

**class  Resource**


An Amplitude resource in a FileSystem.

This base class represents a resource (sound files, assets, etc.) in a FileSystem.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [GetPath](#GetPath) | Gets the path to the resource.  |
| [Load](#Load) | Loads the resource from the given FileSystem.  |

## Function Details

### GetPath<a name="GetPath"></a>
!!! function "[[nodiscard]] virtual const AmOsString&amp; GetPath() const = 0"

    
    Gets the path to the resource.
             
    
    
    

### Load<a name="Load"></a>
!!! function "virtual void Load(const FileSystem&#42; loader) = 0"

    
    Loads the resource from the given FileSystem.
             
    
    
    

