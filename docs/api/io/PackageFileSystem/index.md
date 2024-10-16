---
title: PackageFileSystem
description: A `FileSystem` implementation that provides access to an Amplitude package file.
generator: doxide
---


# PackageFileSystem

**class  PackageFileSystem final : public FileSystem**


A `FileSystem` implementation that provides access to an Amplitude package file.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [PackageFileSystem](#PackageFileSystem) | Constructs a new `PackageFileSystem` instance.  |
| [~PackageFileSystem](#_u007ePackageFileSystem) | Destroys the `PackageFileSystem` instance.  |
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
| [IsValid](#IsValid) | Returns if the package file is valid and loaded. |

## Function Details

### Exists<a name="Exists"></a>
!!! function "[[nodiscard]] bool Exists(const AmOsString&amp; path) const override"

    
    @inherit
            
    

### GetBasePath<a name="GetBasePath"></a>
!!! function "[[nodiscard]] const AmOsString&amp; GetBasePath() const override"

    
    @inherit
            
    

### IsDirectory<a name="IsDirectory"></a>
!!! function "[[nodiscard]] bool IsDirectory(const AmOsString&amp; path) const override"

    
    @inherit
            
    

### IsValid<a name="IsValid"></a>
!!! function "[[nodiscard]] bool IsValid() const"

    
    Returns if the package file is valid and loaded.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the package file is valid and loaded, `false` otherwise.
            
    

### Join<a name="Join"></a>
!!! function "[[nodiscard]] AmOsString Join(const std::vector&lt;AmOsString&gt;&amp; parts) const override"

    
    @inherit
            
    

### OpenFile<a name="OpenFile"></a>
!!! function "[[nodiscard]] std::shared_ptr&lt;File&gt; OpenFile(const AmOsString&amp; path, eFileOpenMode mode = eFileOpenMode_Read) const override"

    
    @inherit
            
    

### PackageFileSystem<a name="PackageFileSystem"></a>
!!! function "PackageFileSystem()"

    
    Constructs a new `PackageFileSystem` instance.
             
    
    
    

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
            
    

### ~PackageFileSystem<a name="_u007ePackageFileSystem"></a>
!!! function "~PackageFileSystem() override"

    
    Destroys the `PackageFileSystem` instance.
             
    
    
    

