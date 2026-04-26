---
title: HRTF Setup
description: Configure Head-Related Transfer Function (HRTF) spatialization for immersive 3D binaural audio.
diataxis: how-to
---

This guide explains how to set up HRTF (Head-Related Transfer Function) spatialization in your Amplitude project for immersive 3D binaural audio. HRTF uses measured or simulated impulse responses from human ears to reproduce spatial audio over standard stereo headphones.

## Prerequisites

Before you begin, ensure you have:

- Amplitude Audio SDK v1.0 or later
- An `.amir` HRIR sphere file (see [Generating an AMIR file](#step-1-generate-or-obtain-an-amir-file))
- Headphones for testing (HRTF is optimized for headphone playback)

## What is HRTF?

HRTF captures how sound waves interact with the human head, torso, and pinnae (outer ears) as they travel from a sound source to each ear. By convolving audio with these direction-specific impulse responses, Amplitude can create a convincing 3D audio experience using only two audio channels.

Amplitude supports multiple HRIR datasets:

| Dataset | Description | Source |
|---------|-------------|--------|
| **IRCAM** | LISTEN database with multiple subjects | [IRCAM](http://recherche.ircam.fr/equipes/salles/listen/download.html) |
| **MIT** | KEMAR dummy head measurements | [MIT Media Lab](http://sound.media.mit.edu/resources/KEMAR.html) |
| **SADIE** | Spatial Audio Database with high resolution | [University of York](https://www.york.ac.uk/sadie-project/database.html) |
| **SOFA** | Custom measurements in SOFA format | [SOFA Conventions](https://www.sofaconventions.org/) |

## Step 1: Generate or Obtain an AMIR File

Amplitude uses its own optimized `.amir` format for HRIR data. You can generate one from supported datasets using the `amir` CLI tool:

```bash
# Convert a SOFA file to AMIR (model 3 = SOFA)
amir -m 3 input.sofa output.amir

# Convert IRCAM data to AMIR (model 0 = IRCAM)
amir -m 0 /path/to/ircam/ output.amir

# Resample to a target sample rate during conversion (model 1 = MIT)
amir -m 1 -r 48000 /path/to/mit_kemar/ output.amir
```

The `amir` tool will:

1. Read the HRIR dataset
2. Compute interaural time differences (ITD)
3. Triangulate the sphere mesh
4. Output an optimized `.amir` file for runtime use

!!! tip "Sample rate matching"
    For best performance, generate the `.amir` file at the same sample rate as your engine output (e.g., 48000 Hz). Mismatched sample rates will trigger runtime resampling.

## Step 2: Configure the Engine

Add the HRTF section to your engine configuration file:

```json
{
  "driver": "miniaudio",
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

### Configuration Options

| Option | Values | Description |
|--------|--------|-------------|
| `amir_file` | File path | Path to the `.amir` HRIR sphere file. |
| `hrir_sampling` | `NearestNeighbor`, `Bilinear` | Sampling method for HRIR lookup. `Bilinear` is smoother but slightly more expensive. |

### Panning Modes

Choose a binaural panning mode in the mixer configuration:

| Mode | Description | Use Case |
|------|-------------|----------|
| `Stereo` | Standard stereo panning | Speakers, no spatialization |
| `BinauralLowQuality` | Fast HRTF with lower accuracy | Performance-constrained devices |
| `BinauralMediumQuality` | Balanced quality and speed | Mobile devices |
| `BinauralHighQuality` | Full HRTF convolution | Desktop, high-end experiences |

## Step 3: Configure Sound Objects for HRTF

Ensure your sound objects use `HRTF` spatialization:

```json
{
  "id": 10,
  "name": "footsteps",
  "path": "sounds/footsteps.wav",
  "spatialization": "HRTF",
  "attenuation": 1
}
```

Available spatialization modes:

| Mode | Description |
|------|-------------|
| `None` | No spatialization; same gain for all channels. |
| `Position` | 2D position-based panning. |
| `PositionOrientation` | 2D position and orientation panning. |
| `HRTF` | Full 3D binaural spatialization using the HRIR sphere. |

## Step 4: Set Up Listeners and Entities

HRTF spatialization depends on accurate listener and entity positions. Ensure your game updates these each frame:

```cpp
// Update listener position and orientation
listener.SetLocation(playerPosition);
listener.SetOrientation(playerOrientation);

// Update entity (sound source) position
entity.SetLocation(enemyPosition);
entity.SetOrientation(enemyOrientation);

// Optional: set directivity for more realistic radiation patterns
entity.SetDirectivity(0.5f, 2.0f);
```

## Step 5: Verify the Pipeline

The default pipeline includes HRTF processing through the `AmbisonicBinauralDecoder` node. If you are using a custom pipeline, ensure it includes the necessary nodes:

```json
{
  "id": 1,
  "name": "hrtf_pipeline",
  "nodes": [
    { "id": 1, "name": "Input", "consume": [] },
    { "id": 2, "name": "Attenuation", "consume": [1] },
    { "id": 3, "name": "AmbisonicPanning", "consume": [2] },
    { "id": 4, "name": "AmbisonicRotator", "consume": [3] },
    { "id": 5, "name": "AmbisonicBinauralDecoder", "consume": [4] },
    { "id": 6, "name": "Output", "consume": [5] }
  ]
}
```

## Runtime API

You can query and configure HRTF settings at runtime:

```cpp
// Get the current HRIR sphere (returns std::shared_ptr<const HRIRSphere>)
auto sphere = amEngine->GetHRIRSphere();

// Check if the sphere is loaded
if (sphere != nullptr && sphere->IsLoaded())
{
    amLogInfo("HRIR sphere loaded with %u vertices", sphere->GetVertexCount());
}

// Query the current sampling mode
eHRIRSphereSamplingMode mode = amEngine->GetHRIRSphereSamplingMode();
```

## Performance Considerations

| Factor | Impact | Recommendation |
|--------|--------|----------------|
| HRIR length | Longer IRs = more convolution CPU cost | Use 128–512 sample IRs for games |
| Vertex count | More vertices = smoother spatialization | 1000–5000 vertices is usually sufficient |
| Sampling mode | `Bilinear` is ~2× more expensive than `NearestNeighbor` | Use `NearestNeighbor` on mobile |
| Panning mode | `BinauralHighQuality` applies full convolution | Use `BinauralMediumQuality` for 20+ simultaneous sources |

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| No spatialization | `spatialization` set to `None` or `Position` | Change to `HRTF` in the sound asset |
| Flat sound | `panning_mode` set to `Stereo` | Change to `BinauralHighQuality` |
| Crackling | HRIR sample rate mismatches output rate | Regenerate `.amir` at the engine output sample rate |
| Front/back confusion | HRIR dataset lacks elevation resolution | Use SADIE or high-resolution SOFA data |

## Next Steps

- Learn about [ambisonic spatialization](ambisonic-setup.md) for speaker-based VR setups.
- Explore the [HRIRSphere API Reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_h_r_i_r_sphere.md).
- Learn how to build custom HRIR datasets with the [`amir` CLI tool](../reference/cli-tools.md#amir).
