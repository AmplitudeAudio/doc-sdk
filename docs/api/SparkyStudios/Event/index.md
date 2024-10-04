---
title: Event
description: An event is mainly used to apply a set of actions at a given time in game.
generator: doxide
---


# Event

**class  Event : public Asset&lt;AmEventID&gt;**


An event is mainly used to apply a set of actions at a given time in game.

This Event class is only referenced through an EventCanceler object and it is
managed by the Engine. Events can be triggered at runtime by calling the
<code>Engine::Trigger()</code> method using the name of the event.
    


