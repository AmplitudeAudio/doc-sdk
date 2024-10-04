---
title: SplitComplex
description: Buffer for split-complex representation of FFT results.
generator: doxide
---


# SplitComplex

**class  SplitComplex**


Buffer for split-complex representation of FFT results.

The split-complex representation stores the real and imaginary parts
of FFT results in two different memory buffers which is useful e.g. for
SIMD optimizations.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [SplitComplex](#SplitComplex) | Creates a new split-complex buffer with the given initial size. |
| [~SplitComplex](#_u007eSplitComplex) | Destroy the split-complex buffer and release all allocated memory.  |
| [Release](#Release) | Releases all allocated memory.  |
| [Resize](#Resize) | Resizes the split-complex buffer to the given size. |
| [Clear](#Clear) | Clears the split-complex buffer.  |
| [CopyFrom](#CopyFrom) | Copies the given split-complex buffer to this one. |
| [GetSize](#GetSize) | Gets the current size of the split-complex buffer. |
| [re](#re) | Gets the real part of the split-complex buffer. |
| [re](#re) | Gets the real part of the split-complex buffer. |
| [im](#im) | Gets the imaginary part of the split-complex buffer. |
| [im](#im) | Gets the imaginary part of the split-complex buffer. |

## Function Details

### Clear<a name="Clear"></a>
!!! function "void Clear() const"

    
    Clears the split-complex buffer.
             
    
    
    

### CopyFrom<a name="CopyFrom"></a>
!!! function "void CopyFrom(const SplitComplex&amp; other) const"

    
    Copies the given split-complex buffer to this one.
    
    
    :material-location-enter: **Parameter** `other`
    :    The split-complex buffer to copy.
                
    

### GetSize<a name="GetSize"></a>
!!! function "[[nodiscard]] inline AmSize GetSize() const"

    
    Gets the current size of the split-complex buffer.
    
    
    :material-keyboard-return: **Return**
    :    The size of the split-complex buffer.
            
    

### Release<a name="Release"></a>
!!! function "void Release()"

    
    Releases all allocated memory.
             
    
    
    

### Resize<a name="Resize"></a>
!!! function "void Resize(AmSize newSize, bool clear = false)"

    
    Resizes the split-complex buffer to the given size.
    
    
    :material-location-enter: **Parameter** `newSize`
    :    The new size of the split-complex buffer.
        
    :material-location-enter: **Parameter** `clear`
    :   
        
    :material-location-enter: **Parameter** `clear`
    :   
                
    

### SplitComplex<a name="SplitComplex"></a>
!!! function "explicit SplitComplex(AmSize initialSize = 0)"

    
    Creates a new split-complex buffer with the given initial size.
    
    
    :material-location-enter: **Parameter** `initialSize`
    :    The initial size of the split-complex buffer.
                
    

### im<a name="im"></a>
!!! function "AmAudioSample&#42; im()"

    
    Gets the imaginary part of the split-complex buffer.
    
    
    :material-keyboard-return: **Return**
    :    The imaginary part of the split-complex buffer.
            
    

!!! function "[[nodiscard]] const AmAudioSample&#42; im() const"

    
    Gets the imaginary part of the split-complex buffer.
    
    
    :material-keyboard-return: **Return**
    :    The imaginary part of the split-complex buffer.
            
    

### re<a name="re"></a>
!!! function "AmAudioSample&#42; re()"

    
    Gets the real part of the split-complex buffer.
    
    
    :material-keyboard-return: **Return**
    :    The real part of the split-complex buffer.
            
    

!!! function "[[nodiscard]] const AmAudioSample&#42; re() const"

    
    Gets the real part of the split-complex buffer.
    
    
    :material-keyboard-return: **Return**
    :    The real part of the split-complex buffer.
            
    

### ~SplitComplex<a name="_u007eSplitComplex"></a>
!!! function "~SplitComplex()"

    
    Destroy the split-complex buffer and release all allocated memory.
             
    
    
    

