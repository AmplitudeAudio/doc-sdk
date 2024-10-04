---
title: am_delete
description: Deleter for unique pointers.
generator: doxide
---


# am_delete

**template&lt;MemoryPoolKind Pool, class T&gt; struct am_delete**


Deleter for unique pointers.


:material-code-tags: **Template parameter** `Pool`
:    The memory pool to delete the pointer from.
    
:material-code-tags: **Template parameter** `T`
:    The type of the pointer to delete.


!!! note
     This deleter uses the `ampooldelete` function to delete the pointer.
          It is templated to ensure that the correct pool is used.
          This allows for a single implementation of the deleter for all pointer types.
          The `std::unique_ptr` will automatically call this deleter when the pointer is deleted.


:material-eye-outline: **See**
:    ampooldelete, AmUniquePtr


    


