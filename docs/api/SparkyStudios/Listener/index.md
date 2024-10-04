---
title: Listener
description: An object whose distance from sounds determines their gain.
generator: doxide
---


# Listener

**class  Listener**


An object whose distance from sounds determines their gain.

The Listener class is a lightweight reference to a ListenerInternalState
which is managed by the Engine. Multiple Listener objects may point to
the same underlying data.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [Listener](#Listener) | Construct an uninitialized Listener. |
| [Clear](#Clear) | Deinitialize this Listener. |
| [Valid](#Valid) | Checks whether this Listener has been initialized. |
| [GetId](#GetId) | Gets the ID of this Listener in game. |
| [GetVelocity](#GetVelocity) | Gets the velocity of the Listener. |
| [GetLocation](#GetLocation) | Returns the location of this Listener. |
| [SetLocation](#SetLocation) | Set the location of this Listener. |
| [GetDirection](#GetDirection) | Get the direction vector of the Listener. |
| [GetUp](#GetUp) | Get the up vector of the Listener. |
| [SetOrientation](#SetOrientation) | Set the location, direction and up vector of this Listener. |
| [GetOrientation](#GetOrientation) | Get the orientation of the Listener. |
| [SetDirectivity](#SetDirectivity) | Sets the directivity and sharpness of Listener. This affects how sounds are perceived * by the Listener. |
| [GetDirectivity](#GetDirectivity) | Gets the directivity of sounds played by this Entity. |
| [GetDirectivitySharpness](#GetDirectivitySharpness) | Gets the directivity sharpness of sounds played by this Entity. |
| [GetInverseMatrix](#GetInverseMatrix) | Gets the inverse matrix of the Listener. |
| [Update](#Update) | Update the state of this Listener. |
| [GetState](#GetState) | Returns the internal state of this Listener. |

## Function Details

### Clear<a name="Clear"></a>
!!! function "void Clear()"

    
    Deinitialize this Listener.
    
    Note that this does not destroy the internal state it references,
    it just removes this reference to it. To destroy the Listener,
    use <code>Engine::RemoveListener();</code>.
            
    

### GetDirection<a name="GetDirection"></a>
!!! function "[[nodiscard]] AmVec3 GetDirection() const"

    
    Get the direction vector of the Listener.
    
    
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
            
    

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmListenerID GetId() const"

    
    Gets the ID of this Listener in game.
    
    
    :material-keyboard-return: **Return**
    :    The game Listener ID.
            
    

### GetInverseMatrix<a name="GetInverseMatrix"></a>
!!! function "[[nodiscard]] const AmMat4&amp; GetInverseMatrix() const"

    
    Gets the inverse matrix of the Listener.
    
    You can use this matrix to transform 3D global space into Listener space.
            
    

### GetLocation<a name="GetLocation"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetLocation() const"

    
    Returns the location of this Listener.
    
    
    :material-keyboard-return: **Return**
    :    AmVec3 The location of this Listener.
            
    

### GetOrientation<a name="GetOrientation"></a>
!!! function "[[nodiscard]] Orientation GetOrientation() const"

    
    Get the orientation of the Listener.
    
    
    :material-keyboard-return: **Return**
    :    The orientation of this Listener.
            
    

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] ListenerInternalState&#42; GetState() const"

    
    Returns the internal state of this Listener.
    
    
    :material-keyboard-return: **Return**
    :    ListenerInternalState*
            
    

### GetUp<a name="GetUp"></a>
!!! function "[[nodiscard]] AmVec3 GetUp() const"

    
    Get the up vector of the Listener.
    
    
    :material-keyboard-return: **Return**
    :    The up vector.
            
    

### GetVelocity<a name="GetVelocity"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetVelocity() const"

    
    Gets the velocity of the Listener.
    
    
    :material-keyboard-return: **Return**
    :    The Listener's velocity.
            
    

### Listener<a name="Listener"></a>
!!! function "Listener()"

    
    Construct an uninitialized Listener.
    
    An uninitialized Listener cannot have its location set or queried.
    To initialize the Listener, use <code>Engine::AddListener();</code>.
            
    

### SetDirectivity<a name="SetDirectivity"></a>
!!! function "void SetDirectivity(AmReal32 directivity, AmReal32 sharpness) const"

    
    Sets the directivity and sharpness of Listener. This affects how sounds are perceived
             * by the Listener.
    
    
    :material-location-enter: **Parameter** `directivity`
    :    The directivity of the listener, in the range [0, 1].
        
    :material-location-enter: **Parameter** `sharpness`
    :    The directivity sharpness of the listener, in the range [1, +INF].
        Increasing this value increases the directivity towards the front of the listener.
                
    

### SetLocation<a name="SetLocation"></a>
!!! function "void SetLocation(const AmVec3&amp; location) const"

    
    Set the location of this Listener.
    
    
    :material-location-enter: **Parameter** `location`
    :    The new location of this Listener.
                
    

### SetOrientation<a name="SetOrientation"></a>
!!! function "void SetOrientation(const Orientation&amp; orientation) const"

    
    Set the location, direction and up vector of this Listener.
    
    
    :material-location-enter: **Parameter** `orientation`
    :    The new orientation of this Listener.
                
    

### Update<a name="Update"></a>
!!! function "void Update() const"

    
    Update the state of this Listener.
    
    This method is called automatically by the Engine
    on each frames.
            
    

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this Listener has been initialized.
    
    
    :material-keyboard-return: **Return**
    :    bool true if this Listener has been initialized.
            
    

