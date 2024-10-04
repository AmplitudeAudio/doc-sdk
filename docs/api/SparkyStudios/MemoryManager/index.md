---
title: MemoryManager
description: Manages memory allocations inside the engine. 
generator: doxide
---


# MemoryManager

**class  MemoryManager**


Manages memory allocations inside the engine.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [Initialize](#Initialize) | Initializes the memory manager. |
| [Deinitialize](#Deinitialize) | Unloads the memory manager.  |
| [IsInitialized](#IsInitialized) | Checks whether the memory manager is initialized. |
| [GetInstance](#GetInstance) | Gets the actual instance of the memory manager.  |
| [Malloc](#Malloc) | Allocates a block of memory with the given size in the given pool. |
| [Malign](#Malign) | Allocates a block of memory with the given size and the given alignment, * in the given pool. |
| [Realloc](#Realloc) | Updates the size of a previously allocated memory. |
| [Realign](#Realign) | Updates the size of a previously allocated aligned memory. |
| [Free](#Free) | Releases an allocated memory block. |
| [TotalReservedMemorySize](#TotalReservedMemorySize) | Gets the total allocated size. |
| [SizeOf](#SizeOf) | Gets the size of the given memory block. |
| [GetMemoryPoolName](#GetMemoryPoolName) | Gets the name of the given memory pool. |
| [GetStats](#GetStats) | Returns the memory allocation statistics for the given pool. |
| [InspectMemoryLeaks](#InspectMemoryLeaks) | Inspect the memory manager for memory leaks. |

## Function Details

### Deinitialize<a name="Deinitialize"></a>
!!! function "static void Deinitialize()"

    
    Unloads the memory manager.
             
    
    
    

### Free<a name="Free"></a>
!!! function "void Free(MemoryPoolKind pool, AmVoidPtr address)"

    
    Releases an allocated memory block.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to release from.
        
    :material-location-enter: **Parameter** `address`
    :    The address of the memory to release.
                
    

### GetInstance<a name="GetInstance"></a>
!!! function "static MemoryManager&#42; GetInstance()"

    
    Gets the actual instance of the memory manager.
             
    
    
    

### GetMemoryPoolName<a name="GetMemoryPoolName"></a>
!!! function "static AmString GetMemoryPoolName(MemoryPoolKind pool)"

    
    Gets the name of the given memory pool.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to get the name for.
    
    
    :material-keyboard-return: **Return**
    :    The name of the memory pool.
            
    

### GetStats<a name="GetStats"></a>
!!! function "[[nodiscard]] const MemoryPoolStats&amp; GetStats(MemoryPoolKind pool) const"

    
    Returns the memory allocation statistics for the given pool.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The pool to get the statistics for.
                
    

### Initialize<a name="Initialize"></a>
!!! function "static void Initialize(const MemoryManagerConfig&amp; config)"

    
    Initializes the memory manager.
    
    @remarks This should be done prior to any call of GetInstance().
            
    

### InspectMemoryLeaks<a name="InspectMemoryLeaks"></a>
!!! function "[[nodiscard]] AmString InspectMemoryLeaks() const"

    
    Inspect the memory manager for memory leaks.
    
    
    !!! note
         This function is most useful after the engine has been deinitialized. Calling it before may just
        report a lot of false positives (allocated memories still in use).
    
    
    :material-keyboard-return: **Return**
    :    A string containing a report for the detected memory leaks.
            
    

### IsInitialized<a name="IsInitialized"></a>
!!! function "[[maybe_unused]] static bool IsInitialized()"

    
    Checks whether the memory manager is initialized.
    
    
    :material-keyboard-return: **Return**
    :    Whether the memory manager is initialized.
            
    

### Malign<a name="Malign"></a>
!!! function "[[nodiscard]] AmVoidPtr Malign(MemoryPoolKind pool, AmSize size, AmUInt32 alignment, const char&#42; file, AmUInt32 line)"

    
    Allocates a block of memory with the given size and the given alignment,
             * in the given pool.
    
    
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
    
    
    :material-keyboard-return: **Return**
    :    A pointer to the allocated block.
            
    

### Malloc<a name="Malloc"></a>
!!! function "[[nodiscard]] AmVoidPtr Malloc(MemoryPoolKind pool, AmSize size, const char&#42; file, AmUInt32 line)"

    
    Allocates a block of memory with the given size in the given pool.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to allocate from.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the block to allocate.
        
    :material-location-enter: **Parameter** `file`
    :    The file in which the allocation was made.
        
    :material-location-enter: **Parameter** `line`
    :    The line in which the allocation was made.
    
    
    :material-keyboard-return: **Return**
    :    A pointer to the allocated block.
            
    

### Realign<a name="Realign"></a>
!!! function "[[nodiscard]] AmVoidPtr Realign( MemoryPoolKind pool, AmVoidPtr address, AmSize size, AmUInt32 alignment, const char&#42; file, AmUInt32 line)"

    
    Updates the size of a previously allocated aligned memory.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to update.
        
    :material-location-enter: **Parameter** `address`
    :    The address of the aligned memory to update.
        
    :material-location-enter: **Parameter** `size`
    :    The new size of the aligned memory.
        
    :material-location-enter: **Parameter** `alignment`
    :    The new alignment of the aligned memory.
        
    :material-location-enter: **Parameter** `file`
    :    The file in which the allocation was made.
        
    :material-location-enter: **Parameter** `line`
    :    The line in which the allocation was made.
    
    
    :material-keyboard-return: **Return**
    :    A pointer to the allocated block. Maybe equal to address if the original pointer had enough memory.
            
    

### Realloc<a name="Realloc"></a>
!!! function "[[nodiscard]] AmVoidPtr Realloc(MemoryPoolKind pool, AmVoidPtr address, AmSize size, const char&#42; file, AmUInt32 line)"

    
    Updates the size of a previously allocated memory.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to update.
        
    :material-location-enter: **Parameter** `address`
    :    The address of the memory to update.
        
    :material-location-enter: **Parameter** `size`
    :    The new size of the memory.
        
    :material-location-enter: **Parameter** `file`
    :    The file in which the allocation was made.
        
    :material-location-enter: **Parameter** `line`
    :    The line in which the allocation was made.
    
    
    :material-keyboard-return: **Return**
    :    A pointer to the allocated block. Maybe equal to address if the original pointer had enough memory.
            
    

### SizeOf<a name="SizeOf"></a>
!!! function "[[nodiscard]] AmSize SizeOf(MemoryPoolKind pool, AmConstVoidPtr address) const"

    
    Gets the size of the given memory block.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The memory pool to get the size from.
        
    :material-location-enter: **Parameter** `address`
    :    The address of the memory block.
    
    
    :material-keyboard-return: **Return**
    :    The size of the given memory block.
            
    

### TotalReservedMemorySize<a name="TotalReservedMemorySize"></a>
!!! function "[[nodiscard]] AmSize TotalReservedMemorySize() const"

    
    Gets the total allocated size.
    
    
    :material-keyboard-return: **Return**
    :    The total currently allocated size.
            
    

