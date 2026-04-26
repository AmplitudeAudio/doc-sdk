---
title: Glossary
description: Definitions of common terms used in the Amplitude Audio SDK documentation.
diataxis: reference
---

## A

**ADPCM** — Adaptive Differential Pulse-Code Modulation. A lossy audio compression algorithm used by the AMS codec.

**Ambisonics** — A full-sphere surround sound technique using spherical harmonics to encode and decode 3D sound fields.

**AMIR** — Amplitude HRIR file format. An optimized binary format for storing Head-Related Impulse Response data.

**AMS** — Amplitude Media Stream. Amplitude's custom ADPCM-compressed audio file format.

**Attenuation** — The reduction of sound level as distance from the source increases.

## B

**B-Format** — The channel representation of an Ambisonic signal (W, X, Y, Z, etc.).

**Bus** — An audio mixing channel that groups sounds together for shared gain, ducking, and effects processing.

## C

**Channel** — A single instance of a playing sound in the mixer. Each `Play()` call creates a channel.

**Codec** — A software component that encodes and/or decodes audio data from a specific file format.

**Collection** — A sound object that groups multiple sounds and selects one to play based on a scheduler.

## D

**Decoder** — The part of a codec that reads compressed audio data and produces raw PCM samples.

**DSP** — Digital Signal Processing. Mathematical manipulation of audio signals (filters, effects, etc.).

**Ducking** — Automatically reducing the gain of one bus when another bus becomes active.

## E

**Encoder** — The part of a codec that writes raw PCM samples into a compressed audio file.

**Entity** — A game object in the Amplitude engine that can emit or receive spatialized audio.

**Environment** — A zone in 3D space where sounds receive a specific effect (reverb, EQ, etc.).

## F

**Fader** — A curve that controls how a value transitions from one point to another over time.

**FlatBuffers** — A binary serialization format used by Amplitude for project assets and configuration files.

## H

**HRTF** — Head-Related Transfer Function. A pair of filters that capture how sound interacts with the human head and ears for 3D spatialization.

**HRIR** — Head-Related Impulse Response. The time-domain representation of an HRTF.

## I

**ILD** — Interaural Level Difference. The difference in sound level between the two ears, used for localization.

**ITD** — Interaural Time Difference. The difference in arrival time of sound between the two ears, used for localization.

## L

**Listener** — A point in 3D space that represents the player's ears. Audio is spatialized relative to listeners.

**LZ4** — A fast lossless compression algorithm used by the `ampk` packager.

## N

**Node** — A processing unit in the Amplimix pipeline. Nodes perform spatialization, effects, mixing, or dynamics.

## P

**Pipeline** — A directed acyclic graph (DAG) of nodes that defines how audio is processed in the mixer.

## R

**Resampler** — A component that converts audio from one sample rate to another.

**Room** — A physically modeled acoustic space with walls, materials, and dimensions that affect reverberation.

**RTPC** — Real-Time Parameter Control. A game value (e.g., speed, health) that dynamically controls audio properties via curves.

## S

**Sound Bank** — A binary asset pack that contains multiple sounds, collections, events, and other assets.

**Sound Object** — A generic term for any playable asset: Sound, Collection, or SwitchContainer.

**Spatialization** — The process of positioning audio in 3D space using panning, HRTF, or Ambisonics.

**Switch Container** — A sound object that plays different audio content based on the current state of a switch.

## V

**Virtual Channel** — A channel that is not actively mixed but is still tracked by the engine. Virtual channels can be promoted to real channels when resources become available.

**Voice** — Another term for a channel or sound instance in the mixer.
