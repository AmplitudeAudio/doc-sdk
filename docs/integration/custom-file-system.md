---
title: Custom File System
description: Implement a custom FileSystem to load audio assets from network, archives, or proprietary storage.
---

This guide explains how to implement a custom `FileSystem` for Amplitude. A custom file system allows you to load audio assets from non-standard sources such as network streams, encrypted archives, or proprietary package formats.

## Overview

Amplitude's `FileSystem` abstraction decouples the engine from platform-specific I/O. The engine requests files through this interface, and your implementation handles the actual reading.

To create a custom file system, you need two classes:

1. **FileSystem** — Manages paths, existence checks, and file opening.
2. **File** — Represents an open file and handles read/write/seek operations.

## Step 1: Implement the File Class

Create a `File` subclass that wraps your underlying storage:

```cpp
// NetworkFile.h

#pragma once

#include <SparkyStudios/Audio/Amplitude/Amplitude.h>

using namespace SparkyStudios::Audio::Amplitude;

class NetworkFile final : public File
{
public:
    explicit NetworkFile(const AmOsString& url);
    ~NetworkFile() override;

    AmSize Read(AmUInt8Buffer buffer, AmSize bytes) override;
    AmSize Write(AmConstUInt8Buffer buffer, AmSize bytes) override;
    bool Seek(AmInt64 offset, eFileSeekOrigin origin) override;
    AmUInt64 Length() override;
    AmUInt64 Position() override;
    bool Eof() override;
    void Close() override;
    bool IsValid() override;
    AmOsString GetPath() override;

private:
    AmOsString _url;
    std::vector<AmUInt8> _data;
    AmUInt64 _position;
    bool _valid;
};
```

Implementation:

```cpp
// NetworkFile.cpp

#include "NetworkFile.h"

NetworkFile::NetworkFile(const AmOsString& url)
    : _url(url)
    , _position(0)
    , _valid(false)
{
    // Fetch the file from the network (synchronous for simplicity)
    _data = DownloadFromNetwork(url);
    _valid = !_data.empty();
}

NetworkFile::~NetworkFile()
{
    Close();
}

AmSize NetworkFile::Read(AmUInt8Buffer buffer, AmSize bytes)
{
    const AmSize remaining = _data.size() - _position;
    const AmSize toRead = AM_MIN(bytes, remaining);
    std::memcpy(buffer, _data.data() + _position, toRead);
    _position += toRead;
    return toRead;
}

AmSize NetworkFile::Write(AmConstUInt8Buffer buffer, AmSize bytes)
{
    // Read-only file system
    return 0;
}

bool NetworkFile::Seek(AmInt64 offset, eFileSeekOrigin origin)
{
    AmInt64 newPos = 0;
    switch (origin)
    {
        case eFileSeekOrigin_Start:
            newPos = offset;
            break;
        case eFileSeekOrigin_Current:
            newPos = static_cast<AmInt64>(_position) + offset;
            break;
        case eFileSeekOrigin_End:
            newPos = static_cast<AmInt64>(_data.size()) + offset;
            break;
    }
    if (newPos < 0 || newPos > static_cast<AmInt64>(_data.size()))
        return false;
    _position = static_cast<AmUInt64>(newPos);
    return true;
}

AmUInt64 NetworkFile::Length()
{
    return _data.size();
}

AmUInt64 NetworkFile::Position()
{
    return _position;
}

bool NetworkFile::Eof()
{
    return _position >= _data.size();
}

void NetworkFile::Close()
{
    _data.clear();
    _valid = false;
}

bool NetworkFile::IsValid()
{
    return _valid;
}

AmOsString NetworkFile::GetPath()
{
    return _url;
}
```

## Step 2: Implement the FileSystem Class

```cpp
// NetworkFileSystem.h

#pragma once

#include "NetworkFile.h"

class NetworkFileSystem final : public FileSystem
{
public:
    NetworkFileSystem();
    ~NetworkFileSystem() override;

    void SetBasePath(const AmOsString& basePath) override;
    const AmOsString& GetBasePath() const override;
    AmOsString ResolvePath(const AmOsString& path) const override;
    bool Exists(const AmOsString& path) const override;
    bool IsDirectory(const AmOsString& path) const override;
    AmOsString Join(const std::vector<AmOsString>& parts) const override;
    std::shared_ptr<File> OpenFile(const AmOsString& path, eFileOpenMode mode) const override;
    void StartOpenFileSystem() override;
    bool TryFinalizeOpenFileSystem() override;
    void StartCloseFileSystem() override;
    bool TryFinalizeCloseFileSystem() override;

private:
    AmOsString _basePath;
};
```

## Step 3: Register the File System

```cpp
#include "NetworkFileSystem.h"

int main()
{
    MemoryManager::Initialize();

    // Create and open the custom file system
    auto fs = std::make_shared<NetworkFileSystem>();
    fs->SetBasePath(AM_OS_STRING("https://assets.mygame.com/audio/"));
    fs->StartOpenFileSystem();
    while (!fs->TryFinalizeOpenFileSystem())
        Thread::Sleep(1);

    // Set it as the engine's file system
    amEngine->SetFileSystem(fs);

    // Continue with engine initialization...
}
```

## Async File Operations

Amplitude supports asynchronous file system open/close to prevent blocking the main thread:

```cpp
// Initiate the open operation
fs->StartOpenFileSystem();

// Poll until complete
while (!fs->TryFinalizeOpenFileSystem())
    Thread::Sleep(1);
```

For file reads, the engine supports async open/close via `StartOpenFile()` / `TryFinalizeOpenFile()` if your `FileSystem` implements them. The base `FileSystem` class provides default synchronous implementations.

## Built-in File Systems

Amplitude includes several built-in file system implementations:

| FileSystem | Description | Use Case |
|------------|-------------|----------|
| `DiskFileSystem` | Standard OS file I/O | Desktop and mobile default |
| `PackageFileSystem` | Reads from `.ampk` packages | Distributed builds |
| `MemoryFileSystem` | In-memory buffers | Tests, procedurally generated data |
| `AndroidAssetManagerFileSystem` | Android `AAssetManager` | Android native apps |
| `NSFileSystem` | iOS `NSBundle` | iOS native apps |

## Best Practices

- **Implement `IsValid()` accurately**: The engine relies on this to detect failed opens.
- **Support seeking**: Codecs need to seek for streaming and loop support.
- **Use async initialization**: `StartOpenFileSystem()` / `TryFinalizeOpenFileSystem()` prevents frame hitches.
- **Cache when possible**: Network and archive file systems benefit from aggressive caching.
- **Thread safety**: `File::Read()` may be called from the audio thread during streaming. Ensure your implementation is thread-safe or copy data during `OpenFile()`.

## Next Steps

- Review the [FileSystem API Reference](../api/io/FileSystem.md).
- Learn how to use the [PackageFileSystem](../api/io/PackageFileSystem.md) for `.ampk` files.
- Explore the [DiskFileSystem API Reference](../api/io/DiskFileSystem.md) for the default implementation.
