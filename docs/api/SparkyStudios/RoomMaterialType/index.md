---
title: RoomMaterialType
description: Defines the material type of a @c Room wall.
generator: doxide
---


# RoomMaterialType

**enum class RoomMaterialType : AmUInt8**


Defines the material type of a @c Room wall.

Use this enum when you want use predefined absorption coefficients for a wall.
Note that the predefined coefficients are only for reference, and may not be
accurate for your specific use case.

You can use the `RoomMaterialType::Custom` to define a custom material. This
will need you to provide the absorption coefficients yourself.
    


