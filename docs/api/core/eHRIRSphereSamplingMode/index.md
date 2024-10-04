---
title: eHRIRSphereSamplingMode
description: Defines how the HRIR sphere is sampled when doing Ambisonics binauralization.
generator: doxide
---


# eHRIRSphereSamplingMode

**enum eHRIRSphereSamplingMode : AmUInt8**


Defines how the HRIR sphere is sampled when doing Ambisonics binauralization.


    


**eHRIRSphereSamplingMode_Bilinear = 0**
:   
Provides the most accurate binauralization, as the HRIR data are smoothly transitioned between sphere points.

See more info about bilinear sampling [here](http://www02.smt.ufrj.br/~diniz/conf/confi117.pdf).
        


**eHRIRSphereSamplingMode_NearestNeighbor = 1**
:   
Provides a more efficient binauralization, as the HRIR data are interpolated using only the nearest neighbors.
         





