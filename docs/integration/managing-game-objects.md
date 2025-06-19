---
title: Managing Game Objects
description: You can add game objects like entities, listeners, environments and rooms in your 3D environments, manage their lifetime and synchronize them with your game through Amplitude.
---

!!! danger "Incomplete documentation"
    This documentation page is WIP and not yet complete.

Amplitude has various items labeled as game objects: [Entities](#entities), [Listeners](#listeners), [Environments](#environments), and [Rooms](#rooms).

## Entities

Entities are game objects used to spatialize a sound source. Entities share with the sound sources they are playing spatial properties like position, orientation, and directivity.

To create a new Entity, you should use the [`AddEntity()`](../api/engine/Engine.md#addentity) method from the Engine:

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
    Note that the played sound source must be configured with either [Position](../api/core/eSpatialization.md), [PositionOrientation](../api/core/eSpatialization.md), or [HRTF](../api/core/eSpatialization.md) spatialization before to accept any spatial data coming from the entity. Learn more about configuring spatialization for sound sources [here](../project/sound-object.md#spatialization).

!!! info
    Learn more about channels and other ways to play audio in the [Playing Audio](./playing-audio.md) integration guide.

If you want to get a reference to an existing entity, You should use the [`GetEntity()`](../api/engine/Engine.md#getentity) method from the Engine:

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

When it's time to remove an Entity, you should call the [`RemoveEntity()`](../api/engine/Engine.md#removeentity) method from the Engine:

```cpp
// Remove an existing entity using its ID
amEngine->RemoveEntity(271097);

// Remove an existing entity using its reference
amEngine->RemoveEntity(&gun);
```

If the entity to remove was already removed, calling this method will do nothing.

!!! tip "API Reference available"
    Check out the [API reference](../api/engine/Entity.md) for the complete list of methods you can use with an Entity.

## Listeners

## Environments

## Rooms
