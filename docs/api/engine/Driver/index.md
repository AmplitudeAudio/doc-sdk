---
title: Driver
description: Base class for audio device driver implementations.
generator: doxide
---


# Driver

**class  Driver**


Base class for audio device driver implementations.

A driver allows to use an audio device to output sounds and
receive data from the microphone.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_name](#m_name) | The driver name.  |
| [m_deviceDescription](#m_deviceDescription) | The device description.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Driver](#Driver) | Creates a new AudioDriver with an unique name. |
| [~Driver](#_u007eDriver) | Default destructor.  |
| [Open](#Open) | Open and start using the audio device. |
| [Close](#Close) | Closes the audio device. |
| [EnumerateDevices](#EnumerateDevices) | Enumerates all the available audio devices. |
| [GetName](#GetName) | Gets the name of this driver. |
| [GetDeviceDescription](#GetDeviceDescription) | Gets the description of the device currently managed by this driver. |
| [Register](#Register) | Registers a new audio driver. |
| [Unregister](#Unregister) | Unregisters an audio driver. |
| [Default](#Default) | Choose the most preferred audio driver. |
| [Find](#Find) | Look up a driver by name. |
| [SetDefault](#SetDefault) | Set the default diver to use in the engine. |
| [LockRegistry](#LockRegistry) | Locks the drivers registry. |
| [UnlockRegistry](#UnlockRegistry) | Unlocks the drivers registry. |

## Variable Details

### m_deviceDescription<a name="m_deviceDescription"></a>

!!! variable "DeviceDescription m_deviceDescription"

    
    The device description.
             
    
    
    

### m_name<a name="m_name"></a>

!!! variable "AmString m_name"

    
    The driver name.
             
    
    
    

## Function Details

### Close<a name="Close"></a>
!!! function "virtual bool Close() = 0"

    
    Closes the audio device.
    
    
    :material-keyboard-return: **Return**
    :    `true` if successful, `false` otherwise.
            
    

### Default<a name="Default"></a>
!!! function "static Driver&#42; Default()"

    
    Choose the most preferred audio driver.
    
    
    :material-keyboard-return: **Return**
    :    The default audio driver.
            
    

### Driver<a name="Driver"></a>
!!! function "explicit Driver(AmString name)"

    
    Creates a new AudioDriver with an unique name.
    
    
    :material-location-enter: **Parameter** `name`
    :    The driver name. Recommended names are "APIName".
        eg. "MiniAudio" or "PortAudio" or "SDL", etc...
                
    

### EnumerateDevices<a name="EnumerateDevices"></a>
!!! function "virtual bool EnumerateDevices(std::vector&lt;DeviceDescription&gt;&amp; devices) = 0"

    
    Enumerates all the available audio devices.
    
    
    :material-location-exit: **Parameter** `devices`
    :    The vector in which to store the device descriptions.
    
    
    :material-keyboard-return: **Return**
    :    `true` if successful, `false` otherwise.
            
    

### Find<a name="Find"></a>
!!! function "static Driver&#42; Find(const AmString&amp; name)"

    
    Look up a driver by name.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the audio driver. Must be registered before.
    
    
    :material-keyboard-return: **Return**
    :    The audio driver with the given name, or `nullptr` if none.
            
    

### GetDeviceDescription<a name="GetDeviceDescription"></a>
!!! function "[[nodiscard]] const DeviceDescription&amp; GetDeviceDescription() const"

    
    Gets the description of the device currently managed by this driver.
    
    
    :material-keyboard-return: **Return**
    :    The device description.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Gets the name of this driver.
    
    
    :material-keyboard-return: **Return**
    :    The name of this driver.
            
    

### LockRegistry<a name="LockRegistry"></a>
!!! function "static void LockRegistry()"

    
    Locks the drivers registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called before the `Engine` initialization, to discard the registration
        of new divers after the engine is fully loaded.
                
    

### Open<a name="Open"></a>
!!! function "virtual bool Open(const DeviceDescription&amp; device) = 0"

    
    Open and start using the audio device.
    
    
    :material-location-enter: **Parameter** `device`
    :    The audio device to use description to use for initializing the physical device.
    
    
    :material-keyboard-return: **Return**
    :    `true` if successful, `false` otherwise.
            
    

### Register<a name="Register"></a>
!!! function "static void Register(Driver&#42; driver)"

    
    Registers a new audio driver.
    
    
    :material-location-enter: **Parameter** `driver`
    :    The audio driver to add in the registry.
                
    

### SetDefault<a name="SetDefault"></a>
!!! function "static void SetDefault(const AmString&amp; name)"

    
    Set the default diver to use in the engine.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the audio driver. Must be registered before.
                
    

### UnlockRegistry<a name="UnlockRegistry"></a>
!!! function "static void UnlockRegistry()"

    
    Unlocks the drivers registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called after the `Engine` deinitialization, to allow the registration
        of new divers after the engine is fully unloaded.
                
    

### Unregister<a name="Unregister"></a>
!!! function "static void Unregister(const Driver&#42; driver)"

    
    Unregisters an audio driver.
    
    
    :material-location-enter: **Parameter** `driver`
    :    The audio driver to remove from the registry.
                
    

### ~Driver<a name="_u007eDriver"></a>
!!! function "virtual ~Driver()"

    
    Default destructor.
             
    
    
    

