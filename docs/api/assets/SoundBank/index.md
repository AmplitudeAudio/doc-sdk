---
title: SoundBank
description: Amplitude Sound Bank Asset.
generator: doxide
---


# SoundBank

**class  SoundBank**


Amplitude Sound Bank Asset.

A Sound Bank is a group of Amplitude assets, registered in a single binary. This way allows
you to pack the needed data for your game as you want (ie. sound banks per levels). A sound bank
need to be loaded by the Engine using `#!cpp Engine::LoadSoundBank()` before to play sounds and
trigger events inside it. When the sound bank data should be released (ie. changing the level, closing
the game, etc.), you need to unload the sound bank using `#!cpp Engine::UnloadSoundBank()`.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [SoundBank](#SoundBank) | Creates an uninitialized `SoundBank`.  |
| [SoundBank](#SoundBank) | Creates a sound bank from the given source file. |
| [Initialize](#Initialize) | Initializes the sound bank by loading all the packed data. |
| [InitializeFromMemory](#InitializeFromMemory) | Initializes the sound bank by loading all the packed data. |
| [Deinitialize](#Deinitialize) | Unloads the sound bank from the Engine. |
| [GetId](#GetId) | Returns the unique ID of this SoundBank. |
| [GetName](#GetName) | Returns the name of this SoundBank. |
| [GetSoundBankDefinition](#GetSoundBankDefinition) | Returns the definition data used to initialize this SoundBank. |
| [GetRefCounter](#GetRefCounter) | Gets the references counter of this instance. |
| [LoadSoundFiles](#LoadSoundFiles) | Load the sound files referenced in the sound bank. |

## Function Details

### Deinitialize<a name="Deinitialize"></a>
!!! function "void Deinitialize(Engine&#42; engine)"

    
    Unloads the sound bank from the Engine.
    
    
    :material-location-enter: **Parameter** `engine`
    :    The engine instance from which unload the sound bank.
                
    

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmBankID GetId() const"

    
    Returns the unique ID of this SoundBank.
    
    
    :material-keyboard-return: **Return**
    :    The SoundBank unique ID.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Returns the name of this SoundBank.
    
    
    :material-keyboard-return: **Return**
    :    The SoundBank name.
            
    

### GetRefCounter<a name="GetRefCounter"></a>
!!! function "RefCounter&#42; GetRefCounter()"

    
    Gets the references counter of this instance.
    
    
    :material-keyboard-return: **Return**
    :    The references counter.
            
    

### GetSoundBankDefinition<a name="GetSoundBankDefinition"></a>
!!! function "[[nodiscard]] const SoundBankDefinition&#42; GetSoundBankDefinition() const"

    
    Returns the definition data used to initialize this SoundBank.
    
    
    :material-keyboard-return: **Return**
    :    The sound bank definition data.
            
    

### Initialize<a name="Initialize"></a>
!!! function "bool Initialize(const AmOsString&amp; filename, Engine&#42; engine)"

    
    Initializes the sound bank by loading all the packed data.
    
    
    :material-location-enter: **Parameter** `filename`
    :    The path to the sound bank file.
        
    :material-location-enter: **Parameter** `engine`
    :    The engine instance in which load the sound bank.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the operation succeeds, `false` otherwise.
            
    

### InitializeFromMemory<a name="InitializeFromMemory"></a>
!!! function "bool InitializeFromMemory(const char&#42; fileData, Engine&#42; engine)"

    
    Initializes the sound bank by loading all the packed data.
    
    
    :material-location-enter: **Parameter** `fileData`
    :    The sound bank file content.
        
    :material-location-enter: **Parameter** `engine`
    :    The engine instance in which load the sound bank.
    
    
    :material-keyboard-return: **Return**
    :    `true` when the operation succeeds, `false` otherwise.
            
    

### LoadSoundFiles<a name="LoadSoundFiles"></a>
!!! function "void LoadSoundFiles(const Engine&#42; engine)"

    
    Load the sound files referenced in the sound bank.
    
    
    :material-location-enter: **Parameter** `engine`
    :    The engine instance from which load the sound files.
    
    
    !!! warning
         This method should not be called directly. It is called automatically by the `Engine` with
        the `#!cpp Engine::StartLoadSoundFiles()` method.
                
    

### SoundBank<a name="SoundBank"></a>
!!! function "SoundBank()"

    
    Creates an uninitialized `SoundBank`.
             
    
    
    

!!! function "explicit SoundBank(const AmString&amp; source)"

    
    Creates a sound bank from the given source file.
    
    
    !!! warning
         This constructor is for internal usage only.
                
    

