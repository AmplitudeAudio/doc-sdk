---
title: Project Architecture
description: An Amplitude project is just a set of organized JSON files, each of them with a specific schema. This page will break down the Amplitude project architecture.
---

An Amplitude project is resumed to a set of `.json` files organized in dedicated directories. The complete architecture of an Amplitude project can be described by this hierarchy:

```text
📁 amplitude_project_name/
├ 📁 attenuators/
├ 📁 collections/
├ 📁 effects/
├ 📁 events/
├ 📁 pipelines/
├ 📁 rtpc/
├ 📁 soundbanks/
├ 📁 sounds/
├ 📁 switch_containers/
├ 📁 switches/
├ 📄 pc.config.json
├ 📄 android.config.json
├ 📄 buses.json
└ 📄 .amproject
```

## Engine configuration files

The Amplitude engine settings are provided through a JSON file at the root of the project. In our previous example, we had two engine configuration files according to the runtime platform: `pc.config.json` and `android.config.json`. The config file to use should be given when initializing Amplitude.

The config files store all the needed settings for the audio device setup, memory allocation, and mixer configuration. Learn more on how to configure the engine in the [Engine Configuration](./engine-config.md) page.

!!! info
    At least one engine configuration file should exist in an Amplitude project directory, and should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/engine_config_definition.fbs).

## Buses file

An Amplitude project should have a file (or files) where the different buses used at runtime are defined. In our previous example, the `buses.json` file plays this role.

You can only use one bus file per engine configuration, by setting his path in that engine configuration file. Learn more on how to configure buses in the [Buses Configuration](./buses-config.md) page.

!!! info
    At least one buses file is expected in an Amplitude project. If no file is specified in the engine settings, the default expected path is `./buses.json`. If the buses file is not found during the engine initialization, the library will throw an exception.

## attenuators/

The `attenuators` directory stores all the configuration files for custom [Attenuation] models. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/attenuation_definition.fbs). Learn more about attenuators in the [Attenuations](./attenuation-model.md) page.

## collections/

The `collections` directory contains the configuration files for [Collection] sound objects. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/collection_definition.fbs). Learn more about collections in the [Collections](./collection.md) page.

## effects/

The `effects` directory contains the configuration files for sound [Effect]s. Each `.json` file should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/effect_definition.fbs). Learn more about effects in the [Effects](./effect.md) page.

## events/

The `events` directory contains the configuration files for [Event]s. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/event_definition.fbs). Learn more about events in the [Events](./event.md) page.

## pipelines/

The `pipelines` directory contains the configuration files for each Amplimix Pipeline you want to use with the engine. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/pipeline_definition.fbs). Learn more about pipelines in the [Pipelines](./pipeline.md) page.

## rtpc/

The `rtpc` directory stores the configuration files to create [RTPC] values. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/rtpc_definition.fbs). Learn more about RTPC values in the [Real-Time Parameter Control](./rtpc.md) page.

## soundbanks/

The `soundbanks` directory is the place where you define all of your game [SoundBank]s. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/sound_bank_definition.fbs). Learn more about sound banks in the [Sound Banks](./sound-bank.md) page.

## sounds/

The `sounds` directory contains the definition files for [Sound] objects. Those files are used to describe raw audio sample assets to make them usable as standalone objects or in Collections and Switch Containers. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/sound_definition.fbs). Learn more on how to create sounds in the [Sounds](./sound.md) page.

## switch_containers/

The `switch_containers` directory contains configuration files for [SwitchContainer] sound objects. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/switch_container_definition.fbs). Learn more about switches and switch containers in the [Switch Container](./switch-container.md) guide.

## switches/

The `switches` directory contains configuration files for [Switch] objects, that will be used in [SwitchContainer]s. Each `.json` file of this directory should match this [flatbuffers schema](https://github.com/AmplitudeAudio/sdk/blob/main/schemas/switch_definition.fbs). Learn more about switches and switch containers in the [Switch State](./switch.md) guide.

[Attenuation]: ../api/assets/Attenuation.md
[Collection]: ../api/assets/Collection.md
[Effect]: ../api/assets/Effect.md
[Event]: ../api/assets/Event.md
[RTPC]: ../api/assets/Rtpc.md
[Sound]: ../api/assets/Sound.md
[SwitchContainer]: ../api/assets/SwitchContainer.md
[Switch]: ../api/assets/Switch.md
