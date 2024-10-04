---
title: Decoder
description: Audio file reader.
generator: doxide
---


# Decoder

**class  Decoder**


Audio file reader.

The `Decoder` is built by a `Codec` instance. It's used to read
an audio file and process its data. Each implementation should
allow to [load](#Load) the entire file into memory or [stream](#Stream)
it from the file system.

The `Stream()` method of a decoder implementation must be thread-safe.
        


## Variables

| Name | Description |
| ---- | ----------- |
| [m_format](#m_format) | The audio sample format of the file currently loaded by this decoder. |
| [m_codec](#m_codec) | The codec instance which built this decoder.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Decoder](#Decoder) | Creates a new instance of the decoder for the given codec. |
| [~Decoder](#_u007eDecoder) | Default destructor.  |
| [Open](#Open) | Opens the given file to start decoding. |
| [Close](#Close) | Closes the previously opened file. |
| [GetFormat](#GetFormat) | Gets the audio sample format. |
| [Load](#Load) | Loads the entire audio file into the output buffer. |
| [Stream](#Stream) | Streams a part of the file from disk into the output buffer. |
| [Seek](#Seek) | Moves the cursor to the given frame. |

## Variable Details

### m_codec<a name="m_codec"></a>

!!! variable "const Codec&#42; m_codec"

    
    The codec instance which built this decoder.
                 
    
    
    

### m_format<a name="m_format"></a>

!!! variable "SoundFormat m_format"

    
    The audio sample format of the file currently loaded by this decoder.
    
    The sound format must be filled during the initialization
    of this decoder.
                
    

## Function Details

### Close<a name="Close"></a>
!!! function "virtual bool Close() = 0"

    
    Closes the previously opened file.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the file was closed successfully, `false` otherwise.
                
    

### Decoder<a name="Decoder"></a>
!!! function "explicit Decoder(const Codec&#42; codec)"

    
    Creates a new instance of the decoder for the given codec.
    
    
    :material-location-enter: **Parameter** `codec`
    :    The codec wrapper for the decoder.
                    
    

### GetFormat<a name="GetFormat"></a>
!!! function "[[nodiscard]] const SoundFormat&amp; GetFormat() const"

    
    Gets the audio sample format.
    
    
    :material-keyboard-return: **Return**
    :    The audio sample format.
    
    
    :material-eye-outline: **See**
    :    SoundFormat
                
    

### Load<a name="Load"></a>
!!! function "virtual AmUInt64 Load(AudioBuffer&#42; out) = 0"

    
    Loads the entire audio file into the output buffer.
    
    The output buffer must allocate enough size for this operation
    to be successful.
    
    
    :material-location-exit: **Parameter** `out`
    :    The buffer to load audio data data into.
    
    
    :material-keyboard-return: **Return**
    :    The number of audio frames loaded into the buffer.
                
    

### Open<a name="Open"></a>
!!! function "virtual bool Open(std::shared_ptr&lt;File&gt; file) = 0"

    
    Opens the given file to start decoding.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file to read.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the file was opened successfully, `false` otherwise.
                
    

### Seek<a name="Seek"></a>
!!! function "virtual bool Seek(AmUInt64 offset) = 0"

    
    Moves the cursor to the given frame.
    
    
    :material-location-enter: **Parameter** `offset`
    :    The offset in frames to move the cursor to.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the cursor was moved successfully, `false` otherwise.
                
    

### Stream<a name="Stream"></a>
!!! function "virtual AmUInt64 Stream(AudioBuffer&#42; out, AmUInt64 bufferOffset, AmUInt64 seekOffset, AmUInt64 length) = 0"

    
    Streams a part of the file from disk into the output buffer.
    
    
    :material-location-exit: **Parameter** `out`
    :    The buffer to stream the file data into.
        
    :material-location-enter: **Parameter** `bufferOffset`
    :    The offset in frames from which start to write in the `out` buffer.
        
    :material-location-enter: **Parameter** `seekOffset`
    :    The offset in frames from which start to read the file.
        
    :material-location-enter: **Parameter** `length`
    :    The length in frames to read from the file.
    
    
    :material-keyboard-return: **Return**
    :    The number of frames read.
                
    

### ~Decoder<a name="_u007eDecoder"></a>
!!! function "virtual ~Decoder() = default"

    
    Default destructor.
                 
    
    
    

