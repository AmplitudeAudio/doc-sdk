---
title: Ambisonic Setup
description: Configure Ambisonic encoding, mixing, and decoding for immersive spatial audio on speakers and headphones.
---

This guide explains how to set up Ambisonic spatialization in your Amplitude project. Ambisonics is a full-sphere surround sound technique that captures and reproduces sound fields in 3D space, making it ideal for VR, AR, and multi-speaker installations.

## What is Ambisonics?

Ambisonics represents a 3D sound field using spherical harmonics. Unlike traditional channel-based audio (stereo, 5.1, 7.1), Ambisonics is **decoder-agnostic**: you encode the sound field once, then decode it for any speaker layout or headphone setup.

Amplitude supports:

- **First to third order** Ambisonics (higher order = better spatial resolution)
- **SN3D/AmbiX** normalization with ACN channel ordering
- **Binaural decoding** via HRIR convolution for headphones
- **Speaker decoding** for multi-channel setups (mono, stereo, 5.1, 7.1, cube, dodecahedron)
- **Ambisonic rotation** to follow listener head orientation

## Step 1: Choose Your Pipeline

Amplitude's default pipeline already includes Ambisonic processing. For a custom pipeline, include these nodes:

```json
{
  "id": 1,
  "name": "ambisonic_pipeline",
  "nodes": [
    { "id": 1, "name": "Input", "consume": [] },
    { "id": 2, "name": "Attenuation", "consume": [1] },
    { "id": 3, "name": "Occlusion", "consume": [2] },
    { "id": 4, "name": "StereoPanning", "consume": [2] },
    { "id": 5, "name": "AmbisonicPanning", "consume": [3] },
    { "id": 6, "name": "NearFieldEffect", "consume": [3] },
    { "id": 7, "name": "AmbisonicRotator", "consume": [5] },
    { "id": 8, "name": "AmbisonicMixer", "consume": [7] },
    { "id": 9, "name": "AmbisonicBinauralDecoder", "consume": [8] },
    { "id": 10, "name": "StereoMixer", "consume": [4, 6, 9] },
    { "id": 11, "name": "Output", "consume": [10] }
  ]
}
```

### Key Pipeline Nodes

| Node | Purpose |
|------|---------|
| `AmbisonicPanning` | Encodes a mono sound source into the Ambisonic sound field based on its 3D position. |
| `AmbisonicRotator` | Rotates the Ambisonic field to match listener head orientation. |
| `AmbisonicMixer` | Mixes multiple Ambisonic streams together. |
| `AmbisonicBinauralDecoder` | Decodes the Ambisonic field to binaural stereo using HRIR convolution. |
| `AmbisonicDecoder` | Decodes the Ambisonic field to a multi-speaker layout. |

## Step 2: Configure Sound Objects

Set the spatialization mode to `HRTF` for sounds that should be encoded into the Ambisonic field:

```json
{
  "id": 10,
  "name": "wind_ambience",
  "path": "sounds/wind.wav",
  "spatialization": "HRTF",
  "attenuation": 2,
  "bus": "ambience"
}
```

The `AmbisonicPanning` node in the pipeline will pick up these sounds and encode them into B-Format channels.

## Step 3: Configure the Engine

Ensure your engine config supports the required channel counts. For third-order Ambisonics, you need 16 channels internally:

```json
{
  "output": {
    "frequency": 48000,
    "buffer_size": 4096,
    "format": "Float32"
  },
  "mixer": {
    "panning_mode": "BinauralHighQuality",
    "active_channels": 50,
    "virtual_channels": 100,
    "pipeline": "default.ampipeline"
  },
  "hrtf": {
    "amir_file": "data/sadie_h12.amir",
    "hrir_sampling": "Bilinear"
  }
}
```

!!! note "Speaker output"
    For speaker arrays instead of headphones, set `panning_mode` to `Stereo` and use the `AmbisonicDecoder` node in your pipeline with the appropriate speaker preset.

## Step 4: Update Listeners in Your Game Loop

Ambisonic rotation requires the listener's orientation to update each frame:

```cpp
// Update listener transform
listener.SetLocation(headPosition);
listener.SetOrientation(headOrientation);

// The AmbisonicRotator node uses this orientation to rotate the sound field
```

The `AmbisonicRotator` node applies a spherical harmonic rotation matrix so that sounds appear stable in world space as the listener turns their head.

## Speaker Presets

When using `AmbisonicDecoder`, choose a speaker preset that matches your output setup:

| Preset | Channels | Description |
|--------|----------|-------------|
| `Mono` | 1 | Single speaker |
| `Stereo` | 2 | Left/right speakers |
| `Quad` | 4 | Front-left, front-right, back-left, back-right |
| `Surround_5_1` | 6 | Standard 5.1 surround |
| `Surround_7_1` | 8 | Standard 7.1 surround |
| `Cube` | 8 | Cube speaker array |
| `Dodecahedron` | 12 | Dodecahedron speaker array |
| `LebedevGrid` | Variable | Lebedev quadrature grid (variable count) |

## Shelf Filtering

Amplitude applies a shelf filter to compensate for the energy loss that occurs at higher Ambisonic orders. The `AmbisonicShelfFilter` node (included in the default pipeline) applies:

- **Max-RE weighting** for horizontal plane optimization
- **Linkwitz-Riley crossover** for smooth band splitting

This ensures that decoded audio has consistent loudness regardless of the Ambisonic order.

## B-Format Channels

Amplitude uses ACN channel ordering with SN3D normalization:

| Order | Channels | Components |
|-------|----------|------------|
| 0th | 1 | W |
| 1st | 4 | W, Y, Z, X |
| 2nd | 9 | W, Y, Z, X, V, T, R, S, U |
| 3rd | 16 | W, Y, Z, X, V, T, R, S, U, Q, O, M, K, L, N, P |

When working with external Ambisonic content, ensure it uses ACN/SN3D (AmbiX) convention. Content in FuMa or N3D format should be converted first.

## Performance Considerations

| Order | Channels | CPU Cost | Best For |
|-------|----------|----------|----------|
| 1st | 4 | Low | Mobile VR, simple scenes |
| 2nd | 9 | Medium | Desktop VR, games with moderate complexity |
| 3rd | 16 | High | High-end VR, cinematic experiences |

Higher orders improve spatial resolution but increase CPU usage for encoding, rotation, and decoding. Most games achieve excellent results with 2nd-order Ambisonics.

## Combining Ambisonics with HRTF

For headphone output, Amplitude uses **Ambisonic binauralization**: sounds are encoded into Ambisonics, rotated, and then decoded to binaural stereo via HRIR convolution. This approach has several advantages over direct HRTF panning:

- **Consistent spatial quality** regardless of source count
- **Natural blending** of multiple overlapping sources
- **Efficient rotation** (rotate the field once, not each source)
- **Support for pre-encoded Ambisonic beds** (ambient recordings, reverbs)

## Next Steps

- Review the [Pipeline Reference](../project/pipeline.md) for node configuration details.
- Learn about [HRTF setup](hrtf-setup.md) for binaural decoding.
- Explore the [AmbisonicBinauralDecoder API Reference](../api/mixer/AmbisonicBinauralDecoderNode.md).
