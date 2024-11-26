---
title: MemoryPoolStats
description: Collects the statistics about the memory allocations * for a specific pool
generator: doxide
---


# MemoryPoolStats

**struct  MemoryPoolStats**


Collects the statistics about the memory allocations
     * for a specific pool


    


## Variables

| Name | Description |
| ---- | ----------- |
| [pool](#pool) | The pool for which this statistics is for.  |
| [maxMemoryUsed](#maxMemoryUsed) | The maximum total memory used by this pool.  |
| [allocCount](#allocCount) | The total count of allocations made on this pool.  |
| [freeCount](#freeCount) | The total count of frees made on this pool.  |

## Operators

| Name | Description |
| ---- | ----------- |
| [operator=](#operator_u003d) | Assignment operator. |

## Functions

| Name | Description |
| ---- | ----------- |
| [MemoryPoolStats](#MemoryPoolStats) | Default constructor.  |
| [MemoryPoolStats](#MemoryPoolStats) | Creates a new `MemoryPoolStats` object. |
| [MemoryPoolStats](#MemoryPoolStats) | Copy constructor. |

## Variable Details

### allocCount<a name="allocCount"></a>

!!! variable "std::atomic&lt;AmUInt64&gt; allocCount"

    
    The total count of allocations made on this pool.
             
    
    
    

### freeCount<a name="freeCount"></a>

!!! variable "std::atomic&lt;AmUInt64&gt; freeCount"

    
    The total count of frees made on this pool.
             
    
    
    

### maxMemoryUsed<a name="maxMemoryUsed"></a>

!!! variable "std::atomic&lt;AmSize&gt; maxMemoryUsed"

    
    The maximum total memory used by this pool.
             
    
    
    

### pool<a name="pool"></a>

!!! variable "eMemoryPoolKind pool"

    
    The pool for which this statistics is for.
             
    
    
    

## Operator Details

### operator=<a name="operator_u003d"></a>

!!! function "MemoryPoolStats&amp; operator=(const MemoryPoolStats&amp; other)"

    
    Assignment operator.
    
    
    :material-location-enter: **Parameter** `other`
    :    The `MemoryPoolStats` object to assign from.
                
    

## Function Details

### MemoryPoolStats<a name="MemoryPoolStats"></a>
!!! function "MemoryPoolStats()"

    
    Default constructor.
             
    
    
    

!!! function "explicit MemoryPoolStats(eMemoryPoolKind pool)"

    
    Creates a new `MemoryPoolStats` object.
    
    
    :material-location-enter: **Parameter** `pool`
    :    The pool to get the statistics for.
                
    

!!! function "MemoryPoolStats(const MemoryPoolStats&amp; copy)"

    
    Copy constructor.
    
    
    :material-location-enter: **Parameter** `copy`
    :    The `MemoryPoolStats` object to copy from.
                
    

