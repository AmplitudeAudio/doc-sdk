---
title: Room
description: The absorption coefficients of the material. Represents a physical space where sound waves can propagate. Any sound source within the room will be affected * by the room's properties, and got applied early reflections and reverberation effects.
generator: doxide
---


# Room

**class  Room**


The absorption coefficients of the material.
         



Represents a physical space where sound waves can propagate. Any sound source within the room will be affected
     * by the room's properties, and got applied early reflections and reverberation effects.


!!! note
     This class is a lightweight wrapper around the internal `RoomInternalState` class.
        


## Functions

| Name | Description |
| ---- | ----------- |
| [Room](#Room) | Creates an uninitialized @c Room. |
| [Room](#Room) | Creates a wrapper instance over the provided state.  |
| [Clear](#Clear) | Uninitializes this @c Room. |
| [Valid](#Valid) | Checks whether this @c Room has been initialized. |
| [GetId](#GetId) | Returns the unique ID of this @c Room. |
| [SetLocation](#SetLocation) | Sets the location @c Room. |
| [GetLocation](#GetLocation) | Gets the current location of this @c Room. |
| [SetOrientation](#SetOrientation) | Sets the orientation of this @c Room. |
| [GetOrientation](#GetOrientation) | Gets the current orientation of this @c Room. |
| [GetDirection](#GetDirection) | Gets the direction vector of this @c Room. |
| [GetUp](#GetUp) | Gets the up vector of this @c Room. |
| [SetDimensions](#SetDimensions) | Sets the shape's dimensions of this @c Room.  |
| [SetShape](#SetShape) | Sets the shape representing this @c Room.  |
| [GetShape](#GetShape) | Gets the shape representing this @c Room. |
| [SetWallMaterial](#SetWallMaterial) | Sets the material of a specific wall of this @c Room. |
| [SetAllWallMaterials](#SetAllWallMaterials) | Sets the material of all walls of this @c Room. |
| [SetWallMaterials](#SetWallMaterials) | Sets the material of each wall of this @c Room. |
| [GetWallMaterial](#GetWallMaterial) | Gets the material of a specific wall of this @c Room. |
| [SetGain](#SetGain) | Sets the gain of the early reflections of sound sources * of this room. |
| [GetGain](#GetGain) | Gets the early reflections gain. |
| [GetVolume](#GetVolume) | Gets the volume of the @c Room in m3. |
| [GetSurfaceArea](#GetSurfaceArea) | Gets the surface area of a specific wall of this @c Room. |
| [Update](#Update) | Update the state of this @c Room. |
| [GetState](#GetState) | Gets the internal state of the @c Room. |

## Function Details

### Clear<a name="Clear"></a>
!!! function "void Clear()"

    
    Uninitializes this @c Room.
    
    
    !!! note
         This doesn't destroy the internal state it references,
        it just removes this reference to it.
                
    

### GetDirection<a name="GetDirection"></a>
!!! function "[[nodiscard]] AmVec3 GetDirection() const"

    
    Gets the direction vector of this @c Room.
    
    
    :material-keyboard-return: **Return**
    :    The direction (forward) vector.
            
    

### GetGain<a name="GetGain"></a>
!!! function "[[nodiscard]] AmReal32 GetGain() const"

    
    Gets the early reflections gain.
    
    
    :material-keyboard-return: **Return**
    :    The early reflections gain.
            
    

### GetId<a name="GetId"></a>
!!! function "[[nodiscard]] AmRoomID GetId() const"

    
    Returns the unique ID of this @c Room.
    
    
    :material-keyboard-return: **Return**
    :    The `Room` unique ID.
            
    

### GetLocation<a name="GetLocation"></a>
!!! function "[[nodiscard]] const AmVec3&amp; GetLocation() const"

    
    Gets the current location of this @c Room.
    
    
    :material-keyboard-return: **Return**
    :    The current location of this `Room.`
            
    

### GetOrientation<a name="GetOrientation"></a>
!!! function "[[nodiscard]] const Orientation&amp; GetOrientation() const"

    
    Gets the current orientation of this @c Room.
    
    
    :material-keyboard-return: **Return**
    :    The current orientation of this `Room.`
            
    

### GetShape<a name="GetShape"></a>
!!! function "[[nodiscard]] const BoxShape&amp; GetShape() const"

    
    Gets the shape representing this @c Room.
    
    
    :material-keyboard-return: **Return**
    :    The `Room` shape.
            
    

### GetState<a name="GetState"></a>
!!! function "[[nodiscard]] RoomInternalState&#42; GetState() const"

    
    Gets the internal state of the @c Room.
    
    
    !!! note
         This method is intended for internal usage only.
                
    

### GetSurfaceArea<a name="GetSurfaceArea"></a>
!!! function "[[nodiscard]] AmReal32 GetSurfaceArea(RoomWall wall) const"

    
    Gets the surface area of a specific wall of this @c Room.
    
    
    :material-location-enter: **Parameter** `wall`
    :    The wall to get the surface area for.
    
    
    :material-keyboard-return: **Return**
    :    The surface area of the specified wall.
            
    

### GetUp<a name="GetUp"></a>
!!! function "[[nodiscard]] AmVec3 GetUp() const"

    
    Gets the up vector of this @c Room.
    
    
    :material-keyboard-return: **Return**
    :    The up vector.
            
    

### GetVolume<a name="GetVolume"></a>
!!! function "[[nodiscard]] AmReal32 GetVolume() const"

    
    Gets the volume of the @c Room in m3.
    
    
    :material-keyboard-return: **Return**
    :    The volume of the room.
            
    

### GetWallMaterial<a name="GetWallMaterial"></a>
!!! function "[[nodiscard]] const RoomMaterial&amp; GetWallMaterial(RoomWall wall) const"

    
    Gets the material of a specific wall of this @c Room.
    
    
    :material-location-enter: **Parameter** `wall`
    :    The wall to get the material for.
    
    
    :material-keyboard-return: **Return**
    :    The material of the specified wall.
            
    

### Room<a name="Room"></a>
!!! function "Room()"

    
    Creates an uninitialized @c Room.
    
    
    !!! note
         An uninitialized `Room` doesn't affect sound sources.
                
    

!!! function "explicit Room(RoomInternalState&#42; state)"

    
    Creates a wrapper instance over the provided state.
             
    
    
    

### SetAllWallMaterials<a name="SetAllWallMaterials"></a>
!!! function "void SetAllWallMaterials(const RoomMaterial&amp; material) const"

    
    Sets the material of all walls of this @c Room.
    
    
    :material-location-enter: **Parameter** `material`
    :    The new material.
                
    

### SetDimensions<a name="SetDimensions"></a>
!!! function "void SetDimensions(AmVec3 dimensions) const"

    
    Sets the shape's dimensions of this @c Room.
             
    
    
    

### SetGain<a name="SetGain"></a>
!!! function "void SetGain(AmReal32 gain) const"

    
    Sets the gain of the early reflections of sound sources
             * of this room.
    
    
    :material-location-enter: **Parameter** `gain`
    :    The gain applied to early reflections of sound sources.
                
    

### SetLocation<a name="SetLocation"></a>
!!! function "void SetLocation(const AmVec3&amp; location) const"

    
    Sets the location @c Room.
    
    
    :material-location-enter: **Parameter** `location`
    :    The new location.
                
    

### SetOrientation<a name="SetOrientation"></a>
!!! function "void SetOrientation(const Orientation&amp; orientation) const"

    
    Sets the orientation of this @c Room.
    
    
    :material-location-enter: **Parameter** `orientation`
    :    The new orientation.
                
    

### SetShape<a name="SetShape"></a>
!!! function "void SetShape(const BoxShape&amp; shape) const"

    
    Sets the shape representing this @c Room.
             
    
    
    

### SetWallMaterial<a name="SetWallMaterial"></a>
!!! function "void SetWallMaterial(RoomWall wall, const RoomMaterial&amp; material) const"

    
    Sets the material of a specific wall of this @c Room.
    
    
    :material-location-enter: **Parameter** `wall`
    :    The wall to set the material for.
        
    :material-location-enter: **Parameter** `material`
    :    The new material.
                
    

### SetWallMaterials<a name="SetWallMaterials"></a>
!!! function "void SetWallMaterials( const RoomMaterial&amp; leftWallMaterial, const RoomMaterial&amp; rightWallMaterial, const RoomMaterial&amp; floorMaterial, const RoomMaterial&amp; ceilingMaterial, const RoomMaterial&amp; frontWallMaterial, const RoomMaterial&amp; backWallMaterial) const"

    
    Sets the material of each wall of this @c Room.
    
    
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

    
    Update the state of this @c Room.
    
    This method is called automatically by the Engine
    on each frames.
            
    

### Valid<a name="Valid"></a>
!!! function "[[nodiscard]] bool Valid() const"

    
    Checks whether this @c Room has been initialized.
    
    
    :material-keyboard-return: **Return**
    :    `true` if this `Room` has been initialized with a
    valid state.
            
    

