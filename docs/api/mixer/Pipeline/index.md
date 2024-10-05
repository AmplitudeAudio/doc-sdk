---
title: Pipeline
description: A pipeline assembles a set of nodes to process audio data.
generator: doxide
---


# Pipeline

**class  Pipeline : public Asset&lt;AmPipelineID&gt;**


A pipeline assembles a set of nodes to process audio data.

For each layer in `Amplimix`, a `PipelineInstance` is created for that specific layer.


:material-eye-outline: **See**
:    [Amplimix](../Amplimix/index.md), [PipelineInstance](../PipelineInstance/index.md)


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~Pipeline](#_u007ePipeline) | Default destructor.  |
| [CreateInstance](#CreateInstance) | Creates a new pipeline instance for the specified layer. |
| [DestroyInstance](#DestroyInstance) | Destroys the specified pipeline instance. |

## Function Details

### CreateInstance<a name="CreateInstance"></a>
!!! function "&#42; CreateInstance(const AmplimixLayer&#42; layer) const"

    
    Creates a new pipeline instance for the specified layer.
    
    
    :material-location-enter: **Parameter** `layer`
    :    The layer for which to create the pipeline instance.
    
    
    :material-keyboard-return: **Return**
    :    A new pipeline instance for the specified layer.
            
    

### DestroyInstance<a name="DestroyInstance"></a>
!!! function "virtual void DestroyInstance(PipelineInstance&#42; instance) const = 0"

    
    Destroys the specified pipeline instance.
    
    
    :material-location-enter: **Parameter** `instance`
    :    The pipeline instance to destroy.
                
    

### ~Pipeline<a name="_u007ePipeline"></a>
!!! function "virtual ~Pipeline() = default"

    
    Default destructor.
             
    
    
    

