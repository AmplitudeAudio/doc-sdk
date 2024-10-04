---
title: FileSystem
description: Base class for files and resources loaders.
generator: doxide
---


# FileSystem

**class  FileSystem**


Base class for files and resources loaders.

The FileSystem class is used by the engine as an interface to
load files and other resources. It provides basic functionnalities
needed by a filesystem
    


## Functions

| Name | Description |
| ---- | ----------- |
| [~FileSystem](#_u007eFileSystem) | Default virtual destructor.  |
| [SetBasePath](#SetBasePath) | Changes the filesystem base path. That path is interpreted by the implementation * and doesn't necessarily have to be a real path on disk. It's just used as the base path * for resolving relative paths from which the engine will load resources. |
| [GetBasePath](#GetBasePath) | Returns the base path of the filesystem. |
| [ResolvePath](#ResolvePath) | Resolves a relative path from the filesystem base path. |
| [Exists](#Exists) | Checks if an item (file or folder) exists on the filesystem. |
| [IsDirectory](#IsDirectory) | Checks if an item (file or folder) is a directory. |
| [Join](#Join) | Merge the given parts of the path into a single path, by joining them with the filesystem * path separator. |
| [OpenFile](#OpenFile) | Opens the file at the given path. |
| [StartOpenFileSystem](#StartOpenFileSystem) | Opens the FileSystem. |
| [TryFinalizeOpenFileSystem](#TryFinalizeOpenFileSystem) | Checks if the FileSystem is initialized. |
| [StartCloseFileSystem](#StartCloseFileSystem) | Stops the FileSystem. |
| [TryFinalizeCloseFileSystem](#TryFinalizeCloseFileSystem) | Checks if the FileSystem is stopped. |

## Function Details

### Exists<a name="Exists"></a>
!!! function "[[nodiscard]] virtual bool Exists(const AmOsString&amp; path) const = 0"

    
    Checks if an item (file or folder) exists on the filesystem.
    
    
    :material-location-enter: **Parameter** `path`
    :    The path to the item.
    
    
    :material-keyboard-return: **Return**
    :    True if the file exists, false otherwise.
            
    

### GetBasePath<a name="GetBasePath"></a>
!!! function "[[nodiscard]] virtual const AmOsString&amp; GetBasePath() const = 0"

    
    Returns the base path of the filesystem.
    
    
    :material-keyboard-return: **Return**
    :    The base path for resolving relative paths from which the engine will load resources.
            
    

### IsDirectory<a name="IsDirectory"></a>
!!! function "[[nodiscard]] virtual bool IsDirectory(const AmOsString&amp; path) const = 0"

    
    Checks if an item (file or folder) is a directory.
    
    
    :material-location-enter: **Parameter** `path`
    :    The path to the item.
    
    
    :material-keyboard-return: **Return**
    :    True if the file is a directory, false otherwise.
            
    

### Join<a name="Join"></a>
!!! function "[[nodiscard]] virtual AmOsString Join(const std::vector&lt;AmOsString&gt;&amp; parts) const = 0"

    
    Merge the given parts of the path into a single path, by joining them with the filesystem
             * path separator.
    
    
    :material-location-enter: **Parameter** `parts`
    :    The parts of the path.
    
    
    :material-keyboard-return: **Return**
    :    A path concatenated with the given parts and the filesystem path separator.
            
    

### OpenFile<a name="OpenFile"></a>
!!! function "[[nodiscard]] virtual std::shared_ptr&lt;File&gt; OpenFile(const AmOsString&amp; path, FileOpenMode mode = eFOM_READ) const = 0"

    
    Opens the file at the given path.
    
    
    :material-location-enter: **Parameter** `path`
    :    The path to the file to open.
        
    :material-location-enter: **Parameter** `mode`
    :    The file open mode.
    
    
    :material-keyboard-return: **Return**
    :    The opened file. The returned File implementation depends on the FileSystem implementation.
            
    

### ResolvePath<a name="ResolvePath"></a>
!!! function "[[nodiscard]] virtual AmOsString ResolvePath(const AmOsString&amp; path) const = 0"

    
    Resolves a relative path from the filesystem base path.
    
    
    :material-keyboard-return: **Return**
    :    The resolved path.
            
    

### SetBasePath<a name="SetBasePath"></a>
!!! function "virtual void SetBasePath(const AmOsString&amp; basePath) = 0"

    
    Changes the filesystem base path. That path is interpreted by the implementation
             * and doesn't necessarily have to be a real path on disk. It's just used as the base path
             * for resolving relative paths from which the engine will load resources.
    
    
    :material-location-enter: **Parameter** `basePath`
    :    The filesystem base path.
                
    

### StartCloseFileSystem<a name="StartCloseFileSystem"></a>
!!! function "virtual void StartCloseFileSystem() = 0"

    
    Stops the FileSystem.
    
    This function MUST be called when the FileSystem is no longer needed.
    It is used to stop the filesystem (eg: unmounting an archive). It is
    recommended to process the stopping in a separate thread.
    
    The implementation is free to ignore this if not needed.
            
    

### StartOpenFileSystem<a name="StartOpenFileSystem"></a>
!!! function "virtual void StartOpenFileSystem() = 0"

    
    Opens the FileSystem.
    
    This function MUST be called before any other actions in the filesystem.
    It is used to initialize the filesystem (eg: mounting an archive). It is
    recommended to process the initialization in a separate thread.
    
    The implementation is free to ignore this if not needed.
            
    

### TryFinalizeCloseFileSystem<a name="TryFinalizeCloseFileSystem"></a>
!!! function "virtual bool TryFinalizeCloseFileSystem() = 0"

    
    Checks if the FileSystem is stopped.
    
    Since the StartCloseFileSystem() function is designed to be asynchronous, this function
    is used to check if the FileSystem has been successfully stopped.
    
    
    :material-keyboard-return: **Return**
    :    True if the FileSystem has been stopped, false otherwise.
            
    

### TryFinalizeOpenFileSystem<a name="TryFinalizeOpenFileSystem"></a>
!!! function "virtual bool TryFinalizeOpenFileSystem() = 0"

    
    Checks if the FileSystem is initialized.
    
    Since the StartOpenFileSystem() function is designed to be asynchronous, this function
    is used to check if the FileSystem has been successfully initialized.
    
    
    :material-keyboard-return: **Return**
    :    True if the FileSystem has been initialized, false otherwise.
            
    

### ~FileSystem<a name="_u007eFileSystem"></a>
!!! function "virtual ~FileSystem() = default"

    
    Default virtual destructor.
             
    
    
    

