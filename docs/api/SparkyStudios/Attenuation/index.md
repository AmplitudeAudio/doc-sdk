---
title: Attenuation
description: Amplitude Attenuation.
generator: doxide
---


# Attenuation

**class  Attenuation : public Asset&lt;AmAttenuationID&gt;**


Amplitude Attenuation.

An Attenuation materializes how the sound volume and other distance-based
parameters are calculated following the distance of the sound source to the listener.

The Attenuation is a shared object between sound sources. They are used only
when the sound need to adjust his volume due to the distance of from the listener,
and many other parameters.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [GetGain](#GetGain) | Returns the gain of the sound from the given distance to the listener. |
| [GetGain](#GetGain) | Returns the gain of the sound from the given distance to the listener. |
| [GetShape](#GetShape) | Returns the shape object of this Attenuation. |
| [GetGainCurve](#GetGainCurve) | Returns the gain curve attached to this Attenuation. |
| [GetMaxDistance](#GetMaxDistance) | Returns the maximum distance for a fully attenuated sound |
| [IsAirAbsorptionEnabled](#IsAirAbsorptionEnabled) | Returns whether air absorption is enabled for this Attenuation. |
| [EvaluateAirAbsorption](#EvaluateAirAbsorption) | Evaluates the air absorption effect for a specific frequency band. |

## Function Details

### EvaluateAirAbsorption<a name="EvaluateAirAbsorption"></a>
!!! function "[[nodiscard]] virtual AmReal32 EvaluateAirAbsorption( const AmVec3&amp; soundLocation, const AmVec3&amp; listenerLocation, AmUInt32 band) const = 0"

    
    Evaluates the air absorption effect for a specific frequency band.
    
    This method calculates the attenuation factor due to air absorption
    at a given frequency band for a sound source located at a specific position
    and a listener located at another specific position.
    
    
    :material-location-enter: **Parameter** `soundLocation`
    :    The location of the sound source.
        
    :material-location-enter: **Parameter** `listenerLocation`
    :    The location of the listener which is hearing the sound.
        
    :material-location-enter: **Parameter** `band`
    :    The frequency band for which the air absorption effect is evaluated.
    
    
    :material-keyboard-return: **Return**
    :    The air absorption attenuation factor for the given frequency band.
    The returned value is in decibels (dB).
            
    

### GetGain<a name="GetGain"></a>
!!! function "[[nodiscard]] virtual AmReal32 GetGain(const AmVec3&amp; soundLocation, const Listener&amp; listener) const = 0"

    
    Returns the gain of the sound from the given distance to the listener.
    
    
    :material-location-enter: **Parameter** `soundLocation`
    :    The location of the sound source.
        
    :material-location-enter: **Parameter** `listener`
    :    The listener which is hearing the sound.
    
    
    :material-keyboard-return: **Return**
    :    The computed gain value fom the curve.
            
    

!!! function "[[nodiscard]] virtual AmReal32 GetGain(const Entity&amp; entity, const Listener&amp; listener) const = 0"

    
    Returns the gain of the sound from the given distance to the listener.
    
    
    :material-location-enter: **Parameter** `entity`
    :    The entity which emits the sound.
        
    :material-location-enter: **Parameter** `listener`
    :    The listener which is hearing the sound.
    
    
    :material-keyboard-return: **Return**
    :    The computed gain value fom the curve.
            
    

### GetGainCurve<a name="GetGainCurve"></a>
!!! function "[[nodiscard]] virtual const Curve&amp; GetGainCurve() const = 0"

    
    Returns the gain curve attached to this Attenuation.
    
    
    :material-keyboard-return: **Return**
    :    The attenuation's gain curve.
            
    

### GetMaxDistance<a name="GetMaxDistance"></a>
!!! function "[[nodiscard]] virtual AmReal64 GetMaxDistance() const = 0"

    
    Returns the maximum distance for a fully attenuated sound
    
    
    :material-keyboard-return: **Return**
    :    The maximum sound attenuation distance.
            
    

### GetShape<a name="GetShape"></a>
!!! function "&#42; GetShape() const"

    
    Returns the shape object of this Attenuation.
    
    
    :material-keyboard-return: **Return**
    :    The Attenuation shape.
            
    

### IsAirAbsorptionEnabled<a name="IsAirAbsorptionEnabled"></a>
!!! function "[[nodiscard]] virtual bool IsAirAbsorptionEnabled() const = 0"

    
    Returns whether air absorption is enabled for this Attenuation.
    
    
    :material-keyboard-return: **Return**
    :    `true` if air absorption is enabled, `false` otherwise.
            
    

