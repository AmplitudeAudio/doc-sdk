---
title: AmUniquePtr
description: Unique pointer type.
generator: doxide
---


# AmUniquePtr

**template&lt;MemoryPoolKind Pool, class T&gt; using AmUniquePtr = std::unique_ptr&lt;T, am_delete&lt;Pool, T&gt;&gt;**


Unique pointer type.


:material-code-tags: **Template parameter** `Pool`
:    The memory pool to allocate the pointer from.
    
:material-code-tags: **Template parameter** `T`
:    The type of the pointer to allocate.


    


