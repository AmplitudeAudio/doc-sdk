---
title: PackageItemFile
description: A File implementation that provides access to an item in an * Amplitude package file. 
generator: doxide
---


# PackageItemFile

**class  PackageItemFile : public DiskFile**


A File implementation that provides access to an item in an
     * Amplitude package file.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [GetPath](#GetPath) |  @copydoc DiskFile::GetPath  |
| [Eof](#Eof) |  @copydoc DiskFile::Eof  |
| [Read](#Read) |  @copydoc DiskFile::Read  |
| [Write](#Write) |  @copydoc DiskFile::Write !!! note Writing is disabled for packages item files.  |
| [Length](#Length) |  @copydoc DiskFile::Length  |
| [Seek](#Seek) |  @copydoc DiskFile::Seek  |
| [Position](#Position) |  @copydoc DiskFile::Position  |

## Function Details

### Eof<a name="Eof"></a>
!!! function "bool Eof() override"

    
    @copydoc DiskFile::Eof
            
    

### GetPath<a name="GetPath"></a>
!!! function "[[nodiscard]] AmOsString GetPath() const override"

    
    @copydoc DiskFile::GetPath
            
    

### Length<a name="Length"></a>
!!! function "AmSize Length() override"

    
    @copydoc DiskFile::Length
            
    

### Position<a name="Position"></a>
!!! function "AmSize Position() override"

    
    @copydoc DiskFile::Position
            
    

### Read<a name="Read"></a>
!!! function "AmSize Read(AmUInt8Buffer dst, AmSize bytes) override"

    
    @copydoc DiskFile::Read
            
    

### Seek<a name="Seek"></a>
!!! function "void Seek(AmInt64 offset, FileSeekOrigin origin) override"

    
    @copydoc DiskFile::Seek
            
    

### Write<a name="Write"></a>
!!! function "AmSize Write(AmConstUInt8Buffer src, AmSize bytes) override"

    
    @copydoc DiskFile::Write
    
    
    !!! note
         Writing is disabled for packages item files.
                
    

