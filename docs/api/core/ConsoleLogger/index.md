---
title: ConsoleLogger
description: The console logger class.
generator: doxide
---


# ConsoleLogger

**class  ConsoleLogger final : public Logger**


The console logger class.

This class logs messages to the console or terminal.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [ConsoleLogger](#ConsoleLogger) | Constructs a new console logger. |
| [~ConsoleLogger](#_u007eConsoleLogger) | Destructor.  |
| [Log](#Log) |  @inherit  |

## Function Details

### ConsoleLogger<a name="ConsoleLogger"></a>
!!! function "explicit ConsoleLogger(bool displayFileAndLine = true)"

    
    Constructs a new console logger.
    
    
    :material-location-enter: **Parameter** `displayFileAndLine`
    :    Whether to display the file and line number in the log messages.
                
    

### Log<a name="Log"></a>
!!! function "void Log(eLogMessageLevel level, const char&#42; file, int line, const AmString&amp; message) override"

    
    @inherit
            
    

### ~ConsoleLogger<a name="_u007eConsoleLogger"></a>
!!! function "~ConsoleLogger() override = default"

    
    Destructor.
             
    
    
    

