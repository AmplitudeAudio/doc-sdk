---
title: NodeInstance
description: An instance of an Amplimix pipeline node.
generator: doxide
---


# NodeInstance

**class  NodeInstance**


An instance of an Amplimix pipeline node.

This class represents the actual node executed within the
Amplimix pipeline. Each node instance has a unique ID assigned
to it, that matches the one provided in the pipeline asset.
    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_id](#m_id) | The unique identifier for the node instance in the pipeline. |
| [m_layer](#m_layer) | The Amplimix layer this node instance is currently associated with. |
| [m_pipeline](#m_pipeline) | The pipeline this node instance belongs to. |

## Functions

| Name | Description |
| ---- | ----------- |
| [Initialize](#Initialize) | Initializes the node instance. |
| [~NodeInstance](#_u007eNodeInstance) | NodeInstance destructor.  |
| [GetId](#GetId) | Returns the unique identifier for the node instance.  |
| [GetLayer](#GetLayer) | Gets the Amplimix layer this node instance is currently associated with.  |
| [Reset](#Reset) | Resets the node instance's internal state. |

## Variable Details

### m_id<a name="m_id"></a>

!!! variable "AmObjectID m_id"

    The unique identifier for the node instance in the pipeline.
    

### m_layer<a name="m_layer"></a>

!!! variable "const AmplimixLayer&#42; m_layer"

    The Amplimix layer this node instance is currently associated with.
    

### m_pipeline<a name="m_pipeline"></a>

!!! variable "const PipelineInstance&#42; m_pipeline"

    The pipeline this node instance belongs to.
    

## Function Details

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmObjectID GetId() const"

    
    Returns the unique identifier for the node instance.
             
    
    
    

### GetLayer<a name="GetLayer"></a>
!!! function "[[nodiscard]] const AmplimixLayer&#42; GetLayer() const"

    
    Gets the Amplimix layer this node instance is currently associated with.
             
    
    
    

### Initialize<a name="Initialize"></a>
!!! function "virtual void Initialize(AmObjectID id, const AmplimixLayer&#42; layer, const PipelineInstance&#42; pipeline)"

    
    Initializes the node instance.
    
    
    :material-location-enter: **Parameter** `id`
    :    Unique identifier for the node instance.
        
    :material-location-enter: **Parameter** `layer`
    :    The Amplimix layer this node instance is currently associated with.
        
    :material-location-enter: **Parameter** `pipeline`
    :    The pipeline this node instance belongs to.
                
    

### Reset<a name="Reset"></a>
!!! function "virtual void Reset() = 0"

    
    Resets the node instance's internal state.
    
    This function should be called automatically by Amplimix, each time the pipeline is
    about to be executed. Call it manually only if you know what you're doing.
            
    

### ~NodeInstance<a name="_u007eNodeInstance"></a>
!!! function "virtual ~NodeInstance() = default"

    
    NodeInstance destructor.
             
    
    
    

