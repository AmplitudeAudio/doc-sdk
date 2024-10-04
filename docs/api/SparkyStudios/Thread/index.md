---
title: Thread
description: 
generator: doxide
---


# Thread



## Types

| Name | Description |
| ---- | ----------- |
| [AwaitablePoolTask](AwaitablePoolTask/index.md) | A pool task that allows a thread to wait until it finishes.  |
| [Pool](Pool/index.md) | Pool tasks scheduler class. |
| [PoolTask](PoolTask/index.md) | Base class for pool tasks.  |

## Functions

| Name | Description |
| ---- | ----------- |
| [CreateMutex](#CreateMutex) | Creates a mutex object. |
| [CreateThread](#CreateThread) | Creates a new thread. |
| [DestroyMutex](#DestroyMutex) | Destroys a mutex object. |
| [GetCurrentThreadId](#GetCurrentThreadId) | Gets the handle of the calling thread.  |
| [GetTimeMillis](#GetTimeMillis) | Gets the total execution time in milliseconds for the calling thread.  |
| [LockMutex](#LockMutex) | Takes ownership of a mutex. |
| [Release](#Release) | Manually stops a thread execution. |
| [Sleep](#Sleep) | Makes the calling thread sleep for the given amount of milliseconds. |
| [UnlockMutex](#UnlockMutex) | Releases ownership of a mutex. |
| [Wait](#Wait) | Waits for the given thread to stop. |

## Function Details

### CreateMutex<a name="CreateMutex"></a>
!!! function "AmMutexHandle CreateMutex(AmUInt64 spinCount = 100)"

    
    Creates a mutex object.
    
    A mutex is an object that a thread can acquire, preventing other
    threads from acquiring it.
    
    To acquire the mutex ownership, you should use LockMutex() with
    the mutex handle as parameter. To release the ownership, use UnlockMutex()
    with the mutex handle as parameter.
            
    

### CreateThread<a name="CreateThread"></a>
!!! function "AmThreadHandle CreateThread(AmThreadFunction threadFunction, AmVoidPtr parameter = nullptr)"

    
    Creates a new thread.
    
    
    :material-location-enter: **Parameter** `threadFunction`
    :    The function to run in the thread.
        
    :material-location-enter: **Parameter** `parameter`
    :    An optional shared data to pass to the thread
                
    

### DestroyMutex<a name="DestroyMutex"></a>
!!! function "void DestroyMutex(AmMutexHandle handle)"

    
    Destroys a mutex object.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The mutex object handle.
                
    

### GetCurrentThreadId<a name="GetCurrentThreadId"></a>
!!! function "AmThreadID GetCurrentThreadId()"

    
    Gets the handle of the calling thread.
             
    
    
    

### GetTimeMillis<a name="GetTimeMillis"></a>
!!! function "AmUInt64 GetTimeMillis()"

    
    Gets the total execution time in milliseconds for the calling thread.
             
    
    
    

### LockMutex<a name="LockMutex"></a>
!!! function "void LockMutex(AmMutexHandle handle)"

    
    Takes ownership of a mutex.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The mutex object handle.
                
    

### Release<a name="Release"></a>
!!! function "void Release(AmThreadHandle&amp; thread)"

    
    Manually stops a thread execution.
    
    
    :material-location-enter: **Parameter** `thread`
    :    The handle of the thread to stop.
                
    

### Sleep<a name="Sleep"></a>
!!! function "void Sleep(AmInt32 milliseconds)"

    
    Makes the calling thread sleep for the given amount of milliseconds.
    
    
    :material-location-enter: **Parameter** `milliseconds`
    :    The amount of time the calling thread should sleep.
                
    

### UnlockMutex<a name="UnlockMutex"></a>
!!! function "void UnlockMutex(AmMutexHandle handle)"

    
    Releases ownership of a mutex.
    
    
    :material-location-enter: **Parameter** `handle`
    :    The mutex object handle.
                
    

### Wait<a name="Wait"></a>
!!! function "void Wait(AmThreadHandle thread)"

    
    Waits for the given thread to stop.
    
    
    :material-location-enter: **Parameter** `thread`
    :    The handle of the thread to wait.
                
    

