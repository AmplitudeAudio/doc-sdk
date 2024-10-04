---
title: AwaitablePoolTask
description: A pool task that allows a thread to wait until it finishes. 
generator: doxide
---


# AwaitablePoolTask

**class  AwaitablePoolTask : public PoolTask**


A pool task that allows a thread to wait until it finishes.
         




## Functions

| Name | Description |
| ---- | ----------- |
| [Work](#Work) |  @copydoc PoolTask::Work  |
| [AwaitableWork](#AwaitableWork) | Pool task execution function.  |
| [Await](#Await) | Makes the calling thread wait for this task to finish.  |
| [Await](#Await) | Makes the calling thread wait for this task to finish. * @param duration The maximum amount of time to wait in milliseconds.  |

## Function Details

### Await<a name="Await"></a>
!!! function "void Await()"

    
    Makes the calling thread wait for this task to finish.
                 
    
    
    

!!! function "bool Await(AmUInt64 duration)"

    
    Makes the calling thread wait for this task to finish.
                 * @param duration The maximum amount of time to wait in milliseconds.
                 
    
    
    

### AwaitableWork<a name="AwaitableWork"></a>
!!! function "virtual void AwaitableWork() = 0"

    
    Pool task execution function.
                 
    
    
    

### Work<a name="Work"></a>
!!! function "void Work() final"

    
    @copydoc PoolTask::Work
                
    

