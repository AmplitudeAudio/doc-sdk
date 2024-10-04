---
title: PackageFileHeaderDescription
description: Provides metadata about the package file.
generator: doxide
---


# PackageFileHeaderDescription

**struct PackageFileHeaderDescription**


Provides metadata about the package file.


    


## Variables

| Name | Description |
| ---- | ----------- |
| [m_Version](#m_Version) | Package file header tag.Package file version. |
| [m_CompressionAlgorithm](#m_CompressionAlgorithm) | The compression algorithm used for this package file.  |
| [m_Items](#m_Items) | The description of each item in the package file. |

## Variable Details

### m_CompressionAlgorithm<a name="m_CompressionAlgorithm"></a>

!!! variable "ePackageFileCompressionAlgorithm m_CompressionAlgorithm"

    
    The compression algorithm used for this package file.
             
    
    
    

### m_Items<a name="m_Items"></a>

!!! variable "std::vector&lt;PackageFileItemDescription&gt; m_Items"

    
    The description of each item in the package file.
    
    The total number of descriptions should match the number of items.
            
    

### m_Version<a name="m_Version"></a>

!!! variable "AmUInt16 m_Version"

    
    Package file header tag.
    
    
    !!! note
         Should be equal to 'AMPK'.
                
    
        Package file version.
    
    This is used to implement new features in package
        files and still be backward compatible with old versions.
                
    

