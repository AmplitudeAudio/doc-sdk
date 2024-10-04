---
title: ProcessorNodeInstance
description: Base class for Amplimix pipeline nodes that can process * audio data in-place. 
generator: doxide
---


# ProcessorNodeInstance

**class  ProcessorNodeInstance : public NodeInstance , public ConsumerNodeInstance , public ProviderNodeInstance**


Base class for Amplimix pipeline nodes that can process
     * audio data in-place.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [ProcessorNodeInstance](#ProcessorNodeInstance) | PropertyNodeInstance constructor. |
| [~ProcessorNodeInstance](#_u007eProcessorNodeInstance) | ProcessorNodeInstance destructor.  |
| [Process](#Process) | Process input audio data and returns the output audio data. |
| [Consume](#Consume) |  @copydoc ConsumerNodeInstance::Consume()  |
| [Connect](#Connect) |  @copydoc ConsumerNodeInstance::Connect()  |
| [Provide](#Provide) |  @copydoc ProviderNodeInstance::Provide()  |
| [Reset](#Reset) |  @copydoc NodeInstance::Reset()  |

## Function Details

### Connect<a name="Connect"></a>
!!! function "void Connect(AmObjectID provider) final"

    
    @copydoc ConsumerNodeInstance::Connect()
            
    

### Consume<a name="Consume"></a>
!!! function "void Consume() final"

    
    @copydoc ConsumerNodeInstance::Consume()
            
    

### Process<a name="Process"></a>
!!! function "&#42; Process(const AudioBuffer&#42; input)"

    
    Process input audio data and returns the output audio data.
    
    
    :material-location-enter: **Parameter** `input`
    :    The input audio data to process.
    
    
    :material-keyboard-return: **Return**
    :    The output audio data.
            
    

### ProcessorNodeInstance<a name="ProcessorNodeInstance"></a>
!!! function "ProcessorNodeInstance(bool processOnEmptyBuffer = false)"

    
    PropertyNodeInstance constructor.
    
    
    :material-location-enter: **Parameter** `processOnEmptyBuffer`
    :    If true, the node will execute the Process() method
        even if the input buffer is `nullptr.`
                
    

### Provide<a name="Provide"></a>
!!! function "const AudioBuffer&#42; Provide() final"

    
    @copydoc ProviderNodeInstance::Provide()
            
    

### Reset<a name="Reset"></a>
!!! function "void Reset() override"

    
    @copydoc NodeInstance::Reset()
            
    

### ~ProcessorNodeInstance<a name="_u007eProcessorNodeInstance"></a>
!!! function "~ProcessorNodeInstance() override = default"

    
    ProcessorNodeInstance destructor.
             
    
    
    

