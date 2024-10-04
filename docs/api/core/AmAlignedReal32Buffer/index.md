---
title: AmAlignedReal32Buffer
description: Class that handles aligned allocations to support vectorized operations.
generator: doxide
---


# AmAlignedReal32Buffer

**class  AmAlignedReal32Buffer**


Class that handles aligned allocations to support vectorized operations.


    


## Operators

| Name | Description |
| ---- | ----------- |
| [operator[]](#operator_u005b_u005d) | Returns a reference to the float at the specified index. |
| [operator[]](#operator_u005b_u005d) | Returns a const reference to the float at the specified index. |

## Functions

| Name | Description |
| ---- | ----------- |
| [Init](#Init) | Allocates and align buffer. |
| [Clear](#Clear) | Clears all data.  |
| [Release](#Release) | Releases the allocated buffer.  |
| [GetSize](#GetSize) | Gets the size of the buffer. |
| [GetBuffer](#GetBuffer) | Gets the current aligned pointer. |
| [GetPointer](#GetPointer) | Gets the raw allocated pointer. |
| [CopyFrom](#CopyFrom) | Copies data from another buffer. |
| [Resize](#Resize) | Resizes the buffer to the specified size. |
| [Swap](#Swap) | Swaps two buffers. |

## Operator Details

### operator[]<a name="operator_u005b_u005d"></a>

!!! function "AmReal32&amp; operator[](AmSize index)"

    
    Returns a reference to the float at the specified index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The index of the float to retrieve.
    
    
    :material-keyboard-return: **Return**
    :    The reference to the float at the specified index.
            
    

!!! function "const AmReal32&amp; operator[](AmSize index) const"

    
    Returns a const reference to the float at the specified index.
    
    
    :material-location-enter: **Parameter** `index`
    :    The index of the float to retrieve.
    
    
    :material-keyboard-return: **Return**
    :    The const reference to the float at the specified index.
            
    

## Function Details

### Clear<a name="Clear"></a>
!!! function "void Clear() const"

    
    Clears all data.
             
    
    
    

### CopyFrom<a name="CopyFrom"></a>
!!! function "void CopyFrom(const AmAlignedReal32Buffer&amp; other) const"

    
    Copies data from another buffer.
    
    
    :material-location-enter: **Parameter** `other`
    :    The other buffer to copy data from.
                
    

### GetBuffer<a name="GetBuffer"></a>
!!! function "[[nodiscard]] inline AmReal32&#42; GetBuffer() const"

    
    Gets the current aligned pointer.
    
    
    :material-keyboard-return: **Return**
    :    The pointer the float buffer
            
    

### GetPointer<a name="GetPointer"></a>
!!! function "[[nodiscard]] inline AmUInt8Buffer GetPointer() const"

    
    Gets the raw allocated pointer.
    
    
    :material-keyboard-return: **Return**
    :    The pointer to the raw allocated memory.
            
    

### GetSize<a name="GetSize"></a>
!!! function "[[nodiscard]] inline AmUInt32 GetSize() const"

    
    Gets the size of the buffer.
    
    
    :material-keyboard-return: **Return**
    :    The number of float values stored in the buffer.
            
    

### Init<a name="Init"></a>
!!! function "AmResult Init(AmUInt32 size, bool clear = true)"

    
    Allocates and align buffer.
    
    
    :material-location-enter: **Parameter** `size`
    :    The buffer size.
        
    :material-location-enter: **Parameter** `clear`
    :    Whether to clear the buffer.
    
    
    :material-location-exit: **Return**
    :    An `AM_ERROR` value indicating if the allocation was successful or not.
            
    

### Release<a name="Release"></a>
!!! function "void Release()"

    
    Releases the allocated buffer.
             
    
    
    

### Resize<a name="Resize"></a>
!!! function "void Resize(AmUInt32 size, bool clear = true)"

    
    Resizes the buffer to the specified size.
    
    
    :material-location-enter: **Parameter** `size`
    :    The new size of the buffer.
        
    :material-location-enter: **Parameter** `clear`
    :    Whether to clear the buffer after resize. If `true`, the buffer will be cleared
        even if the new size equals the old size.
                
    

### Swap<a name="Swap"></a>
!!! function "static void Swap(AmAlignedReal32Buffer&amp; a, AmAlignedReal32Buffer&amp; b)"

    
    Swaps two buffers.
    
    
    :material-location-enter: **Parameter** `a`
    :    The first buffer.
        
    :material-location-enter: **Parameter** `b`
    :    The second buffer.
                
    

