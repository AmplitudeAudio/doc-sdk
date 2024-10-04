---
title: DeviceDescription
description: The device description.
generator: doxide
---


# DeviceDescription

**struct DeviceDescription**


The device description.

This stores the settings requested from the engine configuration
and the actual settings provided by the device.

The device settings are filled after the Amplimix initialization,
and are provided by the selected Driver.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [mDeviceName](#mDeviceName) | The device name.  |
| [mDeviceID](#mDeviceID) | The device ID.  |
| [mRequestedOutputFormat](#mRequestedOutputFormat) | The requested device output format.  |
| [mDeviceOutputFormat](#mDeviceOutputFormat) | The actual device format.  |
| [mRequestedOutputChannels](#mRequestedOutputChannels) | The requested device output channel layout.  |
| [mDeviceOutputChannels](#mDeviceOutputChannels) | The actual device channel layout.  |
| [mRequestedOutputSampleRate](#mRequestedOutputSampleRate) | The requested device sample rate.  |
| [mDeviceOutputSampleRate](#mDeviceOutputSampleRate) | The actual device sample rate.  |
| [mOutputBufferSize](#mOutputBufferSize) | The device output buffer size.  |
| [mDeviceState](#mDeviceState) | The device state.  |

## Variable Details

### mDeviceID<a name="mDeviceID"></a>

!!! variable "AmObjectID mDeviceID"

    
    The device ID.
             
    
    
    

### mDeviceName<a name="mDeviceName"></a>

!!! variable "AmString mDeviceName"

    
    The device name.
             
    
    
    

### mDeviceOutputChannels<a name="mDeviceOutputChannels"></a>

!!! variable "PlaybackOutputChannels mDeviceOutputChannels"

    
    The actual device channel layout.
             
    
    
    

### mDeviceOutputFormat<a name="mDeviceOutputFormat"></a>

!!! variable "PlaybackOutputFormat mDeviceOutputFormat"

    
    The actual device format.
             
    
    
    

### mDeviceOutputSampleRate<a name="mDeviceOutputSampleRate"></a>

!!! variable "AmUInt32 mDeviceOutputSampleRate"

    
    The actual device sample rate.
             
    
    
    

### mDeviceState<a name="mDeviceState"></a>

!!! variable "DeviceState mDeviceState"

    
    The device state.
             
    
    
    

### mOutputBufferSize<a name="mOutputBufferSize"></a>

!!! variable "AmUInt32 mOutputBufferSize"

    
    The device output buffer size.
             
    
    
    

### mRequestedOutputChannels<a name="mRequestedOutputChannels"></a>

!!! variable "PlaybackOutputChannels mRequestedOutputChannels"

    
    The requested device output channel layout.
             
    
    
    

### mRequestedOutputFormat<a name="mRequestedOutputFormat"></a>

!!! variable "PlaybackOutputFormat mRequestedOutputFormat"

    
    The requested device output format.
             
    
    
    

### mRequestedOutputSampleRate<a name="mRequestedOutputSampleRate"></a>

!!! variable "AmUInt32 mRequestedOutputSampleRate"

    
    The requested device sample rate.
             
    
    
    

