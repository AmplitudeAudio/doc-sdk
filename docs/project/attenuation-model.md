---
title: Attenuation Model
description: Attenuation models are settings that describe how the gain of a sound object should fade according to the distance from its listener and a given shape. Read this article to learn more about them.
---

Attenuation models are a way to specify how the gain of a sound object is affected by its position in space (in the case of spatialized sounds), and its distance from the attached listener.

!!! info
    The flatbuffers schema of this file can be found [here](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/attenuation_definition.fbs).

An attenuation model is configured with the following properties:

## id

`uint64` `required`

A unique identifier for the attenuation model. This will be used later to specify the attenuation model in the sound objects. This value should be different from `0`.

## name

`string` `required`

A unique name for the attenuation model. This may be used in runtime to access the attenuation instance from the engine.

## max_distance

`double` `required`

The maximum distance for the sound object to propagate. When the distance from a sound object to its attached listener is greater than the `max_distance` value, the gain is automatically set to zero.

## shape

`AttenuationShape` `required`

Each attenuation model is represented by a shape instructing the engine on how to affect the sound object's gain.

The value of the `shape` property is an object with the following properties:

### zone

`Zone` `required`

This value stores the definition of the type of shape you want for the attenuation model. The final attenuation behavior will depend on the specified shape. Amplitude made available the following shapes for attenuation models:

- Box Shape
- Capsule Shape
- Cone Shape
- Sphere Shape

!!! info
    To learn more about shapes and their properties, please refer to the [Shape](../api/math/Shape/index.md) API reference.

### max_attenuation_factor

`float` `required`

The `max_attenuation_factor` value defines the maximum amount of attenuation to apply to the sound object. This value is used when the listener is inside the outer zone of the shape but outside its inner zone.

## gain_curve

`Curve` `required`

This specifies the curve used to change the sound object's gain. The values over the X-axis of the curve are the distance between the sound object and the listener, and over the Y-axis of the curve is the gain of the sound object.
For best results, the curve must fit in the range `[0, max_distance]` over the X-axis, and in the range `[0, 1]` over the Y-axis.

## Example

An example of a simple attenuation model with a box shape may be:

```json {title="room.json"}
{
  "id": 2,
  "name": "room",
  "max_distance": 40,
  "shape": {
    "zone_type": "Box",
    "zone": {
      "inner": {
        "half_width": 15,
        "half_height": 5,
        "half_depth": 5
      },
      "outer": {
        "half_width": 20,
        "half_height": 35,
        "half_depth": 10
      }
    },
    "max_attenuation_factor": 0.125
  },
  "gain_curve": {
    "parts": [
      {
        "start": {
          "x": 0,
          "y": 1
        },
        "end": {
          "x": 40,
          "y": 0
        },
        "fader": "ExponentialSmooth"
      }
    ]
  }
}
```
