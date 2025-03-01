---
title: am_delete
description: Deleter for unique/shared pointers.
generator: doxide
---


# am_delete

**template&lt;class T, eMemoryPoolKind Pool = eMemoryPoolKind_Default&gt; struct am_delete**


Deleter for unique/shared pointers.


:material-code-tags: **Template parameter** `T`
:    The type of the pointer to delete.
    
:material-code-tags: **Template parameter** `Pool`
:    The memory pool to delete the pointer from.


!!! note
     This deleter uses the `ampooldelete` function to delete the pointer.
          It is templated to ensure that the correct pool is used.
          This allows for a single implementation of the deleter for all pointer types.
          The `std::unique_ptr` and `std::shared_ptr` will automatically call this deleter when the pointer is deleted.


:material-eye-outline: **See**
:    ampooldelete, AmUniquePtr, AmSharedPtr


    


