---
title: API Reference
description: Amplitude Audio SDK public API reference and documentation.
generator: doxide
---


# API Reference

Amplitude Audio SDK public API reference and documentation.

:material-format-section: [Core](core/index.md)
:   Core functionalities of the SDK

:material-format-section: [Engine](engine/index.md)
:   Engine-specific functionalities

:material-format-section: [Assets](assets/index.md)
:   Assets API

:material-format-section: [IO](io/index.md)
:   Input/Output API

:material-format-section: [Math](math/index.md)
:   Math libraries and utilities

:material-format-section: [Memory](memory/index.md)
:   Memory management and allocation

:material-package: [SparkyStudios](SparkyStudios/index.md)
:   

## Macros

| Name | Description |
| ---- | ----------- |
| [AM_ID_CHAR_FMT](#AM_ID_CHAR_FMT) | Compiling for a Linux platform Defines the format used to print AmObjectId value  |
| [AM_LIB_EXPORT](#AM_LIB_EXPORT) | Call policy  |
| [AM_OS_CHAR_FMT](#AM_OS_CHAR_FMT) | Defines the format used to print AmOsString text  |
| [AM_OS_STRING](#AM_OS_STRING) | Macro used to convert a string literal to an AmOsString string at compile-time  |
| [AM_OS_STRING_TO_STRING](#AM_OS_STRING_TO_STRING) | Conversion between OS strings and default strings  |
| [amMemory](#amMemory) | Shortcut access to the Amplitude's memory manager instance.  |
| [ampoolmalloc](#ampoolmalloc) | Allocates a block of memory from the specified memory pool. |
| [ampoolmalign](#ampoolmalign) | Allocates an aligned block of memory from the specified memory pool. |
| [ampoolrealloc](#ampoolrealloc) | Reallocates a block of memory from the specified memory pool. |
| [ampoolrealign](#ampoolrealign) | Reallocates an aligned block of memory from the specified memory pool. |
| [ampoolfree](#ampoolfree) | Deallocates a block of memory from the specified memory pool. |
| [ammalloc](#ammalloc) | Allocates a block of memory from the default memory pool. |
| [ammalign](#ammalign) | Allocates a block of memory from the default memory pool. |
| [amrealloc](#amrealloc) | Reallocates a block of memory from the deault memory pool. |
| [amrealign](#amrealign) | Reallocates an aligned block of memory from the default memory pool. |
| [amfree](#amfree) | Deallocates a block of memory from the default memory pool. |
| [ampoolnew](#ampoolnew) | Allocates memory for a new object in the Default pool using the memory manager. |
| [ampooldelete](#ampooldelete) | Deallocates a memory allocated with @a ampoolnew. |
| [amnew](#amnew) | Allocates memory for a new object in the Default pool using the memory manager. |
| [amdelete](#amdelete) | Deallocates a memory allocated with @a amnew. |
| [amVersion](#amVersion) | Gets the current Amplitude SDK version.  |
| [AM_ID_CHAR_FMT](#AM_ID_CHAR_FMT) | Compiling for an Apple platform Compiling for iOS or tvOS (iPhone, iPad, iPod, Apple TV. |
| [M_PI](#M_PI) | Define the value of Pi if the platform doesn't do that  |
| [AM_FILTERS_PER_STREAM](#AM_FILTERS_PER_STREAM) | Maximum number of filters per stream  |
| [AM_MAX_THREAD_POOL_TASKS](#AM_MAX_THREAD_POOL_TASKS) | Maximum number of tasks in a single pool  |
| [amEngine](#amEngine) | Macro to get the current Amplitude engine instance.  |
| [amLogger](#amLogger) | The global logger instance.  |
| [amLog](#amLog) | Logs a message with the given level. |
| [amLogDebug](#amLogDebug) | Logs a debug message. |
| [amLogInfo](#amLogInfo) | Logs an informational message. |
| [amLogWarning](#amLogWarning) | Logs a warning message. |
| [amLogError](#amLogError) | Logs an error message. |
| [amLogCritical](#amLogCritical) | Logs a critical message. |

## Macro Details

### AM_FILTERS_PER_STREAM<a name="AM_FILTERS_PER_STREAM"></a>

!!! macro "#define AM_FILTERS_PER_STREAM"

    Maximum number of filters per stream
    

### AM_ID_CHAR_FMT<a name="AM_ID_CHAR_FMT"></a>

!!! macro "#define AM_ID_CHAR_FMT"

    Compiling for a Linux platform
    Defines the format used to print AmObjectId value
    

### AM_ID_CHAR_FMT<a name="AM_ID_CHAR_FMT"></a>

!!! macro "#define AM_ID_CHAR_FMT"

    Compiling for an Apple platform
    Compiling for iOS or tvOS (iPhone, iPad, iPod, Apple TV...)
    Compiling for Mac OS X
    Defines the format used to print AmObjectId value
    

### AM_LIB_EXPORT<a name="AM_LIB_EXPORT"></a>

!!! macro "#define AM_LIB_EXPORT"

    Call policy
    

### AM_MAX_THREAD_POOL_TASKS<a name="AM_MAX_THREAD_POOL_TASKS"></a>

!!! macro "#define AM_MAX_THREAD_POOL_TASKS"

    Maximum number of tasks in a single pool
    

### AM_OS_CHAR_FMT<a name="AM_OS_CHAR_FMT"></a>

!!! macro "#define AM_OS_CHAR_FMT"

    Defines the format used to print AmOsString text
    

### AM_OS_STRING<a name="AM_OS_STRING"></a>

!!! macro "#define AM_OS_STRING(s)"

    Macro used to convert a string literal to an AmOsString string at compile-time
    

### AM_OS_STRING_TO_STRING<a name="AM_OS_STRING_TO_STRING"></a>

!!! macro "#define AM_OS_STRING_TO_STRING(s)"

    Conversion between OS strings and default strings
    

### M_PI<a name="M_PI"></a>

!!! macro "#define M_PI"

    Define the value of Pi if the platform doesn't do that
    

### amEngine<a name="amEngine"></a>

!!! macro "#define amEngine"

    
    Macro to get the current Amplitude engine instance.
     
    
    
    

### amLog<a name="amLog"></a>

!!! macro "#define amLog(_level_, _message_, ...)                                                                                                     \"

    
    Logs a message with the given level.
    
    
    :material-location-enter: **Parameter** `_level_`
    :    The level of the log message.
        
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
        
    

### amLogCritical<a name="amLogCritical"></a>

!!! macro "#define amLogCritical(_message_, ...)"

    
    Logs a critical message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
        
    

### amLogDebug<a name="amLogDebug"></a>

!!! macro "#define amLogDebug(_message_, ...)"

    
    Logs a debug message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
        
    

### amLogError<a name="amLogError"></a>

!!! macro "#define amLogError(_message_, ...)"

    
    Logs an error message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
        
    

### amLogInfo<a name="amLogInfo"></a>

!!! macro "#define amLogInfo(_message_, ...)"

    
    Logs an informational message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
        
    

### amLogWarning<a name="amLogWarning"></a>

!!! macro "#define amLogWarning(_message_, ...)"

    
    Logs a warning message.
    
    
    :material-location-enter: **Parameter** `_message_`
    :    The message to log.
        
    :material-location-enter: **Parameter** `The`
    :    arguments to format the message with.
        
    

### amLogger<a name="amLogger"></a>

!!! macro "#define amLogger"

    
    The global logger instance.
     
    
    
    

### amMemory<a name="amMemory"></a>

!!! macro "#define amMemory"

    
    Shortcut access to the Amplitude's memory manager instance.
     
    
    
    

### amVersion<a name="amVersion"></a>

!!! macro "#define amVersion"

    
    Gets the current Amplitude SDK version.
     
    
    
    

### amdelete<a name="amdelete"></a>

!!! macro "#define amdelete(_type_, _ptr_)"

    
    Deallocates a memory allocated with @a amnew.
    
    This will call the object's destructor before the memory is freed.
    
    
    :material-eye-outline: **See**
    :    amnew
    
    

### amfree<a name="amfree"></a>

!!! macro "#define amfree(_ptr_)"

    
    Deallocates a block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to deallocate.
    
    
    :material-eye-outline: **See**
    :    ampoolfree
    
    

### ammalign<a name="ammalign"></a>

!!! macro "#define ammalign(_size_, _alignment_)"

    
    Allocates a block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_size_`
    :    The size of the memory to allocate.
        
    :material-location-enter: **Parameter** `_alignment_`
    :    The alignment of the memory to allocate.
    
    
    :material-eye-outline: **See**
    :    ampoolmalign
    
    

### ammalloc<a name="ammalloc"></a>

!!! macro "#define ammalloc(_size_)"

    
    Allocates a block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_size_`
    :    The size of the memory to allocate.
    
    
    :material-eye-outline: **See**
    :    ampoolmalloc
    
    

### amnew<a name="amnew"></a>

!!! macro "#define amnew(_type_, ...)"

    
    Allocates memory for a new object in the Default pool using the memory manager.
    
    This will create a new memory allocation in the Default pool. The allocated
    memory will be freed when the object is destroyed using *amdelete.*
    
    
    :material-eye-outline: **See**
    :    amdelete
    
    

### ampooldelete<a name="ampooldelete"></a>

!!! macro "#define ampooldelete(_pool_, _type_, _ptr_)                                                                                                \"

    
    Deallocates a memory allocated with @a ampoolnew.
    
    This will call the object's destructor before the memory is freed.
    
    
    :material-eye-outline: **See**
    :    ampoolnew
    
    

### ampoolfree<a name="ampoolfree"></a>

!!! macro "#define ampoolfree(_pool_, _ptr_)"

    
    Deallocates a block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to deallocate from.
        
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to deallocate.
        
    

### ampoolmalign<a name="ampoolmalign"></a>

!!! macro "#define ampoolmalign(_pool_, _size_, _alignment_)"

    
    Allocates an aligned block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to deallocate from.
        
    :material-location-enter: **Parameter** `_size_`
    :    The size of the memory to allocate.
        
    :material-location-enter: **Parameter** `_alignment_`
    :    The alignment of the memory to allocate.
        
    

### ampoolmalloc<a name="ampoolmalloc"></a>

!!! macro "#define ampoolmalloc(_pool_, _size_)"

    
    Allocates a block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to allocate from.
        
    :material-location-enter: **Parameter** `_size_`
    :    The size of the memory to allocate.
        
    

### ampoolnew<a name="ampoolnew"></a>

!!! macro "#define ampoolnew(_pool_, _type_, ...)"

    
    Allocates memory for a new object in the Default pool using the memory manager.
    
    This will create a new memory allocation in the Default pool. The allocated
    memory will be freed when the object is destroyed using *amdelete.*
    
    
    :material-eye-outline: **See**
    :    ampooldelete
    
    

### ampoolrealign<a name="ampoolrealign"></a>

!!! macro "#define ampoolrealign(_pool_, _ptr_, _size_, _alignment_)"

    
    Reallocates an aligned block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to reallocate from. Should be the same as the one used to allocate the memory.
        
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to reallocate.
        
    :material-location-enter: **Parameter** `_size_`
    :    The new size of the memory.
        
    :material-location-enter: **Parameter** `_alignment_`
    :    The alignment of the memory to allocate.
        
    

### ampoolrealloc<a name="ampoolrealloc"></a>

!!! macro "#define ampoolrealloc(_pool_, _ptr_, _size_)"

    
    Reallocates a block of memory from the specified memory pool.
    
    
    :material-location-enter: **Parameter** `_pool_`
    :    The memory pool to reallocate from. Should be the same as the one used to allocate the memory.
        
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to reallocate.
        
    :material-location-enter: **Parameter** `_size_`
    :    The new size of the memory.
        
    

### amrealign<a name="amrealign"></a>

!!! macro "#define amrealign(_ptr_, _size_, _alignment_)                                                                                              \"

    
    Reallocates an aligned block of memory from the default memory pool.
    
    
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to reallocate.
        
    :material-location-enter: **Parameter** `_size_`
    :    The new size of the memory.
        
    :material-location-enter: **Parameter** `_alignment_`
    :    The alignment of the memory to allocate.
    
    
    :material-eye-outline: **See**
    :    ampoolrealign
    
    

### amrealloc<a name="amrealloc"></a>

!!! macro "#define amrealloc(_ptr_, _size_)"

    
    Reallocates a block of memory from the deault memory pool.
    
    
    :material-location-enter: **Parameter** `_ptr_`
    :    The pointer to reallocate.
        
    :material-location-enter: **Parameter** `_size_`
    :    The new size of the memory.
    
    
    :material-eye-outline: **See**
    :    ampoolrealloc
    
    

