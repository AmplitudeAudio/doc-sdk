---
title: Encoder
description: Audio file writer.
generator: doxide
---


# Encoder

**class  Encoder**


Audio file writer.

The `Encoder` is built by a `Codec` instance. It's used to write
data to an audio file.

The `Write()` methods of an encoder implementation must be thread safe.
        


## Variables

| Name | Description |
| ---- | ----------- |
| [m_format](#m_format) | The audio sample format of the file to write using this encoder. |
| [m_codec](#m_codec) | The codec instance which built this decoder.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Encoder](#Encoder) | Creates a new instance of the encoder for the given codec. |
| [~Encoder](#_u007eEncoder) | Default destructor.  |
| [Open](#Open) | Opens or create a file at the given path to start encoding. |
| [Close](#Close) | Closes a previously opened file. |
| [SetFormat](#SetFormat) | Sets the audio sample format. |
| [Write](#Write) | Writes the given buffer into the file. |

## Variable Details

### m_codec<a name="m_codec"></a>

!!! variable "const Codec&#42; m_codec"

    
    The codec instance which built this decoder.
                 
    
    
    

### m_format<a name="m_format"></a>

!!! variable "SoundFormat m_format"

    
    The audio sample format of the file to write using this encoder.
    
    The sound format must be set before the initialization of this encoder. Otherwise,
    the encoder initialization should fail.
    
    
    !!! note
         The final behavior depend on the specific codec implementation.
                    
    

## Function Details

### Close<a name="Close"></a>
!!! function "virtual bool Close() = 0"

    
    Closes a previously opened file.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the file was closed successfully, `false` otherwise.
                
    

### Encoder<a name="Encoder"></a>
!!! function "explicit Encoder(const Codec&#42; codec)"

    
    Creates a new instance of the encoder for the given codec.
    
    
    :material-location-enter: **Parameter** `codec`
    :    The codec wrapper for the encoder.
                    
    

### Open<a name="Open"></a>
!!! function "virtual bool Open(std::shared_ptr&lt;File&gt; file) = 0"

    
    Opens or create a file at the given path to start encoding.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file to write.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the file was opened successfully, `false` otherwise.
                
    

### SetFormat<a name="SetFormat"></a>
!!! function "virtual void SetFormat(const SoundFormat&amp; format)"

    
    Sets the audio sample format.
    
    
    :material-location-enter: **Parameter** `format`
    :    The audio sample format.
                    
    

### Write<a name="Write"></a>
!!! function "virtual AmUInt64 Write(AudioBuffer&#42; in, AmUInt64 offset, AmUInt64 length) = 0"

    
    Writes the given buffer into the file.
    
    
    :material-location-enter: **Parameter** `in`
    :    The buffer to write into the the file.
        
    :material-location-enter: **Parameter** `offset`
    :    The offset in frames from which write the input buffer.
        
    :material-location-enter: **Parameter** `length`
    :    The length in frames to write from the input buffer.
    
    
    :material-keyboard-return: **Return**
    :    The number of frames written.
                
    

### ~Encoder<a name="_u007eEncoder"></a>
!!! function "virtual ~Encoder() = default"

    
    Default destructor.
                 
    
    
    

