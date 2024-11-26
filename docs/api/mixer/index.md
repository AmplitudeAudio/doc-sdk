---
title: Mixer
description: Mixer & Pipeline API
generator: doxide
---


# Mixer

Mixer & Pipeline API

## Types

| Name | Description |
| ---- | ----------- |
| [Amplimix](Amplimix/index.md) | Amplitude Audio Mixer. |
| [AmplimixLayer](AmplimixLayer/index.md) | A single layer in the mixer. |
| [ConsumerNodeInstance](ConsumerNodeInstance/index.md) | Interface for Amplimix pipeline nodes that can consume audio data from an input buffer. |
| [InputNodeInstance](InputNodeInstance/index.md) | Class used to mark the input of the pipeline. |
| [MixerNodeInstance](MixerNodeInstance/index.md) | Base class for Amplimix pipeline nodes that can mix audio data from multiple input buffers. |
| [Node](Node/index.md) | Base class for Amplimix pipeline nodes. |
| [NodeInstance](NodeInstance/index.md) | An instance of an Amplimix pipeline node. |
| [OutputNodeInstance](OutputNodeInstance/index.md) | Class used to mark the output of the pipeline. |
| [Pipeline](Pipeline/index.md) | A pipeline assembles a set of nodes to process audio data. |
| [PipelineInstance](PipelineInstance/index.md) | Represents an instance of a pipeline for a specific layer. |
| [ProcessorNodeInstance](ProcessorNodeInstance/index.md) | Base class for Amplimix pipeline nodes that can process audio data in-place. |
| [ProviderNodeInstance](ProviderNodeInstance/index.md) | Interface for Amplimix pipeline nodes that can provide audio data to an output buffer. |

## Functions

| Name | Description |
| ---- | ----------- |
| [AM_CALLBACK](#AM_CALLBACK) | Called just after the mixer process audio data. |

## Function Details

### AM_CALLBACK<a name="AM_CALLBACK"></a>
!!! function "AM_CALLBACK(void, AfterMixCallback)(const Amplimix&#42; mixer, const AudioBuffer&#42; buffer, AmUInt32 frames)"

    
    Called just after the mixer process audio data.
    
    
    :material-location-enter: **Parameter** `mixer`
    :    The Amplimix instance.
        
    :material-location-enter: **Parameter** `buffer`
    :    The audio buffer that has been mixed.
        
    :material-location-enter: **Parameter** `frames`
    :    The number of audio frames that have been mixed.
    
    
        
    

