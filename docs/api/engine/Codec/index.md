---
title: Codec
description: Audio file reader and writer.
generator: doxide
---


# Codec

**class  Codec**


Audio file reader and writer.

The `Codec` class is used to implement an audio file reader and writer.
This is the base class for all audio codecs, each implementation should
allow to build decoders and encoders.


    


## Types

| Name | Description |
| ---- | ----------- |
| [Decoder](Decoder/index.md) | Audio file reader. |
| [Encoder](Encoder/index.md) | Audio file writer. |

## Variables

| Name | Description |
| ---- | ----------- |
| [m_name](#m_name) | The name of this codec.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [Codec](#Codec) | Create a new Codec instance. |
| [~Codec](#_u007eCodec) | Default destructor.  |
| [CreateDecoder](#CreateDecoder) | Creates a new instance of the decoder associated to this codec. |
| [DestroyDecoder](#DestroyDecoder) | Destroys the decoder associated to this codec. |
| [CreateEncoder](#CreateEncoder) | Creates a new instance of the encoder associated to this codec. |
| [DestroyEncoder](#DestroyEncoder) | Destroys the encoder associated to this codec. |
| [CanHandleFile](#CanHandleFile) | Checks whether this `Codec` can handle the file at the given path. |
| [GetName](#GetName) | Gets the name of this codec. |
| [Register](#Register) | Registers a new audio codec. |
| [Unregister](#Unregister) | Unregisters a audio codec. |
| [Find](#Find) | Look up a codec by name. |
| [FindCodecForFile](#FindCodecForFile) | Finds the codec which can handle the given file. |
| [LockRegistry](#LockRegistry) | Locks the codecs registry. |
| [UnlockRegistry](#UnlockRegistry) | Unlocks the codecs registry. |

## Variable Details

### m_name<a name="m_name"></a>

!!! variable "AmString m_name"

    
    The name of this codec.
             
    
    
    

## Function Details

### CanHandleFile<a name="CanHandleFile"></a>
!!! function "[[nodiscard]] virtual bool CanHandleFile(std::shared_ptr&lt;File&gt; file) const = 0"

    
    Checks whether this `Codec` can handle the file at the given path.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file to check.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the `Codec` can handle the file, `false` otherwise.
            
    

### Codec<a name="Codec"></a>
!!! function "explicit Codec(AmString name)"

    
    Create a new Codec instance.
    
    
    :material-location-enter: **Parameter** `name`
    :    The codec name. Recommended names are "FILE_EXTENSION".
        eg. "WAV" or "OGG".
                
    

### CreateDecoder<a name="CreateDecoder"></a>
!!! function "&#42; CreateDecoder()"

    
    Creates a new instance of the decoder associated to this codec.
    
    
    :material-keyboard-return: **Return**
    :    A `Decoder` instance.
            
    

### CreateEncoder<a name="CreateEncoder"></a>
!!! function "&#42; CreateEncoder()"

    
    Creates a new instance of the encoder associated to this codec.
    
    
    :material-keyboard-return: **Return**
    :    An `Encoder` instance.
            
    

### DestroyDecoder<a name="DestroyDecoder"></a>
!!! function "virtual void DestroyDecoder(Decoder&#42; decoder) = 0"

    
    Destroys the decoder associated to this codec.
    
    
    :material-location-enter: **Parameter** `decoder`
    :    The decoder instance to destroy.
                
    

### DestroyEncoder<a name="DestroyEncoder"></a>
!!! function "virtual void DestroyEncoder(Encoder&#42; encoder) = 0"

    
    Destroys the encoder associated to this codec.
    
    
    :material-location-enter: **Parameter** `encoder`
    :    The encoder instance to destroy.
                
    

### Find<a name="Find"></a>
!!! function "static Codec&#42; Find(const AmString&amp; name)"

    
    Look up a codec by name.
    
    
    :material-location-enter: **Parameter** `name`
    :    The name of the codec to find.
    
    
    :material-keyboard-return: **Return**
    :    The codec with the given name, or `nullptr` if none.
            
    

### FindCodecForFile<a name="FindCodecForFile"></a>
!!! function "static Codec&#42; FindCodecForFile(std::shared_ptr&lt;File&gt; file)"

    
    Finds the codec which can handle the given file.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file to find the codec for.
    
    
    :material-keyboard-return: **Return**
    :    The codec which can handle the given file, or `nullptr` if none.
            
    

### GetName<a name="GetName"></a>
!!! function "[[nodiscard]] const AmString&amp; GetName() const"

    
    Gets the name of this codec.
    
    
    :material-keyboard-return: **Return**
    :    The name of this codec.
            
    

### LockRegistry<a name="LockRegistry"></a>
!!! function "static void LockRegistry()"

    
    Locks the codecs registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called before the `Engine` initialization, to discard the registration
        of new codecs after the engine is fully loaded.
                
    

### Register<a name="Register"></a>
!!! function "static void Register(Codec&#42; codec)"

    
    Registers a new audio codec.
    
    
    :material-location-enter: **Parameter** `codec`
    :    The audio codec to add in the registry.
                
    

### UnlockRegistry<a name="UnlockRegistry"></a>
!!! function "static void UnlockRegistry()"

    
    Unlocks the codecs registry.
    
    
    !!! warning
         This function is mainly used for internal purposes. It's
        called after the `Engine` deinitialization, to allow the registration
        of new codecs after the engine is fully unloaded.
                
    

### Unregister<a name="Unregister"></a>
!!! function "static void Unregister(const Codec&#42; codec)"

    
    Unregisters a audio codec.
    
    
    :material-location-enter: **Parameter** `codec`
    :    The audio codec to remove from the registry.
                
    

### ~Codec<a name="_u007eCodec"></a>
!!! function "virtual ~Codec()"

    
    Default destructor.
             
    
    
    

