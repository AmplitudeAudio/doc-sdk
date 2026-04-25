---
title: AMS Codec
description: Reference for the Amplitude Media Stream (AMS) ADPCM compression format.
---

The AMS (Amplitude Media Stream) codec is Amplitude's custom audio compression format. It provides a good balance between compression ratio, decode speed, and audio quality for game sound effects and music.

## Overview

| Property | Value |
|----------|-------|
| **Algorithm** | ADPCM (Adaptive Differential Pulse-Code Modulation) |
| **Compression** | ~4:1 vs 16-bit PCM |
| **Decode speed** | Very fast (single multiply-accumulate per sample) |
| **Seeking** | Sample-accurate |
| **Bit depth** | 16-bit equivalent |

## Encoding

Use the [`amac`](cli-tools.md#amac) CLI tool to create AMS files:

```bash
# Basic encoding
amac -e input.wav output.ams

# High quality with increased look-ahead
amac -e --look-ahead 5 input.wav output.ams

# Disable noise shaping (faster encode, slightly lower quality)
amac -e --no-noise-shaping input.wav output.ams

# Custom block size
amac -e --block-size-shift 2 input.wav output.ams
```

### Encoding Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `look-ahead` | `3` | Number of samples to look ahead for better prediction. Higher values improve quality at the cost of encode time. |
| `noise-shaping` | Enabled | Applies noise shaping to push quantization error into less audible frequencies. |
| `block-size-shift` | `0` | Controls the ADPCM block size as a power-of-two shift. Larger blocks improve compression but reduce seek granularity. |
| `resample` | Disabled | Resamples the input to a target sample rate before encoding. |

## Decoding

The AMS decoder is included in Amplitude by default. It is automatically selected for files with the `.ams` extension.

```json
{
  "id": 1,
  "name": "compressed_sfx",
  "path": "sounds/explosion.ams"
}
```

## File Format

The AMS file format consists of:

```
AMS Header
├── Magic number (4 bytes): "AMS\0"
├── Version (2 bytes)
├── Sample rate (4 bytes)
├── Channels (2 bytes)
├── Bits per sample (2 bytes)
├── Total frames (8 bytes)
├── Block size (4 bytes)
├── Look-ahead (4 bytes)
│
ADPCM Blocks
├── Block 1: predictor state + compressed samples
├── Block 2: predictor state + compressed samples
├── ...
```

Each block starts with a fresh predictor state, allowing sample-accurate seeking to any block boundary.

## Performance

| Operation | Relative Cost |
|-----------|---------------|
| AMS decode | ~1.5× faster than MP3 decode |
| AMS decode | ~10× faster than Vorbis decode |
| AMS encode | ~5× faster than Vorbis encode |

The decode speed makes AMS ideal for games with many simultaneous sounds or tight CPU budgets.

## Quality

AMS is a lossy format. The quality is comparable to:

- **IMA ADPCM** (similar algorithm, but AMS uses improved prediction)
- **Low-bitrate MP3** (~96–128 kbps for music)

AMS is **not** suitable for:

- Professional music mastering (use uncompressed WAV)
- Content requiring transparent quality (use FLAC or WAV)
- Heavy transient material (drums, impacts may show artifacts)

## When to Use AMS

| Use Case | Recommendation |
|----------|---------------|
| Sound effects (gunshots, UI) | ✅ Excellent |
| Ambient loops | ✅ Good |
| Music (mobile) | ✅ Acceptable |
| Music (desktop/console) | ⚠️ Consider FLAC or uncompressed |
| Voice/dialogue | ✅ Good |

## Next Steps

- Use [`amac`](cli-tools.md#amac) to encode your audio.
- Learn about the [built-in codecs](codecs.md) for other format options.
