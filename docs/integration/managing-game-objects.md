---
title: Managing Game Objects
description: You can add game objects like entities, listeners, environments and rooms in your 3D environments, manage their lifetime and synchronize them with your game through Amplitude.
diataxis: how-to
---

Amplitude has various items labeled as game objects: [Entities](#entities), [Listeners](#listeners), [Environments](#environments), and [Rooms](#rooms).

## Entities

Entities are game objects used to spatialize sound sources. Entities share with the sound sources they are playing spatial properties like position, orientation, and directivity.

To create a new Entity, you should use the [`AddEntity()`](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_engine.md#public-functions) method from the Engine:

```cpp
// Adding an entity
Entity speaker = amEngine->AddEntity(1234); // 1234 is the entity unique ID
```

You must provide a unique ID for the Entity when creating it, attempting to create another Entity with the same ID, will just return the previously created entity.

!!! tip
    It's strongly recommended using the same ID from your game's entity, to easily recognize what entity in Amplitude is linked to what entity in your game.

!!! warning
    The maximum number of entities you can add is restricted by the loaded [engine configuration](../project/engine-config.md#entities). Please make sure to set the appropriate value for your project.

Once you have a valid Entity, you can use it to play a sound on it:

```cpp
// Create a gun entity
Entity gun = amEngine->AddEntity(271097);

// Play a gunfire sound on a gun entity
Channel gunfire = amEngine->Play("weapons/ak47/gunfires", gun);

// Now the gun entity will feed the sound source with spatial properties...
```
!!! warning
    Note that the played sound source must be configured with either [Position](../api/group__core.md#public-types), [PositionOrientation](../api/group__core.md#public-types), or [HRTF](../api/group__core.md#public-types) spatialization before to accept any spatial data coming from the entity. Learn more about configuring spatialization for sound sources [here](../project/sound-object.md#spatialization).

!!! info
    Learn more about channels and other ways to play audio in the [Playing Audio](./playing-audio.md) integration guide.

If you want to get a reference to an existing entity, You should use the [`GetEntity()`](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_engine.md#public-functions) method from the Engine:

```cpp
// Get an existing entity
Entity gun = amEngine->GetEntity(271097);
```

If an entity queried this way does not exist, an **invalid entity** will be returned instead. So it's always safe to check for the entity validity before using it:

```cpp
// Get an entity
Entity speaker = amEngine->GetEntity(1234);

// Check if the entity is valid
if (!speaker.Valid())
    amLogError("Unable to find an entity with ID: 1234");
```

When it's time to remove an Entity, you should call the [`RemoveEntity()`](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_engine.md#public-functions) method from the Engine:

```cpp
// Remove an existing entity using its ID
amEngine->RemoveEntity(271097);

// Remove an existing entity using its reference
amEngine->RemoveEntity(&gun);
```

If the entity to remove was already removed, calling this method will do nothing.

!!! tip "API Reference available"
    Check out the [API reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_entity.md) for the complete list of methods you can use with an Entity.

## Listeners

Listeners are the "ears" of your audio scene - they represent points in 3D space from which sound is rendered. At least one Listener is required for Amplitude to render any spatialized sound sources. Typically, a Listener is attached to the player's camera or character.

### Creating and Removing Listeners

To create a new Listener, use the [`AddListener()`](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_engine.md#public-functions) method from the Engine:

```cpp
// Adding a listener with a unique ID
Listener playerListener = amEngine->AddListener(1); // 1 is the listener unique ID
```

You must provide a unique ID for the Listener. Attempting to create another Listener with the same ID will return the previously created listener.

!!! warning
    The maximum number of listeners you can add is restricted by the loaded [engine configuration](../project/engine-config.md#listeners). Please make sure to set the appropriate value for your project.

To retrieve an existing Listener, use the [`GetListener()`](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_engine.md#public-functions) method:

```cpp
// Get an existing listener
Listener listener = amEngine->GetListener(1);

// Always verify the listener is valid
if (!listener.Valid())
    amLogError("Unable to find a listener with ID: 1");
```

To remove a Listener when it's no longer needed:

```cpp
// Remove by ID
amEngine->RemoveListener(1);

// Or remove by reference
amEngine->RemoveListener(&playerListener);
```

### Listener Properties

Listeners have several properties that control how they perceive sound in the 3D environment:

#### Location and Orientation

The most essential properties are position and orientation in world space:

```cpp
// Set listener position (world coordinates)
listener.SetLocation({ 10.0f, 1.8f, 5.0f });

// Set listener orientation using forward and up vectors
Orientation orientation({ 0.0f, 0.0f, -1.0f }, { 0.0f, 1.0f, 0.0f });
listener.SetOrientation(orientation);

// Alternatively, create orientation from yaw, pitch, roll angles (in radians)
Orientation angularOrientation(0.0f, 0.0f, 0.0f); // yaw, pitch, roll
listener.SetOrientation(angularOrientation);
```

!!! tip
    Update listener position and orientation every frame to match your game camera or player character. This is typically done before calling `AdvanceFrame()`.

#### Directivity

Directivity controls how focused the listener's hearing is. A directivity of `0.0` means omnidirectional hearing (hears equally in all directions), while `1.0` means fully directional (hears best in the forward direction):

```cpp
// Set directivity and sharpness together
// directivity: 0.0 = omnidirectional, 1.0 = fully directional
// sharpness: 1.0 to +INF, higher values = tighter front lobe
listener.SetDirectivity(0.5f, 2.0f);
```

!!! info
    Directivity is useful for simulating focused listening, such as a character cupping their ear or using a listening device.

### Velocity and Doppler Effect

Amplitude automatically calculates listener velocity from position changes between frames. This velocity is used for Doppler effect calculations when sounds move relative to the listener.

```cpp
// Velocity is calculated automatically, but you can retrieve it
AmVector3 velocity = listener.GetVelocity();
```

### Multiple Listeners

Amplitude supports multiple simultaneous listeners, which is useful for:

- Split-screen multiplayer games
- Picture-in-picture scenarios
- Security camera views with audio

```cpp
// Create listeners for split-screen players
Listener player1Listener = amEngine->AddListener(1);
Listener player2Listener = amEngine->AddListener(2);

// Update each listener independently
player1Listener.SetLocation(player1Camera.GetPosition());
player2Listener.SetLocation(player2Camera.GetPosition());
```

!!! tip "API Reference available"
    Check out the [API reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_listener.md) for the complete list of methods you can use with a Listener.

## Environments

Environments are spatial zones that apply audio effects to sounds playing within them. They combine a geometric zone definition with an audio effect, creating areas where sounds are processed differently - such as a cave with reverb or an underwater area with muffled audio.

### Creating and Managing Environments

To create an Environment:

```cpp
// Add an environment with a unique ID
Environment caveEnvironment = amEngine->AddEnvironment(100);
```

To retrieve or remove an Environment:

```cpp
// Get an existing environment
Environment env = amEngine->GetEnvironment(100);

// Check validity
if (!env.Valid())
    amLogError("Environment not found");

// Remove when no longer needed
amEngine->RemoveEnvironment(100);
```

!!! warning
    The maximum number of environments is restricted by your [engine configuration](../project/engine-config.md#environments).

### Configuring Environment Zones

Environments use **Zones** to define their spatial boundaries. A Zone has an inner shape and an outer shape:

- **Inside the inner shape**: Effect is applied at full strength (factor = 1.0)
- **Between inner and outer shapes**: Effect gradually increases (factor transitions 0.0 → 1.0)
- **Outside the outer shape**: No effect applied (factor = 0.0)

```cpp
// Create inner and outer box shapes (half-width, half-height, half-depth)
auto innerShape = amshared(BoxShape, 5.0f, 5.0f, 2.5f);
auto outerShape = amshared(BoxShape, 10.0f, 10.0f, 5.0f);

// Create a box zone from the shapes
auto zone = amshared(BoxZone, innerShape, outerShape);

// Set the zone location
zone->SetLocation({ 100.0f, 0.0f, 50.0f });

// Assign the zone to the environment
caveEnvironment.SetZone(zone);
```

Amplitude supports several zone shapes:

| Zone Type | Shape | Description | Use Case |
|-----------|-------|-------------|----------|
| `BoxZone` | `BoxShape` | Rectangular cuboid | Rooms, corridors |
| `SphereZone` | `SphereShape` | Spherical volume | Point sources of effect |
| `CapsuleZone` | `CapsuleShape` | Cylinder with hemispherical caps | Tunnels, pipes |
| `ConeZone` | `ConeShape` | Conical volume | Directional effect areas |

### Assigning Effects to Environments

Each Environment is linked to an [Effect](../project/effect.md) that processes audio within the zone:

```cpp
// Set the effect by ID
caveEnvironment.SetEffect(42);

// Or by name
caveEnvironment.SetEffect("cave_reverb");
```

### Environment Position and Orientation

Environments can be positioned and rotated in world space:

```cpp
// Position the environment
caveEnvironment.SetLocation({ 100.0f, 0.0f, 50.0f });

// Set orientation using forward and up vectors
Orientation envOrientation({ 1.0f, 0.0f, 0.0f }, { 0.0f, 1.0f, 0.0f });
caveEnvironment.SetOrientation(envOrientation);
```

### How Environment Factors Work

During each frame, Amplitude calculates an **environment factor** for each entity based on its position relative to environment zones. This factor determines how much of the environment's effect is applied:

```
Entity Position          Factor    Effect Application
─────────────────────────────────────────────────────
Inside inner zone        1.0       Full effect
In fade zone             0.0-1.0   Gradual blend
Outside outer zone       0.0       No effect
```

You can query the environment factor for any position or entity:

```cpp
// Get factor for a specific location
AmReal32 factor = caveEnvironment.GetFactor({ 105.0f, 0.0f, 55.0f });

// Get factor for an entity
Entity player = amEngine->GetEntity(1);
AmReal32 entityFactor = caveEnvironment.GetFactor(player);
```

!!! info "Performance Optimization"
    Amplitude caches environment factors and only recalculates them when an entity moves or an environment changes. This is handled automatically during `AdvanceFrame()`.

!!! note "Custom Environment Tracking"
    By default, Amplitude automatically computes environment factors using the zones you define. However, if your game has its own spatial awareness system (e.g., a custom physics or zone system), you can disable automatic computation by setting `track_environments: false` in your [engine configuration](../project/engine-config.md). When disabled, your game is responsible for computing and sending environment levels to the engine, and any zones defined in environments will be ignored. See the [engine configuration schema](../project/api.md) for more details.

!!! tip "API Reference available"
    Check out the [API reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_environment.md) for the complete list of methods you can use with an Environment.

## Rooms

Rooms are physically-modeled acoustic spaces that apply early reflections and reverberation to sounds within them. Unlike Environments (which apply arbitrary effects), Rooms simulate real acoustic properties based on room geometry and wall materials.

### Creating and Managing Rooms

To create a Room:

```cpp
// Add a room with a unique ID
Room concertHall = amEngine->AddRoom(200);
```

To retrieve or remove a Room:

```cpp
// Get an existing room
Room room = amEngine->GetRoom(200);

// Check validity
if (!room.Valid())
    amLogError("Room not found");

// Remove when no longer needed
amEngine->RemoveRoom(200);
```

!!! warning
    The maximum number of rooms is restricted by your [engine configuration](../project/engine-config.md#rooms).

### Room Dimensions

Rooms are defined as box-shaped volumes with specific dimensions:

```cpp
// Set room dimensions (width, depth, height in meters)
concertHall.SetDimensions({ 30.0f, 50.0f, 15.0f });

// Position the room in world space
concertHall.SetLocation({ 0.0f, 0.0f, 0.0f });

// Set room orientation using forward and up vectors
Orientation roomOrientation({ 0.0f, 0.0f, 1.0f }, { 0.0f, 1.0f, 0.0f });
concertHall.SetOrientation(roomOrientation);
```

The room's acoustic properties (reverb time, early reflections) are automatically calculated based on these dimensions and the wall materials.

### Wall Materials

Each room has 6 walls, and each wall can have a different material that affects sound absorption:

```cpp
// Available walls:
// eRoomWall_Left, eRoomWall_Right
// eRoomWall_Floor (or eRoomWall_Bottom), eRoomWall_Ceiling (or eRoomWall_Top)
// eRoomWall_Front, eRoomWall_Back

// Set individual wall materials using predefined types
concertHall.SetWallMaterial(eRoomWall_Floor, RoomWallMaterial(eRoomWallMaterialType_Wood));
concertHall.SetWallMaterial(eRoomWall_Ceiling, RoomWallMaterial(eRoomWallMaterialType_AcousticTile));
concertHall.SetWallMaterial(eRoomWall_Left, RoomWallMaterial(eRoomWallMaterialType_GypsumBoard));
concertHall.SetWallMaterial(eRoomWall_Right, RoomWallMaterial(eRoomWallMaterialType_GypsumBoard));
concertHall.SetWallMaterial(eRoomWall_Front, RoomWallMaterial(eRoomWallMaterialType_Glass));
concertHall.SetWallMaterial(eRoomWall_Back, RoomWallMaterial(eRoomWallMaterialType_ConcreteUnpainted));

// Or set all walls to the same material
concertHall.SetAllWallMaterials(RoomWallMaterial(eRoomWallMaterialType_ConcreteUnpainted));

// Or set each wall individually in one call
concertHall.SetWallMaterials(
    RoomWallMaterial(eRoomWallMaterialType_GypsumBoard),    // left
    RoomWallMaterial(eRoomWallMaterialType_GypsumBoard),    // right
    RoomWallMaterial(eRoomWallMaterialType_Wood),           // floor
    RoomWallMaterial(eRoomWallMaterialType_AcousticTile),   // ceiling
    RoomWallMaterial(eRoomWallMaterialType_Glass),          // front
    RoomWallMaterial(eRoomWallMaterialType_ConcreteUnpainted) // back
);
```

#### Available Wall Materials

| Material Type | Description | Absorption |
|---------------|-------------|------------|
| `eRoomWallMaterialType_Transparent` | No acoustic effect | Very High |
| `eRoomWallMaterialType_AcousticTile` | Sound-absorbing ceiling tiles | High |
| `eRoomWallMaterialType_HeavyDrapes` | Heavy curtains/drapes | High |
| `eRoomWallMaterialType_CarpetOnConcrete` | Carpeted floor | Medium-High |
| `eRoomWallMaterialType_FoamPanel` | Acoustic foam panels | Medium-High |
| `eRoomWallMaterialType_GypsumBoard` | Drywall/plasterboard | Medium |
| `eRoomWallMaterialType_PlasterSmooth` | Smooth plaster | Medium |
| `eRoomWallMaterialType_Wood` | Wooden panels or floors | Medium-Low |
| `eRoomWallMaterialType_BrickPainted` | Painted brick | Low |
| `eRoomWallMaterialType_ConcreteUnpainted` | Raw concrete surfaces | Low |
| `eRoomWallMaterialType_Glass` | Glass windows/walls | Very Low |
| `eRoomWallMaterialType_Marble` | Marble or stone | Very Low |
| `eRoomWallMaterialType_Metal` | Metal surfaces | Very Low |
| `eRoomWallMaterialType_WaterSurface` | Water surface | Variable |
| `eRoomWallMaterialType_IceSurface` | Ice/frozen surface | Very Low |
| `eRoomWallMaterialType_Custom` | User-defined coefficients | Custom |

!!! info
    Materials with lower absorption create longer reverb tails (more reflective), while high-absorption materials create shorter, deader acoustics.

### Room Gain

You can scale the overall effect of room acoustics with the gain parameter:

```cpp
// Set room gain (0.0 = no room effect, 1.0 = full effect)
concertHall.SetGain(0.8f);
```

### Custom Wall Materials

For precise acoustic modeling, you can create custom wall materials with specific absorption coefficients across 9 frequency bands:

```cpp
// Create a custom material
RoomWallMaterial customMaterial; // Defaults to eRoomWallMaterialType_Custom

// Set absorption coefficients for 9 frequency bands (low to high)
customMaterial.m_absorptionCoefficients[0] = 0.10f; // Very low frequencies
customMaterial.m_absorptionCoefficients[1] = 0.15f;
customMaterial.m_absorptionCoefficients[2] = 0.20f;
customMaterial.m_absorptionCoefficients[3] = 0.25f;
customMaterial.m_absorptionCoefficients[4] = 0.30f; // Mid frequencies
customMaterial.m_absorptionCoefficients[5] = 0.35f;
customMaterial.m_absorptionCoefficients[6] = 0.40f;
customMaterial.m_absorptionCoefficients[7] = 0.45f;
customMaterial.m_absorptionCoefficients[8] = 0.50f; // High frequencies

concertHall.SetWallMaterial(eRoomWall_Back, customMaterial);
```

### Room Shape and Volume

You can also define the room using a `BoxShape` directly, and query room properties:

```cpp
// Set room shape directly
BoxShape roomShape(15.0f, 25.0f, 7.5f); // half-width, half-height, half-depth
concertHall.SetShape(roomShape);

// Query room properties
AmReal32 volume = concertHall.GetVolume();           // Volume in cubic meters
AmVector3 dimensions = concertHall.GetDimensions();   // Full dimensions
AmReal32 floorArea = concertHall.GetSurfaceArea(eRoomWall_Floor); // Wall surface area
```

### Room Processing Priority

When multiple rooms exist in a scene, Amplitude processes them in order of volume (largest first). This ensures that the most significant acoustic spaces take priority when computational resources are limited.

!!! tip "API Reference available"
    Check out the [API reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_room.md) for the complete list of methods you can use with a Room.
