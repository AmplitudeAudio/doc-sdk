---
title: Event
description: Amplitude allows you to create and trigger a sequence of actions at runtime with events.
---

An event is a set of actions Amplitude have to execute once it has been triggered at runtime, during your game. Event assets are described with the following properties:

!!! info
    The flatbuffers schema of this file can be found [here](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/event_definition.fbs).

## id

`uint64` `required`

A unique value across event assets that represents the ID of this object. It may be reused later to get the instance of this event from the engine at runtime.

## name

`string` `required`

A unique value across event assets that represents the name of this object. It may be reused later to get the instance of this event from the engine at runtime.

## actions

`EventActionDefinition[]` `required`

An array of actions to execute. When this event will be triggered, each action will be executed sequentially in the order they are defined in this array. Each object of this is defined by the given properties:

### type

`EventActionType` `default: None`

This specifies the type of action to execute. The possible values of this enumeration are:

| ID        | Description                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------- |
| None      | _noop_ action.                                                                                       |
| Play      | Plays the sound objects with the identifiers given in the `targets` property.                        |
| Pause     | Pauses the sound objects with the identifiers given in the `targets` property.                       |
| Resume    | Resumes the sound objects with the identifiers given in the `targets` property.                      |
| Stop      | Stops the sound objects with the identifiers given in the `targets` property.                        |
| Seek      | Seeks the sound objects with the identifiers given in the `targets` property, to the given position. |
| MuteBus   | Mutes the buses with the identifiers given in the `targets` property.                                |
| UnmuteBus | Unmutes the buses with the identifiers given in the `targets` property.                              |

!!! warning
    The `Seek` action is not yet supported. Creating a `Seek` action will result in a _noop_.

### active

`bool` `default: true`

Defines whether the action is active or not. An inactive action will not be executed when the parent event will be triggered at runtime.

### targets

`uint64[]` `required`

A list of object identifiers on which execute the given `action`. For `Play`, `Pause`, `Resume`, `Stop` and `Seek` actions, this array should contain [Sound Objects] identifiers. For `MuteBus` and `UnmuteBus` actions, this array should contain [Buses] identifiers.

### scope

`Scope` `default: Entity`

Set the [Scope] in which this action will be executed. If this value is set to `Entity`, the event should be triggered with a valid entity at runtime.

## Example

```json {title="player_footstep.json"}
{
  "name": "player_footstep",
  "id": 876,
  "actions": [
    {
      "type": "Play",
      "active": true,
      "targets": [
      200
      ],
      "scope": "Entity"
    }
  ]
}
```

[Sound Objects]: ./sound-object.md
[Buses]: ./buses-config.md
[Scope]: ./api.md#scope
