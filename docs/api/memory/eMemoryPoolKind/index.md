---
title: eMemoryPoolKind
description: Available memory pools.
generator: doxide
---


# eMemoryPoolKind

**enum eMemoryPoolKind : AmUInt8**


Available memory pools.


    


**eMemoryPoolKind_Engine**
:   
Amplitude Engine allocations.
         




**eMemoryPoolKind_Amplimix**
:   
Amplimix allocations.
         




**eMemoryPoolKind_SoundData**
:   
Sound data and streams.
         




**eMemoryPoolKind_Filtering**
:   
Filters related allocations.
         




**eMemoryPoolKind_Codec**
:   
Encoding/Decoding allocations.

        


**eMemoryPoolKind_IO**
:   
I/O and filesystem related allocations.
         




**eMemoryPoolKind_Default**
:   
Default allocations pool. Use this when the allocated memory pool is not available.


!!! note
     `amnew` use this pool to allocate memory from the memory manager.
            


**eMemoryPoolKind_COUNT**
:   
The total number of memory pools.
         





