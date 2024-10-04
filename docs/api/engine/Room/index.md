---
title: Room
description: The absorption coefficients of the material. Represents a physical space where sound waves can propagate.
generator: doxide
---


# Room

**class  Room**


The absorption coefficients of the material.
         



Represents a physical space where sound waves can propagate.

Any sound source within the room will be affected by the room's properties,
and got applied early reflections and reverberation effects.

This class is a lightweight wrapper around the internal `RoomInternalState` class.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Room](#Room) | Creates an uninitialized `Room`. |
| [Room](#Room) | Creates a wrapper instance over the provided state. |
| [Clear](#Clear) | Uninitializes this `Room`. |
| [Valid](#Valid) | Checks whether this `Room` has been initialized. |
| [GetId](#GetId) | Returns the unique ID of this `Room`. |
| [SetLocation](#SetLocation) | Sets the location `Room`. |
| [GetLocation](#GetLocation) | Gets the current location of this `Room`. |
| [SetOrientation](#SetOrientation) | Sets the orientation of this `Room`. |
| [GetOrientation](#GetOrientation) | Gets the current orientation of this `Room`. |
| [GetDirection](#GetDirection) | Gets the direction vector of this `Room`. |
| [GetUp](#GetUp) | Gets the up vector of this `Room`. |
| [SetDimensions](#SetDimensions) | Sets the shape's dimensions of this `Room`. |
| [SetShape](#SetShape) | Sets the shape representing this `Room`. |
| [GetShape](#GetShape) | Gets the shape representing this `Room`. |
| [SetWallMaterial](#SetWallMaterial) | Sets the material of a specific wall of this `Room`. |
| [SetAllWallMaterials](#SetAllWallMaterials) | Sets the material of all walls of this `Room`. |
| [SetWallMaterials](#SetWallMaterials) | Sets the material of each wall of this `Room`. |
| [GetWallMaterial](#GetWallMaterial) | Gets the material of a specific wall of this `Room`. |
| [SetGain](#SetGain) | Sets the room effects gain. |
| [GetGain](#GetGain) | Gets the room effects gain. |
| [GetVolume](#GetVolume) | Gets the volume of the `Room` in m3. |
| [GetSurfaceArea](#GetSurfaceArea) | Gets the surface area of a specific wall of this `Room`. |
| [Update](#Update) | Updates the state of this `Room`. |
| [GetState](#GetState) | Gets the internal state of the `Room`. |

## Function Details

### Clear<a name="Clear"></a>
!!! function "void Clear()"

    
    Uninitializes this `Room`.
    
    This doesn't destroy the internal state it references,
    it just removes this reference to it.
    
    To completely destroy the `Room`, use `RemoveRoom()` method
    of the `Engine` instance.
    ```cpp
    amEngine->RemoveRoom(1234); // You should provide the room ID
    ```
            
    

### GetDirection<a name="GetDirection"></a>
!!! function "[[nodiscard]] AmVec3 GetDirection() const"

    
    Gets the direction vector of this `Room`.
    
    
    :material-keyboard-return: **Return**
    :    The direction (forward) vector.
            
    

### GetGain<a name="GetGain"></a>
!!! function "[[nodiscard]] AmReal32 GetGain() const"

    
    Gets the room effects gain.
    
    
    :material-keyboard-return: **Return**
    :    The room effects gain.
            
    

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmRoomID GetId() const"

    
    Returns the unique ID of this `Room`.
    
    
    :material-keyboard-return: **Return**
    :    The `Room` unique ID.
            
    

### GetLocation<a name="GetLocation"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetLocation() const"

    
    Gets the current location of this `Room`.
    
    
    :material-keyboard-return: **Return**
    :    The current location of this `Room`.
            
    

### GetOrientation<a name="GetOrientation"></a>
!!! function "[[nodiscard]] const Orientation&amp; GetOrientation() const"

    
    Gets the current orientation of this `Room`.
    
    
    :material-keyboard-return: **Return**
    :    The current orientation of this `Room`.
            
    

### GetShape<a name="GetShape"></a>
!!! function "[[nodiscard]] const BoxShape&amp; GetShape() const"

    
    Gets the shape representing this `Room`.
    
    
    :material-keyboard-return: **Return**
    :    The `Room` shape.
            
    

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] RoomInternalState&#42; GetState() const"

    
    Gets the internal state of the `Room`.
    
    
    :material-keyboard-return: **Return**
    :    The `Room` internal state.
    
    
    !!! warning
         This method is for internal usage only.
                
    

### GetSurfaceArea<a name="GetSurfaceArea"></a>
!!! function "[[nodiscard]] AmReal32 GetSurfaceArea(RoomWall wall) const"

    
    Gets the surface area of a specific wall of this `Room`.
    
    
    :material-location-enter: **Parameter** `wall`
    :    The wall to get the surface area for.
    
    
    :material-keyboard-return: **Return**
    :    The surface area of the specified wall.
            
    

### GetUp<a name="GetUp"></a>
!!! function "[[nodiscard]] AmVec3 GetUp() const"

    
    Gets the up vector of this `Room`.
    
    
    :material-keyboard-return: **Return**
    :    The up vector.
            
    

### GetVolume<a name="GetVolume"></a>
!!! function "[[nodiscard]] AmReal32 GetVolume() const"

    
    Gets the volume of the `Room` in m3.
    
    
    :material-keyboard-return: **Return**
    :    The volume of the room's shape.
            
    

### GetWallMaterial<a name="GetWallMaterial"></a>
!!! function "[[nodiscard]] const RoomMaterial&amp; GetWallMaterial(RoomWall wall) const"

    
    Gets the material of a specific wall of this `Room`.
    
    
    :material-location-enter: **Parameter** `wall`
    :    The wall to get the material for.
    
    
    :material-keyboard-return: **Return**
    :    The material of the specified wall.
            
    

### Room<a name="Room"></a>
!!! function "Room()"

    
    Creates an uninitialized `Room`.
    
    An uninitialized `Room` doesn't affect sound sources.
    
    To create an initialized `Room`, use the `AddRoom()` method of the
    `Engine` instance.
    ```cpp
    amEngine->AddRoom(1234); // You should provide an unique ID
    ```
            
    

!!! function "explicit Room(RoomInternalState&#42; state)"

    
    Creates a wrapper instance over the provided state.
    
    
    :material-location-enter: **Parameter** `state`
    :    The internal state to wrap.
    
    
    !!! warning
         This constructor is for internal usage only.
                
    

### SetAllWallMaterials<a name="SetAllWallMaterials"></a>
!!! function "void SetAllWallMaterials(const RoomMaterial&amp; material) const"

    
    Sets the material of all walls of this `Room`.
    
    
    :material-location-enter: **Parameter** `material`
    :    The new material.
                
    

### SetDimensions<a name="SetDimensions"></a>
!!! function "void SetDimensions(AmVec3 dimensions) const"

    
    Sets the shape's dimensions of this `Room`.
    
    
    :material-location-enter: **Parameter** `dimensions`
    :    The new dimensions.
                
    

### SetGain<a name="SetGain"></a>
!!! function "void SetGain(AmReal32 gain) const"

    
    Sets the room effects gain.
    
    
    :material-location-enter: **Parameter** `gain`
    :    The gain applied to early reflections and reverberations effects.
                
    

### SetLocation<a name="SetLocation"></a>
!!! function "void SetLocation(const AmVec3&amp; location) const"

    
    Sets the location `Room`.
    
    
    :material-location-enter: **Parameter** `location`
    :    The new location.
                
    

### SetOrientation<a name="SetOrientation"></a>
!!! function "void SetOrientation(const Orientation&amp; orientation) const"

    
    Sets the orientation of this `Room`.
    
    
    :material-location-enter: **Parameter** `orientation`
    :    The new orientation.
                
    

### SetShape<a name="SetShape"></a>
!!! function "void SetShape(const BoxShape&amp; shape) const"

    
    Sets the shape representing this `Room`.
    
    
    :material-location-enter: **Parameter** `shape`
    :    The new shape.
                
    

### SetWallMaterial<a name="SetWallMaterial"></a>
!!! function "void SetWallMaterial(RoomWall wall, const RoomMaterial&amp; material) const"

    
    Sets the material of a specific wall of this `Room`.
    
    
    :material-location-enter: **Parameter** `wall`
    :    The wall to set the material for.
        
    :material-location-enter: **Parameter** `material`
    :    The new material.
                
    

### SetWallMaterials<a name="SetWallMaterials"></a>
!!! function "void SetWallMaterials( const RoomMaterial&amp; leftWallMaterial, const RoomMaterial&amp; rightWallMaterial, const RoomMaterial&amp; floorMaterial, const RoomMaterial&amp; ceilingMaterial, const RoomMaterial&amp; frontWallMaterial, const RoomMaterial&amp; backWallMaterial) const"

    
    Sets the material of each wall of this `Room`.
    
    
    :material-location-enter: **Parameter** `leftWallMaterial`
    :    The material for the left wall.
        
    :material-location-enter: **Parameter** `rightWallMaterial`
    :    The material for the right wall.
        
    :material-location-enter: **Parameter** `floorMaterial`
    :    The material for the floor.
        
    :material-location-enter: **Parameter** `ceilingMaterial`
    :    The material for the ceiling.
        
    :material-location-enter: **Parameter** `frontWallMaterial`
    :    The material for the front wall.
        
    :material-location-enter: **Parameter** `backWallMaterial`
    :    The material for the back wall.
                
    

### Update<a name="Update"></a>
!!! function "void Update() const"

    
    Updates the state of this `Room`.
    
    This method is called automatically by the Engine
    on each frames to update the internal state of the `Room`
    
    
    !!! warning
         This method is for internal usage only.
                
    

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this `Room` has been initialized.
    
    
    :material-keyboard-return: **Return**
    :    `true` if this `Room` has been initialized with a
    valid state.
            
    

