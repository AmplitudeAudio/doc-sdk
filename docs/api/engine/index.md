---
title: Engine
description: Engine-specific functionalities
generator: doxide
---


# Engine

Engine-specific functionalities

## Types

| Name | Description |
| ---- | ----------- |
| [Bus](Bus/index.md) | An object representing one node in the tree of buses. Buses are used to adjust a set of channel gains in tandem. |
| [Channel](Channel/index.md) | An object that represents a single channel of audio. |
| [ChannelEvent](ChannelEvent/index.md) | Enumerates the events triggered by a `Channel` during playback. |
| [ChannelEventCallback](ChannelEventCallback/index.md) | A callback function for handling channel events. |
| [ChannelEventInfo](ChannelEventInfo/index.md) | The event info passed to the channel event listener. |
| [ChannelEventListener](ChannelEventListener/index.md) | Channel Event listener. |
| [ChannelPlaybackState](ChannelPlaybackState/index.md) | Enumerates the playback states for a `Channel`. |
| [Codec](Codec/index.md) | Audio file reader and writer. |
| [DeviceDescription](DeviceDescription/index.md) | The device description. |
| [DeviceNotification](DeviceNotification/index.md) | The possible device notification types. |
| [DeviceState](DeviceState/index.md) | The device state. |
| [Driver](Driver/index.md) | Base class for audio device driver implementations. |
| [Engine](Engine/index.md) | The Amplitude Engine. |
| [PlaybackOutputChannels](PlaybackOutputChannels/index.md) | The playback output channel layout of the device. |
| [PlaybackOutputFormat](PlaybackOutputFormat/index.md) | The playback output format of the device. |

## Macros

| Name | Description |
| ---- | ----------- |
| [AM_AUDIO_SAMPLE_MAX](#AM_AUDIO_SAMPLE_MAX) | The maximum value for an audio sample. |
| [AM_AUDIO_SAMPLE_MIN](#AM_AUDIO_SAMPLE_MIN) | The minimum value for an audio sample. |
| [AM_INVALID_HANDLE](#AM_INVALID_HANDLE) | Define an invalid object handle. |
| [AM_IS_VALID_HANDLE](#AM_IS_VALID_HANDLE) | Checks if a handle is valid |

## Functions

| Name | Description |
| ---- | ----------- |
| [CallDeviceNotificationCallback](#CallDeviceNotificationCallback) | Calls the registered device notification callback. |
| [RegisterDeviceNotificationCallback](#RegisterDeviceNotificationCallback) | The device notification callback.Registers a callback to listen to device state changes. |

## Macro Details

### AM_AUDIO_SAMPLE_MAX<a name="AM_AUDIO_SAMPLE_MAX"></a>

!!! macro "#define AM_AUDIO_SAMPLE_MAX"

    
    The maximum value for an audio sample.
    
    
    
    

### AM_AUDIO_SAMPLE_MIN<a name="AM_AUDIO_SAMPLE_MIN"></a>

!!! macro "#define AM_AUDIO_SAMPLE_MIN"

    
    The minimum value for an audio sample.
    
    
    
    

### AM_INVALID_HANDLE<a name="AM_INVALID_HANDLE"></a>

!!! macro "#define AM_INVALID_HANDLE"

    
    Define an invalid object handle.
    
    
    
    

### AM_IS_VALID_HANDLE<a name="AM_IS_VALID_HANDLE"></a>

!!! macro "#define AM_IS_VALID_HANDLE(handle)"

    
    Checks if a handle is valid
    
    
    :material-location-enter: **Parameter** `handle`
    :    The handle to check
    
    
    :material-keyboard-return: **Return**
    :    `true` if the handle is valid, `false` otherwise.
    
    
    
    

## Function Details

### CallDeviceNotificationCallback<a name="CallDeviceNotificationCallback"></a>
!!! function "void CallDeviceNotificationCallback(DeviceNotification notification, const DeviceDescription&amp; device, Driver&#42; driver)"

    
    Calls the registered device notification callback.
    
    
    :material-location-enter: **Parameter** `notification`
    :    The notification type.
        
    :material-location-enter: **Parameter** `device`
    :    The device description.
        
    :material-location-enter: **Parameter** `driver`
    :    The driver which triggered the device notification.
    
    
        
    

### RegisterDeviceNotificationCallback<a name="RegisterDeviceNotificationCallback"></a>
!!! function "void RegisterDeviceNotificationCallback(DeviceNotificationCallback callback)"

    
    The device notification callback.
    
    
    :material-location-enter: **Parameter** `notification`
    :    The notification type.
        
    :material-location-enter: **Parameter** `device`
    :    The device description.
        
    :material-location-enter: **Parameter** `driver`
    :    The driver which triggered the device notification.
    
    
        
    
    Registers a callback to listen to device state changes.
    
    
    :material-location-enter: **Parameter** `callback`
    :    The callback to register.
    
    
        
    

