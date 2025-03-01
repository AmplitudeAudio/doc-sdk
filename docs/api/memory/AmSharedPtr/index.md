---
title: AmSharedPtr
description: Shared pointer type.
generator: doxide
---


# AmSharedPtr

**template&lt;class T, eMemoryPoolKind Pool = eMemoryPoolKind_Default&gt; class AmSharedPtr : public std::shared_ptr&lt;T&gt;**


Shared pointer type.


:material-code-tags: **Template parameter** `T`
:    The type of the pointer to allocate.
    
:material-code-tags: **Template parameter** `Pool`
:    The memory pool to allocate the pointer from.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Make](#Make) | Construct a shared pointer from the given parameters. |
| [AmSharedPtr](#AmSharedPtr) | Creates a new shared pointer. |

## Function Details

### AmSharedPtr<a name="AmSharedPtr"></a>
!!! function "AmSharedPtr(T&#42; ptr)"

    
    Creates a new shared pointer.
    
    
    :material-location-enter: **Parameter** `ptr`
    :    The pointer to wrap.
                
    

### Make<a name="Make"></a>
!!! function "template&lt;class... Args&gt; static AmSharedPtr&lt;T, Pool&gt; Make(Args&amp;&amp;... args)"

    
    Construct a shared pointer from the given parameters.
    
    
    :material-location-enter: **Parameter** `args`
    :    The parameters to pass to the constructor.
    
    
    :material-keyboard-return: **Return**
    :    The created shared pointer.
            
    

