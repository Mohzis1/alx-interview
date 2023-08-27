#!/usr/bin/python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    # Number of bytes to expect for the current character
    bytes_to_expect = 0
    
    for byte in data:
        # Check if the current byte starts with 10, which is invalid for the first byte
        if bytes_to_expect == 0 and (byte >> 6) == 2:
            return False
        
        if bytes_to_expect == 0:
            # Determine the number of bytes to expect for the current character
            if (byte >> 7) == 0:
                bytes_to_expect = 0  # Single-byte character
            elif (byte >> 5) == 6:
                bytes_to_expect = 1  # Two-byte character
            elif (byte >> 4) == 14:
                bytes_to_expect = 2  # Three-byte character
            elif (byte >> 3) == 30:
                bytes_to_expect = 3  # Four-byte character
            else:
                return False
        else:
            # Check if the current byte starts with 10, which is valid for continuation bytes
            if (byte >> 6) != 2:
                return False
            bytes_to_expect -= 1
    
    # All expected bytes were found
    return bytes_to_expect == 0

# Test cases
print(validUTF8([197, 130, 1]))  # Should return True
print(validUTF8([235, 140, 4]))  # Should return False

