---
title: CLI Tools
description: Reference for the Amplitude Audio SDK command-line tools.
diataxis: reference

---

The Amplitude Audio SDK ships with three command-line tools for asset processing and pipeline management. This reference documents their usage, options, and exit codes.

## Overview

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `amac` | Amplitude Audio Compressor | WAV, MP3 | AMS (ADPCM) or WAV |
| `amir` | Amplitude HRIR Sphere Builder | IRCAM, MIT, SADIE, SOFA | `.amir` file |
| `ampk` | Amplitude Packager | Project directory | `.ampk` package |

All tools follow a consistent CLI style and support `--verbose`, `--quiet`, `--no-logo`, and `--version` flags.

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
| `-q, --quiet` | `false` | Quiet mode: suppress all output (implies `--no-logo` and disables verbose). |
| `-0` … `-8` | `-3` | Look-ahead level for encoding (0 = fastest/lowest quality, 8 = slowest/highest quality). Default is level 3. Encode-only. |
| `-f` | — | Disable noise shaping during encoding. Encode-only. |
| `-b, --block-size-shift N` | `0` | ADPCM block size exponent. Must be in the range `[8, 15]`; when `0`, the block size is computed automatically from channel count and sample rate. Encode-only. |
| `-r, --resample FREQ` | — | Resample input data to `FREQ` Hz before encoding. Accepted range: `[8000, 384000]`. Encode-only. |

### Examples

```bash
# Encode a WAV to AMS (default look-ahead level 3)
amac -e input.wav output.ams

# Encode with noise shaping disabled and look-ahead level 5
amac -e -f -5 input.wav output.ams

# Encode with a custom block-size-shift
amac -e -b 12 input.wav output.ams

# Decode AMS back to WAV
amac -d input.ams output.wav

# Encode and resample to 48 kHz
amac -e -r 48000 input.wav output.ams
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

| Dataset | Model value (`-m`) | Source |
|---------|-------------------|--------|
| IRCAM | `0` | [IRCAM LISTEN](http://recherche.ircam.fr/equipes/salles/listen/download.html) |
| MIT KEMAR | `1` | [MIT Media Lab](http://sound.media.mit.edu/resources/KEMAR.html) |
| SADIE II | `2` | [University of York](https://www.york.ac.uk/sadie-project/database.html) |
| SOFA | `3` | [SOFA Conventions](https://www.sofaconventions.org/) |

### Usage

```bash
amir [OPTIONS] DATASET_DIR OUTPUT_FILE
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `-m, --model {0,1,2,3}` | — | **(Required)** Source dataset model: `0` = IRCAM, `1` = MIT KEMAR, `2` = SADIE II, `3` = SOFA. |
| `-l, --no-logo` | `false` | Hide the logo and copyright notice. |
| `-v, --verbose` | `false` | Print detailed processing information. |
| `-q, --quiet` | `false` | Quiet mode: suppress all output (implies `--no-logo` and disables verbose). |
| `-d, --debug` | `false` | Output a 3D visualization mesh of the HRIR sphere as `debug_hrir_sphere.obj`. |
| `-r, --resample FREQ` | — | Resample IR data to `FREQ` Hz before writing the `.amir` file. |

### Examples

```bash
# Convert a SOFA file to AMIR (model 3 = SOFA)
amir -m 3 hrtf.sofa hrtf.amir

# Convert MIT KEMAR data with resampling to 48 kHz (model 1 = MIT)
amir -m 1 -r 48000 /path/to/mit_kemar/ output.amir

# Convert IRCAM data and emit a debug visualization mesh (model 0 = IRCAM)
amir -m 0 --debug /path/to/ircam/ output.amir
# Produces output.amir + debug_hrir_sphere.obj (visualization mesh)
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
| `-c, --compression {0,1}` | `0` | Compression mode: `0` = uncompressed, `1` = LZ4. |
| `-s, --block-size N` | `64` | Compression block size in KB. Only used when LZ4 compression is active. |
| `-l, --no-logo` | `false` | Hide the logo and copyright notice. |
| `-v, --verbose` | `false` | Print detailed packaging information. |
| `-q, --quiet` | `false` | Quiet mode: suppress all output (implies `--no-logo` and disables verbose). |

### Examples

```bash
# Create an uncompressed package
ampk ./my_project/ output.ampk

# Create an LZ4-compressed package with 128KB blocks
ampk -c 1 -s 128 ./my_project/ output.ampk

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
- Explore the [PackageFileSystem API](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_package_file_system.md) for runtime package loading.
