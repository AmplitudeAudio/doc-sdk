---
title: Amplimix
description: Amplitude Audio Mixer.
generator: doxide
---


# Amplimix

**class  Amplimix**


Amplitude Audio Mixer.

This class handles processing of audio data by mixing multiple audio sources.
The resulting audio stream are next handled by the `Driver` for playback or recording.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [UpdateDevice](#UpdateDevice) | Saves the information about the rendering audio device. |
| [IsInitialized](#IsInitialized) | Checks if the mixer is initialized. |
| [Mix](#Mix) | Processes the audio data by mixing multiple audio sources for the specified number of frames. |
| [GetDeviceDescription](#GetDeviceDescription) | Gets the description of the rendering audio device. |

## Function Details

### GetDeviceDescription<a name="GetDeviceDescription"></a>
!!! function "[[nodiscard]] virtual const DeviceDescription&amp; GetDeviceDescription() const = 0"

    
    Gets the description of the rendering audio device.
    
    
    :material-keyboard-return: **Return**
    :    The description of the rendering audio device.
            
    

### IsInitialized<a name="IsInitialized"></a>
!!! function "[[nodiscard]] virtual bool IsInitialized() const = 0"

    
    Checks if the mixer is initialized.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the mixer is initialized, `false` otherwise.
            
    

### Mix<a name="Mix"></a>
!!! function "virtual AmUInt64 Mix(AudioBuffer&#42;&#42; outBuffer, AmUInt64 frameCount) = 0"

    
    Processes the audio data by mixing multiple audio sources for the specified number of frames.
    
    
    :material-location-enter: **Parameter** `outBuffer`
    :    The buffer to store the mixed audio data.
        
    :material-location-enter: **Parameter** `frameCount`
    :    The number of frames to mix.
    
    
    :material-keyboard-return: **Return**
    :    The number of frames actually mixed.
            
    

### UpdateDevice<a name="UpdateDevice"></a>
!!! function "virtual void UpdateDevice( AmObjectID deviceID, AmString deviceName, AmUInt32 deviceOutputSampleRate, PlaybackOutputChannels deviceOutputChannels, PlaybackOutputFormat deviceOutputFormat) = 0"

    
    Saves the information about the rendering audio device.
    
    
    :material-location-enter: **Parameter** `deviceID`
    :    The ID of the audio device.
        
    :material-location-enter: **Parameter** `deviceName`
    :    The name of the audio device.
        
    :material-location-enter: **Parameter** `deviceOutputSampleRate`
    :    The sample rate of the audio device's output.
        
    :material-location-enter: **Parameter** `deviceOutputChannels`
    :    The number of audio channels of the audio device's output.
        
    :material-location-enter: **Parameter** `deviceOutputFormat`
    :    The format of the audio device's output.
                
    

