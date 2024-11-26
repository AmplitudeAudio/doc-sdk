---
title: InputNodeInstance
description: Class used to mark the input of the pipeline.
generator: doxide
---


# InputNodeInstance

**class  InputNodeInstance : public NodeInstance , public ProviderNodeInstance**


Class used to mark the input of the pipeline.


!!! warning
     This node is automatically added to the pipeline when created. And thus
    should not be manually added to the pipeline asset.


:material-eye-outline: **See**
:    [ProviderNodeInstance](../ProviderNodeInstance/index.md)


    


## Functions

| Name | Description |
| ---- | ----------- |
| [InputNodeInstance](#InputNodeInstance) | InputNodeInstance constructor.  |
| [~InputNodeInstance](#_u007eInputNodeInstance) | Default destructor.  |
| [SetInput](#SetInput) | Sets the input of the pipeline. |
| [Provide](#Provide) |  @inherit  |
| [Reset](#Reset) |  @inherit  |

## Function Details

### InputNodeInstance<a name="InputNodeInstance"></a>
!!! function "InputNodeInstance()"

    
    InputNodeInstance constructor.
             
    
    
    

### Provide<a name="Provide"></a>
!!! function "const AudioBuffer&#42; Provide() override"

    
    @inherit
            
    

### Reset<a name="Reset"></a>
!!! function "void Reset() override"

    
    @inherit
            
    

### SetInput<a name="SetInput"></a>
!!! function "void SetInput(AudioBuffer&#42; buffer)"

    
    Sets the input of the pipeline.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The buffer to set as the input.
                
    

### ~InputNodeInstance<a name="_u007eInputNodeInstance"></a>
!!! function "~InputNodeInstance() override = default"

    
    Default destructor.
             
    
    
    

