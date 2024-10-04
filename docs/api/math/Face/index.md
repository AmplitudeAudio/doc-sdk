---
title: Face
description: Represents a triangulated face.
generator: doxide
---


# Face

**struct  Face**


Represents a triangulated face.

A face is defined by three vertices. This structure is optimized for use
with an existing indexed vertex array, so only the indices of each face's
vertex need to be provided.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_A](#m_A) | Index of the first vertex. |
| [m_B](#m_B) | Index of the second vertex. |
| [m_C](#m_C) | Index of the third vertex. |

## Functions

| Name | Description |
| ---- | ----------- |
| [IsValid](#IsValid) | Checks if the face is valid. |

## Variable Details

### m_A<a name="m_A"></a>

!!! variable "AmSize m_A"

    Index of the first vertex.
    

### m_B<a name="m_B"></a>

!!! variable "AmSize m_B"

    Index of the second vertex.
    

### m_C<a name="m_C"></a>

!!! variable "AmSize m_C"

    Index of the third vertex.
    

## Function Details

### IsValid<a name="IsValid"></a>
!!! function "[[nodiscard]] bool IsValid() const"

    
    Checks if the face is valid.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the face is valid, `false` otherwise.
            
    

