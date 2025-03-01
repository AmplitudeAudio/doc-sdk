---
title: Fader
description: Helper class to process faders.
generator: doxide
---


# Fader

**class  Fader**


Helper class to process faders.

A fader is used to move a value to a specific target value
during an amount of time and according to a fading algorithm.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_name](#m_name) | The name of this Fader.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Fader](#Fader) | Create a new Fader instance. |
| [Fader](#Fader) | Default Fader constructor. |
| [~Fader](#_u007eFader) | Default destructor.  |
| [CreateInstance](#CreateInstance) | Creates a new instance of the Fader. |
| [DestroyInstance](#DestroyInstance) | Destroys an instance of the Fader. |
| [GetName](#GetName) | Gets the name of this Fader. |
| [GetControlPoints](#GetControlPoints) | Gets the control points of the transition curve used by this Fader. |
| [Register](#Register) | Registers a new fader. |
| [Unregister](#Unregister) | Unregister a fader. |
| [Construct](#Construct) | Creates a new instance of the fader with the given name and returns its pointer. |
| [Destruct](#Destruct) | Destroys the given fader instance. |
| [LockRegistry](#LockRegistry) | Locks the faders registry. |
| [UnlockRegistry](#UnlockRegistry) | Unlocks the fader's registry. |
| [GetRegistry](#GetRegistry) | Gets the list of registered Faders. |

## Variable Details

### m_name<a name="m_name"></a>

!!! variable "AmString m_name"

    
    The name of this Fader.
             
    
    
    

## Function Details

### Construct<a name="Construct"></a>
!!! function "static FaderInstance&#42; Construct(const AmString&amp; name)"

    
    Creates a new instance of the fader with the given name and returns its pointer.
    
    
    !!! note
         The returned pointer should be deleted using [`Destruct()`.](#Destruct)
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the fader.
    
    
    :material-keyboard-return: **Return**
    :    The fader with the given name, or `nullptr` if none.
            
    

### CreateInstance<a name="CreateInstance"></a>
!!! function "&#42; CreateInstance()"

    
    Creates a new instance of the Fader.
    
    
    :material-keyboard-return: **Return**
    :    A new instance of the Fader.
            
    

### DestroyInstance<a name="DestroyInstance"></a>
!!! function "virtual void DestroyInstance(FaderInstance&#42; instance) = 0"

    
    Destroys an instance of the Fader.
    
    
    !!! note
         The instance should have been created with CreateInstance().
    
    
    :material-location-enter: **Parameter** `instance`
    :    The Fader instance to be destroyed.
                
    

### Destruct<a name="Destruct"></a>
!!! function "static void Destruct(const AmString&amp; name, FaderInstance&#42; instance)"

    
    Destroys the given fader instance.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the fader.
        
    :material-location-enter: **Parameter** `instance`
    :    The fader instance to destroy.
                
    

### Fader<a name="Fader"></a>
!!! function "explicit Fader(AmString name)"

    
    Create a new Fader instance.
    
    
    :material-location-enter: **Parameter** `name`
    :    The Fader name. eg. "MiniAudioLinear".
                
    

!!! function "Fader()"

    
    Default Fader constructor.
    
    This will not automatically register the Fader. It's meant for internal Faders only.
            
    

### GetControlPoints<a name="GetControlPoints"></a>
!!! function "[[nodiscard]] virtual BezierCurveControlPoints GetControlPoints() const = 0"

    
    Gets the control points of the transition curve used by this Fader.
    
    
    :material-keyboard-return: **Return**
    :    The control points of the transition curve used by this Fader.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Gets the name of this Fader.
    
    
    :material-keyboard-return: **Return**
    :    The name of this Fader.
            
    

### GetRegistry<a name="GetRegistry"></a>
!!! function "static const std::map&lt;AmString, std::shared_ptr&lt;Fader&gt;&gt;&amp; GetRegistry()"

    
    Gets the list of registered Faders.
    
    
    :material-keyboard-return: **Return**
    :    The registry of Faders.
            
    

### LockRegistry<a name="LockRegistry"></a>
!!! function "static void LockRegistry()"

    
    Locks the faders registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called before the `Engine` initialization, to discard the registration
        of new fader after the engine is fully loaded.
                
    

### Register<a name="Register"></a>
!!! function "static void Register(std::shared_ptr&lt;Fader&gt; fader)"

    
    Registers a new fader.
    
    
    :material-location-enter: **Parameter** `fader`
    :    The Fader to add in the registry.
                
    

### UnlockRegistry<a name="UnlockRegistry"></a>
!!! function "static void UnlockRegistry()"

    
    Unlocks the fader's registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called after the `Engine` deinitialization, to allow the registration
        of new fader after the engine is fully unloaded.
                
    

### Unregister<a name="Unregister"></a>
!!! function "static void Unregister(std::shared_ptr&lt;const Fader&gt; fader)"

    
    Unregister a fader.
    
    
    :material-location-enter: **Parameter** `fader`
    :    The Fader to remove from the registry.
                
    

### ~Fader<a name="_u007eFader"></a>
!!! function "virtual ~Fader()"

    
    Default destructor.
             
    
    
    

