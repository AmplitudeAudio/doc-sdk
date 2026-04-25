---
title: Dynamic Plugins
description: Load and use dynamic plugins at runtime to extend codec, driver, filter, and fader support.
diataxis: how-to
---

This guide explains how to load and use **dynamic plugins** with Amplitude. Dynamic plugins are shared libraries (`.dll` on Windows, `.so` on Linux, `.dylib` on macOS) that extend the engine with new codecs, drivers, filters, faders, or pipeline nodes at runtime.

## Overview

Dynamic plugins are supported on **desktop platforms only** (Windows, Linux, macOS). On mobile platforms (iOS, Android), all extensions must be statically linked.

The engine loads plugins from a search path and automatically registers any codecs, drivers, filters, faders, or nodes they provide.

## Building a Dynamic Plugin

A dynamic plugin is a shared library that exports a single registration function:

```cpp
// my_plugin.cpp

#include <SparkyStudios/Audio/Amplitude/Amplitude.h>

using namespace SparkyStudios::Audio::Amplitude;

// The engine calls this function when the plugin is loaded
extern "C" AM_API_PUBLIC bool RegisterPlugin(Engine* engine, MemoryManager* memoryManager)
{
    // Register your extensions
    Codec::Register(std::make_shared<MyCustomCodec>());
    Filter::Register(std::make_shared<MyCustomFilter>());
    return true;
}
```

### Build Configuration

Use your platform's shared library build system. For example, with XMake:

```lua
-- xmake.lua for the plugin
target("my_plugin")
    set_kind("shared")
    add_files("my_plugin.cpp")
    add_includedirs("$(AM_SDK_PATH)/include")
    add_links("amplitude")
```

Or with CMake:

```cmake
# CMakeLists.txt
add_library(my_plugin SHARED my_plugin.cpp)
target_include_directories(my_plugin PRIVATE ${AM_SDK_PATH}/include)
target_link_libraries(my_plugin PRIVATE amplitude)
```

## Loading Plugins at Runtime

### Setting the Search Path

Before initializing the engine, tell it where to look for plugins:

```cpp
// Add a plugin search path
Engine::AddPluginSearchPath(AM_OS_STRING("./plugins"));

// Add multiple paths
Engine::AddPluginSearchPath(AM_OS_STRING("./plugins"));
Engine::AddPluginSearchPath(AM_OS_STRING("/usr/share/amplitude/plugins"));
```

### Loading Specific Plugins

Load a plugin by its base name (without extension):

```cpp
// Load a single plugin
Engine::LoadPlugin(AM_OS_STRING("vorbis_plugin"));

// The engine will look for:
// - vorbis_plugin.dll (Windows)
// - libvorbis_plugin.so (Linux)
// - libvorbis_plugin.dylib (macOS)
```

### Loading All Plugins in a Directory

<!-- FIXME: unverified - Engine::LoadPlugins() does not exist in the public API; load each plugin individually with Engine::LoadPlugin() -->
Load each plugin individually using `Engine::LoadPlugin()`. There is no bulk `LoadPlugins()` helper in the public API.

## Registration Order

The engine locks all registries during `Engine::Initialize()`. Therefore:

1. Set plugin search paths **before** calling `amEngine->Initialize()`.
2. Load plugins **before** calling `amEngine->Initialize()`.
3. After `amEngine->Initialize()`, no new plugins can be registered.

```cpp
int main()
{
    MemoryManager::Initialize();
    // ... initialize file system, etc.

    // Register built-in extensions
    Engine::RegisterDefaultExtensions();

    // Set plugin search paths and load dynamic plugins
    Engine::AddPluginSearchPath(AM_OS_STRING("./plugins"));
    Engine::LoadPlugin(AM_OS_STRING("vorbis_plugin"));

    // Now initialize the engine (registries are locked after this)
    amEngine->Initialize(AM_OS_STRING("config.amconfig"));
}
```

## Plugin Lifecycle

| Phase | Action |
|-------|--------|
| **Load** | The engine calls `dlopen`/`LoadLibrary` on the shared library. |
| **Register** | The engine calls `RegisterPlugin()` to register extensions. |
| **Active** | The plugin's codecs, filters, etc. are available for use. |
| **Unload** | When the engine shuts down, the library is automatically unloaded. |

## Platform-Specific Notes

### Windows

Plugins must be built with the same compiler and CRT as the engine. Mixing debug and release builds, or different MSVC versions, can cause crashes.

Place plugin `.dll` files in the same directory as the executable or in a subdirectory added via `AddPluginSearchPath()`.

### Linux

Ensure the plugin's `.so` file has the correct `rpath` or is in a directory listed in `LD_LIBRARY_PATH`.

```bash
# Check plugin dependencies
ldd libmy_plugin.so
```

### macOS

Plugins must be signed with the same team ID as the main application if running with hardened runtime.

Use `@rpath` or `@loader_path` for library paths:

```bash
install_name_tool -change libamplitude.dylib @rpath/libamplitude.dylib libmy_plugin.dylib
```

## Debugging Plugins

If a plugin fails to load, check the engine log for error messages:

```
[ERROR] Failed to load plugin 'vorbis_plugin': Plugin not found
[ERROR] Failed to load plugin 'my_plugin': Symbol 'RegisterPlugin' not found
```

Common issues:

| Issue | Cause | Solution |
|-------|-------|----------|
| Plugin not found | Wrong search path or missing file | Verify the path and file extension |
| Symbol not found | `RegisterPlugin` not exported with `extern "C"` | Add `extern "C"` and `AM_API_PUBLIC` |
| Crash on load | ABI mismatch | Rebuild with the same compiler/settings |
| Codec not used | Registration after `amEngine->Initialize()` | Load plugins before engine init |

## Best Practices

- **Version your plugins**: Include the Amplitude SDK version in your plugin's build to avoid ABI mismatches.
- **Keep plugins small**: Each plugin should focus on one extension type (one codec, one filter, etc.).
- **Handle errors gracefully**: If `RegisterPlugin()` fails partially, log the error and return `false` rather than crashing.
- **Document dependencies**: If your plugin depends on third-party libraries, list them clearly.

## Next Steps

- Learn how to write [custom codecs](../tutorials/custom-codec.md), [effects](../tutorials/custom-effect.md), [drivers](../tutorials/custom-driver.md), and [faders](../tutorials/custom-fader.md).
- Review the [Plugin Architecture](../explanation/plugin-architecture.md) explanation for deeper understanding.
