---
title: ConsumerNodeInstance
description: Interface for Amplimix pipeline nodes that can consume audio data from an input buffer.
generator: doxide
---


# ConsumerNodeInstance

**class  ConsumerNodeInstance**


Interface for Amplimix pipeline nodes that can consume audio data from an input buffer.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Consume](#Consume) | Consumes audio data from the provider node. |
| [Connect](#Connect) | Sets the input provider node ID for this node. |

## Function Details

### Connect<a name="Connect"></a>
!!! function "virtual void Connect(AmObjectID provider) = 0"

    
    Sets the input provider node ID for this node.
    
    
    :material-location-enter: **Parameter** `provider`
    :    The provider node for this node.
                
    

### Consume<a name="Consume"></a>
!!! function "virtual void Consume() = 0"

    
    Consumes audio data from the provider node.
    
    The provider node should be  specified with the call of [`Connect()`.](#Connect)
            
    

