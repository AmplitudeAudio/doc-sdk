---
title: Node
description: Base class for Amplimix pipeline nodes.
generator: doxide
---


# Node

**class  Node**


Base class for Amplimix pipeline nodes.

This class presents the basic structure to create Amplimix
pipeline nodes. Each `Node` must be derived from this class
and implement the `Node::CreateInstance()` and
`Node::DestroyInstance()` methods.
    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_name](#m_name) | The name of this node.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Node](#Node) | Node constructor. |
| [~Node](#_u007eNode) | Node destructor.  |
| [CreateInstance](#CreateInstance) | Creates a new instance of the node. |
| [DestroyInstance](#DestroyInstance) | Destroys the specified instance of the node. |
| [GetName](#GetName) | Returns the name of the node.  |
| [Register](#Register) | Registers a new node. |
| [Unregister](#Unregister) | Unregisters a node. |
| [Construct](#Construct) | Creates a new instance of the the node with the given name * and returns its pointer. The returned pointer should be deleted using Node::Destruct(). |
| [Destruct](#Destruct) | Destroys the given node instance. |
| [LockRegistry](#LockRegistry) | Locks the nodes registry. |
| [UnlockRegistry](#UnlockRegistry) | Unlocks the nodes registry. |
| [Find](#Find) | Look up a node by name. |

## Variable Details

### m_name<a name="m_name"></a>

!!! variable "AmString m_name"

    
    The name of this node.
             
    
    
    

## Function Details

### Construct<a name="Construct"></a>
!!! function "static NodeInstance&#42; Construct(const AmString&amp; name)"

    
    Creates a new instance of the the node with the given name
             * and returns its pointer. The returned pointer should be deleted using Node::Destruct().
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the node.
    
    
    :material-keyboard-return: **Return**
    :    The node with the given name, or NULL if none.
            
    

### CreateInstance<a name="CreateInstance"></a>
!!! function "&#42; CreateInstance() const"

    
    Creates a new instance of the node.
    
    
    :material-location-enter: **Parameter** `id`
    :    Unique identifier for the new instance.
        
    :material-location-enter: **Parameter** `layer`
    :    The Amplimix layer associated with the new instance.
        
    :material-location-enter: **Parameter** `pipeline`
    :    The pipeline associated with the new instance.
    
    
    :material-keyboard-return: **Return**
    :    A new instance of the node.
            
    

### DestroyInstance<a name="DestroyInstance"></a>
!!! function "virtual void DestroyInstance(NodeInstance&#42; instance) const = 0"

    
    Destroys the specified instance of the node.
    
    
    :material-location-enter: **Parameter** `instance`
    :    Pointer to the instance to be destroyed.
                
    

### Destruct<a name="Destruct"></a>
!!! function "static void Destruct(const AmString&amp; name, NodeInstance&#42; instance)"

    
    Destroys the given node instance.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the node.
        
    :material-location-enter: **Parameter** `instance`
    :    The node instance to destroy.
                
    

### Find<a name="Find"></a>
!!! function "static Node&#42; Find(const AmString&amp; name)"

    
    Look up a node by name.
    
    
    :material-keyboard-return: **Return**
    :    The node with the given name, or NULL if none.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Returns the name of the node.
             
    
    
    

### LockRegistry<a name="LockRegistry"></a>
!!! function "static void LockRegistry()"

    
    Locks the nodes registry.
    
    This function is mainly used for internal purposes. Its
    called before the Engine initialization, to discard the
    registration of new nodes after the engine is fully loaded.
            
    

### Node<a name="Node"></a>
!!! function "Node(AmString name)"

    
    Node constructor.
    
    
    :material-location-enter: **Parameter** `name`
    :    Name of the node. Should be unique within the pipeline.
                
    

### Register<a name="Register"></a>
!!! function "static void Register(Node&#42; node)"

    
    Registers a new node.
    
    
    :material-location-enter: **Parameter** `node`
    :    The node to add in the registry.
                
    

### UnlockRegistry<a name="UnlockRegistry"></a>
!!! function "static void UnlockRegistry()"

    
    Unlocks the nodes registry.
    
    This function is mainly used for internal purposes. Its
    called after the Engine deinitialization, to allow the
    registration of new divers after the engine is fully unloaded.
            
    

### Unregister<a name="Unregister"></a>
!!! function "static void Unregister(const Node&#42; node)"

    
    Unregisters a node.
    
    
    :material-location-enter: **Parameter** `node`
    :    The node to remove from the registry.
                
    

### ~Node<a name="_u007eNode"></a>
!!! function "virtual ~Node()"

    
    Node destructor.
             
    
    
    

