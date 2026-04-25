---
title: Installation
description: Step by step process to install Amplitude in your machine and make the SDK available for your projects.
diataxis: how-to

---

Follow these steps to install Amplitude Audio SDK from official releases or by building from sources.

## Download from releases

!!! warning
    Amplitude Audio SDK is still in beta, so no official release is available yet. Please follow the **[Build the SDK from sources](#build-from-sources)** process instead, or grab a binary from the [nightly builds](#nightly-builds) to quickly get started.

## Nightly builds

You have access to nightly builds through [GitHub Actions](https://github.com/AmplitudeAudio/sdk/actions/workflows/build.yml?query=branch%3Adevelop++). The nightly builds are intended for development only and are not recommended for production environments.

## Build from sources

!!! warning Caution
    If you are facing issues during installation, we encourage you to [join our Discord server](https://discord.gg/QR2uBpzJ5f) and ask for support.

To build Amplitude from sources, you first need to install some dependencies:

- [XMake](https://xmake.io) - XMake is a simple and fast cross-platform build system based on Lua.
- [flatc](https://google.github.io/flatbuffers/) (optional) - `flatc` is the compiler of the Flatbuffers serialization format used by Amplitude to generate assets. This is only needed at build time if you are going to compile Amplitude with the bundled samples.

Once you have installed dependencies you can clone the repository from GitHub using `git` as follows:

```bash
git clone https://github.com/AmplitudeAudio/sdk.git
```

This will create a directory named `sdk` at the location you cloned the repository. Enter that directory and use XMake to generate build files for your system:

```bash
cd sdk
xmake f
```

??? note "Build with samples"
    You can optionally build the SDK with the bundled samples. Note that by enabling the samples, the sources will depend on `SDL2`, which will be automatically fetched for you.

    To enable the samples, add `--build_samples=y` to the previous XMake command.

Once the generation is done, you can build the SDK with the following command:

```bash
xmake b
```

And then deploy it with:

```bash
xmake i -o sdk
```

This will deploy the SDK in the same folder as the sources, in the `sdk` directory. You can change the output directory with the `-o` option.

## Install the SDK

Once you have a copy of the SDK, to install it you need to add a `AM_SDK_PATH` environment variable in your system. That environment variable should point to the path of the output directory used when deploying the SDK.

!!! info
    By installing the SDK through [Amplitude Studio](https://studio.amplitudeaudiosdk.com), the environment variable will be automatically set.

That's it! You can now use Amplitude Audio SDK in your projects!
