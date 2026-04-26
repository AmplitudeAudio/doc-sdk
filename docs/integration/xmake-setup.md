---
title: XMake Setup
description: Integrate Amplitude into any XMake-based project through the official xrepo package repository.
diataxis: how-to
---

!!! note
    Make sure you have followed the [installation instructions](../getting-started/installation.md) first. If you encounter problems, please ask for support in our [Discord server](https://discord.gg/QR2uBpzJ5f).

The Amplitude Audio SDK and its official plugins are published as [XMake](https://xmake.io) packages through a dedicated repository at [`AmplitudeAudio/repo-xmake`](https://github.com/AmplitudeAudio/repo-xmake). The repository ships:

| Package                       | Purpose                                |
| ----------------------------- | -------------------------------------- |
| `amplitudeaudiosdk`           | The core Amplitude Audio SDK.          |
| `amplitude-plugin-vorbis`     | Official Vorbis/OGG codec plugin.      |
| `amplitude-plugin-flac`       | Official FLAC codec plugin.            |
| `amplitude-plugin-profiler`   | Official profiler plugin.              |

## Register the repository

Add the repository to `xrepo` once per machine using the `xrepo` CLI:

```bash
xrepo add-repo amplitudeaudio https://github.com/AmplitudeAudio/repo-xmake
```

Or, for a project-local registration, declare the repository directly in your `xmake.lua`:

```lua
add_repositories("amplitudeaudio https://github.com/AmplitudeAudio/repo-xmake")
```

## Require the SDK in your project

Add the SDK as a project requirement in `xmake.lua`:

```lua
add_requires("amplitudeaudiosdk")
```

You can also pin a specific version, or override the default `shared` library configuration:

```lua
-- Pin a specific version
add_requires("amplitudeaudiosdk 1.0.0")

-- Build as a static library (disables runtime plugin loading)
add_requires("amplitudeaudiosdk", { configs = { shared = false } })
```

!!! warning
    Linking against the static library prevents the engine from loading plugins at runtime. Use the default `shared` configuration if your project needs dynamic plugin loading (e.g. the official Vorbis or FLAC codecs).

Then attach the package to the targets that need it:

```lua
target("my_game")
    set_kind("binary")
    add_files("src/*.cpp")
    add_packages("amplitudeaudiosdk")
```

## Add official plugins

Plugins follow the same flow. Declare them in `add_requires` and link them into the targets that should ship them:

```lua
add_requires("amplitudeaudiosdk", "amplitude-plugin-vorbis", "amplitude-plugin-flac")

target("my_game")
    set_kind("binary")
    add_files("src/*.cpp")
    add_packages("amplitudeaudiosdk", "amplitude-plugin-vorbis", "amplitude-plugin-flac")
```

At runtime you still need to call `Engine::LoadPlugin()` for each plugin (see [Dynamic Plugins](dynamic-plugins.md)).

## Install on demand without xmake.lua

If you only want the SDK headers and binaries on disk (for use with another build system or for inspection), install the package directly:

```bash
xrepo install amplitudeaudiosdk
```

`xrepo` resolves dependencies, builds the package for the current platform, and prints the install location. Use `xrepo --help install` for arch / mode / config flags.

## Upgrade or rebuild

When the repository ships a new version, refresh your local cache and rebuild:

```bash
xrepo update-repo
xmake require --upgrade amplitudeaudiosdk
```

## See also

- [CMake Setup](cmake-setup.md) — the equivalent flow for CMake-based projects.
- [Initializing the Engine](initializing-the-engine.md) — the next step after the SDK is linked.
- [Dynamic Plugins](dynamic-plugins.md) — how to load codec and DSP plugins at runtime.
