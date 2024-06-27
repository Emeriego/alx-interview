#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    """ Checks if a data set is valid utf8 encoded
    """
    def is_valid_byte(byte):
        return 0x00 <= byte <= 0xFF
    
    n_bytes = 0  # Number of continuation bytes expected
    
    for byte in data:
        if not is_valid_byte(byte):
            return False

        if n_bytes == 0:
            # Determine how many bytes are in this UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                n_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                n_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                n_bytes = 3
            elif (byte >> 7):  # 1-byte character should start with 0
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0

# Example usage
data = [197, 130, 1]  # Valid UTF-8
print(validUTF8(data))  # True

data = [235, 140, 4]  # Invalid UTF-8
print(validUTF8(data))  # False
