---
title: InputNodeInstance
description: Class used to marks the input of the pipeline.
generator: doxide
---


# InputNodeInstance

**class  InputNodeInstance final : public NodeInstance , public ProviderNodeInstance**


Class used to marks the input of the pipeline.

This node is automatically added to the pipeline when created. And thus
should not be manually added to the pipeline asset.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [InputNodeInstance](#InputNodeInstance) | InputNodeInstance constructor.  |
| [~InputNodeInstance](#_u007eInputNodeInstance) | InputNodeInstance destructor.  |
| [SetInput](#SetInput) | Set the input of the pipeline. |
| [Provide](#Provide) |  @copydoc ProviderNodeInstance::Provide()  |
| [Reset](#Reset) |  @copydoc NodeInstance::Reset()  |

## Function Details

### InputNodeInstance<a name="InputNodeInstance"></a>
!!! function "InputNodeInstance()"

    
    InputNodeInstance constructor.
             
    
    
    

### Provide<a name="Provide"></a>
!!! function "const AudioBuffer&#42; Provide() override"

    
    @copydoc ProviderNodeInstance::Provide()
            
    

### Reset<a name="Reset"></a>
!!! function "void Reset() override"

    
    @copydoc NodeInstance::Reset()
            
    

### SetInput<a name="SetInput"></a>
!!! function "void SetInput(AudioBuffer&#42; buffer)"

    
    Set the input of the pipeline.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The buffer to set as the input.
                
    

### ~InputNodeInstance<a name="_u007eInputNodeInstance"></a>
!!! function "~InputNodeInstance() override = default"

    
    InputNodeInstance destructor.
             
    
    
    

