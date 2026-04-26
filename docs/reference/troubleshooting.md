---
title: Troubleshooting
description: Common issues and solutions when integrating and using the Amplitude Audio SDK.
diataxis: reference
---

This reference documents common issues encountered when using the Amplitude Audio SDK and their recommended solutions.

## Engine Initialization

### Issue: `amEngine->Initialize()` returns false

| Cause | Solution |
|-------|----------|
| File system not initialized | Call `StartOpenFileSystem()` and `TryFinalizeOpenFileSystem()` before `amEngine->Initialize()`. |
| Missing engine config file | Verify the path to the loaded config file and ensure it exists. |
| Invalid JSON in config | Validate the config against the [Engine Configuration schema](../project/engine-config.md). |
| Codec/Driver registry locked | Register extensions **before** `amEngine->Initialize()`. |
| Memory manager not initialized | Call `MemoryManager::Initialize()` first. |

### Issue: Crash during `amEngine->Initialize()`

| Cause | Solution |
|-------|----------|
| Null file system pointer | Ensure `SetFileSystem()` is called with a valid pointer. |
| Plugin ABI mismatch | Rebuild plugins with the same compiler and SDK version. |
| Corrupt project files | Try to regenerate project files with `build_project.py`. |

## Audio Playback

### Issue: No sound output

| Cause | Solution |
|-------|----------|
| Driver not found | Verify the `driver` field in the engine config, and ensure its value is not `"null"` and references a registered driver. |
| Master bus gain is 0 | Check bus configuration and `Bus::SetGain()`. |
| Sound bank not loaded | Call `Engine::LoadSoundBank()` and verify the path. |
| All channels virtualized | Increase `active_channels` in the mixer config or reduce concurrent sounds. |
| Entity too far from listener | Check attenuation model `max_distance`. |

### Issue: Sound is distorted or clipping

| Cause | Solution |
|-------|----------|
| Gain too high | Reduce sound object gain or bus gain. |
| Multiple sounds summing above 0 dB | Add a `LimiterNode` to the pipeline. |
| Interleaved vs de-interleaved mismatch | Ensure your codec outputs de-interleaved float32. |

### Issue: Sound cuts off abruptly

| Cause | Solution |
|-------|----------|
| Sound bank unloaded too early | Keep the bank loaded until all sounds finish playing. |
| Channel stolen by higher priority | Increase the sound's `priority` or `active_channels`. |
| Stream buffer underrun | Increase `buffer_size` in the output config. |

## Spatial Audio

### Issue: HRTF spatialization sounds flat

| Cause | Solution |
|-------|----------|
| `spatialization` not set to `HRTF` | Change the sound object's `spatialization` field. |
| `panning_mode` is `Stereo` | Change mixer `panning_mode` to `BinauralHighQuality`. |
| Missing `.amir` file | Verify the `hrtf.amir_file` path in the engine config. |
| Listener not updated | Call `listener.SetLocation()` and `listener.SetOrientation()` each frame. |

### Issue: Front/back confusion

| Cause | Solution |
|-------|----------|
| Low-resolution HRIR dataset | Use SADIE or high-resolution SOFA data. |
| Wrong listener orientation | Verify the up and forward vectors are orthonormal. |

### Issue: Ambisonic decoding sounds wrong

| Cause | Solution |
|-------|----------|
| Missing `AmbisonicRotator` | Ensure the pipeline includes `AmbisonicRotator` after `AmbisonicPanning`. |

## Performance

### Issue: High CPU usage

| Cause | Solution |
|-------|----------|
| Too many active channels | Reduce `active_channels` or use virtual channels. |
| HRTF with many sources | Switch to `BinauralMediumQuality` or use Ambisonic panning. |
| Long HRIR files | Use shorter IRs (128–512 samples). |
| Third-order Ambisonics | Drop to second or first order for mobile. |
| No `ShouldSkip()` in custom nodes | Implement `ShouldSkip()` to bypass inactive nodes. |

### Issue: Audio dropouts or stuttering

| Cause | Solution |
|-------|----------|
| Buffer size too small | Increase `buffer_size` (try 1024 or 2048). |
| Main thread blocking audio thread | Move heavy game logic off the main thread or reduce audio thread workload. |
| Streaming file I/O too slow | Pre-load short sounds; stream only long music. |

## Asset Pipeline

### Issue: build_project.py fails

| Cause | Solution |
|-------|----------|
| Missing FlatBuffers compiler | Install `flatc` and ensure it's in your PATH. |
| Invalid JSON syntax | Validate all `.json` files with a JSON linter. |
| Missing sound file | Verify all `path` references in sound assets exist. |
| Duplicate IDs | Ensure all asset IDs are unique across the project. |

### Issue: Sound bank loads but files are silent

| Cause | Solution |
|-------|----------|
| Codec not registered | Register the codec before `amEngine->Initialize()`. |
| Wrong file extension | Ensure the file extension matches a registered codec. |
| Sound files not loaded | Sound files need to be manually loaded after sound bank. |

## Memory

### Issue: Memory leaks reported on shutdown

| Cause | Solution |
|-------|----------|
| Custom allocator missing `Free()` | Verify your allocator frees all memory. |
| Sound banks not unloaded | Call `amEngine->UnloadSoundBank()` before `amEngine->Deinitialize()`. |
| Objects not destroyed | Use `amdelete` / `ampooldelete` for all `amnew` / `ampoolnew` allocations. |

### Issue: Out of memory on mobile

| Cause | Solution |
|-------|----------|
| All sounds loaded into memory | Enable `stream: true` for large sound assets. |
| Too many virtual channels | Reduce `virtual_channels` in the mixer config. |
| Large HRIR sphere | Use a smaller `.amir` file or `NearestNeighbor` sampling. |

## Platform-Specific

### Android

| Issue | Solution |
|-------|----------|
| No audio output | Request `AUDIO` permission in `AndroidManifest.xml`. |
| High latency | Use the AAudio driver path in MiniAudio (enabled by default). |
| AssetManagerFileSystem not found | Use `AndroidAssetManagerFileSystem` for APK assets. |

### iOS

| Issue | Solution |
|-------|----------|
| No audio after backgrounding | Re-initialize the audio session when returning to foreground. |
| High latency | Enable low-latency mode in the audio session category. |

## Getting Help

If your issue is not listed here:

1. Check the [API Reference](../api/index.md) for detailed behavior.
2. Enable verbose logging: `amLogInfo("...")` and review the output.
3. Run with the Null driver to isolate audio device issues.
4. Join the [Discord server](https://discord.gg/QR2uBpzJ5f) for community support.
5. Open a [GitHub issue](https://github.com/AmplitudeAudio/sdk/issues) with a minimal reproduction.
