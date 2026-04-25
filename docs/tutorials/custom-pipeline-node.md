---
title: Custom Pipeline Node
description: Learn how to extend the Amplimix pipeline with custom audio processing nodes.
---

This tutorial walks you through creating a custom pipeline node for the Amplitude engine. You will build a **Gain LFO Node** — a node that modulates the gain of a sound with a low-frequency oscillator — and learn how to register it so it can be used in any pipeline asset.

## Architecture Overview

Pipeline nodes in Amplitude follow a two-class pattern:

1. **Node** — Defines the node metadata (name) and acts as a factory for creating instances.
2. **NodeInstance** — Holds per-layer state and performs the actual audio processing.

```mermaid
classDiagram
    class Node {
        +CreateInstance() shared_ptr~NodeInstance~
    }

    class NodeInstance {
        +Initialize(config)
        +Reset()
        +Process(in, out, frames)
        +GetOutputFrameCount() AmUInt64
        +GetOutputChannelCount() AmUInt16
        +ShouldSkip() bool
    }

    Node --> NodeInstance : creates
```

At runtime, the engine creates a `NodeInstance` for each active mixer layer that uses the pipeline containing your node.

## Step 1: Choose a Base Class

Amplitude provides several `NodeInstance` base classes depending on your node's role:

| Base Class | Role | Methods |
|------------|------|---------|
| `ProcessorNodeInstance` | In-place transformation | `Process()`, `Consume()`, `Connect()`, `Provide()` |
| `MixerNodeInstance` | Multi-input mixing | `Consume()` (multi), `Connect()`, `Provide()` |
| `ConsumerNodeInstance` | Output/sink | `Consume()`, `Connect()` |
| `ProviderNodeInstance` | Input/source | `Provide()` |

For a gain LFO, we need `ProcessorNodeInstance` because we transform audio in-place.

## Step 2: Define the Node Classes

Create a header file for your custom node:

```cpp
// GainLFONode.h

#pragma once

#include <SparkyStudios/Audio/Amplitude/Amplitude.h>

using namespace SparkyStudios::Audio::Amplitude;

class GainLFONodeInstance final : public ProcessorNodeInstance
{
public:
    GainLFONodeInstance();
    ~GainLFONodeInstance() override = default;

    bool Initialize(const AmString& name, const AmUInt32 id, const PipelineInstance* pipeline) override;
    void Reset() override;
    AmUInt64 GetOutputFrameCount() const override;
    AmUInt16 GetOutputChannelCount() const override;
    bool ShouldSkip() const override;

protected:
    AmUInt64 Process(AudioBuffer* out, AmUInt64 outFrameOffset, AmUInt64 neededFrames) override;

private:
    AmReal32 _phase;
    AmReal32 _rate;
    AmReal32 _depth;
};

class GainLFONode final : public Node
{
public:
    GainLFONode()
        : Node("GainLFO")
    {}

    std::shared_ptr<NodeInstance> CreateInstance() override
    {
        return ampoolshared(eMemoryPoolKind_Amplimix, GainLFONodeInstance);
    }
};
```

## Step 3: Implement the Instance

```cpp
// GainLFONode.cpp

#include "GainLFONode.h"

#include <cmath>

GainLFONodeInstance::GainLFONodeInstance()
    : _phase(0.0f)
    , _rate(5.0f)
    , _depth(0.1f)
{}

bool GainLFONodeInstance::Initialize(const AmString& name, const AmUInt32 id, const PipelineInstance* pipeline)
{
    // You can read custom configuration here if your node supports parameters
    return ProcessorNodeInstance::Initialize(name, id, pipeline);
}

void GainLFONodeInstance::Reset()
{
    _phase = 0.0f;
}

AmUInt64 GainLFONodeInstance::GetOutputFrameCount() const
{
    // Pass-through: output frame count equals input frame count
    return GetInputFrameCount();
}

AmUInt16 GainLFONodeInstance::GetOutputChannelCount() const
{
    // Pass-through: channel count is unchanged
    return GetInputChannelCount();
}

bool GainLFONodeInstance::ShouldSkip() const
{
    // Skip if depth is zero (no audible effect)
    return _depth <= 0.0f;
}

AmUInt64 GainLFONodeInstance::Process(AudioBuffer* out, AmUInt64 outFrameOffset, AmUInt64 neededFrames)
{
    const AmUInt16 channels = out->GetChannelCount();
    const AmUInt32 sampleRate = GetSampleRate();

    for (AmUInt64 i = 0; i < neededFrames; ++i)
    {
        // Compute LFO value: sine wave [-1, 1]
        const AmReal32 lfo = std::sin(2.0f * AM_PI * _phase);

        // Map to gain range [1 - depth, 1 + depth]
        const AmReal32 gain = 1.0f + lfo * _depth;

        // Apply gain to all channels
        for (AmUInt16 ch = 0; ch < channels; ++ch)
        {
            out->GetData()[ch][outFrameOffset + i] *= gain;
        }

        // Advance phase
        _phase += _rate / sampleRate;
        if (_phase >= 1.0f)
            _phase -= 1.0f;
    }

    return neededFrames;
}
```

## Step 4: Register the Node

Before initializing the engine, register your node:

```cpp
#include "GainLFONode.h"

int main(int argc, char* argv[])
{
    // ... initialize memory manager, file system, etc.

    // Register the custom pipeline node
    Node::Register(std::make_shared<GainLFONode>());

    // Register built-in extensions
    Engine::RegisterDefaultExtensions();

    // Now initialize the engine
    Engine::Init(config);
}
```

!!! tip "Registration order"
    Nodes must be registered **before** `Engine::Init()` is called. Once the engine is initialized, the node registry is locked.

## Step 5: Use the Node in a Pipeline

Create a pipeline asset JSON file that includes your custom node:

```json
{
  "id": 3,
  "name": "lfx_pipeline",
  "nodes": [
    { "id": 1, "name": "Input", "consume": [] },
    { "id": 2, "name": "Attenuation", "consume": [1] },
    { "id": 3, "name": "GainLFO", "consume": [2] },
    { "id": 4, "name": "StereoPanning", "consume": [3] },
    { "id": 5, "name": "Output", "consume": [4] }
  ]
}
```

Assign this pipeline to a sound object or the engine mixer configuration:

```json
{
  "id": 10,
  "name": "pulsing_ambience",
  "path": "sounds/ambience.wav",
  "loop": { "enabled": true },
  "pipeline": "lfx_pipeline"
}
```

## Key Concepts

### Frame Counts and Offsets

The `Process()` method receives:

- `out`: The output buffer (also the input buffer for in-place processors)
- `outFrameOffset`: Where to start writing in the buffer
- `neededFrames`: How many frames to process

Always process exactly `neededFrames` unless you reach the end of the source data.

### Channel Count

Your node can change the channel count (e.g., mono-to-stereo panning) or preserve it (like our gain LFO). Return the correct count from `GetOutputChannelCount()`.

### ShouldSkip()

Implement `ShouldSkip()` to let the mixer bypass your node when it has no audible effect:

```cpp
bool ShouldSkip() const override
{
    return _depth <= 0.0f || _enabled == false;
}
```

This reduces CPU usage for layers where the node is inactive.

### Reset()

`Reset()` is called when a layer is recycled or reinitialized. Clear all state to ensure deterministic behavior:

```cpp
void Reset() override
{
    _phase = 0.0f;
}
```

## Parameters

To make your node configurable from the pipeline asset, read parameters during `Initialize()`:

```cpp
bool GainLFONodeInstance::Initialize(const AmString& name, const AmUInt32 id, const PipelineInstance* pipeline)
{
    // Access the pipeline asset definition
    auto* def = pipeline->GetDefinition();
    // Read custom parameters from the asset JSON
    // (requires extending the FlatBuffers schema)

    return ProcessorNodeInstance::Initialize(name, id, pipeline);
}
```

Full parameter support requires extending the pipeline FlatBuffers schema. For simple hard-coded behavior, compile-time constants are sufficient.

## Memory Management

Always use Amplitude's pool-aware allocation for node state:

```cpp
// Good: uses the Amplimix pool
return ampoolshared(eMemoryPoolKind_Amplimix, GainLFONodeInstance);

// Bad: bypasses memory tracking
return std::make_shared<GainLFONodeInstance>();
```

## Thread Safety

`Process()` is called from the audio thread. It must be:

- **Lock-free**: No mutexes, semaphores, or blocking operations.
- **Realtime-safe**: No memory allocation, file I/O, or logging.
- **Deterministic**: Same input must produce same output for a given state.

If you need to communicate with the game thread, use atomic variables or lock-free queues.

## Next Steps

- Review the [Pipeline Reference](../project/pipeline.md) for the full DAG architecture.
- Explore the [Node API Reference](../api/mixer/Node.md).
- Look at the built-in nodes in `sdk/src/Mixer/Nodes/` for production examples.
