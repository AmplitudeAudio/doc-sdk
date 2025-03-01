---
title: Memory
description: Memory management and allocation
generator: doxide
---


# Memory

Memory management and allocation

## Types

| Name | Description |
| ---- | ----------- |
| [AmFakeSharedPtr](AmFakeSharedPtr/index.md) | Fake shared pointer. |
| [AmSharedPtr](AmSharedPtr/index.md) | Shared pointer type. |
| [AmUniquePtr](AmUniquePtr/index.md) | Unique pointer type. |
| [DefaultMemoryAllocator](DefaultMemoryAllocator/index.md) | Default memory allocator. |
| [MemoryAllocator](MemoryAllocator/index.md) | Memory Allocator Interface. |
| [MemoryPoolStats](MemoryPoolStats/index.md) | Collects the statistics about the memory allocations * for a specific pool |
| [ScopedMemoryAllocation](ScopedMemoryAllocation/index.md) | Allocates a block of memory with the given size in the given pool. |
| [am_delete](am_delete/index.md) | Deleter for unique/shared pointers. |
| [eMemoryPoolKind](eMemoryPoolKind/index.md) | Available memory pools. |

## Macros

| Name | Description |
| ---- | ----------- |
| [amMemory](#amMemory) | Shortcut access to the Amplitude's memory manager instance. |
| [amdelete](#amdelete) | Deallocates a memory allocated with @ref amnew amnew. |
| [amfree](#amfree) | Deallocates a block of memory from the default memory pool. |
| [ammalign](#ammalign) | Allocates a block of memory from the default memory pool. |
| [ammalloc](#ammalloc) | Allocates a block of memory from the default memory pool. |
| [amnew](#amnew) | Allocates memory for a new object in the Default pool using the memory manager. |
| [ampooldelete](#ampooldelete) | Deallocates a memory allocated with @ref ampoolnew ampoolnew. |
| [ampoolfree](#ampoolfree) | Deallocates a block of memory from the specified memory pool. |
| [ampoolmalign](#ampoolmalign) | Allocates an aligned block of memory from the specified memory pool. |
| [ampoolmalloc](#ampoolmalloc) | Allocates a block of memory from the specified memory pool. |
| [ampoolnew](#ampoolnew) | Allocates memory for a new object in the given memory pool. |
| [ampoolrealign](#ampoolrealign) | Reallocates an aligned block of memory from the specified memory pool. |
| [ampoolrealloc](#ampoolrealloc) | Reallocates a block of memory from the specified memory pool. |
| [amrealign](#amrealign) | Reallocates an aligned block of memory from the default memory pool. |
| [amrealloc](#amrealloc) | Reallocates a block of memory from the default memory pool. |

## Macro Details

### amMemory<a name="amMemory"></a>

!!! macro "#define amMemory"

    
    Shortcut access to the Amplitude's memory manager instance.
    
    
    
    

### amdelete<a name="amdelete"></a>

!!! macro "#define amdelete(_type_, _ptr_)"

    
    Deallocates a memory allocated with @ref amnew amnew.
    
    This will call the object's destructor before the memory is freed.
    
    
    :material-location-enter: **Parameter** `_type_`
    :    The type of the object to deallocate.
        
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to the object to deallocate.
    
    
    :material-eye-outline: **See**
    :    [amnew](#amnew)
    
    
    
    

### amfree<a name="amfree"></a>

!!! macro "#define amfree(_ptr_)"

    
    Deallocates a block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to deallocate.
    
    
    :material-eye-outline: **See**
    :    [ampoolfree](#ampoolfree)
    
    
    
    

### ammalign<a name="ammalign"></a>

!!! macro "#define ammalign(_size_, _alignment_)"

    
    Allocates a block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_size_`
    :    The size of the memory to allocate.
        
    :material-location-enter: **Parameter** `_alignment_`
    :    The alignment of the memory to allocate.
    
    
    :material-eye-outline: **See**
    :    [ampoolmalign](#ampoolmalign)
    
    
    
    

### ammalloc<a name="ammalloc"></a>

!!! macro "#define ammalloc(_size_)"

    
    Allocates a block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_size_`
    :    The size of the memory to allocate.
    
    
    :material-eye-outline: **See**
    :    [ampoolmalloc](#ampoolmalloc)
    
    
    
    

### amnew<a name="amnew"></a>

!!! macro "#define amnew(_type_, ...)"

    
    Allocates memory for a new object in the Default pool using the memory manager.
    
    This will create a new memory allocation in the Default pool. The allocated
    memory will be freed when the object is destroyed using [amdelete.](#amdelete)
    
    
    :material-location-enter: **Parameter** `_type_`
    :    The type of the object to allocate.
        
    :material-location-enter: **Parameter** `Additional`
    :    arguments to pass to the constructor of the object.
    
    
    :material-eye-outline: **See**
    :    [amdelete](#amdelete)
    
    
    
    

### ampooldelete<a name="ampooldelete"></a>

!!! macro "#define ampooldelete(_pool_, _type_, _ptr_)                                                                                                \"

    
    Deallocates a memory allocated with @ref ampoolnew ampoolnew.
    
    This will call the object's destructor before to free the memory.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to deallocate from.
        
    :material-location-enter: **Parameter** `_type_`
    :    The type of the object to deallocate.
        
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to the object to deallocate.
    
    
    :material-eye-outline: **See**
    :    [ampoolnew](#ampoolnew)
    
    
    
    

### ampoolfree<a name="ampoolfree"></a>

!!! macro "#define ampoolfree(_pool_, _ptr_)"

    
    Deallocates a block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to deallocate from.
        
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to deallocate.
    
    
    
    

### ampoolmalign<a name="ampoolmalign"></a>

!!! macro "#define ampoolmalign(_pool_, _size_, _alignment_)"

    
    Allocates an aligned block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to deallocate from.
        
    :material-location-enter: **Parameter** `_size_`
    :    The size of the memory to allocate.
        
    :material-location-enter: **Parameter** `_alignment_`
    :    The alignment of the memory to allocate.
    
    
    
    

### ampoolmalloc<a name="ampoolmalloc"></a>

!!! macro "#define ampoolmalloc(_pool_, _size_)"

    
    Allocates a block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to allocate from.
        
    :material-location-enter: **Parameter** `_size_`
    :    The size of the memory to allocate.
    
    
    
    

### ampoolnew<a name="ampoolnew"></a>

!!! macro "#define ampoolnew(_pool_, _type_, ...)"

    
    Allocates memory for a new object in the given memory pool.
    
    This will create a new memory allocation in the given pool. The allocated
    memory will be freed when the object is destroyed using [ampooldelete.](#ampooldelete)
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to allocate from.
        
    :material-location-enter: **Parameter** `_type_`
    :    The type of the object to allocate.
        
    :material-location-enter: **Parameter** `Additional`
    :    arguments to pass to the constructor of the object.
    
    
    :material-eye-outline: **See**
    :    [ampooldelete](#ampooldelete)
    
    
    
    

### ampoolrealign<a name="ampoolrealign"></a>

!!! macro "#define ampoolrealign(_pool_, _ptr_, _size_, _alignment_)"

    
    Reallocates an aligned block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to reallocate from. Should be the same as the one used to allocate the memory.
        
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to reallocate.
        
    :material-location-enter: **Parameter** `_size_`
    :    The new size of the memory.
        
    :material-location-enter: **Parameter** `_alignment_`
    :    The alignment of the memory to reallocate.
    
    
    
    

### ampoolrealloc<a name="ampoolrealloc"></a>

!!! macro "#define ampoolrealloc(_pool_, _ptr_, _size_)"

    
    Reallocates a block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to reallocate from. Should be the same as the one used to allocate the memory.
        
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to reallocate.
        
    :material-location-enter: **Parameter** `_size_`
    :    The new size of the memory.
    
    
    
    

### amrealign<a name="amrealign"></a>

!!! macro "#define amrealign(_ptr_, _size_, _alignment_)                                                                                              \"

    
    Reallocates an aligned block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to reallocate.
        
    :material-location-enter: **Parameter** `_size_`
    :    The new size of the memory.
        
    :material-location-enter: **Parameter** `_alignment_`
    :    The alignment of the memory to reallocate.
    
    
    :material-eye-outline: **See**
    :    [ampoolrealign](#ampoolrealign)
    
    
    
    

### amrealloc<a name="amrealloc"></a>

!!! macro "#define amrealloc(_ptr_, _size_)"

    
    Reallocates a block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to reallocate.
        
    :material-location-enter: **Parameter** `_size_`
    :    The new size of the memory.
    
    
    :material-eye-outline: **See**
    :    [ampoolrealloc](#ampoolrealloc)
    
    
    
    

