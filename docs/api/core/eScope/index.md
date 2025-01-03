---
title: eScope
description: Enumerates the list of available scopes for sound objects.
generator: doxide
---


# eScope

**enum eScope : AmUInt8**


Enumerates the list of available scopes for sound objects.


    


**eScope_World**
:   
The sound object is within the game world. Instances of collections played in this scope
         * will be treated as one object across all entities.
         




**eScope_Entity**
:   
The sound object is within a specific entity. Instances of collections played in this scope
         * will be treated as separate objects, and no data will be shared across entities.


!!! note
     Sound objects using this scope are required to be attached to an [`Entity`](./Entity.md).
            



