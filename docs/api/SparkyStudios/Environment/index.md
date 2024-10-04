---
title: Environment
description: An Environment is a zone where every spatialized audio playing inside him got * applied a specific effect.
generator: doxide
---


# Environment

**class  Environment**


An Environment is a zone where every spatialized audio playing inside him got
     * applied a specific effect.

The Environment class is a lightweight reference to a EnvironmentInternalState object
which is managed by the Engine.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [Environment](#Environment) | Creates an uninitialized Environment. |
| [Clear](#Clear) | Uninitializes this Environment. |
| [Valid](#Valid) | Checks whether this Environment has been initialized. |
| [GetId](#GetId) | Returns the unique ID of this Environment. |
| [SetLocation](#SetLocation) | Sets the location of this Environment. |
| [GetLocation](#GetLocation) | Gets the current location of this Environment. |
| [SetOrientation](#SetOrientation) | Sets the orientation of this Environment. |
| [GetOrientation](#GetOrientation) | Gets the current orientation of this Environment. |
| [GetDirection](#GetDirection) | Get the direction vector of the Environment. |
| [GetUp](#GetUp) | Get the up vector of the Environment. |
| [GetFactor](#GetFactor) | Get the Environment factor for the given location. |
| [GetFactor](#GetFactor) | Get the Environment factor for the given entity. |
| [SetEffect](#SetEffect) | Set the Effect applied in the Environment. |
| [SetEffect](#SetEffect) | Set the Effect applied in the Environment. |
| [SetEffect](#SetEffect) | Set the Effect applied in the Environment. |
| [GetEffect](#GetEffect) | Get the Effect linked to this environment. |
| [SetZone](#SetZone) | Set the Zone for this environment. |
| [GetZone](#GetZone) | Get the Zone linked to this environment. |
| [GetState](#GetState) | Returns the internal state of this Environment. |
| [Update](#Update) | Update the state of this Environment. |

## Function Details

### Clear<a name="Clear"></a>
!!! function "void Clear()"

    
    Uninitializes this Environment.
    
    Note that this does not destroy the internal state it references,
    it just removes this reference to it.
            
    

### Environment<a name="Environment"></a>
!!! function "Environment()"

    
    Creates an uninitialized Environment.
    
    An uninitialized Environment cannot provide location and orientation
    information, and therefore cannot play sounds.
            
    

### GetDirection<a name="GetDirection"></a>
!!! function "[[nodiscard]] AmVec3 GetDirection() const"

    
    Get the direction vector of the Environment.
    
    
    :material-keyboard-return: **Return**
    :    The direction vector.
            
    

### GetEffect<a name="GetEffect"></a>
!!! function "[[nodiscard]] const Effect&#42; GetEffect() const"

    
    Get the Effect linked to this environment.
    
    
    :material-keyboard-return: **Return**
    :    An Effect instance.
            
    

### GetFactor<a name="GetFactor"></a>
!!! function "[[nodiscard]] AmReal32 GetFactor(const AmVec3&amp; location) const"

    
    Get the Environment factor for the given location.
    
    
    :material-location-enter: **Parameter** `location`
    :    The location for which compute the environment factor.
    
    
    :material-keyboard-return: **Return**
    :    The environment factor.
            
    

!!! function "[[nodiscard]] AmReal32 GetFactor(const Entity&amp; entity) const"

    
    Get the Environment factor for the given entity.
    
    
    :material-location-enter: **Parameter** `entity`
    :    The entity for which compute the environment factor.
    
    
    :material-keyboard-return: **Return**
    :    The environment factor.
            
    

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmEnvironmentID GetId() const"

    
    Returns the unique ID of this Environment.
    
    
    :material-keyboard-return: **Return**
    :    The Environment unique ID.
            
    

### GetLocation<a name="GetLocation"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetLocation() const"

    
    Gets the current location of this Environment.
    
    
    :material-keyboard-return: **Return**
    :    The current location of this Environment.
            
    

### GetOrientation<a name="GetOrientation"></a>
!!! function "[[nodiscard]] const Orientation&amp; GetOrientation() const"

    
    Gets the current orientation of this Environment.
    
    
    :material-keyboard-return: **Return**
    :    The current orientation of this Environment.
            
    

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] EnvironmentInternalState&#42; GetState() const"

    
    Returns the internal state of this Environment.
    
    
    :material-keyboard-return: **Return**
    :    The Environment internal state.
            
    

### GetUp<a name="GetUp"></a>
!!! function "[[nodiscard]] AmVec3 GetUp() const"

    
    Get the up vector of the Environment.
    
    
    :material-keyboard-return: **Return**
    :    The up vector.
            
    

### GetZone<a name="GetZone"></a>
!!! function "[[nodiscard]] Zone&#42; GetZone() const"

    
    Get the Zone linked to this environment.
    
    
    :material-keyboard-return: **Return**
    :    An Zone instance.
            
    

### SetEffect<a name="SetEffect"></a>
!!! function "void SetEffect(AmEffectID effect) const"

    
    Set the Effect applied in the Environment.
    
    
    :material-location-enter: **Parameter** `effect`
    :    The effect to apply in the Environment.
                
    

!!! function "void SetEffect(const std::string&amp; effect) const"

    
    Set the Effect applied in the Environment.
    
    
    :material-location-enter: **Parameter** `effect`
    :    The effect to apply in the Environment.
                
    

!!! function "void SetEffect(const Effect&#42; effect) const"

    
    Set the Effect applied in the Environment.
    
    
    :material-location-enter: **Parameter** `effect`
    :    The effect to apply in the Environment.
                
    

### SetLocation<a name="SetLocation"></a>
!!! function "void SetLocation(const AmVec3&amp; location) const"

    
    Sets the location of this Environment.
    
    
    :material-location-enter: **Parameter** `location`
    :    The new location.
                
    

### SetOrientation<a name="SetOrientation"></a>
!!! function "void SetOrientation(const Orientation&amp; orientation) const"

    
    Sets the orientation of this Environment.
    
    
    :material-location-enter: **Parameter** `orientation`
    :    The new orientation.
                
    

### SetZone<a name="SetZone"></a>
!!! function "void SetZone(Zone&#42; zone) const"

    
    Set the Zone for this environment.
    
    
    :material-location-enter: **Parameter** `zone`
    :    The environment's zone.
                
    

### Update<a name="Update"></a>
!!! function "void Update() const"

    
    Update the state of this Environment.
    
    This method is called automatically by the Engine
    on each frames.
            
    

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this Environment has been initialized.
    
    
    :material-keyboard-return: **Return**
    :    boolean true if this Environment has been initialized.
            
    

