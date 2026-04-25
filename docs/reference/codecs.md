---
title: Built-in Codecs
description: Reference for the audio codecs included with the Amplitude Audio SDK.
diataxis: reference

---

This reference documents the audio codecs built into the Amplitude Audio SDK, including supported formats, capabilities, and usage notes.

## Overview

Amplitude includes three built-in codecs. Additional codecs are available via plugins.

| Codec | Extension | Decoding | Encoding | Streaming | Description |
|-------|-----------|----------|----------|-----------|-------------|
| **WAV** | `.wav` | ✅ | ✅ | ✅ | PCM and IEEE float formats via dr_wav |
| **MP3** | `.mp3` | ✅ | ❌ | ✅ | MPEG-1/2 Audio Layer III via dr_mp3 |
| **AMS** | `.ams` | ✅ | ✅ | ✅ | Amplitude's custom ADPCM compression |

## WAV Codec

The WAV codec supports standard RIFF/WAVE files via the [dr_wav](https://github.com/mackron/dr_libs) library.

### Supported Formats

| Format | Bits Per Sample | Notes |
|--------|-----------------|-------|
| PCM | 8, 16, 24, 32 | Integer PCM |
| IEEE Float | 32 | Floating-point samples |

### Behavior

- Decoded audio is always converted to **32-bit float** (`eAudioSampleFormat_Float32`) internally.
- The codec supports both full `Load()` and streaming `Stream()` modes.
- IMA/DVI ADPCM WAV files are **not** handled by the WAV codec; they are routed to the AMS codec.

### Usage

```json
{
  "id": 1,
  "name": "gunshot",
  "path": "sounds/gunshot.wav"
}
```

## MP3 Codec

The MP3 codec supports MPEG-1/2 Audio Layer III decoding via [dr_mp3](https://github.com/mackron/dr_libs).

### Supported Formats

| Format | Notes |
|--------|-------|
| MPEG-1 Layer III | Standard MP3 |
| MPEG-2 Layer III | Lower sample rates |

### Behavior

- Decoded audio is always converted to **32-bit float** internally.
- Supports streaming for long music tracks.
- **Encoding is not supported.** Use external tools to create MP3 files.

### Usage

```json
{
  "id": 2,
  "name": "music_track",
  "path": "music/background.mp3",
  "stream": true
}
```

## AMS Codec

The AMS (Amplitude Media Stream) codec is Amplitude's custom ADPCM compression format. It provides a good balance between compression ratio and decoding speed.

### Features

| Feature | Description |
|---------|-------------|
| Compression | ~4:1 over 16-bit PCM |
| Decode speed | Very fast (simple ADPCM predictor) |
| Seeking | Sample-accurate |
| Bit depth | 16-bit equivalent quality |

### Creating AMS Files

Use the [`amac`](cli-tools.md#amac) CLI tool to encode WAV or MP3 to AMS:

```bash
amac -e input.wav output.ams
```

### Behavior

- The AMS codec uses a look-ahead buffer and optional noise shaping for improved quality.
- Block size is configurable at encode time.
- Supports both loading and streaming.

### Usage

```json
{
  "id": 3,
  "name": "compressed_ambience",
  "path": "sounds/ambience.ams",
  "stream": true
}
```

## Plugin Codecs

Additional codecs are available as plugins:

| Plugin | Format | Repository |
|--------|--------|------------|
| Vorbis | OGG Vorbis | [plugin-vorbis](https://github.com/AmplitudeAudio/plugin-vorbis) |
| FLAC | FLAC | [plugin-flac](https://github.com/AmplitudeAudio/plugin-flac) |

Plugin codecs are loaded dynamically at runtime:

```cpp
Engine::LoadPlugin(AM_OS_STRING("vorbis_plugin"));
```

## Codec Selection at Runtime

When loading a sound file, Amplitude automatically selects the appropriate codec based on the file extension and the `CanHandleFile()` check:

1. The engine queries each registered codec's `CanHandleFile()` method.
2. The first codec that returns `true` handles the file.
3. If no codec matches, the load fails with `eErrorCode_FileLoadFailed`.

Registration order matters if multiple codecs claim the same extension. Register your custom codecs after the built-in ones if you want to override behavior.

## Memory Pools

All codec allocations use the `eMemoryPoolKind_Codec` memory pool:

```cpp
// Good: pool-aware allocation inside your codec
void* buffer = ampoolmalloc(eMemoryPoolKind_Codec, size);
```

This allows the engine to track codec memory usage and enforce budgets in future versions.

## Next Steps

- Learn how to write a [custom codec](../tutorials/custom-codec.md).
- Review the [Codec API Reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_codec.md).
- Explore the [AMS codec tool](cli-tools.md#amac).
