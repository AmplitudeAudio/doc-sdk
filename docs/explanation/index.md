---
title: Explanation
description: Deep dives into Amplitude's architecture, concepts, and design decisions.
diataxis: explanation
---

# Explanation

This section contains in-depth explanations of Amplitude's architecture and concepts.

## Fundamentals

- **[Introduction](introduction.md)** - Overview of Amplitude's features
- **[Concepts](concepts.md)** - Engine architecture and data flow
- **[Project Architecture](../project/project-architecture.md)** - How Amplitude projects are organized

## Architecture

- **[Plugin Architecture](plugin-architecture.md)** - How the plugin registry system works
- **[Memory Management](memory-management.md)** - Pool-based allocation and leak detection
- **[Threading Model](threading-model.md)** - Game thread, audio thread, and command queues
- **[Codec Architecture](codec-architecture.md)** - How codecs decode and encode audio

## Spatial Audio

- **[Ambisonics](ambisonics.md)** - Full-sphere surround sound with spherical harmonics
- **[HRTF and Binaural Audio](hrtf-binaural.md)** - 3D audio over headphones

## Samples

- **[Sample Projects](sample-projects.md)** - Overview of the included SDK samples
