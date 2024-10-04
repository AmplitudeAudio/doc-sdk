---
title: Entity
description: An Entity represent an object in the game.
generator: doxide
---


# Entity

**class  Entity**


An Entity represent an object in the game.

Amplitude use entities to link sound to an object in the game. Each sounds
played from an entity get the location and orientation data fom that entity.

The Entity class is a lightweight reference to a EntityInternalState object
which is managed by the Engine.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [Entity](#Entity) | Creates an uninitialized Entity. |
| [Clear](#Clear) | Uninitializes this Entity. |
| [Valid](#Valid) | Checks whether this Entity has been initialized. |
| [GetId](#GetId) | Gets the ID of this Entity in game. |
| [GetVelocity](#GetVelocity) | Gets the velocity of the Entity. |
| [SetLocation](#SetLocation) | Sets the location of this Entity. |
| [GetLocation](#GetLocation) | Gets the current location of this Entity. |
| [SetOrientation](#SetOrientation) | Sets the orientation of this Entity. |
| [GetDirection](#GetDirection) | Get the direction vector of the Entity. |
| [GetUp](#GetUp) | Get the up vector of the Entity. |
| [GetOrientation](#GetOrientation) | Get the orientation of the Entity. |
| [Update](#Update) | Update the state of this Entity. |
| [SetObstruction](#SetObstruction) | Set the obstruction level of sounds played by this Entity. |
| [SetOcclusion](#SetOcclusion) | Set the occlusion level of sounds played by this Entity. |
| [SetDirectivity](#SetDirectivity) | Sets the directivity and sharpness of sounds played by this Entity. |
| [GetObstruction](#GetObstruction) | Get the obstruction level of sounds played by this Entity. |
| [GetOcclusion](#GetOcclusion) | Get the occlusion level of sounds played by this Entity. |
| [GetDirectivity](#GetDirectivity) | Gets the directivity of sounds played by this Entity. |
| [GetDirectivitySharpness](#GetDirectivitySharpness) | Gets the directivity sharpness of sounds played by this Entity. |
| [SetEnvironmentFactor](#SetEnvironmentFactor) | Sets the environment factor for this Entity in the given environment. |
| [GetEnvironmentFactor](#GetEnvironmentFactor) | Gets the environment factor of this Entity for the given environment. |
| [GetEnvironments](#GetEnvironments) | Get the list of environments where this Entity belongs or has visited. |
| [GetState](#GetState) | Returns the internal state of this Entity. |

## Function Details

### Clear<a name="Clear"></a>
!!! function "void Clear()"

    
    Uninitializes this Entity.
    
    Note that this does not destroy the internal state it references,
    it just removes this reference to it.
            
    

### Entity<a name="Entity"></a>
!!! function "Entity()"

    
    Creates an uninitialized Entity.
    
    An uninitialized Entity cannot provide location and orientation
    information, and therefore cannot play sounds.
            
    

### GetDirection<a name="GetDirection"></a>
!!! function "[[nodiscard]] AmVec3 GetDirection() const"

    
    Get the direction vector of the Entity.
    
    
    :material-keyboard-return: **Return**
    :    The direction vector.
            
    

### GetDirectivity<a name="GetDirectivity"></a>
!!! function "[[nodiscard]] AmReal32 GetDirectivity() const"

    
    Gets the directivity of sounds played by this Entity.
    
    
    :material-keyboard-return: **Return**
    :    The directivity of sound sources.
            
    

### GetDirectivitySharpness<a name="GetDirectivitySharpness"></a>
!!! function "[[nodiscard]] AmReal32 GetDirectivitySharpness() const"

    
    Gets the directivity sharpness of sounds played by this Entity.
    
    
    :material-keyboard-return: **Return**
    :    The directivity sharpness of sounds played by this Entity.
            
    

### GetEnvironmentFactor<a name="GetEnvironmentFactor"></a>
!!! function "[[nodiscard]] AmReal32 GetEnvironmentFactor(AmEnvironmentID environment) const"

    
    Gets the environment factor of this Entity for the given environment.
    
    
    :material-location-enter: **Parameter** `environment`
    :    The environment ID.
    
    
    :material-keyboard-return: **Return**
    :    The environment factor.
            
    

### GetEnvironments<a name="GetEnvironments"></a>
!!! function "[[nodiscard]] const std::map&lt;AmEnvironmentID, AmReal32&gt;&amp; GetEnvironments() const"

    
    Get the list of environments where this Entity belongs or has visited.
    
    
    :material-keyboard-return: **Return**
    :    The list of environments where this Entity belongs or has visited.
            
    

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmEntityID GetId() const"

    
    Gets the ID of this Entity in game.
    
    
    :material-keyboard-return: **Return**
    :    The game Entity ID.
            
    

### GetLocation<a name="GetLocation"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetLocation() const"

    
    Gets the current location of this Entity.
    
    
    :material-keyboard-return: **Return**
    :    The current location of this Entity.
            
    

### GetObstruction<a name="GetObstruction"></a>
!!! function "[[nodiscard]] AmReal32 GetObstruction() const"

    
    Get the obstruction level of sounds played by this Entity.
    
    
    :material-keyboard-return: **Return**
    :    The obstruction amount.
            
    

### GetOcclusion<a name="GetOcclusion"></a>
!!! function "[[nodiscard]] AmReal32 GetOcclusion() const"

    
    Get the occlusion level of sounds played by this Entity.
    
    
    :material-keyboard-return: **Return**
    :    The occlusion amount.
            
    

### GetOrientation<a name="GetOrientation"></a>
!!! function "[[nodiscard]] const Orientation&amp; GetOrientation() const"

    
    Get the orientation of the Entity.
    
    
    :material-keyboard-return: **Return**
    :    The entity's orientation.
            
    

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] EntityInternalState&#42; GetState() const"

    
    Returns the internal state of this Entity.
    
    
    :material-keyboard-return: **Return**
    :    The Entity internal state.
            
    

### GetUp<a name="GetUp"></a>
!!! function "[[nodiscard]] AmVec3 GetUp() const"

    
    Get the up vector of the Entity.
    
    
    :material-keyboard-return: **Return**
    :    The up vector.
            
    

### GetVelocity<a name="GetVelocity"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetVelocity() const"

    
    Gets the velocity of the Entity.
    
    
    :material-keyboard-return: **Return**
    :    The Entity's velocity.
            
    

### SetDirectivity<a name="SetDirectivity"></a>
!!! function "void SetDirectivity(AmReal32 directivity, AmReal32 sharpness) const"

    
    Sets the directivity and sharpness of sounds played by this Entity.
    
    
    :material-location-enter: **Parameter** `directivity`
    :    The directivity of the sound source, in the range [0, 1].
        
    :material-location-enter: **Parameter** `sharpness`
    :    The directivity sharpness of the sound source, in the range [1, +INF].
        Increasing this value increases the directivity towards the front of the source.
                
    

### SetEnvironmentFactor<a name="SetEnvironmentFactor"></a>
!!! function "void SetEnvironmentFactor(AmEnvironmentID environment, AmReal32 factor) const"

    
    Sets the environment factor for this Entity in the given environment.
    
    
    :material-location-enter: **Parameter** `environment`
    :    The environment ID.
        
    :material-location-enter: **Parameter** `factor`
    :    The environment factor.
                
    

### SetLocation<a name="SetLocation"></a>
!!! function "void SetLocation(const AmVec3&amp; location) const"

    
    Sets the location of this Entity.
    
    
    :material-location-enter: **Parameter** `location`
    :    The new location.
                
    

### SetObstruction<a name="SetObstruction"></a>
!!! function "void SetObstruction(AmReal32 obstruction) const"

    
    Set the obstruction level of sounds played by this Entity.
    
    
    :material-location-enter: **Parameter** `obstruction`
    :    The obstruction amount. This is provided by the
        game engine.
                
    

### SetOcclusion<a name="SetOcclusion"></a>
!!! function "void SetOcclusion(AmReal32 occlusion) const"

    
    Set the occlusion level of sounds played by this Entity.
    
    
    :material-location-enter: **Parameter** `occlusion`
    :    The occlusion amount. This is provided by the
        game engine.
                
    

### SetOrientation<a name="SetOrientation"></a>
!!! function "void SetOrientation(const Orientation&amp; orientation) const"

    
    Sets the orientation of this Entity.
    
    
    :material-location-enter: **Parameter** `orientation`
    :    The new orientation.
                
    

### Update<a name="Update"></a>
!!! function "void Update() const"

    
    Update the state of this Entity.
    
    This method is called automatically by the Engine
    on each frames.
            
    

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this Entity has been initialized.
    
    
    :material-keyboard-return: **Return**
    :    boolean true if this Entity has been initialized.
            
    
