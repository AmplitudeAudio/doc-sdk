---
title: DiskFile
description: A `File` implementation that reads and writes a file on disk.
generator: doxide
---


# DiskFile

**class  DiskFile : public File**


A `File` implementation that reads and writes a file on disk.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [DiskFile](#DiskFile) | Creates a new `DiskFile` instance.  |
| [DiskFile](#DiskFile) | Creates a new `DiskFile` instance from a file handle. |
| [DiskFile](#DiskFile) | Creates a new DiskFile instance by opening a file at the given path. |
| [~DiskFile](#_u007eDiskFile) | Destroys the instance and release the file handler.  |
| [GetPath](#GetPath) |  @inherit  |
| [Eof](#Eof) |  @inherit  |
| [Read](#Read) |  @inherit  |
| [Write](#Write) |  @inherit  |
| [Length](#Length) |  @inherit  |
| [Seek](#Seek) |  @inherit  |
| [Position](#Position) |  @inherit  |
| [GetPtr](#GetPtr) |  @inherit  |
| [IsValid](#IsValid) |  @inherit  |
| [Open](#Open) | Opens a file at the given path. |
| [Close](#Close) | Closes the file.  |

## Function Details

### Close<a name="Close"></a>
!!! function "void Close()"

    
    Closes the file.
             
    
    
    

### DiskFile<a name="DiskFile"></a>
!!! function "DiskFile()"

    
    Creates a new `DiskFile` instance.
             
    
    
    

!!! function "explicit DiskFile(AmFileHandle fp)"

    
    Creates a new `DiskFile` instance from a file handle.
    
    
    :material-location-enter: **Parameter** `fp`
    :    The file handle to manage in this instance.
                
    

!!! function "explicit DiskFile( const std::filesystem::path&amp; fileName, eFileOpenMode mode = eFileOpenMode_Read, eFileOpenKind kind = eFileOpenKind_Binary)"

    
    Creates a new DiskFile instance by opening a file at the given path.
    
    
    :material-location-enter: **Parameter** `fileName`
    :    The path to the file to open.
        
    :material-location-enter: **Parameter** `mode`
    :    The open mode to use.
        
    :material-location-enter: **Parameter** `kind`
    :    The type of file to open.
                
    

### Eof<a name="Eof"></a>
!!! function "bool Eof() override"

    
    @inherit
            
    

### GetPath<a name="GetPath"></a>
!!! function "[[nodiscard]] AmOsString GetPath() const override"

    
    @inherit
            
    

### GetPtr<a name="GetPtr"></a>
!!! function "AmVoidPtr GetPtr() override"

    
    @inherit
            
    

### IsValid<a name="IsValid"></a>
!!! function "[[nodiscard]] bool IsValid() const override"

    
    @inherit
            
    

### Length<a name="Length"></a>
!!! function "AmSize Length() override"

    
    @inherit
            
    

### Open<a name="Open"></a>
!!! function "AmResult Open( const std::filesystem::path&amp; filePath, eFileOpenMode mode = eFileOpenMode_Read, eFileOpenKind kind = eFileOpenKind_Binary)"

    
    Opens a file at the given path.
    
    
    :material-location-enter: **Parameter** `filePath`
    :    The path to the file to open.
        
    :material-location-enter: **Parameter** `mode`
    :    The open mode to use.
        
    :material-location-enter: **Parameter** `kind`
    :    The type of file to open.
    
    
    :material-keyboard-return: **Return**
    :    The result of the operation.
            
    

### Position<a name="Position"></a>
!!! function "AmSize Position() override"

    
    @inherit
            
    

### Read<a name="Read"></a>
!!! function "AmSize Read(AmUInt8Buffer dst, AmSize bytes) override"

    
    @inherit
            
    

### Seek<a name="Seek"></a>
!!! function "void Seek(AmInt64 offset, eFileSeekOrigin origin) override"

    
    @inherit
            
    

### Write<a name="Write"></a>
!!! function "AmSize Write(AmConstUInt8Buffer src, AmSize bytes) override"

    
    @inherit
            
    

### ~DiskFile<a name="_u007eDiskFile"></a>
!!! function "~DiskFile() override"

    
    Destroys the instance and release the file handler.
             
    
    
    

