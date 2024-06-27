#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    """ Checks if a data set is valid utf8 encoded
    """
    def is_valid_byte(byte):
        return 0x00 <= byte <= 0xFF
    
    n_bytes = 0
    
    for byte in data:
        if not is_valid_byte(byte):
            return False

        if n_bytes == 0:
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
