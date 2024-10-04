---
title: PlaybackOutputFormat
description: The playback output format of the device.
generator: doxide
---


# PlaybackOutputFormat

**enum class PlaybackOutputFormat : AmUInt16**


The playback output format of the device.


    


**Default = 0**
:   
The default output format of the device.

This instruct to use the output format provided by the device.
        


**UInt8 = 1**
:   
Send audio samples as unsigned 8-bit integers to the device.
         




**Int16 = 2**
:   
Send audio samples as signed 16-bit integers to the device.
         




**Int24 = 3**
:   
Send audio samples as signed 24-bit integers to the device.
         




**Int32 = 4**
:   
Send audio samples as signed 32-bit integers to the device.
         




**Float32 = 5**
:   
Send audio samples as 32-bit floating point values to the device.
         





