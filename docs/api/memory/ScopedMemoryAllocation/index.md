---
title: ScopedMemoryAllocation
description: Allocates a block of memory with the given size in the given pool.
generator: doxide
---


# ScopedMemoryAllocation

**class  ScopedMemoryAllocation**


Allocates a block of memory with the given size in the given pool.

That allocation will be restricted to the current scope, and will be freed
automatically when the scope ends.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [ScopedMemoryAllocation](#ScopedMemoryAllocation) | Default constructor.  |
| [ScopedMemoryAllocation](#ScopedMemoryAllocation) | Creates a new scoped memory allocation. |
| [ScopedMemoryAllocation](#ScopedMemoryAllocation) | Creates a new scoped aligned memory allocation. |
| [~ScopedMemoryAllocation](#_u007eScopedMemoryAllocation) | Releases the allocated memory.  |
| [PointerOf](#PointerOf) | Gets the allocated memory address. |
| [As](#As) | Converts the allocated memory address to a different type. |
| [Address](#Address) | Gets the allocated memory address. |

## Function Details

### Address<a name="Address"></a>
!!! function "[[nodiscard]] inline AmVoidPtr Address() const"

    
    Gets the allocated memory address.
    
    
    :material-keyboard-return: **Return**
    :    The allocated memory address.
            
    

### As<a name="As"></a>
!!! function "template&lt;typename T, typename std::enable_if_t&lt;std::is_pointer_v&lt;T&gt;, bool&gt; = false&gt; [[nodiscard]] inline T As() const"

    
    Converts the allocated memory address to a different type.
    
    
    :material-keyboard-return: **Return**
    :    The allocated memory address converted to the specified type.
            
    

### PointerOf<a name="PointerOf"></a>
!!! function "template&lt;typename T&gt; [[nodiscard]] inline T&#42; PointerOf() const"

    
    Gets the allocated memory address.
    
    
    :material-keyboard-return: **Return**
    :    The allocated memory address.
            
    

### ScopedMemoryAllocation<a name="ScopedMemoryAllocation"></a>
!!! function "ScopedMemoryAllocation() = default"

    
    Default constructor.
             
    
    
    

!!! function "ScopedMemoryAllocation(eMemoryPoolKind pool, AmSize size, const char&#42; file, AmUInt32 line)"

    
    Creates a new scoped memory allocation.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to allocate from.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the block to allocate.
        
    :material-location-enter: **Parameter** `file`
    :    The file in which the allocation was made.
        
    :material-location-enter: **Parameter** `line`
    :    The line in which the allocation was made.
                
    

!!! function "ScopedMemoryAllocation(eMemoryPoolKind pool, AmSize size, AmUInt32 alignment, const char&#42; file, AmUInt32 line)"

    
    Creates a new scoped aligned memory allocation.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to allocate from.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the block to allocate.
        
    :material-location-enter: **Parameter** `alignment`
    :    The alignment of the block to allocate.
        
    :material-location-enter: **Parameter** `file`
    :    The file in which the allocation was made.
        
    :material-location-enter: **Parameter** `line`
    :    The line in which the allocation was made.
                
    

### ~ScopedMemoryAllocation<a name="_u007eScopedMemoryAllocation"></a>
!!! function "~ScopedMemoryAllocation()"

    
    Releases the allocated memory.
             
    
    
    

