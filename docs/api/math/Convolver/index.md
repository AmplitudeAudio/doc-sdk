---
title: Convolver
description: Implementation of a partitioned FFT convolution algorithm with uniform block size.
generator: doxide
---


# Convolver

**class Convolver**


Implementation of a partitioned FFT convolution algorithm with uniform block size.

Some notes on how to use it:

- After initialization with an impulse response, subsequent data portions of
  arbitrary length can be convolved. The convolver internally can handle
  this by using appropriate buffering.

- The convolver works without "latency" (except for the required
  processing time, of course), i.e. the output always is the convolved
  input for each processing call.

- The convolver is suitable for real-time processing which means that no
  "unpredictable" operations like allocations, locking, API calls, etc. are
  performed during processing (all necessary allocations and preparations take
  place during initialization).


    


## Functions

| Name | Description |
| ---- | ----------- |
| [Convolver](#Convolver) | Default constructor. |
| [~Convolver](#_u007eConvolver) | Destructor. |
| [Init](#Init) | Initializes the convolver. |
| [Process](#Process) | Convolves the the given input samples and immediately outputs the result. |
| [Reset](#Reset) | Resets the convolver state and discards the set impulse response. |
| [GetSegmentSize](#GetSegmentSize) | Gets the size of a single convolution segment. |
| [GetSegmentCount](#GetSegmentCount) | Gets the number of convolution segments. |

## Function Details

### Convolver<a name="Convolver"></a>
!!! function "Convolver()"

    
    Default constructor.
    
    Creates an uninitialized convolver.
            
    

### GetSegmentCount<a name="GetSegmentCount"></a>
!!! function "[[nodiscard]] AmSize GetSegmentCount() const"

    
    Gets the number of convolution segments.
    
    
    :material-keyboard-return: **Return**
    :    The number of convolution segments.
            
    

### GetSegmentSize<a name="GetSegmentSize"></a>
!!! function "[[nodiscard]] AmSize GetSegmentSize() const"

    
    Gets the size of a single convolution segment.
    
    
    :material-keyboard-return: **Return**
    :    The size of a single convolution segment.
            
    

### Init<a name="Init"></a>
!!! function "bool Init(AmSize blockSize, const AmAudioSample&#42; ir, AmSize irLen)"

    
    Initializes the convolver.
    
    
    :material-location-enter: **Parameter** `blockSize`
    :    Block size internally used by the convolver (partition size)
        
    :material-location-enter: **Parameter** `ir`
    :    The impulse response
        
    :material-location-enter: **Parameter** `irLen`
    :    Length of the impulse response
    
    
    :material-keyboard-return: **Return**
    :    `true` when the convolver is successfully initialized, `false` otherwise.
            
    

### Process<a name="Process"></a>
!!! function "void Process(const AmAudioSample&#42; input, AmAudioSample&#42; output, AmSize len)"

    
    Convolves the the given input samples and immediately outputs the result.
    
    
    :material-location-enter: **Parameter** `input`
    :    The input samples.
        
    :material-location-exit: **Parameter** `output`
    :    The convolution result.
        
    :material-location-enter: **Parameter** `len`
    :    Number of input/output samples to process.
                
    

### Reset<a name="Reset"></a>
!!! function "void Reset()"

    
    Resets the convolver state and discards the set impulse response.
    
    The convolver will need to be [initialized](#Init) again after this call.
            
    

### ~Convolver<a name="_u007eConvolver"></a>
!!! function "virtual ~Convolver()"

    
    Destructor.
    
    Destroys the convolver and frees all allocated resources.
            
    

