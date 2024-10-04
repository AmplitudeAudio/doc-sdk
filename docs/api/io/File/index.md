---
title: File
description: Base class for a file in a `FileSystem`.
generator: doxide
---


# File

**class  File**


Base class for a file in a `FileSystem`.


    


## Functions

| Name | Description |
| ---- | ----------- |
| [~File](#_u007eFile) | Default destructor.  |
| [GetPath](#GetPath) | Gets the path to the file in the loaded `FileSystem`. |
| [Read8](#Read8) | Reads a single byte from the file in an `AmUInt8`. |
| [Read16](#Read16) | Reads two bytes from the file in an `AmUInt16`. |
| [Read32](#Read32) | Reads four bytes from the file in an `AmUInt32`. |
| [Read64](#Read64) | Reads eight bytes from the file in an `AmUInt64`. |
| [ReadString](#ReadString) | Reads a string from the file. |
| [Write8](#Write8) | Writes a single byte to the file from an `AmUInt8`. |
| [Write16](#Write16) | Writes two bytes to the file from an `AmUInt16`. |
| [Write32](#Write32) | Writes four bytes to the file from an `AmUInt32`. |
| [Write64](#Write64) | Writes eight bytes to the file from an `AmUInt64`. |
| [WriteString](#WriteString) | Writes a string to the file. |
| [Eof](#Eof) | Checks if the read cursor is at the end of the file. |
| [Read](#Read) | Reads data from the file. |
| [Write](#Write) | Writes data to the file. |
| [Length](#Length) | Gets the size of the file in bytes. |
| [Seek](#Seek) | Seeks the read/write to the specified offset. |
| [Seek](#Seek) | Seeks the read/write to the specified offset, starting at the given origin. |
| [Position](#Position) | Gets the current position of the read/write cursor. |
| [GetPtr](#GetPtr) | Gets the pointer to the internal file handle. |
| [IsValid](#IsValid) | Checks if the file is valid. |

## Function Details

### Eof<a name="Eof"></a>
!!! function "virtual bool Eof() = 0"

    
    Checks if the read cursor is at the end of the file.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the read cursor is at the end of the file, `false` otherwise.
            
    

### GetPath<a name="GetPath"></a>
!!! function "[[nodiscard]] virtual AmOsString GetPath() const = 0"

    
    Gets the path to the file in the loaded `FileSystem`.
    
    
    :material-keyboard-return: **Return**
    :    The path to the file.
            
    

### GetPtr<a name="GetPtr"></a>
!!! function "virtual AmVoidPtr GetPtr()"

    
    Gets the pointer to the internal file handle.
    
    
    :material-keyboard-return: **Return**
    :    The internal file handle. This depends on the implementation.
            
    

### IsValid<a name="IsValid"></a>
!!! function "[[nodiscard]] virtual bool IsValid() const = 0"

    
    Checks if the file is valid.
    
    Validity of a file is determined by the underlying implementation. But this should
    primarily mean that the file exists AND has been opened.
    
    
    :material-keyboard-return: **Return**
    :    `true` if the file is valid, `false` otherwise.
            
    

### Length<a name="Length"></a>
!!! function "virtual AmSize Length() = 0"

    
    Gets the size of the file in bytes.
    
    
    :material-keyboard-return: **Return**
    :    The size of the file in bytes.
            
    

### Position<a name="Position"></a>
!!! function "virtual AmSize Position() = 0"

    
    Gets the current position of the read/write cursor.
    
    
    :material-keyboard-return: **Return**
    :    The actual position of the read/write cursor.
            
    

### Read<a name="Read"></a>
!!! function "virtual AmSize Read(AmUInt8Buffer dst, AmSize bytes) = 0"

    
    Reads data from the file.
    
    
    :material-location-enter: **Parameter** `dst`
    :    The destination buffer of the read data.
        
    :material-location-enter: **Parameter** `bytes`
    :    The number of bytes to read from the file. The destination buffer must be at least as large as the number of
        bytes to read.
    
    
    :material-keyboard-return: **Return**
    :    The number of bytes read from the file.
            
    

### Read16<a name="Read16"></a>
!!! function "AmUInt16 Read16()"

    
    Reads two bytes from the file in an `AmUInt16`.
    
    
    :material-keyboard-return: **Return**
    :    The read value.
            
    

### Read32<a name="Read32"></a>
!!! function "AmUInt32 Read32()"

    
    Reads four bytes from the file in an `AmUInt32`.
    
    
    :material-keyboard-return: **Return**
    :    The read value.
            
    

### Read64<a name="Read64"></a>
!!! function "AmUInt64 Read64()"

    
    Reads eight bytes from the file in an `AmUInt64`.
    
    
    :material-keyboard-return: **Return**
    :    The read value.
            
    

### Read8<a name="Read8"></a>
!!! function "AmUInt8 Read8()"

    
    Reads a single byte from the file in an `AmUInt8`.
    
    
    :material-keyboard-return: **Return**
    :    The read value.
            
    

### ReadString<a name="ReadString"></a>
!!! function "AmString ReadString()"

    
    Reads a string from the file.
    
    
    :material-keyboard-return: **Return**
    :    The read value.
            
    

### Seek<a name="Seek"></a>
!!! function "void Seek(AmSize offset)"

    
    Seeks the read/write to the specified offset.
    
    
    :material-location-enter: **Parameter** `offset`
    :    The offset in bytes from the beginning of the file.
                
    

!!! function "virtual void Seek(AmInt64 offset, eFileSeekOrigin origin) = 0"

    
    Seeks the read/write to the specified offset, starting at the given origin.
    
    
    :material-location-enter: **Parameter** `offset`
    :    The offset in bytes from the beginning of the file.
        
    :material-location-enter: **Parameter** `origin`
    :    The origin from which to begin seeking.
                
    

### Write<a name="Write"></a>
!!! function "virtual AmSize Write(AmConstUInt8Buffer src, AmSize bytes) = 0"

    
    Writes data to the file.
    
    
    :material-location-enter: **Parameter** `src`
    :    The source buffer of the data to write.
        
    :material-location-enter: **Parameter** `bytes`
    :    The number of bytes to write to the file. The source buffer must be at least as large as the number of bytes to
        write.
    
    
    :material-keyboard-return: **Return**
    :    The number of bytes written to the file.
            
    

### Write16<a name="Write16"></a>
!!! function "AmSize Write16(AmUInt16 value)"

    
    Writes two bytes to the file from an `AmUInt16`.
    
    
    :material-location-enter: **Parameter** `value`
    :    The value to write.
                
    

### Write32<a name="Write32"></a>
!!! function "AmSize Write32(AmUInt32 value)"

    
    Writes four bytes to the file from an `AmUInt32`.
    
    
    :material-location-enter: **Parameter** `value`
    :    The value to write.
                
    

### Write64<a name="Write64"></a>
!!! function "AmSize Write64(AmUInt64 value)"

    
    Writes eight bytes to the file from an `AmUInt64`.
    
    
    :material-location-enter: **Parameter** `value`
    :    The value to write.
                
    

### Write8<a name="Write8"></a>
!!! function "AmSize Write8(AmUInt8 value)"

    
    Writes a single byte to the file from an `AmUInt8`.
    
    
    :material-location-enter: **Parameter** `value`
    :    The value to write.
                
    

### WriteString<a name="WriteString"></a>
!!! function "AmSize WriteString(const AmString&amp; value)"

    
    Writes a string to the file.
    
    
    :material-location-enter: **Parameter** `value`
    :    The value to write.
                
    

### ~File<a name="_u007eFile"></a>
!!! function "virtual ~File() = default"

    
    Default destructor.
             
    
    
    

