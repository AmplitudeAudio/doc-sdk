---
title: Built-in Pipeline Nodes
description: Reference for all built-in nodes available in the Amplimix audio processing pipeline.
diataxis: reference

---

This reference documents every built-in pipeline node in the Amplitude Audio SDK. Pipeline nodes are the building blocks of the audio processing graph executed by Amplimix each frame.

## Node Categories

All nodes fall into one of four categories:

| Category | Description |
|----------|-------------|
| **Input** | Marks the entry point of audio into the pipeline. |
| **Output** | Marks the exit point of processed audio. |
| **Processor** | Transforms audio in-place (single input, single output). |
| **Mixer** | Combines multiple inputs into one output. |

## Input / Output

### InputNode

Marks the start of the pipeline. Receives audio from the sound source.

```json
{ "id": 1, "name": "Input", "consume": [] }
```

### OutputNode

Marks the end of the pipeline. Sends audio to the audio device.

```json
{ "id": 99, "name": "Output", "consume": [98] }
```

## Spatial Nodes

### AttenuationNode

Applies distance-based gain attenuation using the sound's assigned attenuation model.

| Parameter | Type | Description |
|-----------|------|-------------|
| `attenuation` | float | Output gain after applying the curve (read-only). |

```json
{ "id": 2, "name": "Attenuation", "consume": [1] }
```

### StereoPanningNode

Pans mono sources to stereo left/right based on azimuth angle.

```json
{ "id": 3, "name": "StereoPanning", "consume": [2] }
```

### AmbisonicPanningNode

Encodes a mono source into Ambisonic B-Format channels based on 3D position.

```json
{ "id": 4, "name": "AmbisonicPanning", "consume": [2] }
```

### AmbisonicRotatorNode

Rotates the Ambisonic sound field to match listener orientation.

```json
{ "id": 5, "name": "AmbisonicRotator", "consume": [4] }
```

### AmbisonicBinauralDecoderNode

Decodes Ambisonic B-Format to binaural stereo using HRIR convolution.

```json
{ "id": 6, "name": "AmbisonicBinauralDecoder", "consume": [5] }
```

### AmbisonicMixerNode

Mixes multiple Ambisonic streams together.

```json
{ "id": 7, "name": "AmbisonicMixer", "consume": [5, 10] }
```

### StereoMixerNode

Mixes multiple stereo streams together.

```json
{ "id": 8, "name": "StereoMixer", "consume": [3, 6] }
```

## Effect Nodes

### EnvironmentEffectNode

Applies the environment's assigned effect to sounds inside the zone.

```json
{ "id": 9, "name": "EnvironmentEffect", "consume": [2] }
```

### NearFieldEffectNode

Simulates near-field pressure effects for very close sources.

```json
{ "id": 10, "name": "NearFieldEffect", "consume": [2] }
```

### ReflectionsNode

Computes early reflections based on room geometry.

```json
{ "id": 11, "name": "Reflections", "consume": [1] }
```

### ReverbNode

Applies late reverberation based on room materials and dimensions.

```json
{ "id": 12, "name": "Reverb", "consume": [1] }
```

## Occlusion / Obstruction

### OcclusionNode

Applies frequency-dependent low-pass filtering based on the entity's occlusion value.

```json
{ "id": 13, "name": "Occlusion", "consume": [2] }
```

### ObstructionNode

Applies low-pass filtering based on the entity's obstruction value.

```json
{ "id": 14, "name": "Obstruction", "consume": [2] }
```

## Dynamics Nodes

### LimiterNode

Prevents clipping by limiting peak amplitude.

| Parameter | Type | Description |
|-----------|------|-------------|
| `threshold` | dB | Level above which limiting begins. |
| `attack` | ms | Time to respond to peaks. |
| `release` | ms | Time to return to unity gain. |

```json
{ "id": 15, "name": "Limiter", "consume": [8] }
```

### ClampNode

Hard-clips samples to a maximum amplitude.

```json
{ "id": 16, "name": "Clamp", "consume": [15] }
```

### HardClipNode

Applies aggressive hard clipping (distortion).

```json
{ "id": 17, "name": "HardClip", "consume": [15] }
```

### RoundoffClipNode

Applies softer roundoff clipping.

```json
{ "id": 18, "name": "RoundoffClip", "consume": [15] }
```

## Default Pipeline

The default pipeline shipped with Amplitude combines most of these nodes:

```json
{
  "id": 1,
  "name": "default",
  "nodes": [
    { "id": 1, "name": "Input", "consume": [] },
    { "id": 2, "name": "Attenuation", "consume": [1] },
    { "id": 3, "name": "Occlusion", "consume": [2] },
    { "id": 4, "name": "StereoPanning", "consume": [17] },
    { "id": 5, "name": "AmbisonicPanning", "consume": [3] },
    { "id": 6, "name": "NearFieldEffect", "consume": [3] },
    { "id": 7, "name": "AmbisonicMixer", "consume": [18] },
    { "id": 8, "name": "StereoMixer", "consume": [4, 6, 10, 12, 14] },
    { "id": 10, "name": "AmbisonicBinauralDecoder", "consume": [7] },
    { "id": 11, "name": "Reflections", "consume": [1] },
    { "id": 12, "name": "AmbisonicBinauralDecoder", "consume": [11] },
    { "id": 13, "name": "HardClip", "consume": [8] },
    { "id": 14, "name": "Reverb", "consume": [1] },
    { "id": 15, "name": "Obstruction", "consume": [3] },
    { "id": 16, "name": "EnvironmentEffect", "consume": [3] },
    { "id": 17, "name": "StereoMixer", "consume": [15, 16] },
    { "id": 18, "name": "AmbisonicRotator", "consume": [5] },
    { "id": 9, "name": "Output", "consume": [13] }
  ]
}
```

## Custom Nodes

You can implement custom pipeline nodes by subclassing `Node` and `NodeInstance`. See the [Custom Pipeline Node Tutorial](../tutorials/custom-pipeline-node.md) for details.

## Next Steps

- Review the [Pipeline Reference](../project/pipeline.md) for DAG architecture and rules.
- Learn how to create [custom pipeline nodes](../tutorials/custom-pipeline-node.md).
- Explore the [Node API Reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_node.md).
