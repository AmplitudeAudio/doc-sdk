---
title: MixerNodeInstance
description: Base class for Amplimix pipeline nodes that can mix audio data from multiple input buffers.
generator: doxide
---


# MixerNodeInstance

**class  MixerNodeInstance : public NodeInstance , public ConsumerNodeInstance , public ProviderNodeInstance**


Base class for Amplimix pipeline nodes that can mix audio data from multiple input buffers.


:material-eye-outline: **See**
:    [NodeInstance](../NodeInstance/index.md), [ConsumerNodeInstance](../ConsumerNodeInstance/index.md),
[ProviderNodeInstance](../ProviderNodeInstance/index.md)


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_providers](#m_providers) | The IDs of the input provider nodes. |

## Functions

| Name | Description |
| ---- | ----------- |
| [MixerNodeInstance](#MixerNodeInstance) | MixerNodeInstance constructor.  |
| [~MixerNodeInstance](#_u007eMixerNodeInstance) | Default destructor.  |
| [Consume](#Consume) |  @inherit  |
| [Connect](#Connect) |  @inherit ! |
| [Connect](#Connect) | Sets the input provider nodes for this mixer node. |
| [Provide](#Provide) |  @inherit  |
| [Reset](#Reset) |  @inherit  |

## Variable Details

### m_providers<a name="m_providers"></a>

!!! variable "std::vector&lt;AmObjectID&gt; m_providers"

    The IDs of the input provider nodes.
    

## Function Details

### Connect<a name="Connect"></a>
!!! function "void Connect(AmObjectID provider) final"

    
    @inherit
    
    
    !!! note
         This method appends the given provider to the list of input
        provider nodes. If the provider node already exists in the list, it
        will not be added again.
                
    

!!! function "void Connect(const std::vector&lt;AmObjectID&gt;&amp; providers)"

    
    Sets the input provider nodes for this mixer node.
    
    
    :material-location-enter: **Parameter** `providers`
    :    The provider nodes for this mixer node.
    
    
    !!! note
         This method clears the existing input provider nodes,
        and replaces them with the provided ones.
                
    

### Consume<a name="Consume"></a>
!!! function "void Consume() final"

    
    @inherit
            
    

### MixerNodeInstance<a name="MixerNodeInstance"></a>
!!! function "MixerNodeInstance()"

    
    MixerNodeInstance constructor.
             
    
    
    

### Provide<a name="Provide"></a>
!!! function "const AudioBuffer&#42; Provide() final"

    
    @inherit
            
    

### Reset<a name="Reset"></a>
!!! function "void Reset() override"

    
    @inherit
            
    

### ~MixerNodeInstance<a name="_u007eMixerNodeInstance"></a>
!!! function "~MixerNodeInstance() override = default"

    
    Default destructor.
             
    
    
    

