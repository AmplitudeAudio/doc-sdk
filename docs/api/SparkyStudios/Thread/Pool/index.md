---
title: Pool
description: Pool tasks scheduler class.
generator: doxide
---


# Pool

**class  Pool**


Pool tasks scheduler class.

The Pool tasks scheduler can pick and run pool tasks on several multiple
threads. The number of threads is defined at initialization.

The maximum number of tasks the pool can manage is defined by the `AM_MAX_THREAD_POOL_TASKS`
macro. The default value is `1024`
        


## Functions

| Name | Description |
| ---- | ----------- |
| [Pool](#Pool) | Creates a new pool tasks scheduler instance.  |
| [Init](#Init) | Initialize and run thread pool. |
| [AddTask](#AddTask) | Add a task to the tasks list. |
| [GetWork](#GetWork) | Called from worker thread to get a new task. |
| [GetThreadCount](#GetThreadCount) | Gets the number of threads this pool is using.  |
| [IsRunning](#IsRunning) | Indicates that the pool is running.  |
| [HasTasks](#HasTasks) | Indicates that has tasks pending.  |

## Function Details

### AddTask<a name="AddTask"></a>
!!! function "void AddTask(const std::shared_ptr&lt;PoolTask&gt;&amp; task)"

    
    Add a task to the tasks list.
    
    
    :material-location-enter: **Parameter** `task`
    :    The PoolTask to add. The task is not automatically deleted when the work is done.
                    
    

### GetThreadCount<a name="GetThreadCount"></a>
!!! function "[[nodiscard]] AmUInt32 GetThreadCount() const"

    
    Gets the number of threads this pool is using.
                 
    
    
    

### GetWork<a name="GetWork"></a>
!!! function "std::shared_ptr&lt;PoolTask&gt; GetWork()"

    
    Called from worker thread to get a new task.
    
    
    !!! note
         This method is called internally, and should not be called in user code.
    
    
    :material-keyboard-return: **Return**
    :    The next PoolTask to execute, or nullptr if no task is available.
                
    

### HasTasks<a name="HasTasks"></a>
!!! function "[[nodiscard]] bool HasTasks() const"

    
    Indicates that has tasks pending.
                 
    
    
    

### Init<a name="Init"></a>
!!! function "void Init(AmUInt32 threadCount)"

    
    Initialize and run thread pool.
    
    
    :material-location-enter: **Parameter** `threadCount`
    :    The number of thread in the pool. For thread count 0, work is done
        at `AddTask` call in the calling thread.
                    
    

### IsRunning<a name="IsRunning"></a>
!!! function "[[nodiscard]] bool IsRunning() const"

    
    Indicates that the pool is running.
                 
    
    
    

### Pool<a name="Pool"></a>
!!! function "Pool()"

    
    Creates a new pool tasks scheduler instance.
                 
    
    
    

