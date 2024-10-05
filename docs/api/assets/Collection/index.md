---
title: Collection
description: Amplitude Collection Asset.
generator: doxide
---


# Collection

**class  Collection : public SoundObject , public Asset&lt;AmCollectionID&gt;**


Amplitude Collection Asset.

A `Collection` is a container sound object that group multiple sounds over the same name. Only
one sound can be playing at a time in the same collection, and the sound picked for playback
is chosen by the collection's `Scheduler`.


:material-eye-outline: **See**
:    [SoundObject](../../engine/SoundObject/index.md)


    


## Functions

| Name | Description |
| ---- | ----------- |
| [SelectFromWorld](#SelectFromWorld) | Returns a Sound from this collection from the World scope. |
| [SelectFromEntity](#SelectFromEntity) | Returns a Sound from this collection from an Entity scope. |
| [ResetEntityScopeScheduler](#ResetEntityScopeScheduler) | Resets the internal state of the scheduler running for the given Entity. |
| [ResetWorldScopeScheduler](#ResetWorldScopeScheduler) | Resets the internal state of the scheduler running for the World.  |
| [GetSounds](#GetSounds) | Returns the list of Sound objects referenced in this collection. |

## Function Details

### GetSounds<a name="GetSounds"></a>
!!! function "[[nodiscard]] virtual const std::vector&lt;AmSoundID&gt;&amp; GetSounds() const = 0"

    
    Returns the list of Sound objects referenced in this collection.
    
    
    :material-keyboard-return: **Return**
    :    The list of Sound IDs.
            
    

### ResetEntityScopeScheduler<a name="ResetEntityScopeScheduler"></a>
!!! function "virtual void ResetEntityScopeScheduler(const Entity&amp; entity) = 0"

    
    Resets the internal state of the scheduler running for the given Entity.
    
    
    :material-location-enter: **Parameter** `entity`
    :    The entity for which reset the scheduler state.
                
    

### ResetWorldScopeScheduler<a name="ResetWorldScopeScheduler"></a>
!!! function "virtual void ResetWorldScopeScheduler() = 0"

    
    Resets the internal state of the scheduler running for the World.
             
    
    
    

### SelectFromEntity<a name="SelectFromEntity"></a>
!!! function "&#42; SelectFromEntity(const Entity&amp; entity, const std::vector&lt;AmSoundID&gt;&amp; toSkip)"

    
    Returns a Sound from this collection from an Entity scope.
    
    
    :material-location-enter: **Parameter** `entity`
    :    The entity from which pick the sound.
        
    :material-location-enter: **Parameter** `toSkip`
    :    The list of Sound IDs to skip fom the selection.
    
    
    :material-keyboard-return: **Return**
    :    The selected Sound.
            
    

### SelectFromWorld<a name="SelectFromWorld"></a>
!!! function "&#42; SelectFromWorld(const std::vector&lt;AmSoundID&gt;&amp; toSkip) const"

    
    Returns a Sound from this collection from the World scope.
    
    
    :material-location-enter: **Parameter** `toSkip`
    :    The list of Sound IDs to skip fom the selection.
    
    
    :material-keyboard-return: **Return**
    :    The selected Sound.
            
    

