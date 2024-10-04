---
title: Allocation
description: A single memory allocation.
generator: doxide
---


# Allocation

**struct Allocation**


A single memory allocation.

This struct describes a single memory allocation. It is used to track memory allocations made by
the engine for each pool, and inspect memory leaks.
        


## Variables

| Name | Description |
| ---- | ----------- |
| [pool](#pool) | The memory pool.  |
| [address](#address) | The address of the allocation.  |
| [size](#size) | The size of the allocation.  |
| [file](#file) | The file in which the allocation was made.  |
| [line](#line) | The line in which the allocation was made.  |

## Operators

| Name | Description |
| ---- | ----------- |
| [AmVoidPtr](#AmVoidPtr) | Explicit conversion to the address of the allocation. |
| [operator==](#operator_u003d_u003d) | Checks if the address matches the provided pointer. |
| [operator==](#operator_u003d_u003d) | Checks if the address matches the provided pointer. |
| [operator<](#operator_u003c) | Checks if the address is less than the provided address. |

## Variable Details

### address<a name="address"></a>

!!! variable "AmVoidPtr address"

    
    The address of the allocation.
                 
    
    
    

### file<a name="file"></a>

!!! variable "const char&#42; file"

    
    The file in which the allocation was made.
                 
    
    
    

### line<a name="line"></a>

!!! variable "AmUInt32 line"

    
    The line in which the allocation was made.
                 
    
    
    

### pool<a name="pool"></a>

!!! variable "MemoryPoolKind pool"

    
    The memory pool.
                 
    
    
    

### size<a name="size"></a>

!!! variable "AmSize size"

    
    The size of the allocation.
                 
    
    
    

## Operator Details

### AmVoidPtr<a name="AmVoidPtr"></a>

!!! function "[[nodiscard]] inline explicit operator AmVoidPtr() const"

    
    Explicit conversion to the address of the allocation.
    
    
    :material-keyboard-return: **Return**
    :    The address of the allocation.
                
    

### operator<<a name="operator_u003c"></a>

!!! function "[[nodiscard]] inline bool operator&lt;(const Allocation&amp; other) const"

    
    Checks if the address is less than the provided address.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other allocation to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the addresses are less than, `false` otherwise.
                
    

### operator==<a name="operator_u003d_u003d"></a>

!!! function "[[nodiscard]] inline bool operator==(const AmVoidPtr&amp; ptr) const"

    
    Checks if the address matches the provided pointer.
    
    
    :material-location-enter: **Parameter** `ptr`
    :    The pointer to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the addresses match, `false` otherwise.
                
    

!!! function "[[nodiscard]] inline bool operator==(const Allocation&amp; other) const"

    
    Checks if the address matches the provided pointer.
    
    
    :material-location-enter: **Parameter** `ptr`
    :    The pointer to compare with.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the addresses match, `false` otherwise.
                
    

