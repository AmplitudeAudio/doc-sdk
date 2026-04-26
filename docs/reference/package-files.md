---
title: Package Files
description: Reference for the Amplitude package file format (.ampk).
diataxis: reference
---

The `.ampk` format is Amplitude's package file format for distributing project assets. This reference documents the file structure, compression options, and runtime usage.

## Overview

An `.ampk` file is a single binary archive that contains an entire Amplitude project directory. It allows games to ship audio assets as one file instead of thousands of individual files.

| Feature | Description |
|---------|-------------|
| **Format** | Binary archive with index |
| **Compression** | None or LZ4 |
| **Block size** | Configurable (default 64 KB) |
| **Seeking** | Random access via index |
| **Platform** | All supported platforms |

## Creating Packages

Use the [`ampk`](cli-tools.md#ampk) CLI tool:

```bash
# Uncompressed (fastest loading)
ampk ./my_project/ output.ampk

# LZ4 compressed (smaller file)
ampk -c 1 -b 128 ./my_project/ output.ampk
```

## File Structure

```
AMPK Header
├── Magic number (4 bytes): "AMPK"
├── Version (2 bytes)
├── Compression mode (1 byte)
├── Block size (4 bytes)
├── Entry count (4 bytes)
│
Entry Index
├── Entry 1: path hash, offset, compressed size, uncompressed size
├── Entry 2: path hash, offset, compressed size, uncompressed size
├── ...
│
Data Blocks
├── Block 1: compressed or raw data
├── Block 2: compressed or raw data
├── ...
```

## Runtime Loading

At runtime, use `PackageFileSystem` to load assets from an `.ampk` file:

```cpp
// Create a package file system
auto packageFs = std::make_shared<PackageFileSystem>();
packageFs->SetBasePath(AM_OS_STRING("assets/audio.pak"));
packageFs->StartOpenFileSystem();
while (!packageFs->TryFinalizeOpenFileSystem())
    Thread::Sleep(1);

// Set it as the engine's file system
amEngine->SetFileSystem(packageFs);
```

The engine will then load all assets (sound banks, configs, etc.) from the package transparently.

## Compression Modes

| Mode | Value | Ratio | Decompression Speed |
|------|-------|-------|---------------------|
| Uncompressed | `0` | 1.0 | N/A (direct read) |
| LZ4 | `1` | ~2.0–3.0× | Very fast |

LZ4 is recommended for mobile and console builds where storage space is limited. Desktop builds may prefer uncompressed packages for the fastest possible load times on SSDs.

## Best Practices

- **Group projects by platform**: Create separate packages for each platform if asset sets differ.
- **Use uncompressed for streaming**: LZ4 decompression adds a small CPU cost; uncompressed is better for streamed music.

## Next Steps

- Review the [`ampk` CLI tool reference](cli-tools.md#ampk).
- Explore the [PackageFileSystem API Reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_package_file_system.md).
