---
title: PoolTask
description: Base class for pool tasks. 
generator: doxide
---


# PoolTask

**class  PoolTask**


Base class for pool tasks.
         




## Functions

| Name | Description |
| ---- | ----------- |
| [Work](#Work) | Main pool task execution function. |
| [Ready](#Ready) | Checks if the task is ready to be picked by the pool scheduler. * @return @c true if the task is ready @c false otherwise.  |

## Function Details

### Ready<a name="Ready"></a>
!!! function "virtual bool Ready()"

    
    Checks if the task is ready to be picked by the pool scheduler.
                 * @return @c true if the task is ready @c false otherwise.
                 
    
    
    

### Work<a name="Work"></a>
!!! function "virtual void Work() = 0"

    
    Main pool task execution function.
    
    When this task will be picked by the pool scheduler, this method
    will be called to execute the task.
                
    

