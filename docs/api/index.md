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

:material-format-section: [DSP](dsp/index.md)
:   Digital Signal Processing (DSP) API

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
| [amVersion](#amVersion) | Gets the current Amplitude SDK version.  |
| [AM_ID_CHAR_FMT](#AM_ID_CHAR_FMT) | Compiling for an Apple platform Compiling for iOS or tvOS (iPhone, iPad, iPod, Apple TV. |
| [M_PI](#M_PI) | Define the value of Pi if the platform doesn't do that  |
| [AM_FILTERS_PER_STREAM](#AM_FILTERS_PER_STREAM) | Maximum number of filters per stream  |
| [AM_MAX_THREAD_POOL_TASKS](#AM_MAX_THREAD_POOL_TASKS) | Maximum number of tasks in a single pool  |
| [amEngine](#amEngine) | Macro to get the current Amplitude engine instance.  |

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
     
    
    
    

### amVersion<a name="amVersion"></a>

!!! macro "#define amVersion"

    
    Gets the current Amplitude SDK version.
     
    
    
    

