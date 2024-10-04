---
title: MemoryPoolKind
description: Available memory pools. 
generator: doxide
---


# MemoryPoolKind

**enum class MemoryPoolKind : AmUInt8**


Available memory pools.
     




**Engine**
:   
Amplitude Engine allocations.
         




**Amplimix**
:   
Amplimix allocations.
         




**SoundData**
:   
Sound data and streams.
         




**Filtering**
:   
Filters related allocations.
         




**Codec**
:   
Encoding/Decoding allocations.

        


**IO**
:   
I/O and filesystem related allocations.
         




**Default**
:   
Default allocations pool. Use this when the allocated memory pool is not available.
         * @note amnew use this pool to allocate memory from the memory manager.
         




**COUNT**
:   
The total number of memory pools.
         





