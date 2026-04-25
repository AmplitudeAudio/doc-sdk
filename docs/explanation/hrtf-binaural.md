---
title: HRTF and Binaural Audio
description: Understand how Amplitude uses Head-Related Transfer Functions to create immersive 3D audio over headphones.
diataxis: explanation
---

Head-Related Transfer Function (HRTF) processing is the foundation of Amplitude's 3D binaural audio. This document explains the science behind HRTF, how Amplitude implements it, and how to get the best results.

## What is HRTF?

When sound travels from a source to your ears, it interacts with your head, torso, and outer ears (pinnae). These interactions create filtering, delays, and reflections that your brain uses to localize sound in 3D space.

An HRTF is a pair of digital filters (one for each ear) that captures this acoustic transformation for every possible direction around the head.

```
Sound Source --> [Head blocking] --> [Pinna filtering] --> [Ear drum]
                     |                    |
                     v                    v
                 Left HRTF            Right HRTF
```

## HRIR vs. HRTF

| Term | Meaning | Domain |
|------|---------|--------|
| **HRIR** | Head-Related Impulse Response | Time domain (raw audio) |
| **HRTF** | Head-Related Transfer Function | Frequency domain (spectrum) |

The HRTF is simply the Fourier transform of the HRIR. In practice, the terms are often used interchangeably because audio engines convolve with the HRIR (time domain) rather than filtering with the HRTF (frequency domain).

## The HRIR Sphere

Amplitude stores HRTF data as an **HRIR Sphere** — a 3D mesh where each vertex contains:

- A direction vector (position on the sphere)
- Left ear impulse response
- Right ear impulse response
- Interaural time difference (ITD) delay

At runtime, when a sound is at a specific direction relative to the listener, Amplitude:

1. Finds the triangle on the sphere mesh that contains the direction.
2. Barycentrically interpolates the three vertex HRIRs (bilinear sampling).
3. Convolves the sound with the interpolated left and right HRIRs.

## Spatial Cues

HRTF provides several cues that the brain uses for localization:

### Interaural Time Difference (ITD)

Sound arrives at the nearer ear slightly before the farther ear. For a source at 90° azimuth, the delay is approximately 0.6–0.7 ms.

- **Primary cue for** horizontal localization (left/right).
- **Effective below** ~1.5 kHz (above this, phase becomes ambiguous).

### Interaural Level Difference (ILD)

The head shadows the farther ear, reducing high-frequency energy. The shadowing is strongest above ~4 kHz.

- **Primary cue for** horizontal localization at high frequencies.
- **Amplitude** varies with direction and frequency.

### Spectral Filtering (Pinna Cues)

The pinna creates direction-dependent notches and peaks in the spectrum. These cues are especially important for:

- **Elevation** (up/down discrimination)
- **Front/back discrimination**

## Supported Datasets

Amplitude supports multiple publicly available HRIR datasets:

| Dataset | Subjects | Resolution | Best For |
|---------|----------|------------|----------|
| **IRCAM LISTEN** | 51 | Medium | General use, averaged listener |
| **MIT KEMAR** | 1 (dummy head) | Medium | Baseline reference |
| **SADIE II** | 71 | High | Research, personalized selection |
| **SOFA** | Varies | Varies | Custom measurements |

The `amir` CLI tool converts these datasets into Amplitude's optimized `.amir` format.

## Binaural vs. Ambisonic Binauralization

Amplitude offers two paths to binaural output:

### Direct HRTF Panning

Each mono source is panned individually using HRTF convolution. This is used by the `StereoPanning` node in HRTF mode.

- **Pros**: Lowest latency, precise per-source control.
- **Cons**: CPU cost scales with source count; blending can sound less natural.

### Ambisonic Binauralization

All sources are encoded into Ambisonics first, then decoded to binaural using Ambisonic-to-HRTF decoding.

- **Pros**: Natural blending, cheap rotation, consistent spatial quality.
- **Cons**: Slightly higher latency, requires Ambisonic pipeline.

The default Amplitude pipeline uses **Ambisonic binauralization** for the best balance of quality and performance.

## Sampling Modes

When looking up HRIR data for an arbitrary direction, Amplitude supports two sampling modes:

| Mode | Method | Quality | Speed |
|------|--------|---------|-------|
| **NearestNeighbor** | Uses the closest vertex | Lower | Faster |
| **Bilinear** | Interpolates within the nearest triangle | Higher | Slower |

For most games, `Bilinear` provides noticeably smoother spatialization with acceptable CPU cost.

## Personalization

HRTF is highly individual. A generic HRTF works for most listeners, but personalization improves accuracy:

1. **Select by anthropometry**: Choose a dataset subject with similar head width and ear shape.
2. **Perceptual selection**: Let the user choose the dataset that sounds most natural.
3. **Custom measurement**: Use the SOFA format to import individually measured HRTF data.

## Performance

HRTF convolution is the most expensive operation in the spatial audio pipeline:

| Factor | Impact |
|--------|--------|
| HRIR length | Longer IRs = more convolution cost. 128–512 samples is typical. |
| Source count | Each HRTF-panned source adds convolution cost. |
| Sampling mode | `Bilinear` is ~2× more expensive than `NearestNeighbor`. |
| FFT efficiency | Amplitude uses partitioned convolution for efficiency. |

For many simultaneous sources, Ambisonic binauralization is more efficient because it performs one decode operation rather than one convolution per source.

## Limitations

- **Headphones required**: HRTF does not work well on speakers due to crosstalk.
- **Individual variation**: Generic HRTFs may cause front/back confusion or inside-the-head localization.
- **Elevation ambiguity**: Elevation perception is less reliable than azimuth.

## Next Steps

- Follow the [HRTF Setup Guide](../integration/hrtf-setup.md) to configure your project.
- Learn about the [Ambisonics Pipeline](ambisonics.md).
- Generate custom `.amir` files with the [`amir` CLI tool](../reference/cli-tools.md#amir).
