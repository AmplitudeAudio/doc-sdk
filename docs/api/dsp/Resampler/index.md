---
title: Resampler
description: Base class to manage resamplers.
generator: doxide
---


# Resampler

**class  Resampler**


Base class to manage resamplers.

A resampler is used to change the sample rate of an audio buffer. The `Resampler` class implements
factory methods to create instances of `ResamplerInstance` objects, which are where the the resampling is done.

The `Resampler` class follows the [plugins architecture](/plugins/anatomy.md), and thus, you are able to create your own resamplers
and register them to the `Engine` by inheriting from this class, and by implementing the necessary dependencies.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_name](#m_name) | The name of this resampler.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Resampler](#Resampler) | Create a new Resampler instance. |
| [Resampler](#Resampler) | Default Resampler constructor. |
| [~Resampler](#_u007eResampler) | Default destructor.  |
| [CreateInstance](#CreateInstance) | Creates a new instance of the resampler. |
| [DestroyInstance](#DestroyInstance) | Destroys an instance of the resampler. |
| [GetName](#GetName) | Gets the name of this resampler. |
| [Register](#Register) | Registers a new resampler. |
| [Unregister](#Unregister) | Unregisters a resampler. |
| [Construct](#Construct) | Creates a new instance of the resampler with the given name and returns its pointer. |
| [Destruct](#Destruct) | Destroys the given resampler instance. |
| [LockRegistry](#LockRegistry) | Locks the resamplers registry. |
| [UnlockRegistry](#UnlockRegistry) | Unlocks the resamplers registry. |
| [GetRegistry](#GetRegistry) | Gets the list of registered Resamplers. |

## Variable Details

### m_name<a name="m_name"></a>

!!! variable "AmString m_name"

    
    The name of this resampler.
             
    
    
    

## Function Details

### Construct<a name="Construct"></a>
!!! function "static ResamplerInstance&#42; Construct(const AmString&amp; name)"

    
    Creates a new instance of the resampler with the given name and returns its pointer.
    
    
    !!! note
         The returned pointer should be deleted using [`Destruct()`.](#Destruct)
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the resampler.
    
    
    :material-keyboard-return: **Return**
    :    The resampler with the given name, or `nullptr` if none.
            
    

### CreateInstance<a name="CreateInstance"></a>
!!! function "&#42; CreateInstance()"

    
    Creates a new instance of the resampler.
    
    
    :material-keyboard-return: **Return**
    :    A new instance of the resampler.
            
    

### DestroyInstance<a name="DestroyInstance"></a>
!!! function "virtual void DestroyInstance(ResamplerInstance&#42; instance) = 0"

    
    Destroys an instance of the resampler.
    
    
    !!! warning
         The instance should have been created with [`CreateInstance()`](#CreateInstance)
        before being destroyed with this method.
    
    
    :material-location-enter: **Parameter** `instance`
    :    The resampler instance to be destroyed.
                
    

### Destruct<a name="Destruct"></a>
!!! function "static void Destruct(const AmString&amp; name, ResamplerInstance&#42; instance)"

    
    Destroys the given resampler instance.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the resampler.
        
    :material-location-enter: **Parameter** `instance`
    :    The resampler instance to destroy.
                
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Gets the name of this resampler.
    
    
    :material-keyboard-return: **Return**
    :    The name of this resampler.
            
    

### GetRegistry<a name="GetRegistry"></a>
!!! function "static const std::map&lt;AmString, std::shared_ptr&lt;Resampler&gt;&gt;&amp; GetRegistry()"

    
    Gets the list of registered Resamplers.
    
    
    :material-keyboard-return: **Return**
    :    The registry of Resamplers.
            
    

### LockRegistry<a name="LockRegistry"></a>
!!! function "static void LockRegistry()"

    
    Locks the resamplers registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called before the `Engine` initialization, to discard the registration
        of new resamplers after the engine is fully loaded.
                
    

### Register<a name="Register"></a>
!!! function "static void Register(std::shared_ptr&lt;Resampler&gt; resampler)"

    
    Registers a new resampler.
    
    
    :material-location-enter: **Parameter** `resampler`
    :    The resampler to add in the registry.
                
    

### Resampler<a name="Resampler"></a>
!!! function "explicit Resampler(AmString name)"

    
    Create a new Resampler instance.
    
    
    :material-location-enter: **Parameter** `name`
    :    The resampler name. e.g. "MiniAudioLinear".
                
    

!!! function "Resampler()"

    
    Default Resampler constructor.
    
    This will not automatically register the resampler. It's meant for internal resamplers only.
            
    

### UnlockRegistry<a name="UnlockRegistry"></a>
!!! function "static void UnlockRegistry()"

    
    Unlocks the resamplers registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called after the `Engine` deinitialization, to allow the registration
        of new resamplers after the engine is fully unloaded.
                
    

### Unregister<a name="Unregister"></a>
!!! function "static void Unregister(std::shared_ptr&lt;const Resampler&gt; resampler)"

    
    Unregisters a resampler.
    
    
    :material-location-enter: **Parameter** `resampler`
    :    The resampler to remove from the registry.
                
    

### ~Resampler<a name="_u007eResampler"></a>
!!! function "virtual ~Resampler()"

    
    Default destructor.
             
    
    
    

