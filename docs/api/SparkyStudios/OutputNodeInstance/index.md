---
title: OutputNodeInstance
description: Class used to marks the output of the pipeline.
generator: doxide
---


# OutputNodeInstance

**class  OutputNodeInstance final : public NodeInstance , public ConsumerNodeInstance**


Class used to marks the output of the pipeline.

This node is automatically added to the pipeline when created. And thus
should not be manually added to the pipeline asset.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [OutputNodeInstance](#OutputNodeInstance) | OutputNodeInstance constructor.  |
| [~OutputNodeInstance](#_u007eOutputNodeInstance) | OutputNodeInstance destructor.  |
| [SetOutput](#SetOutput) | Set the output of the pipeline. |
| [Consume](#Consume) |  @copydoc ConsumerNodeInstance::Consume()  |
| [Connect](#Connect) |  @copydoc ConsumerNodeInstance::Connect()  |
| [Reset](#Reset) |  @copydoc NodeInstance::Reset()  |

## Function Details

### Connect<a name="Connect"></a>
!!! function "void Connect(AmObjectID provider) override"

    
    @copydoc ConsumerNodeInstance::Connect()
            
    

### Consume<a name="Consume"></a>
!!! function "void Consume() override"

    
    @copydoc ConsumerNodeInstance::Consume()
            
    

### OutputNodeInstance<a name="OutputNodeInstance"></a>
!!! function "OutputNodeInstance()"

    
    OutputNodeInstance constructor.
             
    
    
    

### Reset<a name="Reset"></a>
!!! function "void Reset() override"

    
    @copydoc NodeInstance::Reset()
            
    

### SetOutput<a name="SetOutput"></a>
!!! function "void SetOutput(AudioBuffer&#42; buffer)"

    
    Set the output of the pipeline.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The buffer to set as the output.
                
    

### ~OutputNodeInstance<a name="_u007eOutputNodeInstance"></a>
!!! function "~OutputNodeInstance() override = default"

    
    OutputNodeInstance destructor.
             
    
    
    

