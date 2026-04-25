---
title: CLI Tools
description: Reference for the Amplitude Audio SDK command-line tools.
---

The Amplitude Audio SDK ships with three command-line tools for asset processing and pipeline management. This reference documents their usage, options, and exit codes.

## Overview

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `amac` | Amplitude Audio Compressor | WAV, MP3 | AMS (ADPCM) or WAV |
| `amir` | Amplitude HRIR Sphere Builder | IRCAM, MIT, SADIE, SOFA | `.amir` file |
| `ampk` | Amplitude Packager | Project directory | `.ampk` package |

All tools follow a consistent CLI style and support `--verbose`, `--no-logo`, and `--version` flags.

---

## amac {#amac}

Amplitude Audio Compressor

`amac` encodes standard audio files into Amplitude's custom AMS ADPCM format, or decodes AMS files back to WAV.

### Usage

```bash
amac [OPTIONS] <input_file> <output_file>
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `-e, --encode` | — | Encode mode: convert input to AMS. |
| `-d, --decode` | — | Decode mode: convert AMS to WAV. |
| `-l, --no-logo` | `false` | Hide the logo and copyright notice. |
| `-v, --verbose` | `false` | Print detailed processing information. |
| `--look-ahead N` | `3` | Look-ahead buffer size for encoding (higher = better quality, slower). |
| `--no-noise-shaping` | `false` | Disable noise shaping during encoding. |
| `--block-size-shift N` | `0` | ADPCM block size shift value. |
| `--resample` | `false` | Resample to a target sample rate. |
| `--target-sample-rate N` | `44100` | Target sample rate when resampling. |

### Examples

```bash
# Encode a WAV to AMS
amac -e input.wav output.ams

# Encode with noise shaping disabled and custom look-ahead
amac -e --no-noise-shaping --look-ahead 5 input.wav output.ams

# Decode AMS back to WAV
amac -d input.ams output.wav

# Encode and resample to 48kHz
amac -e --resample --target-sample-rate 48000 input.wav output.ams
```

### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | Invalid arguments or file not found |
| `2` | Encoding/decoding error |

---

## amir {#amir}

Amplitude HRIR Sphere Builder

`amir` converts HRIR (Head-Related Impulse Response) datasets into Amplitude's optimized `.amir` sphere format for runtime HRTF spatialization.

### Supported Datasets

| Dataset | Flag | Source |
|---------|------|--------|
| IRCAM | `--dataset-model IRCAM` | [IRCAM LISTEN](http://recherche.ircam.fr/equipes/salles/listen/download.html) |
| MIT KEMAR | `--dataset-model MIT` | [MIT Media Lab](http://sound.media.mit.edu/resources/KEMAR.html) |
| SADIE II | `--dataset-model SADIE` | [University of York](https://www.york.ac.uk/sadie-project/database.html) |
| SOFA | `--dataset-model SOFA` | [SOFA Conventions](https://www.sofaconventions.org/) |

### Usage

```bash
amir [OPTIONS] <input_file> <output_file>
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `-m, --dataset-model MODEL` | `IRCAM` | Source dataset model. |
| `-l, --no-logo` | `false` | Hide the logo and copyright notice. |
| `-v, --verbose` | `false` | Print detailed processing information. |
| `--debug` | `false` | Output a 3D visualization mesh of the HRIR sphere in OBJ format. |
| `--resample` | `false` | Resample IR data to a target sample rate. |
| `--target-sample-rate N` | `44100` | Target sample rate when resampling. |

### Examples

```bash
# Convert a SOFA file to AMIR
amir --dataset-model SOFA hrtf.sofa hrtf.amir

# Convert MIT data with resampling to 48kHz
amir --dataset-model MIT --resample --target-sample-rate 48000 mit_data.wav output.amir

# Generate with debug mesh
amir --dataset-model IRCAM --debug ircam_data.wav output.amir
# Produces output.amir + output.obj (visualization mesh)
```

### Output Format

The `.amir` file contains:

- Triangulated sphere mesh (vertices + faces)
- Left and right ear HRIR data per vertex
- Interaural time difference (ITD) delays
- Sample rate and IR length metadata

### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | Invalid arguments or file not found |
| `2` | Processing error (invalid dataset format) |

---

## ampk {#ampk}

Amplitude Packager

`ampk` packs an entire Amplitude project directory into a single `.ampk` file for efficient distribution and loading at runtime.

### Usage

```bash
ampk [OPTIONS] <project_dir> <output_file>
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `-c, --compression MODE` | `0` | Compression mode: `0` = uncompressed, `1` = LZ4. |
| `-b, --block-size N` | `64` | Compression block size in KB (only for LZ4). |
| `-l, --no-logo` | `false` | Hide the logo and copyright notice. |
| `-v, --verbose` | `false` | Print detailed packaging information. |

### Examples

```bash
# Create an uncompressed package
ampk ./my_project/ output.ampk

# Create an LZ4-compressed package with 128KB blocks
ampk -c 1 -b 128 ./my_project/ output.ampk

# Package verbosely
ampk -v ./my_project/ output.ampk
```

### Compression Modes

| Mode | Value | Description | Use Case |
|------|-------|-------------|----------|
| Uncompressed | `0` | No compression; fastest load times | Desktop, SSD storage |
| LZ4 | `1` | Fast compression and decompression | Mobile, console, streaming |

LZ4 compression reduces file size with minimal CPU overhead during decompression. The block size controls the compression granularity; larger blocks yield better compression but use more memory during loading.

### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | Invalid arguments or directory not found |
| `2` | Packaging or I/O error |

---

## Common Options

All three tools support these global flags:

| Flag | Description |
|------|-------------|
| `--version` | Print the tool version and exit. |
| `--help` | Print usage information and exit. |

## Building the Tools

The tools are built automatically when `build_tools` is enabled in the XMake configuration:

```bash
xmake config --build_tools=y
xmake
```

Binaries are placed in the `build/[platform]/[arch]/[mode]/` directory.

## Next Steps

- Learn how to [set up HRTF](../integration/hrtf-setup.md) using `amir`.
- Learn how to [compile Amplitude projects](../integration/compiling-amplitude-project.md).
- Explore the [PackageFileSystem API](../api/io/PackageFileSystem.md) for runtime package loading.
