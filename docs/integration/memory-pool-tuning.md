---
title: Memory Pool Tuning
description: Configure and monitor Amplitude's pool-based memory allocator for optimal performance.
diataxis: how-to
---

This guide explains how to configure and tune Amplitude's **memory pools** for your game's specific needs. Proper tuning ensures efficient allocation, reduces fragmentation, and helps you stay within platform memory budgets.

## Overview

Amplitude uses a pool-based memory management system. All allocations are tagged with a **pool kind**, allowing the engine to track usage per subsystem and apply platform-specific strategies.

### Memory Pool Kinds

| Pool | Purpose | Typical Usage |
|------|---------|---------------|
| `Engine` | Core engine state | Entities, listeners, channels, buses |
| `Amplimix` | Mixer and pipeline | Audio buffers, layer state, node instances |
| `SoundData` | Sound file data | Decoded audio buffers, streaming chunks |
| `Filtering` | DSP effects | Filter instances, effect state |
| `Codec` | Codecs | Decoder/encoder state, internal buffers |
| `IO` | File system | File handles, read buffers, package data |
| `Default` | Uncategorized | Fallback for untagged allocations |

## Initializing the Memory Manager

The memory manager must be initialized before any other Amplitude subsystem:

```cpp
#include <SparkyStudios/Audio/Amplitude/Core/Memory.h>

int main()
{
    // Initialize with default settings
    MemoryManager::Initialize();

    // Or initialize with custom allocator
    MemoryManager::Initialize(std::make_shared<MyCustomAllocator>());
}
```

## Using Pool-Aware Allocation

Always use Amplitude's allocation macros when working with the SDK:

```cpp
// Allocate from a specific pool
void* buffer = ampoolmalloc(eMemoryPoolKind_SoundData, 1024);

// Aligned allocation for SIMD
void* aligned = ampoolmalign(eMemoryPoolKind_Amplimix, 4096, 32);

// Reallocate
buffer = ampoolrealloc(eMemoryPoolKind_SoundData, buffer, 2048);

// Free
ampoolfree(eMemoryPoolKind_SoundData, buffer);
```

### C++ Object Construction

Use pool-aware `new` and `delete` macros:

```cpp
// Construct an object in the Engine pool
MyClass* obj = ampoolnew(eMemoryPoolKind_Engine, MyClass, args);

// Destroy it
ampooldelete(eMemoryPoolKind_Engine, MyClass, obj);
```

### Smart Pointers

Amplitude provides pool-aware smart pointers:

```cpp
// Unique pointer
AmUniquePtr<MyClass, eMemoryPoolKind_Engine> ptr = ampoolunique(eMemoryPoolKind_Engine, MyClass, args);

// Shared pointer
AmSharedPtr<MyClass, eMemoryPoolKind_Engine> shared = AmSharedPtr<MyClass, eMemoryPoolKind_Engine>::Make(args);
```

## Memory Statistics

Query memory usage at runtime to monitor pools:

```cpp
for (AmUInt32 i = 0; i < eMemoryPoolKind_COUNT; ++i)
{
    const auto pool = static_cast<eMemoryPoolKind>(i);
    const MemoryPoolStats& poolStats = amMemory->GetStats(pool);

    amLogInfo("Pool %s: maxMemoryUsed=%zu, allocCount=%llu, freeCount=%llu",
        MemoryManager::GetMemoryPoolName(pool).c_str(),
        poolStats.maxMemoryUsed.load(),
        poolStats.allocCount.load(),
        poolStats.freeCount.load());
}
```

### Enabling Statistics

Statistics tracking is enabled by default unless you define `AM_NO_MEMORY_STATS` at compile time. Disabling statistics reduces overhead slightly:

```cmake
target_compile_definitions(my_target PRIVATE AM_NO_MEMORY_STATS)
```

## Scoped Allocations

Use `ScopedMemoryAllocation` for temporary buffers that should be freed automatically:

```cpp
{
    ScopedMemoryAllocation scoped(eMemoryPoolKind_Amplimix, 4096, __FILE__, __LINE__);
    void* tempBuffer = scoped.Address();

    // Use tempBuffer...

} // Automatically freed when scope ends
```

## Custom Allocators

You can provide a custom `MemoryAllocator` implementation:

```cpp
class MyAllocator final : public MemoryAllocator
{
public:
    AmVoidPtr Malloc(eMemoryPoolKind pool, AmSize size) override
    {
        return std::malloc(size);
    }

    AmVoidPtr Malign(eMemoryPoolKind pool, AmSize size, AmUInt32 alignment) override
    {
        return aligned_alloc(alignment, size);
    }

    AmVoidPtr Realloc(eMemoryPoolKind pool, AmVoidPtr address, AmSize size) override
    {
        return std::realloc(address, size);
    }

    AmVoidPtr Realign(eMemoryPoolKind pool, AmVoidPtr address, AmSize size, AmUInt32 alignment) override
    {
        auto* newPtr = Malign(pool, size, alignment);
        std::memcpy(newPtr, address, size); // Simplified; real impl would copy old size
        Free(pool, address);
        return newPtr;
    }

    void Free(eMemoryPoolKind pool, AmVoidPtr address) override
    {
        std::free(address);
    }

    AmSize SizeOf(eMemoryPoolKind pool, AmVoidPtr address) override
    {
        // Platform-specific; return 0 if unsupported
        return 0;
    }
};

// Use it
MemoryManager::Initialize(std::make_shared<MyAllocator>());
```

## Performance Tips

| Tip | Impact |
|-----|--------|
| Use `ampoolmalloc` instead of `malloc` | Enables statistics tracking and pool isolation |
| Pre-allocate large buffers | Avoids runtime allocation during gameplay |
| Use `ScopedMemoryAllocation` for temp data | Prevents leaks and reduces manual free calls |
| Enable `AM_NO_MEMORY_STATS` on release | Slight reduction in allocation overhead |
| Align audio buffers to 32 bytes | Enables SIMD optimizations in the mixer |

## Memory Budgets

While Amplitude does not enforce hard memory limits per pool, you can implement budgeting in your custom allocator:

```cpp
AmVoidPtr MyAllocator::Malloc(eMemoryPoolKind pool, AmSize size)
{
    if (mCurrentUsage + size > mBudget)
    {
        amLogError("Memory budget exceeded!");
        return nullptr;
    }
    mCurrentUsage += size;
    return std::malloc(size);
}
```

Future versions of Amplitude will include built-in memory budget enforcement.

## Next Steps

- Review the [Memory Management API Reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_memory_manager.md).
- Learn how to implement [custom allocators](../tutorials/custom-codec.md) in your codecs.
