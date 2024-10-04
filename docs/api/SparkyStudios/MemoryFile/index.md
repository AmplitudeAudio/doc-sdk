---
title: MemoryFile
description: A File implementation that reads and writes a memory buffer. 
generator: doxide
---


# MemoryFile

**class  MemoryFile : public File**


A File implementation that reads and writes a memory buffer.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [MemoryFile](#MemoryFile) | Creates a new MemoryFile instance.  |
| [MemoryFile](#MemoryFile) | Creates a new MemoryFile instance from a memory buffer. |
| [~MemoryFile](#_u007eMemoryFile) | Destroys the instance and release the memory buffer if owned.  |
| [GetPath](#GetPath) |  @copydoc File::GetPath  |
| [Eof](#Eof) |  @copydoc File::Eof  |
| [Read](#Read) |  @copydoc File::Read  |
| [Write](#Write) |  @copydoc File::Write  |
| [Length](#Length) |  @copydoc File::Length  |
| [Seek](#Seek) |  @copydoc File::Seek  |
| [Position](#Position) |  @copydoc File::Position  |
| [GetPtr](#GetPtr) |  @copydoc File::GetPtr  |
| [IsValid](#IsValid) |  @copydoc File::IsValid  |
| [Open](#Open) | Opens a new memory buffer with the specified size. |
| [OpenMem](#OpenMem) | Opens a memory buffer. |
| [OpenToMem](#OpenToMem) | Opens a memory buffer from a file content. |
| [OpenFileToMem](#OpenFileToMem) | Copies data from a file instance to a memory buffer. The file content is entirely copied. |
| [Close](#Close) | Closes the memory buffer and releases associated resources.  |

## Function Details

### Close<a name="Close"></a>
!!! function "void Close()"

    
    Closes the memory buffer and releases associated resources.
             
    
    
    

### Eof<a name="Eof"></a>
!!! function "bool Eof() override"

    
    @copydoc File::Eof
            
    

### GetPath<a name="GetPath"></a>
!!! function "[[nodiscard]] AmOsString GetPath() const override"

    
    @copydoc File::GetPath
            
    

### GetPtr<a name="GetPtr"></a>
!!! function "AmVoidPtr GetPtr() override"

    
    @copydoc File::GetPtr
            
    

### IsValid<a name="IsValid"></a>
!!! function "[[nodiscard]] bool IsValid() const override"

    
    @copydoc File::IsValid
            
    

### Length<a name="Length"></a>
!!! function "AmSize Length() override"

    
    @copydoc File::Length
            
    

### MemoryFile<a name="MemoryFile"></a>
!!! function "MemoryFile()"

    
    Creates a new MemoryFile instance.
             
    
    
    

!!! function "MemoryFile(AmUInt8Buffer buffer, AmSize size, bool copy = false, bool takeOwnership = true)"

    
    Creates a new MemoryFile instance from a memory buffer.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The memory buffer to manage in this instance.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the memory buffer.
        
    :material-location-enter: **Parameter** `copy`
    :    If true, the memory buffer will be copied.
        
    :material-location-enter: **Parameter** `takeOwnership`
    :    If true, the memory buffer will be owned by this instance, and released when this instance is destroyed.
                
    

### Open<a name="Open"></a>
!!! function "AmResult Open(AmSize size)"

    
    Opens a new memory buffer with the specified size.
    
    
    :material-location-enter: **Parameter** `size`
    :    The size of the buffer.
    
    
    :material-keyboard-return: **Return**
    :    The result of the operation.
            
    

### OpenFileToMem<a name="OpenFileToMem"></a>
!!! function "AmResult OpenFileToMem(File&#42; file)"

    
    Copies data from a file instance to a memory buffer. The file content is entirely copied.
    
    
    :material-location-enter: **Parameter** `file`
    :    The file isntance to copy data from.
    
    
    :material-keyboard-return: **Return**
    :    The result of the operation.
            
    

### OpenMem<a name="OpenMem"></a>
!!! function "AmResult OpenMem(AmConstUInt8Buffer buffer, AmSize size, bool copy = false, bool takeOwnership = true)"

    
    Opens a memory buffer.
    
    
    :material-location-enter: **Parameter** `buffer`
    :    The memory buffer to open.
        
    :material-location-enter: **Parameter** `size`
    :    The size of the memory buffer.
        
    :material-location-enter: **Parameter** `copy`
    :    If true, the memory buffer will be copied.
        
    :material-location-enter: **Parameter** `takeOwnership`
    :    If true, the memory buffer will be owned by this instance, and released when this instance is destroyed.
    
    
    :material-keyboard-return: **Return**
    :    The result of the operation.
            
    

### OpenToMem<a name="OpenToMem"></a>
!!! function "AmResult OpenToMem(const std::filesystem::path&amp; fileName)"

    
    Opens a memory buffer from a file content.
    
    
    :material-location-enter: **Parameter** `fileName`
    :    The path to the file to open.
    
    
    :material-keyboard-return: **Return**
    :    The result of the operation.
            
    

### Position<a name="Position"></a>
!!! function "AmSize Position() override"

    
    @copydoc File::Position
            
    

### Read<a name="Read"></a>
!!! function "AmSize Read(AmUInt8Buffer dst, AmSize bytes) override"

    
    @copydoc File::Read
            
    

### Seek<a name="Seek"></a>
!!! function "void Seek(AmInt64 offset, FileSeekOrigin origin) override"

    
    @copydoc File::Seek
            
    

### Write<a name="Write"></a>
!!! function "AmSize Write(AmConstUInt8Buffer src, AmSize bytes) override"

    
    @copydoc File::Write
            
    

### ~MemoryFile<a name="_u007eMemoryFile"></a>
!!! function "~MemoryFile() override"

    
    Destroys the instance and release the memory buffer if owned.
             
    
    
    

