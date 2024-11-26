---
title: DefaultMemoryAllocator
description: Default memory allocator.
generator: doxide
---


# DefaultMemoryAllocator

**class  DefaultMemoryAllocator final : public MemoryAllocator**


Default memory allocator.

This implementation uses a fast and efficient "proxy" allocator designed to handle many small allocations/deallocations in heavy
multithreaded scenarios.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [DefaultMemoryAllocator](#DefaultMemoryAllocator) | Initializes a new default memory allocator. |
| [~DefaultMemoryAllocator](#_u007eDefaultMemoryAllocator) | Destroy the allocator.  |
| [Malloc](#Malloc) |  @inherit  |
| [Realloc](#Realloc) |  @inherit  |
| [Malign](#Malign) |  @inherit  |
| [Realign](#Realign) |  @inherit  |
| [Free](#Free) |  @inherit  |
| [SizeOf](#SizeOf) |  @inherit  |

## Function Details

### DefaultMemoryAllocator<a name="DefaultMemoryAllocator"></a>
!!! function "DefaultMemoryAllocator(AmUInt32 bucketsCount, AmSize bucketSizeInBytes)"

    
    Initializes a new default memory allocator.
    
    This constructor will create the given number of allocator buckets, each of the
    given size.
    
    
    :material-location-enter: **Parameter** `bucketsCount`
    :    The number of allocator buckets to create.
        
    :material-location-enter: **Parameter** `bucketSizeInBytes`
    :    The size of each allocator bucket in bytes.
                
    

### Free<a name="Free"></a>
!!! function "void Free(eMemoryPoolKind pool, AmVoidPtr address) override"

    
    @inherit
            
    

### Malign<a name="Malign"></a>
!!! function "AmVoidPtr Malign(eMemoryPoolKind pool, AmSize size, AmUInt32 alignment) override"

    
    @inherit
            
    

### Malloc<a name="Malloc"></a>
!!! function "AmVoidPtr Malloc(eMemoryPoolKind pool, AmSize size) override"

    
    @inherit
            
    

### Realign<a name="Realign"></a>
!!! function "AmVoidPtr Realign(eMemoryPoolKind pool, AmVoidPtr address, AmSize size, AmUInt32 alignment) override"

    
    @inherit
            
    

### Realloc<a name="Realloc"></a>
!!! function "AmVoidPtr Realloc(eMemoryPoolKind pool, AmVoidPtr address, AmSize size) override"

    
    @inherit
            
    

### SizeOf<a name="SizeOf"></a>
!!! function "AmSize SizeOf(eMemoryPoolKind pool, AmVoidPtr address) override"

    
    @inherit
            
    

### ~DefaultMemoryAllocator<a name="_u007eDefaultMemoryAllocator"></a>
!!! function "~DefaultMemoryAllocator() override"

    
    Destroy the allocator.
             
    
    
    

