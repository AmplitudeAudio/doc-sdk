---
title: RefCounter
description: Holds the number of references to an object.
generator: doxide
---


# RefCounter

**class  RefCounter**


Holds the number of references to an object.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [RefCounter](#RefCounter) | Constructs a new `RefCounter`. |
| [Increment](#Increment) | Updates the counter by adding one reference. |
| [Decrement](#Decrement) | Updates the counter by removing one reference. |
| [GetCount](#GetCount) | Gets the current number of references. |

## Function Details

### Decrement<a name="Decrement"></a>
!!! function "AmInt32 Decrement()"

    
    Updates the counter by removing one reference.
    
    
    :material-keyboard-return: **Return**
    :    The number of references.
            
    

### GetCount<a name="GetCount"></a>
!!! function "[[nodiscard]] inline AmInt32 GetCount() const"

    
    Gets the current number of references.
    
    
    :material-keyboard-return: **Return**
    :    The current number of references.
            
    

### Increment<a name="Increment"></a>
!!! function "AmInt32 Increment()"

    
    Updates the counter by adding one reference.
    
    
    :material-keyboard-return: **Return**
    :    The number of references.
            
    

### RefCounter<a name="RefCounter"></a>
!!! function "RefCounter()"

    
    Constructs a new `RefCounter`.
    
    This initializes the internal counter to 0.
            
    

