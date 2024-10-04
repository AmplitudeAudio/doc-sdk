---
title: Filter
description: Helper class to manage filters.
generator: doxide
---


# Filter

**class  Filter**


Helper class to manage filters.

A filter applies transformations on an audio buffer..
    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_name](#m_name) | The name of this filter.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Filter](#Filter) | Create a new @c Filter instance. |
| [GetParamCount](#GetParamCount) | Get the maximum number of parameters available for this filter. |
| [GetParamName](#GetParamName) | Get the name of the parameter at the given index. |
| [GetParamType](#GetParamType) | Get the type of the parameter at the given index. |
| [GetParamMax](#GetParamMax) | Get the maximum allowed value of the parameter at the given index. |
| [GetParamMin](#GetParamMin) | Get the minimum allowed value of the parameter at the given index. |
| [CreateInstance](#CreateInstance) | Creates a new instance of the filter. |
| [DestroyInstance](#DestroyInstance) | Destroys an instance of the filter. The instance should have * been created with @c Filter::CreateInstance(). |
| [GetName](#GetName) | Gets the name of this filter. |
| [Register](#Register) | Registers a new filter. |
| [Unregister](#Unregister) | Unregisters a filter. |
| [Find](#Find) | Look up a filter by name. |
| [Construct](#Construct) | Creates a new instance of the the filter with the given name * and returns its pointer. The returned pointer should be deleted using @c Filter::Destruct(). |
| [Destruct](#Destruct) | Destroys the given filter instance. |
| [LockRegistry](#LockRegistry) | Locks the filters registry. |
| [UnlockRegistry](#UnlockRegistry) | Unlocks the filters registry. |
| [GetRegistry](#GetRegistry) | Gets the list of registered filters. |

## Variable Details

### m_name<a name="m_name"></a>

!!! variable "AmString m_name"

    
    The name of this filter.
             
    
    
    

## Function Details

### Construct<a name="Construct"></a>
!!! function "static FilterInstance&#42; Construct(const AmString&amp; name)"

    
    Creates a new instance of the the filter with the given name
             * and returns its pointer. The returned pointer should be deleted using @c Filter::Destruct().
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the filter.
    
    
    :material-keyboard-return: **Return**
    :    The filter with the given name, or `nullptr` if none.
            
    

### CreateInstance<a name="CreateInstance"></a>
!!! function "&#42; CreateInstance()"

    
    Creates a new instance of the filter.
    
    
    :material-keyboard-return: **Return**
    :    A new instance of the filter.
            
    

### DestroyInstance<a name="DestroyInstance"></a>
!!! function "virtual void DestroyInstance(FilterInstance&#42; instance) = 0"

    
    Destroys an instance of the filter. The instance should have
             * been created with @c Filter::CreateInstance().
    
    
    :material-location-enter: **Parameter** `instance`
    :    The filter instance to be destroyed.
                
    

### Destruct<a name="Destruct"></a>
!!! function "static void Destruct(const AmString&amp; name, FilterInstance&#42; instance)"

    
    Destroys the given filter instance.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the filter.
        
    :material-location-enter: **Parameter** `instance`
    :    The filter instance to destroy.
                
    

### Filter<a name="Filter"></a>
!!! function "explicit Filter(AmString name)"

    
    Create a new @c Filter instance.
    
    
    :material-location-enter: **Parameter** `name`
    :    The filter name. eg. "Delay".
                
    

### Find<a name="Find"></a>
!!! function "static Filter&#42; Find(const AmString&amp; name)"

    
    Look up a filter by name.
    
    
    :material-keyboard-return: **Return**
    :    The filter with the given name, or `nullptr` if none.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Gets the name of this filter.
    
    
    :material-keyboard-return: **Return**
    :    The name of this filter.
            
    

### GetParamCount<a name="GetParamCount"></a>
!!! function "[[nodiscard]] virtual AmUInt32 GetParamCount() const"

    
    Get the maximum number of parameters available for this filter.
    
    
    :material-keyboard-return: **Return**
    :    The maximum number of filter parameters.
            
    

### GetParamMax<a name="GetParamMax"></a>
!!! function "[[nodiscard]] virtual AmReal32 GetParamMax(AmUInt32 index) const"

    
    Get the maximum allowed value of the parameter at the given index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The parameter index.
    
    
    :material-keyboard-return: **Return**
    :    The maximum allowed value of the parameter at the given index.
            
    

### GetParamMin<a name="GetParamMin"></a>
!!! function "[[nodiscard]] virtual AmReal32 GetParamMin(AmUInt32 index) const"

    
    Get the minimum allowed value of the parameter at the given index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The parameter index.
    
    
    :material-keyboard-return: **Return**
    :    The minimum allowed value of the parameter at the given index.
            
    

### GetParamName<a name="GetParamName"></a>
!!! function "[[nodiscard]] virtual AmString GetParamName(AmUInt32 index) const"

    
    Get the name of the parameter at the given index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The parameter index.
    
    
    :material-keyboard-return: **Return**
    :    The name of the parameter at the given index.
            
    

### GetParamType<a name="GetParamType"></a>
!!! function "[[nodiscard]] virtual AmUInt32 GetParamType(AmUInt32 index) const"

    
    Get the type of the parameter at the given index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The parameter index.
    
    
    :material-keyboard-return: **Return**
    :    The type of the parameter at the given index.
            
    

### GetRegistry<a name="GetRegistry"></a>
!!! function "static const std::map&lt;AmString, Filter&#42;&gt;&amp; GetRegistry()"

    
    Gets the list of registered filters.
    
    
    :material-keyboard-return: **Return**
    :    The registry of filters.
            
    

### LockRegistry<a name="LockRegistry"></a>
!!! function "static void LockRegistry()"

    
    Locks the filters registry.
    
    This function is mainly used for internal purposes. Its
    called before the Engine initialization, to discard the
    registration of new filters after the engine is fully loaded.
            
    

### Register<a name="Register"></a>
!!! function "static void Register(Filter&#42; filter)"

    
    Registers a new filter.
    
    
    :material-location-enter: **Parameter** `filter`
    :    The filter to add in the registry.
                
    

### UnlockRegistry<a name="UnlockRegistry"></a>
!!! function "static void UnlockRegistry()"

    
    Unlocks the filters registry.
    
    This function is mainly used for internal purposes. Its
    called after the Engine deinitialization, to allow the
    registration of new divers after the engine is fully unloaded.
            
    

### Unregister<a name="Unregister"></a>
!!! function "static void Unregister(const Filter&#42; filter)"

    
    Unregisters a filter.
    
    
    :material-location-enter: **Parameter** `filter`
    :    The filter to remove from the registry.
                
    
