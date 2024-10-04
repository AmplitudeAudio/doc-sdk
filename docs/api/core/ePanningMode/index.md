---
title: ePanningMode
description: Enumerates the list of available panning modes.
generator: doxide
---


# ePanningMode

**enum ePanningMode : AmUInt8**


Enumerates the list of available panning modes.


    


**ePanningMode_Stereo = 0**
:   
2D stereo panning. This panning mode won't provide HRTF-related features.


!!! note
     The Ambisonic decoder will use a virtual array of 2 loudspeakers
    evenly arranged in front of the listener.
            


**ePanningMode_BinauralLowQuality = 1**
:   
3D binaural panning using first-order HRTF.


!!! note
     The Ambisonic decoder will use a virtual array of 8 loudspeakers
    arranged in a cube configuration around the listener.
            


**ePanningMode_BinauralMediumQuality = 2**
:   
3D binaural panning using second-order HRTF.


!!! note
     The Ambisonic decoder will use a virtual array of 12 loudspeakers
    arranged in a dodecahedral configuration (using faces of the dodecahedron).
            


**ePanningMode_BinauralHighQuality = 3**
:   
3D binaural panning using third-order HRTF.


!!! note
     The Ambisonic decoder will use a virtual array of 26 loudspeakers
    arranged in a Lebedev grid. See: https://people.sc.fsu.edu/~jburkardt/m_src/sphere_lebedev_rule/sphere_lebedev_rule.html
            



