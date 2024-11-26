---
title: MemoryAllocator
description: Memory Allocator Interface.
generator: doxide
---


# MemoryAllocator

**class  MemoryAllocator**


Memory Allocator Interface.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~MemoryAllocator](#_u007eMemoryAllocator) | Default Destructor.  |
| [Malloc](#Malloc) | Allocates a block of memory. |
| [Realloc](#Realloc) | Reallocates a block of memory. |
| [Malign](#Malign) | Allocates an aligned block of memory. |
| [Realign](#Realign) | Reallocates an aligned block of memory. |
| [Free](#Free) | Deallocates a block of memory. |
| [SizeOf](#SizeOf) | Gets the size of the memory at the given address. |

## Function Details

### Free<a name="Free"></a>
!!! function "virtual void Free(eMemoryPoolKind pool, AmVoidPtr address) = 0"

    
    Deallocates a block of memory.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to deallocate from.
        
    :material-location-enter: **Parameter** `address`
    :    The pointer to the memory to deallocate.
                
    

### Malign<a name="Malign"></a>
!!! function "virtual AmVoidPtr Malign(eMemoryPoolKind pool, AmSize size, AmUInt32 alignment) = 0"

    
    Allocates an aligned block of memory.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to allocate from.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the memory to allocate.
        
    :material-location-enter: **Parameter** `alignment`
    :    The alignment of the memory to allocate.
    
    
    :material-keyboard-return: **Return**
    :    A pointer to the allocated memory.
            
    

### Malloc<a name="Malloc"></a>
!!! function "virtual AmVoidPtr Malloc(eMemoryPoolKind pool, AmSize size) = 0"

    
    Allocates a block of memory.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to allocate from.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the memory to allocate.
    
    
    :material-keyboard-return: **Return**
    :    A pointer to the allocated memory.
            
    

### Realign<a name="Realign"></a>
!!! function "virtual AmVoidPtr Realign(eMemoryPoolKind pool, AmVoidPtr address, AmSize size, AmUInt32 alignment) = 0"

    
    Reallocates an aligned block of memory.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to reallocate from.
        
    :material-location-enter: **Parameter** `address`
    :    The pointer to the memory to reallocate.
        
    :material-location-enter: **Parameter** `size`
    :    The new size of the memory.
        
    :material-location-enter: **Parameter** `alignment`
    :    The alignment of the memory to reallocate.
    
    
    :material-keyboard-return: **Return**
    :    A pointer to the reallocated memory.
            
    

### Realloc<a name="Realloc"></a>
!!! function "virtual AmVoidPtr Realloc(eMemoryPoolKind pool, AmVoidPtr address, AmSize size) = 0"

    
    Reallocates a block of memory.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to reallocate from.
        
    :material-location-enter: **Parameter** `address`
    :    The pointer to the memory to reallocate.
        
    :material-location-enter: **Parameter** `size`
    :    The new size of the memory.
    
    
    :material-keyboard-return: **Return**
    :    A pointer to the reallocated memory.
            
    

### SizeOf<a name="SizeOf"></a>
!!! function "virtual AmSize SizeOf(eMemoryPoolKind pool, AmVoidPtr address) = 0"

    
    Gets the size of the memory at the given address.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to get the size from.
        
    :material-location-enter: **Parameter** `address`
    :    The address of the memory.
    
    
    :material-keyboard-return: **Return**
    :    The size of the memory at the given address.
            
    

### ~MemoryAllocator<a name="_u007eMemoryAllocator"></a>
!!! function "virtual ~MemoryAllocator() = default"

    
    Default Destructor.
             
    
    
    

