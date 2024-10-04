---
title: FFT
description: The Fast Fourier Transform (FFT) class.
generator: doxide
---


# FFT

**class  FFT**


The Fast Fourier Transform (FFT) class.

This utility class is used to perform Fast Fourier Transform (FFT) operations
on audio data with real-to-complex/complex-to-real routines. The algorithm is
highly optimized for speed, and the class provides and high-level API for the
user.

The output of the operation is ready-to-use, that means all the post processing
operations (scale, normalization, etc.) have been applied.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [GetOutputSize](#GetOutputSize) | Gets the FFT output buffer size. |
| [FFT](#FFT) | The default constructor.  |
| [~FFT](#_u007eFFT) | Destructor.  |
| [Initialize](#Initialize) | Initializes the FFT instance. |
| [Forward](#Forward) | Performs the forward FFT operation. |
| [Backward](#Backward) | Performs the inverse FFT operation. |

## Function Details

### Backward<a name="Backward"></a>
!!! function "void Backward(AmReal32&#42; output, SplitComplex&amp; splitComplex) const"

    
    Performs the inverse FFT operation.
    
    
    :material-location-exit: **Parameter** `output`
    :    The output audio data. This buffer needs to be of the same size as the one provided to the [`Initialize()`](#Initialize) method.
        
    :material-location-enter: **Parameter** `splitComplex`
    :    The complex buffer output separated into real and imaginary parts. The buffer will be resized if
        necessary.
                
    

### FFT<a name="FFT"></a>
!!! function "FFT()"

    
    The default constructor.
             
    
    
    

### Forward<a name="Forward"></a>
!!! function "void Forward(const AmReal32&#42; input, SplitComplex&amp; splitComplex) const"

    
    Performs the forward FFT operation.
    
    
    :material-location-enter: **Parameter** `input`
    :    The input audio data. This buffer needs to be of the same size as the one provided to the [`Initialize()`](#Initialize) method.
        
    :material-location-exit: **Parameter** `splitComplex`
    :    The complex buffer output separated into real and imaginary parts. The buffer will be resized if
        necessary.
                
    

### GetOutputSize<a name="GetOutputSize"></a>
!!! function "static AmUInt64 GetOutputSize(AmUInt64 inputSize)"

    
    Gets the FFT output buffer size.
    
    
    :material-location-enter: **Parameter** `inputSize`
    :    The size of the input buffer.
    
    
    :material-keyboard-return: **Return**
    :    The size of the FFT output buffer for the given input size.
            
    

### Initialize<a name="Initialize"></a>
!!! function "void Initialize(AmSize size) const"

    
    Initializes the FFT instance.
    
    
    :material-location-enter: **Parameter** `size`
    :    The size of the input (as a power of 2).
                
    

### ~FFT<a name="_u007eFFT"></a>
!!! function "~FFT()"

    
    Destructor.
             
    
    
    

