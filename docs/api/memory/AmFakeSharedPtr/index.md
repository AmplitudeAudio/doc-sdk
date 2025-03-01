---
title: AmFakeSharedPtr
description: Fake shared pointer.
generator: doxide
---


# AmFakeSharedPtr

**template&lt;typename T&gt; struct AmFakeSharedPtr : public std::shared_ptr&lt;T&gt;**


Fake shared pointer.

This is a fake shared pointer that does nothing on deletion. It is used to
make use of `AmSharedPtr` in places where a shared pointer is required, but
the object is not owned by the shared pointer.


:material-code-tags: **Template parameter** `T`
:    The type of the object being wrapped.


:material-eye-outline: **See**
:    AmSharedPtr


    


## Functions

| Name | Description |
| ---- | ----------- |
| [AmFakeSharedPtr](#AmFakeSharedPtr) | Creates a new fake shared pointer. |

## Function Details

### AmFakeSharedPtr<a name="AmFakeSharedPtr"></a>
!!! function "AmFakeSharedPtr(T&#42; ptr)"

    
    Creates a new fake shared pointer.
    
    
    :material-location-enter: **Parameter** `ptr`
    :    The pointer to wrap.
                
    

