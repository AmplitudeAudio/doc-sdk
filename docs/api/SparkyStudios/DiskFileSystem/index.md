---
title: DiskFileSystem
description: A FileSystem implementation that reads and write files * from disk. 
generator: doxide
---


# DiskFileSystem

**class  DiskFileSystem final : public FileSystem**


A FileSystem implementation that reads and write files
     * from disk.
     




## Functions

| Name | Description |
| ---- | ----------- |
| [DiskFileSystem](#DiskFileSystem) | Create a new instance of the DiskFileSystem class.  |
| [SetBasePath](#SetBasePath) |  @copydoc FileSystem::SetBasePath  |
| [GetBasePath](#GetBasePath) |  @copydoc FileSystem::GetBasePath  |
| [ResolvePath](#ResolvePath) |  @copydoc FileSystem::ResolvePath  |
| [Exists](#Exists) |  @copydoc FileSystem::Exists  |
| [IsDirectory](#IsDirectory) |  @copydoc FileSystem::IsDirectory  |
| [Join](#Join) |  @copydoc FileSystem::Join  |
| [OpenFile](#OpenFile) |  @copydoc FileSystem::OpenFile  |
| [StartOpenFileSystem](#StartOpenFileSystem) |  @copydoc FileSystem::StartOpenFileSystem  |
| [TryFinalizeOpenFileSystem](#TryFinalizeOpenFileSystem) |  @copydoc FileSystem::TryFinalizeOpenFileSystem  |
| [StartCloseFileSystem](#StartCloseFileSystem) |  @copydoc FileSystem::StartCloseFileSystem  |
| [TryFinalizeCloseFileSystem](#TryFinalizeCloseFileSystem) |  @copydoc FileSystem::TryFinalizeCloseFileSystem  |

## Function Details

### DiskFileSystem<a name="DiskFileSystem"></a>
!!! function "DiskFileSystem()"

    
    Create a new instance of the DiskFileSystem class.
             
    
    
    

### Exists<a name="Exists"></a>
!!! function "[[nodiscard]] bool Exists(const AmOsString&amp; path) const override"

    
    @copydoc FileSystem::Exists
            
    

### GetBasePath<a name="GetBasePath"></a>
!!! function "[[nodiscard]] const AmOsString&amp; GetBasePath() const override"

    
    @copydoc FileSystem::GetBasePath
            
    

### IsDirectory<a name="IsDirectory"></a>
!!! function "[[nodiscard]] bool IsDirectory(const AmOsString&amp; path) const override"

    
    @copydoc FileSystem::IsDirectory
            
    

### Join<a name="Join"></a>
!!! function "[[nodiscard]] AmOsString Join(const std::vector&lt;AmOsString&gt;&amp; parts) const override"

    
    @copydoc FileSystem::Join
            
    

### OpenFile<a name="OpenFile"></a>
!!! function "[[nodiscard]] std::shared_ptr&lt;File&gt; OpenFile(const AmOsString&amp; path, FileOpenMode mode) const override"

    
    @copydoc FileSystem::OpenFile
            
    

### ResolvePath<a name="ResolvePath"></a>
!!! function "[[nodiscard]] AmOsString ResolvePath(const AmOsString&amp; path) const override"

    
    @copydoc FileSystem::ResolvePath
            
    

### SetBasePath<a name="SetBasePath"></a>
!!! function "void SetBasePath(const AmOsString&amp; basePath) override"

    
    @copydoc FileSystem::SetBasePath
            
    

### StartCloseFileSystem<a name="StartCloseFileSystem"></a>
!!! function "void StartCloseFileSystem() override"

    
    @copydoc FileSystem::StartCloseFileSystem
            
    

### StartOpenFileSystem<a name="StartOpenFileSystem"></a>
!!! function "void StartOpenFileSystem() override"

    
    @copydoc FileSystem::StartOpenFileSystem
            
    

### TryFinalizeCloseFileSystem<a name="TryFinalizeCloseFileSystem"></a>
!!! function "bool TryFinalizeCloseFileSystem() override"

    
    @copydoc FileSystem::TryFinalizeCloseFileSystem
            
    

### TryFinalizeOpenFileSystem<a name="TryFinalizeOpenFileSystem"></a>
!!! function "bool TryFinalizeOpenFileSystem() override"

    
    @copydoc FileSystem::TryFinalizeOpenFileSystem
            
    
