---
title: Common API
description: Browse the API of common types and enumerations shared between Amplitude assets.
diataxis: reference
---

## CurveDefinition {#curve-definition}

Describes a function that is applied on a value to transform the result.

### parts {#curve-definition-parts}

`CurvePartDefinition[]` `required`

An array of objects representing each part of the curve. Each object provides a start point, an end point, and fading function to use to link them. Check the [CurvePartDefinition] section for more information.

The final range of the curve will be bounded within the lowest point and the highest point of all the curve parts.

### Example {#curve-definition-example}

```json
{
  "parts": [
    {
      "start": {
        "x": 0,
        "y": 0
      },
      "end": {
        "x": 1,
        "y": 1
      },
      "fader": "Linear"
    }
  ]
}
```

---

## CurvePartDefinition {#curve-part-definition}

An object describing a single part of a curve. Allowed properties are:

### start {#curve-part-definition-start}

`CurvePointDefinition` `required`

The start point of the curve. It stores the coordinates of the point in the graph. Check the [CurvePointDefinition] section for more information.

### end {#curve-part-definition-end}

`CurvePointDefinition` `required`

The end point of the curve. It stores the coordinates of the point in the graph. Check the [CurvePointDefinition] section for more information.

### fader {#curve-part-definition-fader}

`string` `required`

The fader transition to use while moving values from the `start` point to the `end` point. This stores as value a name to a registered fader transition.

### Example {#curve-part-definition-example}

```json
{
  "start": {
    "x": 0,
    "y": 0
  },
  "end": {
    "x": 1,
    "y": 1
  },
  "fader": "SCurveSmooth"
}
```

---

## CurvePointDefinition {#curve-point-definition}

Represents a point in a curve graph. It's an object defined by 2 coordinate values:

### x {#curve-point-definition-x}

`double` `required`

The position of the point over the X-axis. The X-axis represents the values passed to the curve for computation.

### y {#curve-point-definition-y}

`float` `required`

The position of the point over the Y-axis. The Y-axis represents the result of the computation for a given value.

### Example {#curve-point-definition-example}

```json
{
  "x": 1,
  "y": 343.33
}
```

---

## FadeTransitionSettings {#fade-transition-settings}

This object defines the settings for a fade transition. It is described by the following attributes:

### duration {#fade-transition-settings-duration}

`double` `required`

The duration of the fade transition, expressed in **milliseconds**.

### fader {#fade-transition-settings-fader}

`string` `required`

The name of the [Fader] algorithm to be used. It can be one of those shipped with the engine or from plugins.

### Example {#fade-transition-settings-example}

```json
{
  "duration": 3000,
  "fader": "ExponentialSmooth"
}
```

---

## RtpcCompatibleValue {#rtpc-compatible-value}

An RTPC-compatible value is an object that can hold a static value or a link to an RTPC value.

### kind {#rtpc-compatible-value-kind}

`ValueKind` `default: Static`

Specifies the kind of value that should be used. The possible values are:

| ID     | Description                                                   |
| ------ | ------------------------------------------------------------- |
| Static | The parameter is static value specified by the `value` field. |
| RTPC   | The parameter is a RTPC value specified by the `rtpc` field.  |

When the `kind` property is set to `Static`, it is required to define a `value` field. When the `kind` property is set to `RTPC`, it is required to define a `rtpc` field.

The default value is `Static`.

### value {#rtpc-compatible-value-value}

`float`

A static value that will be used at runtime. This property is only available when the `kind` property is set to `Static`.

### rtpc {#rtpc-compatible-value-rtpc}

`RtpcParameter`

An object that describe how the value should be updated according to a RTPC object. This object takes as input:

- `id`: The ID of the RTPC object to use.
- `curve`: A [CurveDefinition] object that defines the function to apply on the RTPC value to compute this parameter value.

Check the [RtpcParameter] section for more information.

### Example {#rtpc-compatible-value-example}

An RTPC-compatible value with a static value:

```json
{
  "kind": "Static",
  "value": 5
}
```

An RTPC-compatible value with an RTPC parameter:

```json
{
  "kind": "RTPC",
  "rtpc": {
    "id": 19,
    "curve": {
      "parts": [
        {
          "start": {
            "x": 0,
            "y": 1
          },
          "end": {
            "x": 100,
            "y": 0
          },
          "fader": "Linear"
        }
      ]
    }
  }
}
```

---

## RtpcParameter {#rtpc-parameter}

An object used to defines how to gather values from a [RtpcCompatibleValue] with the `kind` property set to `RTPC`. This allows you to use a curve to convert values from the RTPC object to other values.

### id {#rtpc-parameter-id}

`uint64` `required`

The id of the RTPC object where to get the value. This value should reference a valid RTPC object.

### curve {#rtpc-parameter-curve}

`CurveDefinition` `required`

The curve to use when converting values from the RTPC object. It stores as value an object matching the specification of a [CurveDefinition]. Check the [CurveDefinition] section for more information.

### Example {#rtpc-parameter-example}

```json
{
  "id": 24,
  "curve": {
    "parts": [
      {
        "start": {
          "x": 0,
          "y": 1
        },
        "end": {
          "x": 1,
          "y": 0
        },
        "fader": "SCurveSharp"
      }
    ]
  }
}
```

---

## BoxShapeDefinition {#box-shape-definition}

Defines a box-shaped zone used in [Attenuation](./attenuation-model.md) models.

| Property      | Type    | Description                           |
| ------------- | ------- | ------------------------------------- |
| `half_width`  | `float` | Half the width of the box (X-axis).   |
| `half_height` | `float` | Half the height of the box (Y-axis).  |
| `half_depth`  | `float` | Half the depth of the box (Z-axis).   |

---

## CapsuleShapeDefinition {#capsule-shape-definition}

Defines a capsule-shaped zone used in [Attenuation](./attenuation-model.md) models.

| Property      | Type    | Description                                  |
| ------------- | ------- | -------------------------------------------- |
| `radius`      | `float` | The radius of the capsule's hemispheres.     |
| `half_height` | `float` | Half the height of the capsule's cylinder.   |

---

## ConeShapeDefinition {#cone-shape-definition}

Defines a cone-shaped zone used in [Attenuation](./attenuation-model.md) models.

| Property | Type    | Description                  |
| -------- | ------- | ---------------------------- |
| `radius` | `float` | The radius of the cone base. |
| `height` | `float` | The height of the cone.      |

---

## SphereShapeDefinition {#sphere-shape-definition}

Defines a sphere-shaped zone used in [Attenuation](./attenuation-model.md) models.

| Property | Type    | Description                |
| -------- | ------- | -------------------------- |
| `radius` | `float` | The radius of the sphere.  |

---

## Spatialization {#spatialization}

The `Spatialization` enum controls how a sound object is rendered in 3D space. It is used by [Sound](./sound.md), [Collection](./collection.md), and [Switch Container](./switch-container.md) assets via the [`spatialization`](./sound-object.md#spatialization) field.

| ID  | Name                | Description                                                                                                                                                                                                |
| --- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | None                | No spatialization. The sound is played at its raw gain.                                                                                                                                                    |
| 1   | Position            | 2D spatialization based on position only. Attenuation and stereo panning may apply.                                                                                                                        |
| 2   | PositionOrientation | 2D spatialization based on position and orientation. Requires the sound object's [`scope`](./sound-object.md#scope) to be `Entity`.                                                                        |
| 3   | HRTF                | 3D spatialization through an [HRIR Sphere](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_h_r_i_r_sphere.md). Requires `scope: Entity` and a configured [`hrtf`](./engine-config.md#hrtf) block.  |

---

## Scope {#scope}

The `Scope` enum controls how playback data is shared between sound instances. It is used by sound objects ([`scope`](./sound-object.md#scope)) and event actions ([`scope`](./event.md#scope)).

| ID  | Name   | Description                                                                                                          |
| --- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| 0   | World  | All instances share the same playback state (one logical voice across the world).                                    |
| 1   | Entity | Each entity gets its own playback state. Required for `PositionOrientation` and `HRTF` spatialization.               |

---

## PanningMode {#panning-mode}

The `PanningMode` enum is used by the [mixer](./engine-config.md#mixer) configuration to select how spatial sounds are rendered to speakers.

| ID  | Name                  | Description                                                                                                                                |
| --- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 0   | Stereo                | 2D stereo (left/right) panning based on horizontal position in listener space.                                                             |
| 1   | BinauralLowQuality    | HRTF-based panning using first-order Ambisonics over a virtual array of 8 loudspeakers (cube layout).                                      |
| 2   | BinauralMediumQuality | HRTF-based panning using second-order Ambisonics over a virtual array of 12 loudspeakers (dodecahedron layout).                            |
| 3   | BinauralHighQuality   | HRTF-based panning using third-order Ambisonics over a virtual array of 26 loudspeakers (Lebedev grid).                                    |

---

## ZoneDefinition {#zone-definition}

`ZoneDefinition` is a FlatBuffers union used by the [`shape.zone`](./attenuation-model.md#zone) field of an attenuation model. The JSON encoding requires both a discriminator (`zone_type`) and a payload (`zone`); see [Union encoding](#flatbuffers-union-encoding) below.

| Variant       | `zone_type`   | Payload table                                                       |
| ------------- | ------------- | ------------------------------------------------------------------- |
| Box zone      | `BoxZone`     | [`BoxZoneSettings`](#box-zone-settings)                             |
| Capsule zone  | `CapsuleZone` | [`CapsuleZoneSettings`](#capsule-zone-settings)                     |
| Cone zone     | `ConeZone`    | [`ConeZoneSettings`](#cone-zone-settings)                           |
| Sphere zone   | `SphereZone`  | [`SphereZoneSettings`](#sphere-zone-settings)                       |

Each variant carries an `inner` and an `outer` shape definition. The space between the two is where the attenuation model interpolates the gain.

### BoxZoneSettings {#box-zone-settings}

| Property | Type                                          | Description                          |
| -------- | --------------------------------------------- | ------------------------------------ |
| `inner`  | [BoxShapeDefinition](#box-shape-definition)   | Inner zone — full-gain region.       |
| `outer`  | [BoxShapeDefinition](#box-shape-definition)   | Outer zone — silent boundary region. |

### CapsuleZoneSettings {#capsule-zone-settings}

| Property | Type                                                  | Description                          |
| -------- | ----------------------------------------------------- | ------------------------------------ |
| `inner`  | [CapsuleShapeDefinition](#capsule-shape-definition)   | Inner zone — full-gain region.       |
| `outer`  | [CapsuleShapeDefinition](#capsule-shape-definition)   | Outer zone — silent boundary region. |

### ConeZoneSettings {#cone-zone-settings}

| Property | Type                                            | Description                          |
| -------- | ----------------------------------------------- | ------------------------------------ |
| `inner`  | [ConeShapeDefinition](#cone-shape-definition)   | Inner zone — full-gain region.       |
| `outer`  | [ConeShapeDefinition](#cone-shape-definition)   | Outer zone — silent boundary region. |

### SphereZoneSettings {#sphere-zone-settings}

| Property | Type                                                | Description                          |
| -------- | --------------------------------------------------- | ------------------------------------ |
| `inner`  | [SphereShapeDefinition](#sphere-shape-definition)   | Inner zone — full-gain region.       |
| `outer`  | [SphereShapeDefinition](#sphere-shape-definition)   | Outer zone — silent boundary region. |

---

## FlatBuffers union encoding {#flatbuffers-union-encoding}

Several Amplitude assets use FlatBuffers [unions](https://flatbuffers.dev/flatbuffers_guide_writing_schema.html#unions) — a tagged variant where the runtime needs both the variant tag and the payload. In JSON form, FlatBuffers encodes a union with **two parallel fields**:

- `<field>_type`: the discriminator (a string naming the variant).
- `<field>`: the payload, whose shape depends on the variant.

For union arrays, both fields are arrays of the same length and the i-th element of `<field>_type` describes the i-th element of `<field>`.

### Single-element example — `ZoneDefinition`

```json
"shape": {
  "zone_type": "BoxZone",
  "zone": {
    "inner": { "half_width": 1.0, "half_height": 1.0, "half_depth": 1.0 },
    "outer": { "half_width": 5.0, "half_height": 5.0, "half_depth": 5.0 }
  },
  "max_attenuation_factor": 0.0
}
```

### Array example — `CollectionEntry[]`

```json
"sounds_type": ["Random", "Random", "Default"],
"sounds": [
  { "sound": 100, "gain": { "kind": "Static", "value": 1.0 }, "weight": 0.5 },
  { "sound": 101, "gain": { "kind": "Static", "value": 1.0 }, "weight": 0.5 },
  { "sound": 102, "gain": { "kind": "Static", "value": 1.0 } }
]
```

### Where unions appear in Amplitude project files

| Asset                                       | Discriminator field | Payload field | Variants                                            |
| ------------------------------------------- | ------------------- | ------------- | --------------------------------------------------- |
| [Attenuation](./attenuation-model.md#zone)  | `zone_type`         | `zone`        | `BoxZone` / `CapsuleZone` / `ConeZone` / `SphereZone` |
| [Collection](./collection.md#sounds)        | `sounds_type[]`     | `sounds[]`    | `Default` / `Random` / `Sequence`                   |
| [Collection scheduler](./collection.md#scheduler) | `config_type` | `config`      | `Random` / `Sequence`                                |

[CurveDefinition]: #curve-definition
[CurvePartDefinition]: #curve-part-definition
[CurvePointDefinition]: #curve-point-definition
[RtpcCompatibleValue]: #rtpc-compatible-value
[RtpcParameter]: #rtpc-parameter
