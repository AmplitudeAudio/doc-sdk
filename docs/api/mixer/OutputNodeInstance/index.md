---
title: OutputNodeInstance
description: Class used to mark the output of the pipeline.
generator: doxide
---


# OutputNodeInstance

**class  OutputNodeInstance final : public NodeInstance , public ConsumerNodeInstance**


Class used to mark the output of the pipeline.


!!! warning
     This node is automatically added to the pipeline when created. And thus
    should not be manually added to the pipeline asset.


:material-eye-outline: **See**
:    [ConsumerNodeInstance](../ConsumerNodeInstance/index.md)


    


## Functions

| Name | Description |
| ---- | ----------- |
| [OutputNodeInstance](#OutputNodeInstance) | OutputNodeInstance constructor.  |
| [~OutputNodeInstance](#_u007eOutputNodeInstance) | Default destructor.  |
| [SetOutput](#SetOutput) | Sets the output of the pipeline. |
| [Consume](#Consume) |  @inherit  |
| [Connect](#Connect) |  @inherit  |
| [Reset](#Reset) |  @inherit  |

## Function Details

### Connect<a name="Connect"></a>
!!! function "void Connect(AmObjectID provider) override"

    
    @inherit
            
    

### Consume<a name="Consume"></a>
!!! function "void Consume() override"

    
    @inherit
            
    

### OutputNodeInstance<a name="OutputNodeInstance"></a>
!!! function "OutputNodeInstance()"

    
    OutputNodeInstance constructor.
             
    
    
    

### Reset<a name="Reset"></a>
!!! function "void Reset() override"

    
    @inherit
            
    

### SetOutput<a name="SetOutput"></a>
!!! function "void SetOutput(AudioBuffer&#42; buffer)"

    
    Sets the output of the pipeline.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The buffer to set as the output.
                
    

### ~OutputNodeInstance<a name="_u007eOutputNodeInstance"></a>
!!! function "~OutputNodeInstance() override = default"

    
    Default destructor.
             
    
    
    

