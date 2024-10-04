---
title: PackageItemFile
description: A `File` implementation that provides access to an item in an Amplitude package file.
generator: doxide
---


# PackageItemFile

**class  PackageItemFile : public DiskFile**


A `File` implementation that provides access to an item in an Amplitude package file.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [PackageItemFile](#PackageItemFile) | Constructs a new `PackageItemFile` instance. |
| [GetPath](#GetPath) |  @inherit  |
| [Eof](#Eof) |  @inherit  |
| [Read](#Read) |  @inherit  |
| [Write](#Write) |  @inherit ! |
| [Length](#Length) |  @inherit  |
| [Seek](#Seek) |  @inherit  |
| [Position](#Position) |  @inherit  |

## Function Details

### Eof<a name="Eof"></a>
!!! function "bool Eof() override"

    
    @inherit
            
    

### GetPath<a name="GetPath"></a>
!!! function "[[nodiscard]] AmOsString GetPath() const override"

    
    @inherit
            
    

### Length<a name="Length"></a>
!!! function "AmSize Length() override"

    
    @inherit
            
    

### PackageItemFile<a name="PackageItemFile"></a>
!!! function "PackageItemFile(const PackageFileItemDescription&#42; item, const std::filesystem::path&amp; packageFile, AmSize headerSize)"

    
    Constructs a new `PackageItemFile` instance.
    
    
    :material-location-enter: **Parameter** `item`
    :    The description of the package item.
        
    :material-location-enter: **Parameter** `packageFile`
    :    The path to the package file.
        
    :material-location-enter: **Parameter** `headerSize`
    :    The size of the package file header.
                
    

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
    
    
    !!! note
         Writing is disabled for packages item files.
                
    

