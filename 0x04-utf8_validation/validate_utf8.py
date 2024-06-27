def is_valid_byte(byte):
    """ Checks each byte of data.
        valid if within 0 - 255
    """
    return 0x00 <= byte <= 0xFF

def validUTF8(data):
    """ Checks if a data is valid utf8 encoded
        single byte: 0b0xxxxxxx no continuation byte
        2 bytes: 0b110xxxxx cont byte must start with 10xxxxxx
        3 bytes: 0b1110xxxx cont byte: 10xxxxxx
        4 bytes: 0b11110xxx cont byte: 10xxxxxx
        you get it?
    """

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
