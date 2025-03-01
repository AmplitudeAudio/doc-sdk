---
title: Node
description: Base class for Amplimix pipeline nodes.
generator: doxide
---


# Node

**class  Node**


Base class for Amplimix pipeline nodes.

This class presents the basic structure to create Amplimix pipeline nodes. Each
`Node` of your pipelines must be derived from this class and implement the [`CreateInstance()`](#CreateInstance)
and [`DestroyInstance()`](#DestroyInstance) methods.


:material-eye-outline: **See**
:    [NodeInstance](../NodeInstance/index.md)


    


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
| [CanConsume](#CanConsume) | Returns `true` if the node can consume audio data. |
| [CanProduce](#CanProduce) | Returns `true` if the node can produce audio data. |
| [GetMaxInputCount](#GetMaxInputCount) | Returns the maximum number of input connections the node can have. |
| [GetMinInputCount](#GetMinInputCount) | Returns the minimum number of input connections the node can have. |
| [Register](#Register) | Registers a new node. |
| [Unregister](#Unregister) | Unregisters a node. |
| [Construct](#Construct) | Creates a new instance of the node with the given name * and returns its pointer. The returned pointer should be deleted using Node::Destruct(). |
| [Destruct](#Destruct) | Destroys the given node instance. |
| [LockRegistry](#LockRegistry) | Locks the nodes' registry. |
| [UnlockRegistry](#UnlockRegistry) | Unlocks the nodes' registry. |
| [GetRegistry](#GetRegistry) | Gets the list of registered nodes. |

## Variable Details

### m_name<a name="m_name"></a>

!!! variable "AmString m_name"

    
    The name of this node.
             
    
    
    

## Function Details

### CanConsume<a name="CanConsume"></a>
!!! function "[[nodiscard]] virtual bool CanConsume() const = 0"

    
    Returns `true` if the node can consume audio data.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the node can consume audio data, `false` otherwise.
            
    

### CanProduce<a name="CanProduce"></a>
!!! function "[[nodiscard]] virtual bool CanProduce() const = 0"

    
    Returns `true` if the node can produce audio data.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the node can produce audio data, `false` otherwise.
            
    

### Construct<a name="Construct"></a>
!!! function "static NodeInstance&#42; Construct(const AmString&amp; name)"

    
    Creates a new instance of the node with the given name
             * and returns its pointer. The returned pointer should be deleted using Node::Destruct().
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the node.
    
    
    :material-keyboard-return: **Return**
    :    The node with the given name, or `nullptr` if none.
            
    

### CreateInstance<a name="CreateInstance"></a>
!!! function "&#42; CreateInstance() const"

    
    Creates a new instance of the node.
    
    
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
                
    

### GetMaxInputCount<a name="GetMaxInputCount"></a>
!!! function "[[nodiscard]] virtual AmSize GetMaxInputCount() const = 0"

    
    Returns the maximum number of input connections the node can have.
    
    
    :material-keyboard-return: **Return**
    :    The maximum number of input connections the node can have.
            
    

### GetMinInputCount<a name="GetMinInputCount"></a>
!!! function "[[nodiscard]] virtual AmSize GetMinInputCount() const = 0"

    
    Returns the minimum number of input connections the node can have.
    
    
    :material-keyboard-return: **Return**
    :    The minimum number of input connections the node can have.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Returns the name of the node.
             
    
    
    

### GetRegistry<a name="GetRegistry"></a>
!!! function "static const std::map&lt;AmString, std::shared_ptr&lt;Node&gt;&gt;&amp; GetRegistry()"

    
    Gets the list of registered nodes.
    
    
    :material-keyboard-return: **Return**
    :    The registry of nodes.
            
    

### LockRegistry<a name="LockRegistry"></a>
!!! function "static void LockRegistry()"

    
    Locks the nodes' registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called before the `Engine` initialization, to discard the registration
        of new nodes after the engine is fully loaded.
                
    

### Node<a name="Node"></a>
!!! function "explicit Node(AmString name)"

    
    Node constructor.
    
    
    :material-location-enter: **Parameter** `name`
    :    Name of the node. Should be unique within the pipeline.
                
    

### Register<a name="Register"></a>
!!! function "static void Register(std::shared_ptr&lt;Node&gt; node)"

    
    Registers a new node.
    
    
    :material-location-enter: **Parameter** `node`
    :    The node to add in the registry.
                
    

### UnlockRegistry<a name="UnlockRegistry"></a>
!!! function "static void UnlockRegistry()"

    
    Unlocks the nodes' registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called after the `Engine` deinitialization, to allow the registration
        of new nodes after the engine is fully unloaded.
                
    

### Unregister<a name="Unregister"></a>
!!! function "static void Unregister(std::shared_ptr&lt;const Node&gt; node)"

    
    Unregisters a node.
    
    
    :material-location-enter: **Parameter** `node`
    :    The node to remove from the registry.
                
    

### ~Node<a name="_u007eNode"></a>
!!! function "virtual ~Node()"

    
    Node destructor.
             
    
    
    

