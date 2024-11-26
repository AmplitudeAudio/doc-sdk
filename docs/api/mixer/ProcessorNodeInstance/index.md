---
title: ProcessorNodeInstance
description: Base class for Amplimix pipeline nodes that can process audio data in-place.
generator: doxide
---


# ProcessorNodeInstance

**class  ProcessorNodeInstance : public NodeInstance , public ConsumerNodeInstance , public ProviderNodeInstance**


Base class for Amplimix pipeline nodes that can process audio data in-place.


:material-eye-outline: **See**
:    [NodeInstance](../NodeInstance/index.md), [ConsumerNodeInstance](../ConsumerNodeInstance/index.md),
[ProviderNodeInstance](../ProviderNodeInstance/index.md)


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_provider](#m_provider) | The ID of the input provider node. |

## Functions

| Name | Description |
| ---- | ----------- |
| [ProcessorNodeInstance](#ProcessorNodeInstance) | PropertyNodeInstance constructor. |
| [~ProcessorNodeInstance](#_u007eProcessorNodeInstance) | Default destructor.  |
| [Process](#Process) | Processes input audio data and returns the output audio data. |
| [Consume](#Consume) |  @inherit  |
| [Connect](#Connect) |  @inherit  |
| [Provide](#Provide) |  @inherit  |
| [Reset](#Reset) |  @inherit  |

## Variable Details

### m_provider<a name="m_provider"></a>

!!! variable "AmObjectID m_provider"

    The ID of the input provider node.
    

## Function Details

### Connect<a name="Connect"></a>
!!! function "void Connect(AmObjectID provider) final"

    
    @inherit
            
    

### Consume<a name="Consume"></a>
!!! function "void Consume() final"

    
    @inherit
            
    

### Process<a name="Process"></a>
!!! function "&#42; Process(const AudioBuffer&#42; input)"

    
    Processes input audio data and returns the output audio data.
    
    
    :material-location-enter: **Parameter** `input`
    :    The input audio data to process.
    
    
    :material-keyboard-return: **Return**
    :    The output audio data.
            
    

### ProcessorNodeInstance<a name="ProcessorNodeInstance"></a>
!!! function "explicit ProcessorNodeInstance(bool processOnEmptyBuffer = false)"

    
    PropertyNodeInstance constructor.
    
    
    :material-location-enter: **Parameter** `processOnEmptyBuffer`
    :    If `true`, the node will execute the [`Process()`](#Process) method
        even if the input buffer is `nullptr`.
                
    

### Provide<a name="Provide"></a>
!!! function "const AudioBuffer&#42; Provide() final"

    
    @inherit
            
    

### Reset<a name="Reset"></a>
!!! function "void Reset() override"

    
    @inherit
            
    

### ~ProcessorNodeInstance<a name="_u007eProcessorNodeInstance"></a>
!!! function "~ProcessorNodeInstance() override = default"

    
    Default destructor.
             
    
    
    

