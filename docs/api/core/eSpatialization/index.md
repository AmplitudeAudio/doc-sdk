---
title: eSpatialization
description: Enumerates the list of available spatialization modes.
generator: doxide
---


# eSpatialization

**enum eSpatialization : AmUInt8**


Enumerates the list of available spatialization modes.


    


**eSpatialization_None**
:   
Disables spatialization.
         




**eSpatialization_Position**
:   
Enables 2D (left-right) spatialization based on sound position.


!!! note
     This mode is available for every panning mode.
            


**eSpatialization_PositionOrientation**
:   
Enables 2D (left-right) spatialization based on sound position and orientation.


!!! note
     The sound instance using this spatialization mode needs to be attached to an `Entity`.


!!! note
     This mode is available for every panning mode.
            


**eSpatialization_HRTF**
:   
Enables 3D spatialization using Head Related Transfer Functions.


!!! note
     This mode is only available for binaural panning modes.
            



