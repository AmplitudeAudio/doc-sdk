---
title: Resource
description: An Amplitude resource in a `FileSystem`.
generator: doxide
---


# Resource

**class  Resource**


An Amplitude resource in a `FileSystem`.

This base class represents a resource (sound files, assets, etc.) in a `FileSystem`.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~Resource](#_u007eResource) | Default destructor.  |
| [GetPath](#GetPath) | Gets the path to the resource.  |
| [Load](#Load) | Loads the resource from the given FileSystem.  |

## Function Details

### GetPath<a name="GetPath"></a>
!!! function "[[nodiscard]] virtual const AmOsString&amp; GetPath() const = 0"

    
    Gets the path to the resource.
             
    
    
    

### Load<a name="Load"></a>
!!! function "virtual void Load(std::shared_ptr&lt;const FileSystem&gt; loader) = 0"

    
    Loads the resource from the given FileSystem.
             
    
    
    

### ~Resource<a name="_u007eResource"></a>
!!! function "virtual ~Resource() = default"

    
    Default destructor.
             
    
    
    

