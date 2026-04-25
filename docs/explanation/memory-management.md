---
title: Memory Management
description: Understand how Amplitude manages memory with pools, aligned allocations, and leak detection.
---

Amplitude includes a custom memory management system designed for predictable performance, debugging, and integration with game engine memory budgets. This document explains how it works and how to use it effectively.

## Why Custom Memory Management?

Standard `malloc`/`free` have several drawbacks for game audio:

- **Unpredictable allocation times**: General-purpose allocators can stall during defragmentation.
- **No budget tracking**: It's hard to know how much memory audio is using.
- **Platform differences**: Console platforms often require custom allocators.
- **Alignment requirements**: SIMD operations need specifically aligned buffers.

Amplitude's memory system addresses these issues with pool-based allocation, alignment support, and optional leak tracking.

## Memory Pools

All allocations are categorized into one of seven pools:

| Pool | Purpose | Typical Lifetime |
|------|---------|------------------|
| `Engine` | Core engine state | Application lifetime |
| `Amplimix` | Mixer buffers and state | Per-frame |
| `SoundData` | Decoded audio data | Sound duration |
| `Filtering` | DSP effect instances | Sound duration |
| `Codec` | Codec internal buffers | File operation |
| `IO` | File system buffers | File operation |
| `Default` | Uncategorized | Varies |

Separating allocations by pool allows:

- **Accurate statistics**: See exactly which subsystem uses memory.
- **Targeted optimization**: Optimize the allocator per pool.
- **Budget enforcement**: Limit memory per subsystem (planned for v1.3).

## Allocation Macros

Amplitude provides macros that wrap the memory manager:

```cpp
// Raw allocation
void* buffer = ampoolmalloc(eMemoryPoolKind_SoundData, 4096);
ampoolfree(eMemoryPoolKind_SoundData, buffer);

// Aligned allocation (for SIMD)
void* aligned = ampoolmalign(eMemoryPoolKind_Amplimix, 4096, 32);
ampoolfree(eMemoryPoolKind_Amplimix, aligned);

// C++ object construction
MyClass* obj = ampoolnew(eMemoryPoolKind_Engine, MyClass, args);
ampooldelete(eMemoryPoolKind_Engine, MyClass, obj);
```

### Smart Pointers

Pool-aware smart pointers ensure correct deallocation:

```cpp
// Unique pointer
AmUniquePtr<MyClass, eMemoryPoolKind_Engine> ptr =
    ampoolunique(eMemoryPoolKind_Engine, MyClass, args);

// Shared pointer
AmSharedPtr<MyClass, eMemoryPoolKind_Engine> shared =
    AmSharedPtr<MyClass, eMemoryPoolKind_Engine>::Make(args);
```

## Default Allocator

The default allocator (`DefaultMemoryAllocator`) is a simple bucket-based allocator that wraps the platform's `malloc`. It is suitable for most desktop and mobile use cases.

You can replace it with a custom allocator:

```cpp
class MyAllocator : public MemoryAllocator
{
public:
    void* Malloc(AmSize size, const char* file, AmUInt32 line) override;
    void* Malign(AmSize size, AmSize alignment, const char* file, AmUInt32 line) override;
    void Free(void* ptr) override;
    // ...
};

MemoryManager::Initialize(std::make_shared<MyAllocator>());
```

## Leak Detection

When statistics are enabled (the default), the memory manager tracks every allocation with its file and line number:

```cpp
// This allocation is tracked
void* buffer = ampoolmalloc(eMemoryPoolKind_Engine, 1024);
// File: MyGame.cpp, Line: 42
```

On shutdown, if any allocations remain, the memory manager logs them:

```
[WARN] Memory leak detected: 1024 bytes allocated at MyGame.cpp:42
```

To disable tracking (for release builds), define `AM_NO_MEMORY_STATS`:

```cmake
target_compile_definitions(my_target PRIVATE AM_NO_MEMORY_STATS)
```

## Scoped Allocations

For temporary buffers, use `ScopedMemoryAllocation`:

```cpp
{
    ScopedMemoryAllocation scoped(eMemoryPoolKind_Amplimix, 4096);
    void* temp = scoped.GetPointer();

    // Process audio...

} // Automatically freed here
```

This prevents leaks and reduces manual `free` calls.

## Alignment

SIMD operations (SSE, AVX, NEON) require aligned memory. Amplitude's `AmAlignedReal32Buffer` uses `ammalign` internally:

```cpp
AmAlignedReal32Buffer buffer;
buffer.Init(1024); // Allocates 1024 floats, 32-byte aligned

// Safe for SIMD
ProcessSIMD(buffer.GetBuffer(), 1024);
```

Always align audio buffers to at least 16 bytes (32 bytes for AVX).

## Best Practices

- **Always use pool macros**: Never use raw `malloc`/`free` for Amplitude-related allocations.
- **Choose the right pool**: This makes debugging and optimization much easier.
- **Use scoped allocations for temporaries**: Prevents leaks and simplifies code.
- **Align to 32 bytes**: Enables AVX optimizations on x86 and NEON on ARM.
- **Check stats in development**: Monitor pool usage to catch unexpected growth.

## Next Steps

- Review the [Memory Tuning Guide](../integration/memory-pool-tuning.md).
- Explore the [MemoryManager API Reference](../api/memory/MemoryManager.md).
