---
title: ProviderNodeInstance
description: Interface for Amplimix pipeline nodes that can provide audio data to an output buffer.
generator: doxide
---


# ProviderNodeInstance

**class  ProviderNodeInstance**


Interface for Amplimix pipeline nodes that can provide audio data to an output buffer.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~ProviderNodeInstance](#_u007eProviderNodeInstance) | Default destructor.  |
| [Provide](#Provide) | Produces audio data ready to be taken as input from a consumer node. |

## Function Details

### Provide<a name="Provide"></a>
!!! function "&#42; Provide()"

    
    Produces audio data ready to be taken as input from a consumer node.
    
    
    :material-keyboard-return: **Return**
    :    The output audio data.
    
    
    :material-eye-outline: **See**
    :    [AudioBuffer](../../core/AudioBuffer/index.md)
            
    

### ~ProviderNodeInstance<a name="_u007eProviderNodeInstance"></a>
!!! function "virtual ~ProviderNodeInstance() = default"

    
    Default destructor.
             
    
    
    

