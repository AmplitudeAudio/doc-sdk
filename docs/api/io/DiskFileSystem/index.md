---
title: DiskFileSystem
description: A `FileSystem` implementation that reads and write files from disk.
generator: doxide
---


# DiskFileSystem

**class  DiskFileSystem final : public FileSystem**


A `FileSystem` implementation that reads and write files from disk.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [DiskFileSystem](#DiskFileSystem) | Creates a new instance of the DiskFileSystem class.  |
| [SetBasePath](#SetBasePath) |  @inherit  |
| [GetBasePath](#GetBasePath) |  @inherit  |
| [ResolvePath](#ResolvePath) |  @inherit  |
| [Exists](#Exists) |  @inherit  |
| [IsDirectory](#IsDirectory) |  @inherit  |
| [Join](#Join) |  @inherit  |
| [OpenFile](#OpenFile) |  @inherit  |
| [StartOpenFileSystem](#StartOpenFileSystem) |  @inherit  |
| [TryFinalizeOpenFileSystem](#TryFinalizeOpenFileSystem) |  @inherit  |
| [StartCloseFileSystem](#StartCloseFileSystem) |  @inherit  |
| [TryFinalizeCloseFileSystem](#TryFinalizeCloseFileSystem) |  @inherit  |

## Function Details

### DiskFileSystem<a name="DiskFileSystem"></a>
!!! function "DiskFileSystem()"

    
    Creates a new instance of the DiskFileSystem class.
             
    
    
    

### Exists<a name="Exists"></a>
!!! function "[[nodiscard]] bool Exists(const AmOsString&amp; path) const override"

    
    @inherit
            
    

### GetBasePath<a name="GetBasePath"></a>
!!! function "[[nodiscard]] const AmOsString&amp; GetBasePath() const override"

    
    @inherit
            
    

### IsDirectory<a name="IsDirectory"></a>
!!! function "[[nodiscard]] bool IsDirectory(const AmOsString&amp; path) const override"

    
    @inherit
            
    

### Join<a name="Join"></a>
!!! function "[[nodiscard]] AmOsString Join(const std::vector&lt;AmOsString&gt;&amp; parts) const override"

    
    @inherit
            
    

### OpenFile<a name="OpenFile"></a>
!!! function "[[nodiscard]] std::shared_ptr&lt;File&gt; OpenFile(const AmOsString&amp; path, eFileOpenMode mode) const override"

    
    @inherit
            
    

### ResolvePath<a name="ResolvePath"></a>
!!! function "[[nodiscard]] AmOsString ResolvePath(const AmOsString&amp; path) const override"

    
    @inherit
            
    

### SetBasePath<a name="SetBasePath"></a>
!!! function "void SetBasePath(const AmOsString&amp; basePath) override"

    
    @inherit
            
    

### StartCloseFileSystem<a name="StartCloseFileSystem"></a>
!!! function "void StartCloseFileSystem() override"

    
    @inherit
            
    

### StartOpenFileSystem<a name="StartOpenFileSystem"></a>
!!! function "void StartOpenFileSystem() override"

    
    @inherit
            
    

### TryFinalizeCloseFileSystem<a name="TryFinalizeCloseFileSystem"></a>
!!! function "bool TryFinalizeCloseFileSystem() override"

    
    @inherit
            
    

### TryFinalizeOpenFileSystem<a name="TryFinalizeOpenFileSystem"></a>
!!! function "bool TryFinalizeOpenFileSystem() override"

    
    @inherit
            
    

