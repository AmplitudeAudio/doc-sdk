---
title: AudioBufferChannel
description: Represents a view to a single channel in an `AudioBuffer`.
generator: doxide
---


# AudioBufferChannel

**class  AudioBufferChannel**


Represents a view to a single channel in an `AudioBuffer`.


:material-eye-outline: **See**
:    AudioBuffer


    


## Operators

| Name | Description |
| ---- | ----------- |
| [operator[]](#operator_u005b_u005d) | Gets the audio sample at the specified index. |
| [operator[]](#operator_u005b_u005d) | Gets the audio sample at the specified index. |
| [operator=](#operator_u003d) | Sets the entire channel data from the provided vector. |
| [operator=](#operator_u003d) | Sets the entire channel data from the provided `AudioBufferChannel`. |
| [operator+=](#operator_u002b_u003d) | Performs point-wise addition of this channel with the provided `AudioBufferChannel`. |
| [operator-=](#operator_u002d_u003d) | Performs point-wise subtraction of this channel with the provided `AudioBufferChannel`. |
| [operator*=](#operator_u002a_u003d) | Point-wise multiplies this channel with the provided `AudioBufferChannel`. |
| [operator*=](#operator_u002a_u003d) | Point-wise multiplies this channel with the provided scalar. |

## Functions

| Name | Description |
| ---- | ----------- |
| [size](#size) | Gets the size of the buffer. |
| [begin](#begin) | Returns a float pointer to the begin of the channel data. |
| [begin](#begin) | Returns a const float pointer to the begin of the channel data. |
| [end](#end) | Returns a float pointer to the end of the channel data. |
| [end](#end) | Returns a const float pointer to the end of the channel data. |
| [clear](#clear) | Clears the channel data with zero.  |
| [enabled](#enabled) | Checks if the channel is enabled. |

## Operator Details

### operator*=<a name="operator_u002a_u003d"></a>

!!! function "AudioBufferChannel&amp; operator&#42;=(const AudioBufferChannel&amp; channel)"

    
    Point-wise multiplies this channel with the provided `AudioBufferChannel`.
    
    
    :material-location-enter: **Parameter** `channel`
    :    The `AudioBufferChannel` to multiply with.
    
    
    :material-keyboard-return: **Return**
    :    A reference to the modified channel.
            
    

!!! function "AudioBufferChannel&amp; operator&#42;=(AmReal32 scalar)"

    
    Point-wise multiplies this channel with the provided scalar.
    
    
    :material-location-enter: **Parameter** `scalar`
    :    The scalar to multiply with.
    
    
    :material-keyboard-return: **Return**
    :    A reference to the modified channel.
            
    

### operator+=<a name="operator_u002b_u003d"></a>

!!! function "AudioBufferChannel&amp; operator+=(const AudioBufferChannel&amp; channel)"

    
    Performs point-wise addition of this channel with the provided `AudioBufferChannel`.
    
    
    :material-location-enter: **Parameter** `channel`
    :    The `AudioBufferChannel` to add.
    
    
    :material-keyboard-return: **Return**
    :    A reference to the modified channel.
            
    

### operator-=<a name="operator_u002d_u003d"></a>

!!! function "AudioBufferChannel&amp; operator-=(const AudioBufferChannel&amp; channel)"

    
    Performs point-wise subtraction of this channel with the provided `AudioBufferChannel`.
    
    
    :material-location-enter: **Parameter** `channel`
    :    The `AudioBufferChannel` to subtract.
    
    
    :material-keyboard-return: **Return**
    :    A reference to the modified channel.
            
    

### operator=<a name="operator_u003d"></a>

!!! function "AudioBufferChannel&amp; operator=(const std::vector&lt;AmReal32&gt;&amp; data)"

    
    Sets the entire channel data from the provided vector.
    
    
    :material-location-enter: **Parameter** `data`
    :    The vector containing the new channel data.
    
    
    :material-keyboard-return: **Return**
    :    A reference to the modified channel.
            
    

!!! function "AudioBufferChannel&amp; operator=(const AudioBufferChannel&amp; channel)"

    
    Sets the entire channel data from the provided `AudioBufferChannel`.
    
    
    :material-location-enter: **Parameter** `channel`
    :    The `AudioBufferChannel` to copy the data from.
    
    
    :material-keyboard-return: **Return**
    :    A reference to the modified channel.
            
    

### operator[]<a name="operator_u005b_u005d"></a>

!!! function "AmReal32&amp; operator[](AmSize index)"

    
    Gets the audio sample at the specified index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The audio sample index.
    
    
    :material-keyboard-return: **Return**
    :    The audio sample at the specified index.
            
    

!!! function "[[nodiscard]] const AmReal32&amp; operator[](AmSize index) const"

    
    Gets the audio sample at the specified index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The audio sample index.
    
    
    :material-keyboard-return: **Return**
    :    The audio sample at the specified index.
            
    

## Function Details

### begin<a name="begin"></a>
!!! function "AmReal32&#42; begin()"

    
    Returns a float pointer to the begin of the channel data.
    
    
    :material-keyboard-return: **Return**
    :    A float pointer to the begin of the channel data.
            
    

!!! function "[[nodiscard]] const AmReal32&#42; begin() const"

    
    Returns a const float pointer to the begin of the channel data.
    
    
    :material-keyboard-return: **Return**
    :    A const float pointer to the begin of the channel data.
            
    

### clear<a name="clear"></a>
!!! function "void clear()"

    
    Clears the channel data with zero.
             
    
    
    

### enabled<a name="enabled"></a>
!!! function "[[nodiscard]] bool enabled() const"

    
    Checks if the channel is enabled.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the channel is enabled, `false` otherwise.
            
    

### end<a name="end"></a>
!!! function "AmReal32&#42; end()"

    
    Returns a float pointer to the end of the channel data.
    
    
    :material-keyboard-return: **Return**
    :    A float pointer to the end of the channel data.
            
    

!!! function "[[nodiscard]] const AmReal32&#42; end() const"

    
    Returns a const float pointer to the end of the channel data.
    
    
    :material-keyboard-return: **Return**
    :    A const float pointer to the end of the channel data.
            
    

### size<a name="size"></a>
!!! function "[[nodiscard]] AmSize size() const"

    
    Gets the size of the buffer.
    
    
    :material-keyboard-return: **Return**
    :    The size of the buffer.
            
    

