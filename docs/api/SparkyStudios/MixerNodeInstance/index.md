---
title: MixerNodeInstance
description: Base class for Amplimix pipeline nodes that can mix * audio data from multiple input buffers, and outputs the result * of the mix. 
generator: doxide
---


# MixerNodeInstance

**class  MixerNodeInstance : public NodeInstance , public ConsumerNodeInstance , public ProviderNodeInstance**


Base class for Amplimix pipeline nodes that can mix
     * audio data from multiple input buffers, and outputs the result
     * of the mix.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [MixerNodeInstance](#MixerNodeInstance) | MixerNodeInstance constructor.  |
| [~MixerNodeInstance](#_u007eMixerNodeInstance) | MixerNodeInstance destructor.  |
| [Consume](#Consume) |  @copydoc ConsumerNodeInstance::Consume()  |
| [Connect](#Connect) |  @copydoc ConsumerNodeInstance::Connect() !!! note This method appends the given provider to the list of input provider nodes. If the provider node already exists in the list, it will not be added again.  |
| [Connect](#Connect) | Set the input provider nodes for this mixer node. |
| [Provide](#Provide) |  @copydoc ProviderNodeInstance::Provide()  |
| [Reset](#Reset) |  @copydoc NodeInstance::Reset()  |

## Function Details

### Connect<a name="Connect"></a>
!!! function "void Connect(AmObjectID provider) final"

    
    @copydoc ConsumerNodeInstance::Connect()
    
    
    !!! note
         This method appends the given provider to the list of input
        provider nodes. If the provider node already exists in the list, it
        will not be added again.
                
    

!!! function "void Connect(const std::vector&lt;AmObjectID&gt;&amp; providers)"

    
    Set the input provider nodes for this mixer node.
    
    
    :material-location-enter: **Parameter** `providers`
    :    The provider nodes for this mixer node.
    
    
    !!! note
         This method clears the existing input provider nodes,
        and replaces them with the provided ones.
                
    

### Consume<a name="Consume"></a>
!!! function "void Consume() final"

    
    @copydoc ConsumerNodeInstance::Consume()
            
    

### MixerNodeInstance<a name="MixerNodeInstance"></a>
!!! function "MixerNodeInstance()"

    
    MixerNodeInstance constructor.
             
    
    
    

### Provide<a name="Provide"></a>
!!! function "const AudioBuffer&#42; Provide() final"

    
    @copydoc ProviderNodeInstance::Provide()
            
    

### Reset<a name="Reset"></a>
!!! function "void Reset() override"

    
    @copydoc NodeInstance::Reset()
            
    

### ~MixerNodeInstance<a name="_u007eMixerNodeInstance"></a>
!!! function "~MixerNodeInstance() override = default"

    
    MixerNodeInstance destructor.
             
    
    
    

