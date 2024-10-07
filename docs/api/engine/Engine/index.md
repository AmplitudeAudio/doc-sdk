---
title: Engine
description: The Amplitude Engine.
generator: doxide
---


# Engine

**class  Engine**


The Amplitude Engine.

This is the main class of the library that manages all the entities
and provides methods to create, destroy, and manipulate them. You can also
access to the internal state of the engine through the public API.

The `Engine` is a singleton class and you can access it using the `amEngine` macro. Before
using most of the methods of the engine, you need to [initialize the
engine](../../../integration/initializing-the-engine.md) first, for example:
```cpp
amEngine->Initialize("config.amconfig");
//...
amEngine->Deinitialize();
```


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Version](#Version) | Gets the version structure. |
| [Initialize](#Initialize) | Initializes the Amplitude engine. |
| [Deinitialize](#Deinitialize) | Deinitializes the Amplitude engine. |
| [IsInitialized](#IsInitialized) | Checks if the Amplitude engine has been successfully initialized. |
| [SetFileSystem](#SetFileSystem) | Sets a file system implementation to be used by the engine. |
| [GetFileSystem](#GetFileSystem) | Gets the file system implementation used by the engine. |
| [StartOpenFileSystem](#StartOpenFileSystem) | Opens the file system, usually in a separate thread.  |
| [TryFinalizeOpenFileSystem](#TryFinalizeOpenFileSystem) | Checks if the file system has been fully loaded. |
| [StartCloseFileSystem](#StartCloseFileSystem) | Closes the file system, usually in a separate thread.  |
| [TryFinalizeCloseFileSystem](#TryFinalizeCloseFileSystem) | Checks if the file system has been fully closed. |
| [AdvanceFrame](#AdvanceFrame) | Updates the engine state for the given number of milliseconds. |
| [OnNextFrame](#OnNextFrame) | Executes the given callback on the next frame. |
| [WaitUntilNextFrame](#WaitUntilNextFrame) | Waits until the next frame is ready. |
| [WaitUntilFrames](#WaitUntilFrames) | Waits until the specified number of frames are ready. |
| [GetTotalTime](#GetTotalTime) | Gets the total elapsed time in milliseconds since the start of the engine. |
| [LoadSoundBank](#LoadSoundBank) | Loads a sound bank from a binary asset file (`.ambank`). |
| [LoadSoundBank](#LoadSoundBank) | Loads a sound bank from a binary asset file (`.ambank`). |
| [LoadSoundBankFromMemory](#LoadSoundBankFromMemory) | Loads a sound bank from memory. |
| [LoadSoundBankFromMemory](#LoadSoundBankFromMemory) | Loads a sound bank from memory. |
| [LoadSoundBankFromMemoryView](#LoadSoundBankFromMemoryView) | Loads a sound bank from memory. |
| [LoadSoundBankFromMemoryView](#LoadSoundBankFromMemoryView) | Loads a sound bank from memory. |
| [UnloadSoundBank](#UnloadSoundBank) | Unloads a sound bank given its filename. |
| [UnloadSoundBank](#UnloadSoundBank) | Unloads a sound bank given its ID. |
| [UnloadSoundBanks](#UnloadSoundBanks) | Unloads all the loaded sound banks.  |
| [StartLoadSoundFiles](#StartLoadSoundFiles) | Starts the loading of sound files referenced in loaded sound banks. |
| [TryFinalizeLoadSoundFiles](#TryFinalizeLoadSoundFiles) | Checks if the loading of sound files has been completed, and releases used resources. |
| [GetSwitchContainerHandle](#GetSwitchContainerHandle) | Gets a `SwitchContainerHandle` given its name as defined in its asset file (`.amswitchcontainer`). |
| [GetSwitchContainerHandle](#GetSwitchContainerHandle) | Gets a `SwitchContainerHandle` given its ID as defined in its asset file (`.amswitchcontainer`). |
| [GetSwitchContainerHandleFromFile](#GetSwitchContainerHandleFromFile) | Gets a `SwitchContainerHandle` given its asset's filename. |
| [GetCollectionHandle](#GetCollectionHandle) | Gets a `CollectionHandle` given its name as defined in its asset file (`.amcollection`). |
| [GetCollectionHandle](#GetCollectionHandle) | Gets a `CollectionHandle` given its ID as defined in its asset file (`.amcollection`). |
| [GetCollectionHandleFromFile](#GetCollectionHandleFromFile) | Gets a `CollectionHandle` given its asset's filename. |
| [GetSoundHandle](#GetSoundHandle) | Gets a `SoundHandle` given its name as defined in its asset file (`.amsound`). |
| [GetSoundHandle](#GetSoundHandle) | Gets a `SoundHandle` given its ID as defined in its asset file (`.amsound`). |
| [GetSoundHandleFromFile](#GetSoundHandleFromFile) | Gets a `SoundHandle` given its asset's filename. |
| [GetSoundObjectHandle](#GetSoundObjectHandle) | Gets a `SoundObjectHandle` given its name as defined in its asset file. |
| [GetSoundObjectHandle](#GetSoundObjectHandle) | Gets a `SoundObjectHandle` given its ID as defined in its asset file. |
| [GetSoundObjectHandleFromFile](#GetSoundObjectHandleFromFile) | Gets a `SoundObjectHandle` given its asset's filename. |
| [GetEventHandle](#GetEventHandle) | Gets an `EventHandle` given its name as defined in its asset file (`.amevent`). |
| [GetEventHandle](#GetEventHandle) | Gets an `EventHandle` given its ID as defined in its asset file (`.amevent`). |
| [GetEventHandleFromFile](#GetEventHandleFromFile) | Gets an `EventHandle` given its asset's filename. |
| [GetAttenuationHandle](#GetAttenuationHandle) | Gets an `AttenuationHandle` given its name as defined in its asset file (`.amattenuation`). |
| [GetAttenuationHandle](#GetAttenuationHandle) | Gets an `AttenuationHandle` given its ID as defined in its asset file (`.amattenuation`). |
| [GetAttenuationHandleFromFile](#GetAttenuationHandleFromFile) | Gets an `AttenuationHandle` given its asset's filename. |
| [GetSwitchHandle](#GetSwitchHandle) | Gets a `SwitchHandle` given its name as defined in its asset file (`.amswitch`). |
| [GetSwitchHandle](#GetSwitchHandle) | Gets a `SwitchHandle` given its ID as defined in its asset file (`.amswitch`). |
| [GetSwitchHandleFromFile](#GetSwitchHandleFromFile) | Gets a `SwitchHandle` given its asset's filename. |
| [GetRtpcHandle](#GetRtpcHandle) | Gets a `RtpcHandle` given its name as defined in its asset file (`.amrtpc`). |
| [GetRtpcHandle](#GetRtpcHandle) | Gets an `RtpcHandle` given its ID as defined in its asset file (`.amrtpc`). |
| [GetRtpcHandleFromFile](#GetRtpcHandleFromFile) | Gets an `RtpcHandle` given its asset's filename. |
| [GetEffectHandle](#GetEffectHandle) | Gets an `EffectHandle` given its name as defined in its asset file (`.amfx`). |
| [GetEffectHandle](#GetEffectHandle) | Gets an `EffectHandle` given its ID as defined in its asset file (`.amfx`). |
| [GetEffectHandleFromFile](#GetEffectHandleFromFile) | Gets an `EffectHandle` given its asset's filename. |
| [GetPipelineHandle](#GetPipelineHandle) | Gets a `PipelineHandle` from the loaded pipeline asset file (`.ampipeline`). |
| [SetMasterGain](#SetMasterGain) | Adjusts the master gain of the mixer. |
| [GetMasterGain](#GetMasterGain) | Gets the mixer master gain. |
| [SetMute](#SetMute) | Mutes the engine, but keep processing audio. |
| [IsMuted](#IsMuted) | Checks whether the engine is currently muted. |
| [Pause](#Pause) | Pauses or resumes all playing sounds and streams. |
| [IsPaused](#IsPaused) | Checks whether the engine is currently paused. |
| [SetDefaultListener](#SetDefaultListener) | Sets the default sound listener. |
| [SetDefaultListener](#SetDefaultListener) | Sets the default sound listener. |
| [GetDefaultListener](#GetDefaultListener) | Gets the default audio `Listener`. |
| [AddListener](#AddListener) | Initializes and returns a new `Listener`. |
| [GetListener](#GetListener) | Returns the `Listener` with the given ID. |
| [RemoveListener](#RemoveListener) | Removes a `Listener` given its ID. |
| [RemoveListener](#RemoveListener) | Removes a `Listener` given its handle. |
| [AddEntity](#AddEntity) | Initializes and returns a new `Entity`. |
| [GetEntity](#GetEntity) | Returns the `Entity` with the given ID. |
| [RemoveEntity](#RemoveEntity) | Removes an `Entity`. |
| [RemoveEntity](#RemoveEntity) | Removes an `Entity` given its ID. |
| [AddEnvironment](#AddEnvironment) | Initializes and return a new `Environment`. |
| [GetEnvironment](#GetEnvironment) | Returns the `Environment` with the given ID. |
| [RemoveEnvironment](#RemoveEnvironment) | Removes an `Environment`. |
| [RemoveEnvironment](#RemoveEnvironment) | Removes an `Environment` given its ID. |
| [AddRoom](#AddRoom) | Initializes and return a new `Room`. |
| [GetRoom](#GetRoom) | Returns the `Room` with the given ID. |
| [RemoveRoom](#RemoveRoom) | Removes a `Room`. |
| [RemoveRoom](#RemoveRoom) | Removes a `Room` given its ID. |
| [FindBus](#FindBus) | Returns the `Bus` with the specified name. |
| [FindBus](#FindBus) | Returns the `Bus` with the given ID. |
| [Play](#Play) | Plays a switch container associated with the given handle in the World scope. |
| [Play](#Play) | Plays a switch container associated with the given handle in the World scope. |
| [Play](#Play) | Plays a switch container associated with the given handle in the World scope. |
| [Play](#Play) | Plays a switch container associated with the given handle in an Entity scope. |
| [Play](#Play) | Plays a switch container associated with the given handle in an Entity scope. |
| [Play](#Play) | Plays a collection associated with the given handle in the World scope. |
| [Play](#Play) | Plays a collection associated with the given handle in the World scope. |
| [Play](#Play) | Plays a collection associated with the given handle in the World scope. |
| [Play](#Play) | Plays a collection associated with the given handle in the Entity scope. |
| [Play](#Play) | Plays a collection associated with the given handle in an Entity scope. |
| [Play](#Play) | Plays a sound associated with the given handle in the World scope. |
| [Play](#Play) | Plays a sound associated with the given handle in the World scope. |
| [Play](#Play) | Plays a sound associated with the given handle in the World scope. |
| [Play](#Play) | Plays a sound associated with the given sound handle in an Entity scope. |
| [Play](#Play) | Plays a sound associated with the given sound handle in an Entity. |
| [Play](#Play) | Plays a sound object associated with the given name in the World scope. |
| [Play](#Play) | Plays a sound object associated with the given name in the World scope. |
| [Play](#Play) | Plays a sound object associated with the given name in the World scope. |
| [Play](#Play) | Plays a sound object associated with the given name in an Entity scope. |
| [Play](#Play) | Plays a sound object associated with the given name in an Entity scope. |
| [Play](#Play) | Plays a sound object associated with the given ID in the  World scope. |
| [Play](#Play) | Plays a sound object associated with the given ID in the World scope. |
| [Play](#Play) | Plays a sound object associated with the given ID in the World scope. |
| [Play](#Play) | Plays a sound object associated with the given ID in an Entity scope. |
| [Play](#Play) | Plays a sound object associated with the given ID in an Entity scope. |
| [StopAll](#StopAll) | Stops all playing sound objects. |
| [Trigger](#Trigger) | Triggers the event associated to the given handle. |
| [Trigger](#Trigger) | Triggers the event associated to the given handle. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetSwitchState](#SetSwitchState) | Sets the active state of the defined `Switch`. |
| [SetRtpcValue](#SetRtpcValue) | Sets the value of a `RTPC`. |
| [SetRtpcValue](#SetRtpcValue) | Sets the value of a `RTPC`. |
| [SetRtpcValue](#SetRtpcValue) | Sets the value of a `RTPC`. |
| [GetDriver](#GetDriver) | Gets the audio driver used by the Engine. |
| [GetMixer](#GetMixer) | Gets the mixer instance. |
| [GetSoundSpeed](#GetSoundSpeed) | Gets the speed of sound, as set in the loaded engine configuration file. |
| [GetDopplerFactor](#GetDopplerFactor) | Get the Doppler factor, as set in the loaded engine configuration file. |
| [GetSamplesPerStream](#GetSamplesPerStream) | Get the number of samples to process in one stream, as set in the loaded engine configuration file. |
| [IsGameTrackingEnvironmentAmounts](#IsGameTrackingEnvironmentAmounts) | Checks whether the game is tracking environment amounts himself. |
| [GetMaxListenersCount](#GetMaxListenersCount) | Gets the maximum number of listeners handled by the engine. |
| [GetMaxEntitiesCount](#GetMaxEntitiesCount) | Gets the maximum number of game entities handled by the engine. |
| [GetOcclusionCoefficientCurve](#GetOcclusionCoefficientCurve) | Gets the occlusion coefficient curve, as set in the loaded engine configuration file. |
| [GetOcclusionGainCurve](#GetOcclusionGainCurve) | Gets the occlusion gain curve, as set in the loaded engine configuration file. |
| [GetObstructionCoefficientCurve](#GetObstructionCoefficientCurve) | Gets the obstruction coefficient curve, as set in the loaded engine configuration file. |
| [GetObstructionGainCurve](#GetObstructionGainCurve) | Gets the obstruction gain curve, as set in the loaded engine configuration file. |
| [GetPanningMode](#GetPanningMode) | Gets the panning mode defined in the loaded engine configuration. |
| [GetHRIRSphereSamplingMode](#GetHRIRSphereSamplingMode) | Gets the HRIR sphere sampling mode defined in the loaded engine configuration. |
| [GetHRIRSphere](#GetHRIRSphere) | Gets the HRIR sphere defined in the loaded engine configuration. |
| [LoadPlugin](#LoadPlugin) | Loads a plugin library from the given path. |
| [AddPluginSearchPath](#AddPluginSearchPath) | Adds a path in the plugins search paths list. |
| [RemovePluginSearchPath](#RemovePluginSearchPath) | Removes a path from the plugins search paths list. |
| [RegisterDefaultPlugins](#RegisterDefaultPlugins) | Register all default plugins.  |
| [UnregisterDefaultPlugins](#UnregisterDefaultPlugins) | Unregister all default plugins.  |
| [GetInstance](#GetInstance) | Returns an unique instance of the Amplitude Engine.  |
| [DestroyInstance](#DestroyInstance) | Destroys the unique instance of the Amplitude Engine.  |

## Function Details

### AddEntity<a name="AddEntity"></a>
!!! function "[[nodiscard]] virtual Entity AddEntity(AmEntityID id) const = 0"

    
    Initializes and returns a new `Entity`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The game entity ID.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Entity`.
            
    

### AddEnvironment<a name="AddEnvironment"></a>
!!! function "[[nodiscard]] virtual Environment AddEnvironment(AmEnvironmentID id) const = 0"

    
    Initializes and return a new `Environment`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The game environment ID.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Environment`.
            
    

### AddListener<a name="AddListener"></a>
!!! function "[[nodiscard]] virtual Listener AddListener(AmListenerID id) const = 0"

    
    Initializes and returns a new `Listener`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The new listener ID.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Listener`.
            
    

### AddPluginSearchPath<a name="AddPluginSearchPath"></a>
!!! function "static void AddPluginSearchPath(const AmOsString&amp; path)"

    
    Adds a path in the plugins search paths list.
    
    
    :material-location-enter: **Parameter** `path`
    :    The path to add in the plugins search paths list.
                
    

### AddRoom<a name="AddRoom"></a>
!!! function "[[nodiscard]] virtual Room AddRoom(AmRoomID id) const = 0"

    
    Initializes and return a new `Room`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The room ID.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Room`.
            
    

### AdvanceFrame<a name="AdvanceFrame"></a>
!!! function "virtual void AdvanceFrame(AmTime delta) const = 0"

    
    Updates the engine state for the given number of milliseconds.
    
    
    :material-location-enter: **Parameter** `delta`
    :    The number of milliseconds since the last frame.
                
    

### Deinitialize<a name="Deinitialize"></a>
!!! function "virtual bool Deinitialize() = 0"

    
    Deinitializes the Amplitude engine.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the engine has been successfully deinitialized, `false` otherwise.
            
    

### DestroyInstance<a name="DestroyInstance"></a>
!!! function "static void DestroyInstance()"

    
    Destroys the unique instance of the Amplitude Engine.
             
    
    
    

### FindBus<a name="FindBus"></a>
!!! function "[[nodiscard]] virtual Bus FindBus(const AmString&amp; name) const = 0"

    
    Returns the `Bus` with the specified name.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the bus.
    
    
    !!! note
         The name should match one of the buses loaded from the asset file (`.ambus`).
    
    
    :material-keyboard-return: **Return**
    :    A valid `Bus` if found, otherwise an invalid `Bus`.
            
    

!!! function "[[nodiscard]] virtual Bus FindBus(AmBusID id) const = 0"

    
    Returns the `Bus` with the given ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the bus.
    
    
    !!! note
         The ID should match one of the buses loaded from the asset file (`.ambus`).
    
    
    :material-keyboard-return: **Return**
    :    A valid `Bus` if found, otherwise an invalid `Bus`.
            
    

### GetAttenuationHandle<a name="GetAttenuationHandle"></a>
!!! function "[[nodiscard]] virtual AttenuationHandle GetAttenuationHandle(const AmString&amp; name) const = 0"

    
    Gets an `AttenuationHandle` given its name as defined in its asset file (`.amattenuation`).
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `AttenuationHandle` for the given name, or an invalid handle if no attenuation with that name
    was found in any loaded sound bank.
            
    

!!! function "[[nodiscard]] virtual AttenuationHandle GetAttenuationHandle(AmAttenuationID id) const = 0"

    
    Gets an `AttenuationHandle` given its ID as defined in its asset file (`.amattenuation`).
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `AttenuationHandle` for the given ID, or an invalid handle if no attenuation with that ID
    was found in any loaded sound bank.
            
    

### GetAttenuationHandleFromFile<a name="GetAttenuationHandleFromFile"></a>
!!! function "[[nodiscard]] virtual AttenuationHandle GetAttenuationHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets an `AttenuationHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `attenuators` directory of your Amplitude
        project, not an absolute path from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "attenuators/impact.amattenuation"
        AttenuationHandle handle = amEngine->GetAttenuationHandleFromFile("impact.amattenuation");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `AttenuationHandle` for the given asset's filename, or an invalid handle if no attenuation
    with that filename was found in any loaded sound bank.
            
    

### GetCollectionHandle<a name="GetCollectionHandle"></a>
!!! function "[[nodiscard]] virtual CollectionHandle GetCollectionHandle(const AmString&amp; name) const = 0"

    
    Gets a `CollectionHandle` given its name as defined in its asset file (`.amcollection`).
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `CollectionHandle` for the given name, or an invalid handle if no collection
    with that name was found in any loaded sound bank.
            
    

!!! function "[[nodiscard]] virtual CollectionHandle GetCollectionHandle(AmCollectionID id) const = 0"

    
    Gets a `CollectionHandle` given its ID as defined in its asset file (`.amcollection`).
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `CollectionHandle` for the given ID, or an invalid handle if no collection
    with that ID was found in any loaded sound bank.
            
    

### GetCollectionHandleFromFile<a name="GetCollectionHandleFromFile"></a>
!!! function "[[nodiscard]] virtual CollectionHandle GetCollectionHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets a `CollectionHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `collections` directory of your Amplitude
        project, not an absolute path from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "collections/weapons/ak47_gunfires.amcollection"
        CollectionHandle handle = amEngine->GetCollectionHandleFromFile("weapons/ak47_gunfires.amcollection");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `CollectionHandle` for the given asset's filename, or an invalid handle if no collection
    with that filename was found in any loaded sound bank.
            
    

### GetDefaultListener<a name="GetDefaultListener"></a>
!!! function "[[nodiscard]] virtual Listener GetDefaultListener() const = 0"

    
    Gets the default audio `Listener`.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Listener` object if a default listener was set,
    otherwise an uninitialized `Listener` object.
            
    

### GetDopplerFactor<a name="GetDopplerFactor"></a>
!!! function "[[nodiscard]] virtual AmReal32 GetDopplerFactor() const = 0"

    
    Get the Doppler factor, as set in the loaded engine configuration file.
    
    
    :material-keyboard-return: **Return**
    :    The Doppler factor.
            
    

### GetDriver<a name="GetDriver"></a>
!!! function "&#42; GetDriver() const"

    
    Gets the audio driver used by the Engine.
    
    
    :material-keyboard-return: **Return**
    :    The audio driver.
            
    

### GetEffectHandle<a name="GetEffectHandle"></a>
!!! function "[[nodiscard]] virtual EffectHandle GetEffectHandle(const AmString&amp; name) const = 0"

    
    Gets an `EffectHandle` given its name as defined in its asset file (`.amfx`).
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `EffectHandle` for the given name, or an invalid handle if no effect with that name
    was found in any loaded sound bank.
            
    

!!! function "[[nodiscard]] virtual EffectHandle GetEffectHandle(AmEffectID id) const = 0"

    
    Gets an `EffectHandle` given its ID as defined in its asset file (`.amfx`).
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `EffectHandle` for the given ID, or an invalid handle if no effect with that ID
    was found in any loaded sound bank.
            
    

### GetEffectHandleFromFile<a name="GetEffectHandleFromFile"></a>
!!! function "[[nodiscard]] virtual EffectHandle GetEffectHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets an `EffectHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `effects` directory of your Amplitude
        project, not an absolute path from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "effects/echo.amfx"
        EffectHandle handle = amEngine->GetEffectHandleFromFile("echo.amfx");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `EffectHandle` for the given asset's filename, or an invalid handle if no effect
    with that filename was found in any loaded sound bank.
            
    

### GetEntity<a name="GetEntity"></a>
!!! function "[[nodiscard]] virtual Entity GetEntity(AmEntityID id) const = 0"

    
    Returns the `Entity` with the given ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The game entity ID.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Entity` if that one has been registered before,
    otherwise an uninitialized `Entity`.
            
    

### GetEnvironment<a name="GetEnvironment"></a>
!!! function "[[nodiscard]] virtual Environment GetEnvironment(AmEnvironmentID id) const = 0"

    
    Returns the `Environment` with the given ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The game environment ID.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Environment` if that one has been registered before,
    otherwise an uninitialized `Environment`.
            
    

### GetEventHandle<a name="GetEventHandle"></a>
!!! function "[[nodiscard]] virtual EventHandle GetEventHandle(const AmString&amp; name) const = 0"

    
    Gets an `EventHandle` given its name as defined in its asset file (`.amevent`).
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `EventHandle` for the given name, or an invalid handle if no event with that name
    was found in any loaded sound bank.
            
    

!!! function "[[nodiscard]] virtual EventHandle GetEventHandle(AmEventID id) const = 0"

    
    Gets an `EventHandle` given its ID as defined in its asset file (`.amevent`).
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `EventHandle` for the given ID, or an invalid handle if no event with that ID
    was found in any loaded sound bank.
            
    

### GetEventHandleFromFile<a name="GetEventHandleFromFile"></a>
!!! function "[[nodiscard]] virtual EventHandle GetEventHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets an `EventHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `events` directory of your Amplitude
        project, not an absolute path from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "events/gameplay/start_menu.amevent"
        EventHandle handle = amEngine->GetEventHandleFromFile("gameplay/start_menu.amevent");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `EventHandle` for the given asset's filename, or an invalid handle if no event
    with that filename was found in any loaded sound bank.
            
    

### GetFileSystem<a name="GetFileSystem"></a>
!!! function "&#42; GetFileSystem() const"

    
    Gets the file system implementation used by the engine.
    
    
    :material-keyboard-return: **Return**
    :    The current file system implementation used by the engine,
    or `nullptr` if no file system has been set.
            
    

### GetHRIRSphere<a name="GetHRIRSphere"></a>
!!! function "&#42; GetHRIRSphere() const"

    
    Gets the HRIR sphere defined in the loaded engine configuration.
    
    
    :material-keyboard-return: **Return**
    :    The HRIR sphere. If no HRIR sphere is defined, returns `nullptr`.
    
    
    !!! note
         The HRIR sphere is optional and can be null in some cases. If the
        engine does not have an HRIR sphere defined, this function will return `nullptr`.
    
    
    :material-eye-outline: **See**
    :    HRIRSphere
            
    

### GetHRIRSphereSamplingMode<a name="GetHRIRSphereSamplingMode"></a>
!!! function "[[nodiscard]] virtual eHRIRSphereSamplingMode GetHRIRSphereSamplingMode() const = 0"

    
    Gets the HRIR sphere sampling mode defined in the loaded engine configuration.
    
    
    :material-keyboard-return: **Return**
    :    The HRIR sphere sampling mode.
            
    

### GetInstance<a name="GetInstance"></a>
!!! function "[[nodiscard]] static Engine&#42; GetInstance()"

    
    Returns an unique instance of the Amplitude Engine.
             
    
    
    

### GetListener<a name="GetListener"></a>
!!! function "[[nodiscard]] virtual Listener GetListener(AmListenerID id) const = 0"

    
    Returns the `Listener` with the given ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The listener ID.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Listener` if a one with the given ID has been registered before,
    otherwise an uninitialized `Listener`.
            
    

### GetMasterGain<a name="GetMasterGain"></a>
!!! function "[[nodiscard]] virtual AmReal32 GetMasterGain() const = 0"

    
    Gets the mixer master gain.
    
    
    :material-keyboard-return: **Return**
    :    The mixer master gain.
            
    

### GetMaxEntitiesCount<a name="GetMaxEntitiesCount"></a>
!!! function "[[nodiscard]] virtual AmUInt32 GetMaxEntitiesCount() const = 0"

    
    Gets the maximum number of game entities handled by the engine.
    
    This value does not reflect the maximum number of simultaneous sound handled by the engine.
    
    
    :material-keyboard-return: **Return**
    :    The maximum number of game entities.
            
    

### GetMaxListenersCount<a name="GetMaxListenersCount"></a>
!!! function "[[nodiscard]] virtual AmUInt32 GetMaxListenersCount() const = 0"

    
    Gets the maximum number of listeners handled by the engine.
    
    
    :material-keyboard-return: **Return**
    :    The maximum number of listeners.
            
    

### GetMixer<a name="GetMixer"></a>
!!! function "&#42; GetMixer() const"

    
    Gets the mixer instance.
    
    
    :material-keyboard-return: **Return**
    :    The `Amplimix` mixer instance.
            
    

### GetObstructionCoefficientCurve<a name="GetObstructionCoefficientCurve"></a>
!!! function "[[nodiscard]] virtual const Curve&amp; GetObstructionCoefficientCurve() const = 0"

    
    Gets the obstruction coefficient curve, as set in the loaded engine configuration file.
    
    
    :material-keyboard-return: **Return**
    :    The obstruction coefficient curve.
            
    

### GetObstructionGainCurve<a name="GetObstructionGainCurve"></a>
!!! function "[[nodiscard]] virtual const Curve&amp; GetObstructionGainCurve() const = 0"

    
    Gets the obstruction gain curve, as set in the loaded engine configuration file.
    
    
    :material-keyboard-return: **Return**
    :    The obstruction gain curve.
            
    

### GetOcclusionCoefficientCurve<a name="GetOcclusionCoefficientCurve"></a>
!!! function "[[nodiscard]] virtual const Curve&amp; GetOcclusionCoefficientCurve() const = 0"

    
    Gets the occlusion coefficient curve, as set in the loaded engine configuration file.
    
    
    :material-keyboard-return: **Return**
    :    The occlusion coefficient curve.
            
    

### GetOcclusionGainCurve<a name="GetOcclusionGainCurve"></a>
!!! function "[[nodiscard]] virtual const Curve&amp; GetOcclusionGainCurve() const = 0"

    
    Gets the occlusion gain curve, as set in the loaded engine configuration file.
    
    
    :material-keyboard-return: **Return**
    :    The occlusion gain curve.
            
    

### GetPanningMode<a name="GetPanningMode"></a>
!!! function "[[nodiscard]] virtual ePanningMode GetPanningMode() const = 0"

    
    Gets the panning mode defined in the loaded engine configuration.
    
    
    :material-keyboard-return: **Return**
    :    The panning mode.
            
    

### GetPipelineHandle<a name="GetPipelineHandle"></a>
!!! function "[[nodiscard]] virtual PipelineHandle GetPipelineHandle() const = 0"

    
    Gets a `PipelineHandle` from the loaded pipeline asset file (`.ampipeline`).
    
    
    !!! note
         Only one pipeline can be loaded at a time. The loaded pipeline asset is defined in the
        [engine configuration file](../../../project/engine-config.md#pipeline).
    
    
    :material-keyboard-return: **Return**
    :    The `PipelineHandle` for the loaded pipeline. This method should always return a valid handle.
            
    

### GetRoom<a name="GetRoom"></a>
!!! function "[[nodiscard]] virtual Room GetRoom(AmRoomID id) const = 0"

    
    Returns the `Room` with the given ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The room ID.
    
    
    :material-keyboard-return: **Return**
    :    An initialized `Room` if that one has been registered before,
    otherwise an uninitialized `Room`.
            
    

### GetRtpcHandle<a name="GetRtpcHandle"></a>
!!! function "[[nodiscard]] virtual RtpcHandle GetRtpcHandle(const AmString&amp; name) const = 0"

    
    Gets a `RtpcHandle` given its name as defined in its asset file (`.amrtpc`).
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `RtpcHandle` for the given name, or an invalid handle if no RTPC with that name
    was found in any loaded sound bank.
            
    

!!! function "[[nodiscard]] virtual RtpcHandle GetRtpcHandle(AmRtpcID id) const = 0"

    
    Gets an `RtpcHandle` given its ID as defined in its asset file (`.amrtpc`).
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `RtpcHandle` for the given ID, or an invalid handle if no RTPC with that ID
    was found in any loaded sound bank.
            
    

### GetRtpcHandleFromFile<a name="GetRtpcHandleFromFile"></a>
!!! function "[[nodiscard]] virtual RtpcHandle GetRtpcHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets an `RtpcHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `rtpc` directory of your Amplitude
        project, not an absolute path from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "rtpc/music_volume.amrtpc"
        RtpcHandle handle = amEngine->GetRtpcHandleFromFile("music_volume.amrtpc");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `RtpcHandle` for the given asset's filename, or an invalid handle if no RTPC
    with that filename was found in any loaded sound bank.
            
    

### GetSamplesPerStream<a name="GetSamplesPerStream"></a>
!!! function "[[nodiscard]] virtual AmUInt32 GetSamplesPerStream() const = 0"

    
    Get the number of samples to process in one stream, as set in the loaded engine configuration file.
    
    
    :material-keyboard-return: **Return**
    :    The number of samples per stream.
            
    

### GetSoundHandle<a name="GetSoundHandle"></a>
!!! function "[[nodiscard]] virtual SoundHandle GetSoundHandle(const AmString&amp; name) const = 0"

    
    Gets a `SoundHandle` given its name as defined in its asset file (`.amsound`).
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `SoundHandle` for the given name, or an invalid handle if no sound with that name
    was found in any loaded sound bank.
            
    

!!! function "[[nodiscard]] virtual SoundHandle GetSoundHandle(AmSoundID id) const = 0"

    
    Gets a `SoundHandle` given its ID as defined in its asset file (`.amsound`).
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `SoundHandle` for the given ID, or an invalid handle if no sound with that ID
    was found in any loaded sound bank.
            
    

### GetSoundHandleFromFile<a name="GetSoundHandleFromFile"></a>
!!! function "[[nodiscard]] virtual SoundHandle GetSoundHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets a `SoundHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `sounds` directory of your Amplitude
        project, not an absolute path from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "sounds/env/forest/calm_lake_bg.amsound"
        SoundHandle handle = amEngine->GetSoundHandleFromFile("env/forest/calm_lake_bg.amsound");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `SoundHandle` for the given asset's filename, or an invalid handle if no sound
    with that filename was found in any loaded sound bank.
            
    

### GetSoundObjectHandle<a name="GetSoundObjectHandle"></a>
!!! function "[[nodiscard]] virtual SoundObjectHandle GetSoundObjectHandle(const AmString&amp; name) const = 0"

    
    Gets a `SoundObjectHandle` given its name as defined in its asset file.
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `SoundObjectHandle` for the given name, or an invalid handle if no sound object
    with that name was found in any loaded sound bank.
    
    
    !!! note
         The return value can be a `SwitchContainerHandle`, a `CollectionHandle`, or a `SoundHandle`.
                
    

!!! function "[[nodiscard]] virtual SoundObjectHandle GetSoundObjectHandle(AmSoundID id) const = 0"

    
    Gets a `SoundObjectHandle` given its ID as defined in its asset file.
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `SoundObjectHandle` for the given ID, or an invalid handle if no sound object
    with that ID was found in any loaded sound bank.
    
    
    !!! note
         The return value can be a `SwitchContainerHandle`, a `CollectionHandle`, or a `SoundHandle`.
                
    

### GetSoundObjectHandleFromFile<a name="GetSoundObjectHandleFromFile"></a>
!!! function "[[nodiscard]] virtual SoundObjectHandle GetSoundObjectHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets a `SoundObjectHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `sounds`, `collections`,
        or `switch_containers` directories of your Amplitude project, not an absolute path
        from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "sounds/env/forest/calm_lake_bg.amsound"
        // Note that the return value in this case is a indeed a `SoundHandle`
        SoundObjectHandle handle = amEngine->GetSoundObjectHandleFromFile("env/forest/calm_lake_bg.amsound");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `SoundObjectHandle` for the given asset's filename, or an invalid handle if no sound object
    with that filename was found in any loaded sound bank.
    
    
    !!! note
         The return value can be a `SwitchContainerHandle`, a `CollectionHandle`, or a `SoundHandle`.
                
    

### GetSoundSpeed<a name="GetSoundSpeed"></a>
!!! function "[[nodiscard]] virtual AmReal32 GetSoundSpeed() const = 0"

    
    Gets the speed of sound, as set in the loaded engine configuration file.
    
    
    :material-keyboard-return: **Return**
    :    The speed of sound.
            
    

### GetSwitchContainerHandle<a name="GetSwitchContainerHandle"></a>
!!! function "[[nodiscard]] virtual SwitchContainerHandle GetSwitchContainerHandle(const AmString&amp; name) const = 0"

    
    Gets a `SwitchContainerHandle` given its name as defined in its asset file (`.amswitchcontainer`).
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `SwitchContainerHandle` for the given name, or an invalid handle if no switch container
    with that name was found in any loaded sound bank.
            
    

!!! function "[[nodiscard]] virtual SwitchContainerHandle GetSwitchContainerHandle(AmSwitchContainerID id) const = 0"

    
    Gets a `SwitchContainerHandle` given its ID as defined in its asset file (`.amswitchcontainer`).
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `SwitchContainerHandle` for the given ID, or an invalid handle if no switch container
    with that ID was found in any loaded sound bank.
            
    

### GetSwitchContainerHandleFromFile<a name="GetSwitchContainerHandleFromFile"></a>
!!! function "[[nodiscard]] virtual SwitchContainerHandle GetSwitchContainerHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets a `SwitchContainerHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `switch_containers` directory of your Amplitude
        project, not an absolute path from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "switch_containers/footsteps.amswitchcontainer"
        SwitchContainerHandle handle = amEngine->GetSwitchContainerHandleFromFile("footsteps.amswitchcontainer");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `SwitchContainerHandle` for the given asset's filename, or an invalid handle if no switch container
    with that filename was found in any loaded sound bank.
            
    

### GetSwitchHandle<a name="GetSwitchHandle"></a>
!!! function "[[nodiscard]] virtual SwitchHandle GetSwitchHandle(const AmString&amp; name) const = 0"

    
    Gets a `SwitchHandle` given its name as defined in its asset file (`.amswitch`).
    
    
    :material-location-enter: **Parameter** `name`
    :    The unique name as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `SwitchHandle` for the given name, or an invalid handle if no switch with that name
    was found in any loaded sound bank.
            
    

!!! function "[[nodiscard]] virtual SwitchHandle GetSwitchHandle(AmSwitchID id) const = 0"

    
    Gets a `SwitchHandle` given its ID as defined in its asset file (`.amswitch`).
    
    
    :material-location-enter: **Parameter** `id`
    :    The unique ID as defined in the asset file.
    
    
    :material-keyboard-return: **Return**
    :    The `SwitchHandle` for the given ID, or an invalid handle if no switch with that ID
    was found in any loaded sound bank.
            
    

### GetSwitchHandleFromFile<a name="GetSwitchHandleFromFile"></a>
!!! function "[[nodiscard]] virtual SwitchHandle GetSwitchHandleFromFile(const AmOsString&amp; filename) const = 0"

    
    Gets a `SwitchHandle` given its asset's filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The asset's filename.
    
    
    !!! note
         The asset's filename should be relative path from the `switches` directory of your Amplitude
        project, not an absolute path from the filesystem base path.
    
    
    !!! example
        
        ```cpp
        // Assuming the asset file is located in "switches/env/surfaces.amswitch"
        SwitchHandle handle = amEngine->GetSwitchHandleFromFile("env/surfaces.amswitch");
        ```
    
    
    :material-keyboard-return: **Return**
    :    The `SwitchHandle` for the given asset's filename, or an invalid handle if no switch
    with that filename was found in any loaded sound bank.
            
    

### GetTotalTime<a name="GetTotalTime"></a>
!!! function "[[nodiscard]] virtual AmTime GetTotalTime() const = 0"

    
    Gets the total elapsed time in milliseconds since the start of the engine.
    
    
    :material-keyboard-return: **Return**
    :    The total elapsed time in milliseconds since the start of the engine.
            
    

### Initialize<a name="Initialize"></a>
!!! function "virtual bool Initialize(const AmOsString&amp; configFile) = 0"

    
    Initializes the Amplitude engine.
    
    
    :material-location-enter: **Parameter** `configFile`
    :    The path to the configuration file.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the engine has been successfully initialized, `false` otherwise.
            
    

### IsGameTrackingEnvironmentAmounts<a name="IsGameTrackingEnvironmentAmounts"></a>
!!! function "[[nodiscard]] virtual bool IsGameTrackingEnvironmentAmounts() const = 0"

    
    Checks whether the game is tracking environment amounts himself.
    
    
    :material-keyboard-return: **Return**
    :    Whether the game is tracking environment amounts.
            
    

### IsInitialized<a name="IsInitialized"></a>
!!! function "[[nodiscard]] virtual bool IsInitialized() const = 0"

    
    Checks if the Amplitude engine has been successfully initialized.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the engine has been successfully initialized, `false` otherwise.
            
    

### IsMuted<a name="IsMuted"></a>
!!! function "[[nodiscard]] virtual bool IsMuted() const = 0"

    
    Checks whether the engine is currently muted.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the engine is muted, `false` otherwise.
            
    

### IsPaused<a name="IsPaused"></a>
!!! function "[[nodiscard]] virtual bool IsPaused() const = 0"

    
    Checks whether the engine is currently paused.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the engine is currently paused, `false` otherwise.
            
    

### LoadPlugin<a name="LoadPlugin"></a>
!!! function "static AmVoidPtr LoadPlugin(const AmOsString&amp; pluginLibraryName)"

    
    Loads a plugin library from the given path.
    
    
    :material-location-enter: **Parameter** `pluginLibraryName`
    :    The name of the plugin library to load.
    
    
    :material-keyboard-return: **Return**
    :    A handle to the loaded plugin library.
            
    

### LoadSoundBank<a name="LoadSoundBank"></a>
!!! function "virtual bool LoadSoundBank(const AmOsString&amp; filename) = 0"

    
    Loads a sound bank from a binary asset file (`.ambank`).
    
    This method queues the sound files in that sound bank for loading. Call
    [`StartLoadSoundFiles()`](#StartLoadSoundFiles) to trigger the loading
    of sound files on a separate thread.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The path to the sound bank asset file.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the sound bank is successfully loaded, `false` otherwise.
            
    

!!! function "virtual bool LoadSoundBank(const AmOsString&amp; filename, AmBankID&amp; outID) = 0"

    
    Loads a sound bank from a binary asset file (`.ambank`).
    
    This method queues the sound files in that sound bank for loading. Call
    [`StartLoadSoundFiles()`](#StartLoadSoundFiles) to trigger the loading
    of sound files on a separate thread.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The path to the sound bank asset file.
        
    :material-location-exit: **Parameter** `outID`
    :    The ID of the loaded sound bank.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the sound bank is successfully loaded, `false` otherwise.
            
    

### LoadSoundBankFromMemory<a name="LoadSoundBankFromMemory"></a>
!!! function "virtual bool LoadSoundBankFromMemory(const char&#42; fileData) = 0"

    
    Loads a sound bank from memory.
    
    This method queues the sound files in that sound bank for loading. Call
    [`StartLoadSoundFiles()`](#StartLoadSoundFiles) to trigger the loading
    of sound files on a separate thread.
    
    
    :material-location-enter: **Parameter** `fileData`
    :    The sound bank data to be loaded.
    
    
    !!! note
         The `fileData` pointer should be null terminated.
    
    
    !!! warning
         The `fileData` pointer should remain valid until the sound bank is unloaded.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the sound bank is successfully loaded, `false` otherwise.
            
    

!!! function "virtual bool LoadSoundBankFromMemory(const char&#42; fileData, AmBankID&amp; outID) = 0"

    
    Loads a sound bank from memory.
    
    This method queues the sound files in that sound bank for loading. Call
    [`StartLoadSoundFiles()`](#StartLoadSoundFiles) to trigger the loading
    of sound files on a separate thread.
    
    
    :material-location-enter: **Parameter** `fileData`
    :    The sound bank data to be loaded.
        
    :material-location-exit: **Parameter** `outID`
    :    The ID of the loaded sound bank.
    
    
    !!! note
         The `fileData` pointer should be null terminated.
    
    
    !!! warning
         The `fileData` pointer should remain valid until the sound bank is unloaded.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the sound bank is successfully loaded, `false` otherwise.
            
    

### LoadSoundBankFromMemoryView<a name="LoadSoundBankFromMemoryView"></a>
!!! function "virtual bool LoadSoundBankFromMemoryView(AmVoidPtr ptr, AmSize size) = 0"

    
    Loads a sound bank from memory.
    
    This method queues the sound files in that sound bank for loading. Call
    [`StartLoadSoundFiles()`](#StartLoadSoundFiles) to trigger the loading
    of sound files on a separate thread.
    
    
    :material-location-enter: **Parameter** `ptr`
    :    The pointer to the sound bank data to be loaded.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the memory to read.
    
    
    !!! note
         The `fileData` pointer should be null terminated.
    
    
    !!! warning
         The `fileData` pointer should remain valid until the sound bank is unloaded.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the sound bank is successfully loaded, `false` otherwise.
            
    

!!! function "virtual bool LoadSoundBankFromMemoryView(AmVoidPtr ptr, AmSize size, AmBankID&amp; outID) = 0"

    
    Loads a sound bank from memory.
    
    This method queues the sound files in that sound bank for loading. Call
    [`StartLoadSoundFiles()`](#StartLoadSoundFiles) to trigger the loading
    of sound files on a separate thread.
    
    
    :material-location-enter: **Parameter** `ptr`
    :    The pointer to the sound bank data to be loaded.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the memory to read.
        
    :material-location-exit: **Parameter** `outID`
    :    The ID of the loaded sound bank.
    
    
    !!! note
         The `ptr` pointer should be null terminated.
    
    
    !!! warning
         The `ptr` pointer should remain valid until the sound bank is unloaded.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the sound bank is successfully loaded, `false` otherwise.
            
    

### OnNextFrame<a name="OnNextFrame"></a>
!!! function "virtual void OnNextFrame(std::function&lt;void(AmTime delta)&gt; callback) const = 0"

    
    Executes the given callback on the next frame.
    
    
    !!! note
         The given callback will be executed at the *beginning* of the next frame,
        before doing the actual frame update.
    
    
    :material-location-enter: **Parameter** `callback`
    :    The callback to be called when the next frame is ready.
                
    

### Pause<a name="Pause"></a>
!!! function "virtual void Pause(bool pause) const = 0"

    
    Pauses or resumes all playing sounds and streams.
    
    
    :material-location-enter: **Parameter** `pause`
    :    Whether to pause or resume the engine.
                
    

### Play<a name="Play"></a>
!!! function "[[nodiscard]] virtual Channel Play(SwitchContainerHandle handle) const = 0"

    
    Plays a switch container associated with the given handle in the World scope.
    
    This method is recommended for switch containers with spatialization disabled, since
    no positional information need to be provided.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the switch container to play.
    
    
    :material-keyboard-return: **Return**
    :    The channel the switch container is being played on. If the switch container could not be
    played, or the given handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SwitchContainerHandle handle, const AmVec3&amp; location) const = 0"

    
    Plays a switch container associated with the given handle in the World scope.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the switch container to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which switch container should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the switch container is being played on. If the switch container could not be
    played, or the given handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SwitchContainerHandle handle, const AmVec3&amp; location, AmReal32 userGain) const = 0"

    
    Plays a switch container associated with the given handle in the World scope.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the switch container to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the switch container should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the switch container is being played on. If the switch container could not be
    played, or the given handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SwitchContainerHandle handle, const Entity&amp; entity) const = 0"

    
    Plays a switch container associated with the given handle in an Entity scope.
    
    
    !!! note
         Switch containers played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the switch container to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the switch container should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the switch container is being played on. If the switch container could not be
    played, the given handle is invalid, or the given entity is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SwitchContainerHandle handle, const Entity&amp; entity, AmReal32 userGain) const = 0"

    
    Plays a switch container associated with the given handle in an Entity scope.
    
    
    !!! note
         Switch containers played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the switch container to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the switch container should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the switch container is being played on. If the switch container could not be
    played, the given handle is invalid, or the given entity is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(CollectionHandle handle) const = 0"

    
    Plays a collection associated with the given handle in the World scope.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the collection to play.
    
    
    :material-keyboard-return: **Return**
    :    The channel the collection is being played on. If the collection could not be
    played, or the handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(CollectionHandle handle, const AmVec3&amp; location) const = 0"

    
    Plays a collection associated with the given handle in the World scope.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the collection to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the collection should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the collection is being played on. If the collection could not be
    played, or the handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(CollectionHandle handle, const AmVec3&amp; location, AmReal32 userGain) const = 0"

    
    Plays a collection associated with the given handle in the World scope.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the collection to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the collection should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the collection is being played on. If the collection could not be
    played, or the handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(CollectionHandle handle, const Entity&amp; entity) const = 0"

    
    Plays a collection associated with the given handle in the Entity scope.
    
    
    !!! note
         Collections played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the collection to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the collection should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the collection is being played on. If the collection could not be
    played, the given handle is invalid, or the given entity is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(CollectionHandle handle, const Entity&amp; entity, AmReal32 userGain) const = 0"

    
    Plays a collection associated with the given handle in an Entity scope.
    
    
    !!! note
         Collections played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the collection to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the collection should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the collection is being played on. If the collection could not be
    played, the given handle is invalid, or the given entity is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SoundHandle handle) const = 0"

    
    Plays a sound associated with the given handle in the World scope.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the sound to play.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound is being played on. If the sound could not be
    played, the given handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SoundHandle handle, const AmVec3&amp; location) const = 0"

    
    Plays a sound associated with the given handle in the World scope.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the sound to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the sound should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound is being played on. If the sound could not be
    played, the given handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SoundHandle handle, const AmVec3&amp; location, AmReal32 userGain) const = 0"

    
    Plays a sound associated with the given handle in the World scope.
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the sound to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the sound should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound is being played on. If the sound could not be
    played, the given handle is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SoundHandle handle, const Entity&amp; entity) const = 0"

    
    Plays a sound associated with the given sound handle in an Entity scope.
    
    
    !!! note
         Sounds played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the sound to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the sound should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound is being played on. If the sound could not be
    played, the given handle is invalid, or the given entity is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(SoundHandle handle, const Entity&amp; entity, AmReal32 userGain) const = 0"

    
    Plays a sound associated with the given sound handle in an Entity.
    
    
    !!! note
         Sounds played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `handle`
    :    A handle to the sound to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the sound should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound is being played on. If the sound could not be
    played, the given handle is invalid, or the given entity is invalid, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(const AmString&amp; name) const = 0"

    
    Plays a sound object associated with the given name in the World scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        name as using the name requires an internal lookup.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the sound object to play.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, or an object with the given name was not found, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(const AmString&amp; name, const AmVec3&amp; location) const = 0"

    
    Plays a sound object associated with the given name in the World scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        name as using the name requires an internal lookup.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the sound object to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the sound should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, or an object with the given name was not found, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(const AmString&amp; name, const AmVec3&amp; location, AmReal32 userGain) const = 0"

    
    Plays a sound object associated with the given name in the World scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        name as using the name requires an internal lookup.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the sound object to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the sound should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, or an object with the given name was not found, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(const AmString&amp; name, const Entity&amp; entity) const = 0"

    
    Plays a sound object associated with the given name in an Entity scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        name as using the name requires an internal lookup.
    
    
    !!! note
         Sound objects played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the sound object to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the sound object should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, an object with the given name was not found, or the entity is invalid,
    an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(const AmString&amp; name, const Entity&amp; entity, AmReal32 userGain) const = 0"

    
    Plays a sound object associated with the given name in an Entity scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        name as using the name requires an internal lookup.
    
    
    !!! note
         Sound objects played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the sound object to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the sound object should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, an object with the given name was not found, or the entity is invalid,
    an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(AmObjectID id) const = 0"

    
    Plays a sound object associated with the given ID in the  World scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        ID as using the ID requires an internal lookup.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the sound object to play.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, or an object with the given ID was not found, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(AmObjectID id, const AmVec3&amp; location) const = 0"

    
    Plays a sound object associated with the given ID in the World scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        ID as using the ID requires an internal lookup.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the sound object to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the sound object should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, or an object with the given ID was not found, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(AmObjectID id, const AmVec3&amp; location, AmReal32 userGain) const = 0"

    
    Plays a sound object associated with the given ID in the World scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        ID as using the ID requires an internal lookup.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the sound object to play.
        
    :material-location-enter: **Parameter** `location`
    :    The location at which the sound object should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, or an object with the given ID was not found, an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(AmObjectID id, const Entity&amp; entity) const = 0"

    
    Plays a sound object associated with the given ID in an Entity scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        ID as using the ID requires an internal lookup.
    
    
    !!! note
         Sound objects played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the sound object to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the sound object should be played.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, an object with the given ID was not found, or the entity is invalid,
    an invalid `Channel` is returned.
            
    

!!! function "[[nodiscard]] virtual Channel Play(AmObjectID id, const Entity&amp; entity, AmReal32 userGain) const = 0"

    
    Plays a sound object associated with the given ID in an Entity scope.
    
    
    !!! tip
         Playing a sound object with its handle is faster than using the
        ID as using the ID requires an internal lookup.
    
    
    !!! note
         Sound objects played using this method should have been set in the `Entity` scope
        from their asset file. See more [here](../../../project/sound-object.md#scope).
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the sound object to play.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which the sound object should be played.
        
    :material-location-enter: **Parameter** `userGain`
    :    The gain of the sound. Must be in the range [0, 1].
    
    
    !!! note
         The `userGain` parameter will not be used directly, but instead, it will be used in the final
        gain computation, which may include other factors like the attenuation and the master gain.
    
    
    :material-keyboard-return: **Return**
    :    The channel the sound object is being played on. If the object could not be
    played, an object with the given ID was not found, or the entity is invalid,
    an invalid `Channel` is returned.
            
    

### RegisterDefaultPlugins<a name="RegisterDefaultPlugins"></a>
!!! function "static bool RegisterDefaultPlugins()"

    
    Register all default plugins.
             
    
    
    

### RemoveEntity<a name="RemoveEntity"></a>
!!! function "virtual void RemoveEntity(const Entity&#42; entity) const = 0"

    
    Removes an `Entity`.
    
    
    :material-location-enter: **Parameter** `entity`
    :    The game entity to be removed.
                
    

!!! function "virtual void RemoveEntity(AmEntityID id) const = 0"

    
    Removes an `Entity` given its ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the game entity to be removed.
                
    

### RemoveEnvironment<a name="RemoveEnvironment"></a>
!!! function "virtual void RemoveEnvironment(const Environment&#42; environment) const = 0"

    
    Removes an `Environment`.
    
    
    :material-location-enter: **Parameter** `environment`
    :    The game environment to be removed.
                
    

!!! function "virtual void RemoveEnvironment(AmEnvironmentID id) const = 0"

    
    Removes an `Environment` given its ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the game environment to be removed.
                
    

### RemoveListener<a name="RemoveListener"></a>
!!! function "virtual void RemoveListener(AmListenerID id) const = 0"

    
    Removes a `Listener` given its ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the `Listener` to be removed.
                
    

!!! function "virtual void RemoveListener(const Listener&#42; listener) const = 0"

    
    Removes a `Listener` given its handle.
    
    
    :material-location-enter: **Parameter** `listener`
    :    The `Listener` to be removed.
                
    

### RemovePluginSearchPath<a name="RemovePluginSearchPath"></a>
!!! function "static void RemovePluginSearchPath(const AmOsString&amp; path)"

    
    Removes a path from the plugins search paths list.
    
    
    :material-location-enter: **Parameter** `path`
    :    The path to remove from the plugins search path list.
                
    

### RemoveRoom<a name="RemoveRoom"></a>
!!! function "virtual void RemoveRoom(const Room&#42; room) const = 0"

    
    Removes a `Room`.
    
    
    :material-location-enter: **Parameter** `room`
    :    The room to be removed.
                
    

!!! function "virtual void RemoveRoom(AmRoomID id) const = 0"

    
    Removes a `Room` given its ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the room to be removed.
                
    

### SetDefaultListener<a name="SetDefaultListener"></a>
!!! function "virtual void SetDefaultListener(const Listener&#42; listener) = 0"

    
    Sets the default sound listener.
    
    This method will set the default listener that will render every played sound sources.
    
    
    !!! note
         This method takes effect only if the
        [`listener_fetch_mode`](../../../project/engine-config.md#listener_fetch_mode)
        engine setting is set to `Default`.
    
    
    :material-location-enter: **Parameter** `listener`
    :    A valid and initialized `Listener` instance.
                
    

!!! function "virtual void SetDefaultListener(AmListenerID id) = 0"

    
    Sets the default sound listener.
    
    This method will set the default listener that will render every played sound sources.
    
    
    !!! note
         This method takes effect only if the
        [`listener_fetch_mode`](../../../project/engine-config.md#listener_fetch_mode)
        engine setting is set to `Default`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of a valid and registered `Listener`.
                
    

### SetFileSystem<a name="SetFileSystem"></a>
!!! function "virtual void SetFileSystem(FileSystem&#42; fs) = 0"

    
    Sets a file system implementation to be used by the engine.
    
    
    :material-location-enter: **Parameter** `fs`
    :    The file system implementation.
                
    

### SetMasterGain<a name="SetMasterGain"></a>
!!! function "virtual void SetMasterGain(AmReal32 gain) const = 0"

    
    Adjusts the master gain of the mixer.
    
    
    :material-location-enter: **Parameter** `gain`
    :    The master gain.
                
    

### SetMute<a name="SetMute"></a>
!!! function "virtual void SetMute(bool mute) const = 0"

    
    Mutes the engine, but keep processing audio.
    
    
    :material-location-enter: **Parameter** `mute`
    :    Whether to mute or unmute the engine.
                
    

### SetRtpcValue<a name="SetRtpcValue"></a>
!!! function "virtual void SetRtpcValue(RtpcHandle handle, double value) const = 0"

    
    Sets the value of a `RTPC`.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The handle of the `RTPC` to update.
        
    :material-location-enter: **Parameter** `value`
    :    The value to set to the `RTPC`.
                
    

!!! function "virtual void SetRtpcValue(AmRtpcID id, double value) const = 0"

    
    Sets the value of a `RTPC`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the `RTPC` to update.
        
    :material-location-enter: **Parameter** `value`
    :    The value to set to the `RTPC`.
                
    

!!! function "virtual void SetRtpcValue(const AmString&amp; name, double value) const = 0"

    
    Sets the value of a `RTPC`.
    
    
    :material-location-enter: **Parameter** `name`
    :    THe name of the `RTPC` to update.
        
    :material-location-enter: **Parameter** `value`
    :    The value to set to the `RTPC`.
                
    

### SetSwitchState<a name="SetSwitchState"></a>
!!! function "virtual void SetSwitchState(SwitchHandle handle, AmObjectID stateId) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The handle of the `Switch`.
        
    :material-location-enter: **Parameter** `stateId`
    :    The ID of the active state to set.
                
    

!!! function "virtual void SetSwitchState(SwitchHandle handle, const AmString&amp; stateName) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The handle of the `Switch`.
        
    :material-location-enter: **Parameter** `stateName`
    :    The name of the active state to set.
                
    

!!! function "virtual void SetSwitchState(SwitchHandle handle, const SwitchState&amp; state) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The handle of the `Switch`.
        
    :material-location-enter: **Parameter** `state`
    :    The active state to set.
                
    

!!! function "virtual void SetSwitchState(AmSwitchID id, AmObjectID stateId) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the `Switch` to update.
        
    :material-location-enter: **Parameter** `stateId`
    :    The ID of the active state to set.
                
    

!!! function "virtual void SetSwitchState(AmSwitchID id, const AmString&amp; stateName) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the `Switch` to update.
        
    :material-location-enter: **Parameter** `stateName`
    :    The name of the active state to set.
                
    

!!! function "virtual void SetSwitchState(AmSwitchID id, const SwitchState&amp; state) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `id`
    :    The ID of the `Switch` to update.
        
    :material-location-enter: **Parameter** `state`
    :    The active state to set.
                
    

!!! function "virtual void SetSwitchState(const AmString&amp; name, AmObjectID stateId) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the `Switch` to update.
        
    :material-location-enter: **Parameter** `stateId`
    :    The ID of the active state to set.
                
    

!!! function "virtual void SetSwitchState(const AmString&amp; name, const AmString&amp; stateName) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the `Switch` to update.
        
    :material-location-enter: **Parameter** `stateName`
    :    The name of the active state to set.
                
    

!!! function "virtual void SetSwitchState(const AmString&amp; name, const SwitchState&amp; state) const = 0"

    
    Sets the active state of the defined `Switch`.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the `Switch` to update.
        
    :material-location-enter: **Parameter** `state`
    :    The active state to set.
                
    

### StartCloseFileSystem<a name="StartCloseFileSystem"></a>
!!! function "virtual void StartCloseFileSystem() = 0"

    
    Closes the file system, usually in a separate thread.
             
    
    
    

### StartLoadSoundFiles<a name="StartLoadSoundFiles"></a>
!!! function "virtual void StartLoadSoundFiles() = 0"

    
    Starts the loading of sound files referenced in loaded sound banks.
    
    This process will run in another thread. You must call [`TryFinalizeLoadSoundFiles()`](#TryFinalizeLoadSoundFiles) to
    know when the loading has completed, and to automaticaly release used resources.
            
    

### StartOpenFileSystem<a name="StartOpenFileSystem"></a>
!!! function "virtual void StartOpenFileSystem() = 0"

    
    Opens the file system, usually in a separate thread.
             
    
    
    

### StopAll<a name="StopAll"></a>
!!! function "virtual void StopAll() const = 0"

    
    Stops all playing sound objects.
    
    This is the equivalent of calling `Stop()` on all generated channels.
            
    

### Trigger<a name="Trigger"></a>
!!! function "[[nodiscard]] virtual EventCanceler Trigger(EventHandle handle, const Entity&amp; entity) const = 0"

    
    Triggers the event associated to the given handle.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The handle of the event to trigger.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which trigger the event.
    
    
    :material-keyboard-return: **Return**
    :    An `EventCanceler` object which may be used to cancel the execution of the event.
            
    

!!! function "[[nodiscard]] virtual EventCanceler Trigger(const AmString&amp; name, const Entity&amp; entity) const = 0"

    
    Triggers the event associated to the given handle.
    
    
    !!! tip
         Triggering an event with its `EventHandle` is faster than using the
        event name as using the name requires an internal lookup.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of event to trigger.
        
    :material-location-enter: **Parameter** `entity`
    :    The entity on which trigger the event.
    
    
    :material-keyboard-return: **Return**
    :    An `EventCanceler` object which may be used to cancel the execution of the event.
            
    

### TryFinalizeCloseFileSystem<a name="TryFinalizeCloseFileSystem"></a>
!!! function "virtual bool TryFinalizeCloseFileSystem() = 0"

    
    Checks if the file system has been fully closed.
    
    This method is helpful when the file system implementation is closed asynchronously. You
    can use this method to wait until the file system is fully closed.
    
    
    !!! example
        
        ```cpp
        // Close the file system
        amEngine->StartCloseFileSystem();
        while (!amEngine->TryFinalizeCloseFileSystem()) {
            // Wait until the file system is fully closed
            Thread::Sleep(100);
        }
        // The file system is now closed
        //...
        ```
    
    
    :material-keyboard-return: **Return**
    :    `true` if the file system has been fully closed, `false` otherwise.
            
    

### TryFinalizeLoadSoundFiles<a name="TryFinalizeLoadSoundFiles"></a>
!!! function "virtual bool TryFinalizeLoadSoundFiles() = 0"

    
    Checks if the loading of sound files has been completed, and releases used resources.
    
    
    !!! note
         This method should be called after calling [`StartLoadSoundFiles()`.](#StartLoadSoundFiles)
    
    
    !!! example
        
        ```cpp
        // Start loading sound files
        amEngine->StartLoadSoundFiles();
        while (!amEngine->TryFinalizeLoadSoundFiles()) {
            // Wait for loading to complete
            Thread::Sleep(100);
        }
        // Sound files have been loaded, and used resources has been released
        ```
    
    
    :material-keyboard-return: **Return**
    :    `true` when the sound files have been successfully loaded, `false` otherwise.
            
    

### TryFinalizeOpenFileSystem<a name="TryFinalizeOpenFileSystem"></a>
!!! function "virtual bool TryFinalizeOpenFileSystem() = 0"

    
    Checks if the file system has been fully loaded.
    
    This method is helpful when the file system implementation is loaded asynchronously. You
    can use this method to wait until the file system is fully loaded before using it.
    
    
    !!! example
        
        ```cpp
        // Open the file system
        amEngine->StartOpenFileSystem();
        while (!amEngine->TryFinalizeOpenFileSystem()) {
            // Wait until the file system is fully loaded
            Thread::Sleep(100);
        }
        // Use the file system now
        //...
        ```
    
    
    :material-keyboard-return: **Return**
    :    `true` if the file system has been fully loaded, `false` otherwise.
            
    

### UnloadSoundBank<a name="UnloadSoundBank"></a>
!!! function "virtual void UnloadSoundBank(const AmOsString&amp; filename) = 0"

    
    Unloads a sound bank given its filename.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The file to unload.
                
    

!!! function "virtual void UnloadSoundBank(AmBankID id) = 0"

    
    Unloads a sound bank given its ID.
    
    
    :material-location-enter: **Parameter** `id`
    :    The sound bank id to unload.
                
    

### UnloadSoundBanks<a name="UnloadSoundBanks"></a>
!!! function "virtual void UnloadSoundBanks() = 0"

    
    Unloads all the loaded sound banks.
             
    
    
    

### UnregisterDefaultPlugins<a name="UnregisterDefaultPlugins"></a>
!!! function "static bool UnregisterDefaultPlugins()"

    
    Unregister all default plugins.
             
    
    
    

### Version<a name="Version"></a>
!!! function "&#42; Version() const"

    
    Gets the version structure.
    
    
    :material-keyboard-return: **Return**
    :    The version string structure
            
    

### WaitUntilFrames<a name="WaitUntilFrames"></a>
!!! function "virtual void WaitUntilFrames(AmUInt64 frameCount) const = 0"

    
    Waits until the specified number of frames are ready.
    
    This method blocks the current thread until the specified number of frames are ready.
    
    
    :material-location-enter: **Parameter** `frameCount`
    :    The number of frames to wait until.
                
    

### WaitUntilNextFrame<a name="WaitUntilNextFrame"></a>
!!! function "virtual void WaitUntilNextFrame() const = 0"

    
    Waits until the next frame is ready.
    
    This method blocks the current thread until the next frame is ready.
            
    

