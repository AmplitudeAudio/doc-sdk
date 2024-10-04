---
title: AudioBuffer
description: Represents an audio buffer containing multiple channels.
generator: doxide
---


# AudioBuffer

**class  AudioBuffer**


Represents an audio buffer containing multiple channels.

An `AudioBuffer` is a de-interleaved memory storage used to store and manipulate audio data,
such as audio samples or Ambisonics sound fields, in a flexible and efficient manner. Accessing
a channel data will return an `AudioBufferChannel` object, which is a view to the memory range storing that channel.


:material-eye-outline: **See**
:    AudioBufferChannel


    


## Operators

| Name | Description |
| ---- | ----------- |
| [operator[]](#operator_u005b_u005d) | Gets the `AudioBufferChannel` at the specified index. |
| [operator[]](#operator_u005b_u005d) | Gets the `AudioBufferChannel` at the specified index. |
| [operator=](#operator_u003d) | Copies the audio buffer data from the provided `AudioBuffer`. |
| [operator+=](#operator_u002b_u003d) | Accumulates the audio buffer data from the provided `AudioBuffer`. |
| [operator-=](#operator_u002d_u003d) | Subtracts the audio buffer data from the provided `AudioBuffer`. |
| [operator*=](#operator_u002a_u003d) | Point-wise multiplies the audio buffer data with the provided `AudioBuffer`. |
| [operator*=](#operator_u002a_u003d) | Point-wise multiplies this channel with the provided scalar. |

## Functions

| Name | Description |
| ---- | ----------- |
| [Copy](#Copy) | Copies the given number of frames from the source buffer to the destination buffer. |
| [AudioBuffer](#AudioBuffer) | Creates an empty audio buffer.  |
| [AudioBuffer](#AudioBuffer) | Creates an audio buffer with the specified number of frames and channels. |
| [AudioBuffer](#AudioBuffer) | Explicitly deletes the audio buffer copy to avoid unintended usage. |
| [AudioBuffer](#AudioBuffer) | Moves the given audio buffer data in this one. |
| [~AudioBuffer](#_u007eAudioBuffer) | Destroys the audio buffer data and release allocated memory.  |
| [IsEmpty](#IsEmpty) | Check if the audio buffer is empty. |
| [GetFrameCount](#GetFrameCount) | Gets the number of frames in the buffer. |
| [GetChannelCount](#GetChannelCount) | Gets the number of channels in the buffer. |
| [Clear](#Clear) | Sets the entire audio buffer data to zero.  |
| [GetData](#GetData) | Gets the wrapped audio buffer data. |
| [GetChannel](#GetChannel) | Gets the `AudioBufferChannel` at the specified index. |
| [GetChannel](#GetChannel) | Gets the `AudioBufferChannel` at the specified index. |
| [Clone](#Clone) | Clones the audio buffer and returns a new instance. |

## Operator Details

### operator*=<a name="operator_u002a_u003d"></a>

!!! function "AudioBuffer&amp; operator&#42;=(const AudioBuffer&amp; buffer)"

    
    Point-wise multiplies the audio buffer data with the provided `AudioBuffer`.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The buffer to multiply with this one.
    
    
    :material-keyboard-return: **Return**
    :    This instance with the multiplied audio buffer data.
            
    

!!! function "AudioBuffer&amp; operator&#42;=(AmReal32 scalar)"

    
    Point-wise multiplies this channel with the provided scalar.
    
    
    :material-location-enter: **Parameter** `scalar`
    :    The scalar to multiply with.
    
    
    :material-keyboard-return: **Return**
    :    A reference to the modified channel.
            
    

### operator+=<a name="operator_u002b_u003d"></a>

!!! function "AudioBuffer&amp; operator+=(const AudioBuffer&amp; buffer)"

    
    Accumulates the audio buffer data from the provided `AudioBuffer`.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The buffer to add in this one.
    
    
    :material-keyboard-return: **Return**
    :    This instance with the added audio buffer data.
            
    

### operator-=<a name="operator_u002d_u003d"></a>

!!! function "AudioBuffer&amp; operator-=(const AudioBuffer&amp; buffer)"

    
    Subtracts the audio buffer data from the provided `AudioBuffer`.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The buffer to subtract from this one.
    
    
    :material-keyboard-return: **Return**
    :    This instance with the subtracted audio buffer data.
            
    

### operator=<a name="operator_u003d"></a>

!!! function "AudioBuffer&amp; operator=(const AudioBuffer&amp; buffer)"

    
    Copies the audio buffer data from the provided `AudioBuffer`.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The other audio buffer to copy.
    
    
    :material-keyboard-return: **Return**
    :    This instance with the copied audio buffer data.
            
    

### operator[]<a name="operator_u005b_u005d"></a>

!!! function "AudioBufferChannel&amp; operator[](AmSize index)"

    
    Gets the `AudioBufferChannel` at the specified index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The channel index.
    
    
    :material-keyboard-return: **Return**
    :    The `AudioBufferChannel` at the specified index.
            
    

!!! function "[[nodiscard]] const AudioBufferChannel&amp; operator[](AmSize index) const"

    
    Gets the `AudioBufferChannel` at the specified index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The channel index.
    
    
    :material-keyboard-return: **Return**
    :    The `AudioBufferChannel` at the specified index.
            
    

## Function Details

### AudioBuffer<a name="AudioBuffer"></a>
!!! function "AudioBuffer()"

    
    Creates an empty audio buffer.
             
    
    
    

!!! function "AudioBuffer(AmSize numFrames, AmSize numChannels)"

    
    Creates an audio buffer with the specified number of frames and channels.
    
    
    :material-location-enter: **Parameter** `numFrames`
    :    The number of frames in the buffer.
        
    :material-location-enter: **Parameter** `numChannels`
    :    The number of channels in the buffer.
                
    

!!! function "AudioBuffer(const AudioBuffer&amp; buffer) = delete"

    
    Explicitly deletes the audio buffer copy to avoid unintended usage.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The other audio buffer to copy.
    
    
    !!! note
         Use the assignment operator to copy the audio buffer.
                
    

!!! function "AudioBuffer(AudioBuffer&amp;&amp; buffer) noexcept"

    
    Moves the given audio buffer data in this one.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The other audio buffer to move.
                
    

### Clear<a name="Clear"></a>
!!! function "void Clear()"

    
    Sets the entire audio buffer data to zero.
             
    
    
    

### Clone<a name="Clone"></a>
!!! function "AudioBuffer Clone() const"

    
    Clones the audio buffer and returns a new instance.
    
    
    :material-keyboard-return: **Return**
    :    A new instance with a cloned copy of the audio buffer data.
            
    

### Copy<a name="Copy"></a>
!!! function "static void Copy( const AudioBuffer&amp; source, AmSize sourceOffset, AudioBuffer&amp; destination, AmSize destinationOffset, AmSize numFrames)"

    
    Copies the given number of frames from the source buffer to the destination buffer.
    
    
    :material-location-enter: **Parameter** `source`
    :    The source buffer to copy.
        
    :material-location-enter: **Parameter** `sourceOffset`
    :    The offset in the source buffer.
        
    :material-location-exit: **Parameter** `destination`
    :    The destination buffer to copy to.
        
    :material-location-enter: **Parameter** `destinationOffset`
    :    The offset in the destination buffer.
        
    :material-location-enter: **Parameter** `numFrames`
    :    The number of frames to copy.
                
    

### GetChannel<a name="GetChannel"></a>
!!! function "AudioBufferChannel&amp; GetChannel(AmSize index)"

    
    Gets the `AudioBufferChannel` at the specified index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The channel index.
    
    
    :material-keyboard-return: **Return**
    :    The `AudioBufferChannel` at the specified index.
            
    

!!! function "[[nodiscard]] const AudioBufferChannel&amp; GetChannel(AmSize index) const"

    
    Gets the `AudioBufferChannel` at the specified index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The channel index.
    
    
    :material-keyboard-return: **Return**
    :    The `AudioBufferChannel` at the specified index.
            
    

### GetChannelCount<a name="GetChannelCount"></a>
!!! function "[[nodiscard]] AmSize GetChannelCount() const"

    
    Gets the number of channels in the buffer.
    
    
    :material-keyboard-return: **Return**
    :    The number of channels in the buffer.
            
    

### GetData<a name="GetData"></a>
!!! function "[[nodiscard]] const AmAlignedReal32Buffer&amp; GetData() const"

    
    Gets the wrapped audio buffer data.
    
    
    :material-keyboard-return: **Return**
    :    The wrapped audio buffer data.
            
    

### GetFrameCount<a name="GetFrameCount"></a>
!!! function "[[nodiscard]] AmSize GetFrameCount() const"

    
    Gets the number of frames in the buffer.
    
    
    :material-keyboard-return: **Return**
    :    The number of frames in the buffer.
            
    

### IsEmpty<a name="IsEmpty"></a>
!!! function "[[nodiscard]] bool IsEmpty() const"

    
    Check if the audio buffer is empty.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the audio buffer is empty, `false` otherwise.
            
    

### ~AudioBuffer<a name="_u007eAudioBuffer"></a>
!!! function "~AudioBuffer()"

    
    Destroys the audio buffer data and release allocated memory.
             
    
    
    

