---
title: HRIRSphereFileHeaderDescription
description: Provides metadata about an HRIR sphere file.
generator: doxide
---


# HRIRSphereFileHeaderDescription

**struct HRIRSphereFileHeaderDescription**


Provides metadata about an HRIR sphere file.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_Version](#m_Version) | HRIR sphere file header tag. Should be always equal to "AMIR". HRIR sphere file version. Allows backward compatibility.  |
| [m_SampleRate](#m_SampleRate) | Sample rate used to encode HRIR data.  |
| [m_IRLength](#m_IRLength) | The length of the HRIR data in number of samples.  |
| [m_VertexCount](#m_VertexCount) | The number of vertices in the HRIR sphere.  |
| [m_IndexCount](#m_IndexCount) | The number of indices in the HRIR sphere.  |

## Variable Details

### m_IRLength<a name="m_IRLength"></a>

!!! variable "AmUInt32 m_IRLength"

    
    The length of the HRIR data in number of samples.
             
    
    
    

### m_IndexCount<a name="m_IndexCount"></a>

!!! variable "AmUInt32 m_IndexCount"

    
    The number of indices in the HRIR sphere.
             
    
    
    

### m_SampleRate<a name="m_SampleRate"></a>

!!! variable "AmUInt32 m_SampleRate"

    
    Sample rate used to encode HRIR data.
             
    
    
    

### m_Version<a name="m_Version"></a>

!!! variable "AmUInt16 m_Version"

    
    HRIR sphere file header tag. Should be always equal to "AMIR".
             
    
    
    
    HRIR sphere file version. Allows backward compatibility.
             
    
    
    

### m_VertexCount<a name="m_VertexCount"></a>

!!! variable "AmUInt32 m_VertexCount"

    
    The number of vertices in the HRIR sphere.
             
    
    
    

