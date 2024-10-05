---
title: PipelineInstance
description: Represents an instance of a pipeline for a specific layer.
generator: doxide
---


# PipelineInstance

**class  PipelineInstance**


Represents an instance of a pipeline for a specific layer.

A pipeline instance is created for each single layer in the mixer. Each pipeline instance
manages its own state, and create a set of node instances following the provided configuration.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~PipelineInstance](#_u007ePipelineInstance) | Default constructor.  |
| [Execute](#Execute) | Executes the pipeline for the given layer. |
| [Reset](#Reset) | Resets the internal state for all nodes in the pipeline. |
| [GetNode](#GetNode) | Gets the node with the specified ID. |

## Function Details

### Execute<a name="Execute"></a>
!!! function "virtual void Execute(const AudioBuffer&amp; in, AudioBuffer&amp; out) = 0"

    
    Executes the pipeline for the given layer.
    
    
    :material-location-enter: **Parameter** `in`
    :    The input buffer to process. This buffer is passed to the input
        node of the pipeline.
        
    :material-location-exit: **Parameter** `out`
    :    The output buffer where the output node will fill processed data.
                
    

### GetNode<a name="GetNode"></a>
!!! function "&#42; GetNode(AmObjectID id) const"

    
    Gets the node with the specified ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the node to retrieve.
    
    
    :material-keyboard-return: **Return**
    :    The node with the specified ID, or `nullptr` if not found.
            
    

### Reset<a name="Reset"></a>
!!! function "virtual void Reset() = 0"

    
    Resets the internal state for all nodes in the pipeline.
    
    
    !!! warning
         This method is called automatically when Amplimix has finished processing a frame
        for a specific layer. You should not manually call this method, unless you know what
        you're doing.
                
    

### ~PipelineInstance<a name="_u007ePipelineInstance"></a>
!!! function "virtual ~PipelineInstance() = default"

    
    Default constructor.
             
    
    
    

