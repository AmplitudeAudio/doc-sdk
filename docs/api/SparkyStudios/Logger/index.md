---
title: Logger
description: The logger class.
generator: doxide
---


# Logger

**class  Logger**


The logger class.

Base class used to perform logging. Implementations of this class have the ability to display or store
log messages wherever they are needed.
    


## Functions

| Name | Description |
| ---- | ----------- |
| [SetLogger](#SetLogger) | Sets the logger instance to use when calling @c amLogger |
| [GetLogger](#GetLogger) | Gets the logger instance to use when calling @c amLogger |
| [Debug](#Debug) | Logs a debug message. |
| [Info](#Info) | Logs an informational message. |
| [Warning](#Warning) | Logs a warning message. |
| [Error](#Error) | Logs an error message. |
| [Critical](#Critical) | Logs a critical message. |
| [Log](#Log) | Logs a message with the given level. |

## Function Details

### Critical<a name="Critical"></a>
!!! function "void Critical(const char&#42; file, int line, const AmString&amp; message)"

    
    Logs a critical message.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file where the message was logged.
        
    :material-location-enter: **Parameter** `line`
    :    The line where the message was logged.
        
    :material-location-enter: **Parameter** `message`
    :    The message to log.
                
    

### Debug<a name="Debug"></a>
!!! function "void Debug(const char&#42; file, int line, const AmString&amp; message)"

    
    Logs a debug message.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file where the message was logged.
        
    :material-location-enter: **Parameter** `line`
    :    The line where the message was logged.
        
    :material-location-enter: **Parameter** `message`
    :    The message to log.
                
    

### Error<a name="Error"></a>
!!! function "void Error(const char&#42; file, int line, const AmString&amp; message)"

    
    Logs an error message.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file where the message was logged.
        
    :material-location-enter: **Parameter** `line`
    :    The line where the message was logged.
        
    :material-location-enter: **Parameter** `message`
    :    The message to log.
                
    

### GetLogger<a name="GetLogger"></a>
!!! function "static Logger&#42; GetLogger()"

    
    Gets the logger instance to use when calling @c amLogger
    
    
    :material-keyboard-return: **Return**
    :    The logger instance.
            
    

### Info<a name="Info"></a>
!!! function "void Info(const char&#42; file, int line, const AmString&amp; message)"

    
    Logs an informational message.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file where the message was logged.
        
    :material-location-enter: **Parameter** `line`
    :    The line where the message was logged.
        
    :material-location-enter: **Parameter** `message`
    :    The message to log.
                
    

### Log<a name="Log"></a>
!!! function "virtual void Log(LogMessageLevel level, const char&#42; file, int line, const AmString&amp; message) = 0"

    
    Logs a message with the given level.
    
    
    :material-location-enter: **Parameter** `level`
    :    The level of the log message.
        
    :material-location-enter: **Parameter** `file`
    :    The file where the message was logged.
        
    :material-location-enter: **Parameter** `line`
    :    The line where the message was logged.
        
    :material-location-enter: **Parameter** `message`
    :    The message to log.
                
    

### SetLogger<a name="SetLogger"></a>
!!! function "static void SetLogger(Logger&#42; loggerInstance)"

    
    Sets the logger instance to use when calling @c amLogger
    
    
    :material-location-enter: **Parameter** `loggerInstance`
    :    The logger instance.
                
    

### Warning<a name="Warning"></a>
!!! function "void Warning(const char&#42; file, int line, const AmString&amp; message)"

    
    Logs a warning message.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file where the message was logged.
        
    :material-location-enter: **Parameter** `line`
    :    The line where the message was logged.
        
    :material-location-enter: **Parameter** `message`
    :    The message to log.
                
    

