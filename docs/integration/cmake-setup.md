---
title: CMake Setup
description: Amplitude provides scripts to quickly be integrated in any CMake-based projects.
---

!!! note
    Make sure you followed the [installation instructions](../getting-started/installation.md) first before to continue this setup. If you encounter problems, please ask for support in our [Discord server](https://discord.gg/QR2uBpzJ5f).

After the SDK has been successfully installed, it can be used into any CMake-based projects. You should make sure the `AM_SDK_PATH` environment variable is set before to configure your project. If not, you can manually set it as a CMake variable using the CLI:

```bash
cmake -DAM_SDK_PATH=/path/to/amplitude/sdk -S /path/to/sources -B /path/to/build
```

Or directly in your `CMakeLists.txt` file:

```cmake
set(AM_SDK_PATH "/path/to/amplitude" CACHE PATH "The path to Amplitude Audio SDK libraries.")
```

After the `AM_SDK_PATH` variable is set, you should add the path to CMake scripts provided by the SDK to the current `CMAKE_MODULE_PATH` variable. For example:

```cmake
# If using the environment variable
list(APPEND CMAKE_MODULE_PATH "$ENV{AM_SDK_PATH}/cmake")

# If using the CMake variable
list(APPEND CMAKE_MODULE_PATH "${AM_SDK_PATH}/cmake")
```

This will make available the `FindAmplitudeAudioSDK.cmake` and the `DetectAmplitudeVersion.cmake` scripts.

You can now call the `find_package` CMake function to make the SDK libraries available to your project:

```cmake
find_package(AmplitudeAudioSDK REQUIRED)
```

The script will try to automatically detect your platform. If you want to set the platform yourself, you can use the `AM_SDK_PLATFORM` CMake variable with the following values:

- `x64-windows`
- `x64-linux`
- `x64-osx`
- `arm64-osx`

For vcpkg users, it's preferred to let Amplitude use the same vcpkg triplet as the project. This can be done in the `CMakeLists.txt` file:

```cmake
set(AM_SDK_PLATFORM ${VCPKG_TARGET_TRIPLET} CACHE STRING "The platform to use for the Amplitude Audio SDK libraries.")
```

!!! warning
    If defined, the `AM_SDK_PLATFORM` variable should be set before to call the CMake `find_package` function.

!!! info
    You have to make sure your SDK installation have the libraries for the requested platform.

After the call to `find_package`, 2 libraries will be available:

- `SparkyStudios::Audio::Amplitude::SDK::Shared`: Amplitude Audio SDK as a shared library. You can link to this library if you intend to use plugins, or you don't want static linking.
- `SparkyStudios::Audio::Amplitude::SDK::Static`: Amplitude Audio SDK as a static library. Linking to this library will make your project unable to load plugins at runtime, as they need dynamic linking to work properly.

You just have to pick the one which suits the best to your needs and link your project with it:

```cmake
# Shared library
target_link_libraries(my_project
    PRIVATE SparkyStudios::Audio::Amplitude::SDK::Shared
)

# Static library
target_link_libraries(my_project
    PRIVATE SparkyStudios::Audio::Amplitude::SDK::Static
)
```

Now you can use the SDK in your project!
