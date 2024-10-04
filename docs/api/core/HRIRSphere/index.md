---
title: HRIRSphere
description: A 3D sphere of HRIR data.
generator: doxide
---


# HRIRSphere

**class  HRIRSphere : public Resource**


A 3D sphere of HRIR data.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [SetSamplingMode](#SetSamplingMode) | Sets the sampling mode for the HRIR sphere. |
| [GetSamplingMode](#GetSamplingMode) | Gets the sampling mode for the HRIR sphere.  |
| [Sample](#Sample) | Samples the HRIR sphere for the given direction. |

## Function Details

### GetSamplingMode<a name="GetSamplingMode"></a>
!!! function "[[nodiscard]] virtual eHRIRSphereSamplingMode GetSamplingMode() const = 0"

    
    Gets the sampling mode for the HRIR sphere.
             
    
    
    

### Sample<a name="Sample"></a>
!!! function "virtual void Sample(const AmVec3&amp; direction, AmReal32&#42; leftHRIR, AmReal32&#42; rightHRIR) const = 0"

    
    Samples the HRIR sphere for the given direction.
    
    
    :material-location-enter: **Parameter** `direction`
    :    The sound to listener direction.
        
    :material-location-exit: **Parameter** `leftHRIR`
    :    The left HRIR data.
        
    :material-location-exit: **Parameter** `rightHRIR`
    :    The right HRIR data.
                
    

### SetSamplingMode<a name="SetSamplingMode"></a>
!!! function "virtual void SetSamplingMode(eHRIRSphereSamplingMode mode) = 0"

    
    Sets the sampling mode for the HRIR sphere.
    
    
    :material-location-enter: **Parameter** `mode`
    :    The sampling mode to use.
                
    

