---
title: Event
description: Amplitude Event Asset.
generator: doxide
---


# Event

**class  Event : public Asset&lt;AmEventID&gt;**


Amplitude Event Asset.

An event is used to apply a set of actions (synchronously or asynchronously) at a given time
in the game.

This `Event` class is only referenced through an `EventCanceler` object and it is
managed by the `Engine`. Events can be triggered at runtime by using the `Trigger()`
method of the `Engine` instance:
```cpp
amEngine->Trigger("an_event_name"); // You can also use the event ID, or its handle.
```


    


