---
title: AmUniquePtr
description: Unique pointer type.
generator: doxide
---


# AmUniquePtr

**template&lt;class T, eMemoryPoolKind Pool = eMemoryPoolKind_Default&gt; using AmUniquePtr = std::unique_ptr&lt;T, am_delete&lt;T, Pool&gt;&gt;**


Unique pointer type.


:material-code-tags: **Template parameter** `T`
:    The type of the pointer to allocate.
    
:material-code-tags: **Template parameter** `Pool`
:    The memory pool to allocate the pointer from.


    


