---
title: Custom Resampler
description: Learn how to extend the Engine by implementing a custom audio resampler for sample rate conversion.
---

This tutorial walks you through creating a custom resampler for the Amplitude engine. You will build a **Linear Resampler** — a simple sample rate converter using linear interpolation — and learn how to register it so codecs and the mixer can use it for runtime sample rate conversion.

## Architecture Overview

In Amplitude, resampling is handled by the **Resampler** system. To create a custom resampler, you need two classes:

1. **Resampler** — Defines the resampler name and acts as a factory for creating instances.
2. **ResamplerInstance** — Holds the runtime state and performs the actual sample rate conversion.

```mermaid
classDiagram
    class Resampler {
        +CreateInstance() shared_ptr~ResamplerInstance~
    }

    class ResamplerInstance {
        +Process(in, out, frames, inputSampleRate, outputSampleRate) AmUInt64
        +SetSampleRate(sampleRate)
        +GetInputLatency() AmUInt64
        +GetOutputLatency() AmUInt64
    }

    Resampler --> ResamplerInstance : creates
```

At runtime, the engine creates a `ResamplerInstance` whenever a sound's sample rate does not match the output device rate, or when an encoder requests resampling.

## Step 1: Define the Resampler Classes

Create a header file for your custom resampler:

```cpp
// LinearResampler.h

#pragma once

#include <SparkyStudios/Audio/Amplitude/Amplitude.h>

using namespace SparkyStudios::Audio::Amplitude;

class LinearResamplerInstance final : public ResamplerInstance
{
public:
    LinearResamplerInstance();
    ~LinearResamplerInstance() override = default;

    void SetSampleRate(AmUInt32 sampleRate) override;

    AmUInt64 Process(
        const AudioBuffer* in,
        AudioBuffer* out,
        AmUInt64 inFrames,
        AmUInt32 inputSampleRate,
        AmUInt32 outputSampleRate) override;

    [[nodiscard]] AmUInt64 GetInputLatency() const override { return 0; }
    [[nodiscard]] AmUInt64 GetOutputLatency() const override { return 0; }

private:
    AmReal64 _phase;
    AmUInt32 _outputSampleRate;
};

class LinearResampler final : public Resampler
{
public:
    LinearResampler()
        : Resampler("Linear")
    {}

    std::shared_ptr<ResamplerInstance> CreateInstance() override
    {
        return ampoolshared(eMemoryPoolKind_Engine, LinearResamplerInstance);
    }
};
```

## Step 2: Implement the Resampler

```cpp
// LinearResampler.cpp

#include "LinearResampler.h"

LinearResamplerInstance::LinearResamplerInstance()
    : _phase(0.0)
    , _outputSampleRate(48000)
{}

void LinearResamplerInstance::SetSampleRate(AmUInt32 sampleRate)
{
    _outputSampleRate = sampleRate;
}

AmUInt64 LinearResamplerInstance::Process(
    const AudioBuffer* in,
    AudioBuffer* out,
    AmUInt64 inFrames,
    AmUInt32 inputSampleRate,
    AmUInt32 outputSampleRate)
{
    if (inputSampleRate == outputSampleRate)
    {
        // No conversion needed; copy directly
        out->CopyFrom(in, 0, 0, inFrames);
        return inFrames;
    }

    const AmReal64 ratio = static_cast<AmReal64>(inputSampleRate) / outputSampleRate;
    const AmUInt16 channels = in->GetChannelCount();

    // Estimate output frames (conservative)
    const AmUInt64 outFrames = static_cast<AmUInt64>(inFrames / ratio);

    out->SetChannelCount(channels);
    out->SetFrameCount(outFrames);

    for (AmUInt16 ch = 0; ch < channels; ++ch)
    {
        const AmAudioSample* src = in->GetData()[ch];
        AmAudioSample* dst = out->GetData()[ch];

        AmReal64 readPos = 0.0;
        for (AmUInt64 i = 0; i < outFrames; ++i)
        {
            const AmUInt64 idx = static_cast<AmUInt64>(readPos);
            const AmReal64 frac = readPos - idx;

            const AmAudioSample s0 = src[AM_MIN(idx, inFrames - 1)];
            const AmAudioSample s1 = src[AM_MIN(idx + 1, inFrames - 1)];

            dst[i] = static_cast<AmAudioSample>(s0 + frac * (s1 - s0));
            readPos += ratio;
        }
    }

    return outFrames;
}
```

## Step 3: Register the Resampler

Before initializing the engine, register your resampler:

```cpp
#include "LinearResampler.h"

int main(int argc, char* argv[])
{
    // ... initialize memory manager, file system, etc.

    // Register the custom resampler
    Resampler::Register(std::make_shared<LinearResampler>());

    // Register other extensions and initialize the engine
    Engine::RegisterDefaultExtensions();
    Engine::Init(config);
}
```

!!! tip "Registration order"
    Resamplers must be registered **before** `Engine::Init()` is called. Once the engine is initialized, the resampler registry is locked.

## How Resampling is Triggered

Amplitude automatically uses a resampler when:

1. A sound file's sample rate differs from the output device rate.
2. The `AudioConverter` DSP node needs to convert between formats.
3. The `amac` tool requests resampling during encoding.

The engine selects the resampler by name. The built-in `Default` resampler is used unless overridden.

## Latency

Resamplers introduce latency due to buffering and filter delay. Report your latency accurately:

```cpp
[[nodiscard]] AmUInt64 GetInputLatency() const override { return _filterTaps / 2; }
[[nodiscard]] AmUInt64 GetOutputLatency() const override { return 0; }
```

The engine uses these values to synchronize audio streams correctly.

## Quality vs. Performance

| Algorithm | Quality | CPU Cost | Best For |
|-----------|---------|----------|----------|
| **Linear** | Low | Very low | Quick preview, tests |
| **Nearest** | Very low | Minimal | Retro/8-bit aesthetics |
| **Sinc** | High | High | Production music |
| **Polyphase** | Very high | Medium-High | Real-time pitch shifting |

The built-in `Default` resampler in Amplitude uses a high-quality algorithm suitable for most games.

## Next Steps

- Review the [Resampler API Reference](../api/dsp/Resampler.md).
- Explore the built-in resampler implementation in the SDK source.
- Learn how to write [custom codecs](../tutorials/custom-codec.md) that use your resampler.
