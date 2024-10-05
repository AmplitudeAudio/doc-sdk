---
title: Initializing the Engine
description: Learn how to initialize the Amplitude Engine with a given project at runtime through this tutorial.
menu:
  docs:
    parent: integration
weight: 203
toc: true
---

!!! note
    You will need to have an Amplitude project to follow these instructions. Please read the [project setup](../project/project-architecture.md) documentation to create a project. You can also get one of the [sample projects](https://github.com/AmplitudeAudio/sdk/tree/develop/samples) provided in the GitHub repository.

Amplitude is built with several components, which should be initialized separately before to start playing audio or interacting with your game.

## Logger

Amplitude comes with a default [`ConsoleLogger`](../api/core/ConsoleLogger/index.md) and a set of shortcut macros for you to use. You are able to change the default logger by implementing the [`Logger`](../api/core/Logger/index.md) interface.

```cpp
// Implement the Logger interface
class MyLogger : public Logger
{
protected:
  void Log(LogMessageLevel level, const char* file, int line, const AmString& message) override
  {
    // Write the log message where you want here, maybe a file, or a network buffer
  }
};

// Create a global instance to your logger class
MyLogger gLogger;

// Set your logger as the default one
Logger::SetDefault(&gLogger);
```

Setting the logger is optional, as it is not a required component. But if you want to use it, it is usually better to initialize it first, as it is used in every part of the SDK.

## MemoryManager

The memory manager is the first **required** component to initialize. It is responsible for all the allocations occurring in the SDK (even the ones due to other components' initialization), and in your application.

While initializing the memory manager, you can customize the allocation functions through the `MemoryManagerConfig` structure. You should either set all the functions, or none of them.

A typical memory manager initialization code will look like this:

```cpp
#include <SparkyStudios/Audio/Amplitude/Amplitude.h>

using namespace SparkyStudios::Audio::Amplitude;

int main(int argc, char* argv[])
{
  // Initialize the memory manager
  // Note that for custom configs, all the functions should be defined
  MemoryManagerConfig config{};
  // config.alignedMalloc = my_malign;
  // config.alignedRealloc = my_realign;
  // config.free = my_free;
  // config.malloc = my_malloc;
  // config.realloc = my_realloc;
  // config.sizeOf = my_sizeof;
  // config.totalReservedMemorySize = my_total_mem_size;
  MemoryManager::Initialize(config); // Using the memory manager configuration.

  // ... your code ...

  MemoryManager::Deinitialize();

  return 0;
}
```

## FileSystem

The file system component is responsible to read/write resources as needed by the SDK. Amplitude comes shipped with a `DiskFileSystem` implementation allowing you to access files on disk, and a `PackageFileSystem` implementation allowing you to read files bundled in an Amplitude Package file (`.ampk`). You can easily create your own file system implementation to fit your needs (eg: accessing assets from the network).

The used file system implementation should be set as the default one in the engine after the initialization. For example, if you use the `DiskFileSystem` implementation, a typical usage will look like:

```cpp
DiskFileSystem fs;
fs.SetBasePath(AM_OS_STRING("./my_project")); // Set the base path of the file system. For the DiskFileSystem, this path is the path to your Amplitude project build files.

amEngine->SetFileSystem(&fs); // Set the file system implementation to use in the engine.
```

According to the implementation, the file system may be opened in a background thread to do an heavy operation (eg: unpacking an archive). If it's the case for you, it is necessary to wait for the file system to load before to continue. You can do this using the following code:

```cpp
// Open the file system
amEngine->StartOpenFileSystem();
while (!amEngine->TryFinalizeOpenFileSystem()) // While the file system is still opening
    Thread::Sleep(1); // Wait for the file system to open
```

The process is similar if you want to close your file system after the engine is being deinitialized or your application
is being closed:

```cpp
// Close the file system
amEngine->StartCloseFileSystem();
while (!amEngine->TryFinalizeCloseFileSystem()) // While the file system is still closing
    Thread::Sleep(1); // Wait for the file system to close
```

## Plugins

Plugins allow you to extend the functionalities of the engine (eg: adding codecs, filters, faders, pipeline nodes, etc...), and therefore, they should be loaded before the engine itself is initialized.

Amplitude comes shipped with some default plugins you may enable if necessary. To do so, you should call the following
function:

```cpp
// Register all the default plugins shipped with the engine
Engine::RegisterDefaultPlugins();
```

!!! info
    Unless you are not going to use any of the bundled features of the engine, it is **highly** recommended enabling default plugins.

You are also able to create custom plugins, and build them as shared libraries for use in your applications. These libraries are loaded dynamically at runtime by the engine.

!!! warning
    If using custom/external plugins, you **must** link Amplitude as a shared library to your program. Otherwise, your program and plugins won't share the same memory space, and plugins won't work properly.

The SDK allows you to set the paths in which to search for external plugins:

```cpp
// The path is relative to the working directory, which is usually the same path as the executable.
Engine::AddPluginSearchPath(AM_OS_STRING("./my_project/plugins"));
```

You must add all the search paths before to load plugins, as you cannot load a plugin using a path, either relative or absolute.

!!! info
    By default, the engine will search first in the working directory **before** to look in the added search paths.

Once the search paths have been added, the engine can now load your plugins:

```cpp
Engine::LoadPlugin(AM_OS_STRING("AmplitudeVorbisCodecPlugin")); // Official plugin for Vorbis/OGG codec
Engine::LoadPlugin(AM_OS_STRING("MyCustomPlugin")); // Any other awesome plugin you will build
```

!!! info
    Note that plugins are loaded using their canonical name, without prefix (eg: `lib` on UNIX platforms) and without extension (eg: `.dll` on Windows platforms). Amplitude will add them for you automatically.

## Amplitude Engine

The Amplitude engine is initialized with a specific configuration, from the ones available in your Amplitude project:

```cpp
// The path to the configuration file is relative to the base path of the file system
if (!amEngine->Initialize(AM_OS_STRING("./pc.config.amconfig")))
  return 1; // There is usually nothing more to do if the engine has failed initializing...
```

Once the engine is initialized, you can start to interact with audio files and with your loaded Amplitude project.

## Wrapping Up

A full example of the SDK initialization may look like this:

```cpp {title="main.cpp"}
#include <SparkyStudios/Audio/Amplitude/Amplitude.h>

using namespace SparkyStudios::Audio::Amplitude;

// Implement the Logger interface
class MyLogger : public Logger
{
protected:
  void Log(LogMessageLevel level, const char* file, int line, const AmString& message) override
  {
    // Write the log message where you want here, maybe a file, or a network buffer
  }
};

// Create a global instance to your logger class
MyLogger gLogger;

int main(int argc, char* argv[])
{
  // Set your logger as the default one
  Logger::SetDefault(&gLogger);

  // Initialize the memory manager
  // Note that for custom configs, all the functions should be set if one of them is specified
  MemoryManagerConfig config{};
  // config.alignedMalloc = my_malign;
  // config.alignedRealloc = my_realign;
  // config.free = my_free;
  // config.malloc = my_malloc;
  // config.realloc = my_realloc;
  // config.sizeOf = my_sizeof;
  // config.totalReservedMemorySize = my_total_mem_size;
  MemoryManager::Initialize(config); // Using the memory manager configuration.

  DiskFileSystem fs;

  // Set the base path of the file system. Usually the path to your Amplitude project.
  fs.SetBasePath(AM_OS_STRING("./my_project"));

  // Set the file system implementation to use in the engine.
  amEngine->SetFileSystem(&fs);

  // Open the file system
  amEngine->StartOpenFileSystem();
  while (!amEngine->TryFinalizeOpenFileSystem()) // While the file system is still opening
      Thread::Sleep(1); // Wait for the file system to open

  // Register all the default plugins shipped with the engine
  Engine::RegisterDefaultPlugins();

  // The path is relative to the working directory, which is usually the same path as the executable.
  Engine::AddPluginSearchPath(AM_OS_STRING("./my_project/plugins"));

  Engine::LoadPlugin(AM_OS_STRING("AmplitudeVorbisCodecPlugin")); // Official plugin for Vorbis/OGG codec
  Engine::LoadPlugin(AM_OS_STRING("MyCustomPlugin")); // Any other awesome plugin you will build

  // The path to the configuration file is relative to the base path of the file system
  if (amEngine->Initialize(AM_OS_STRING("./pc.config.amconfig")))
  {
    // ... Can now play audio files and access project data ...

    // Deinitialize the Amplitude engine
    amEngine->Deinitialize();
  }

  // Close the file system
  amEngine->StartCloseFileSystem();
  while (!amEngine->TryFinalizeCloseFileSystem()) // While the file system is still closing
      Thread::Sleep(1); // Wait for the file system to close

  // Unregister all default plugins
  Engine::UnregisterDefaultPlugins();

  // Destroy the Amplitude engine instance
  amEngine->DestroyInstance();

  // Deinitialize the memory manager
  MemoryManager::Deinitialize();

  return 0;
}
```
