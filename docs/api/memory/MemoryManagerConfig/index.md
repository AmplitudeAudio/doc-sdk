---
title: MemoryManagerConfig
description: Configures the memory management system.
generator: doxide
---


# MemoryManagerConfig

**struct  MemoryManagerConfig**


Configures the memory management system.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [malloc](#malloc) | Memory allocation callback.  |
| [realloc](#realloc) | Memory reallocation callback.  |
| [alignedMalloc](#alignedMalloc) | Aligned memory allocation callback.  |
| [alignedRealloc](#alignedRealloc) | Aligned memory reallocation callback.  |
| [free](#free) | Memory release callback.  |
| [totalReservedMemorySize](#totalReservedMemorySize) | Callback to get the total size of the memory allocated across memory pools |
| [sizeOf](#sizeOf) | Callback to get the total size of memory for a specific pool.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [MemoryManagerConfig](#MemoryManagerConfig) | Creates a new configuration set for the memory manager.  |

## Variable Details

### alignedMalloc<a name="alignedMalloc"></a>

!!! variable "AmMemoryMallocAlignedCallback alignedMalloc"

    
    Aligned memory allocation callback.
             
    
    
    

### alignedRealloc<a name="alignedRealloc"></a>

!!! variable "AmMemoryReallocAlignedCallback alignedRealloc"

    
    Aligned memory reallocation callback.
             
    
    
    

### free<a name="free"></a>

!!! variable "AmMemoryFreeCallback free"

    
    Memory release callback.
             
    
    
    

### malloc<a name="malloc"></a>

!!! variable "AmMemoryMallocCallback malloc"

    
    Memory allocation callback.
             
    
    
    

### realloc<a name="realloc"></a>

!!! variable "AmMemoryReallocCallback realloc"

    
    Memory reallocation callback.
             
    
    
    

### sizeOf<a name="sizeOf"></a>

!!! variable "AmMemorySizeOfCallback sizeOf"

    
    Callback to get the total size of memory for a specific pool.
             
    
    
    

### totalReservedMemorySize<a name="totalReservedMemorySize"></a>

!!! variable "AmMemoryTotalReservedMemorySizeCallback totalReservedMemorySize"

    
    Callback to get the total size of the memory allocated across memory pools
    
            
    

## Function Details

### MemoryManagerConfig<a name="MemoryManagerConfig"></a>
!!! function "MemoryManagerConfig()"

    
    Creates a new configuration set for the memory manager.
             
    
    
    

