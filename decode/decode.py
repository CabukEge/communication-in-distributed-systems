import sys

"""
Teil A
"""
def nrz_decode(sequence):
    try:
        char = chr(int(sequence, 2))
        if char.isupper():
            return char
        else:
            raise ValueError("Decoded value is not an uppercase ASCII character")
    except ValueError:
        raise ValueError("Invalid input or non-ASCII character")

def differential_decode(sequence):
    try:
        decoded = ""
        last_bit = '0'
        for bit in sequence:
            decoded_bit = '1' if bit != last_bit else '0'
            decoded += decoded_bit
            last_bit = bit
        char = chr(int(decoded, 2))
        if char.isupper():
            return char
        else:
            raise ValueError("Invalid ASCII character")
    except ValueError:
        raise ValueError("Invalid input or non-ASCII character")

def revised_4b5b_decode(sequence):
    _4b5b_encoding_table = {
        '11110': '0000', '01001': '0001', '10100': '0010', '10101': '0011',
        '01010': '0100', '01011': '0101', '01110': '0110', '01111': '0111',
        '10010': '1000', '10011': '1001', '10110': '1010', '10111': '1011',
        '11010': '1100', '11011': '1101', '11100': '1110', '11101': '1111',
    }
    try:
        block1, block2 = sequence[:5], sequence[5:]
        decoded1 = _4b5b_encoding_table.get(block1, None)
        decoded2 = _4b5b_encoding_table.get(block2, None)
        if decoded1 is None or decoded2 is None:
            raise ValueError("Invalid 4B5B sequence")
        char = chr(int(decoded1 + decoded2, 2))
        if char.isupper():
            return char
        else:
            raise ValueError("Invalid ASCII character")
    except ValueError:
        raise ValueError("Invalid input or non-ASCII character")

def byte_decode(encoding, sequence):
    if encoding == "nrz":
        return nrz_decode(sequence)
    elif encoding == "differential":
        return differential_decode(sequence)
    elif encoding == "4b5b":
        return revised_4b5b_decode(sequence)
    else:
        raise ValueError("Unsupported encoding type")


"""
Teil B
"""

def bytestring_decode(encoding, sequence):
    decoded_text = ""
    if encoding not in ["nrz", "differential", "4b5b"]:
        raise ValueError("Unsupported encoding type")

    # Encoding-Spezifische Länge cheken
    byte_length = 10 if encoding == "4b5b" else 8

    # Muss Vielfaches von Bytelength sein
    if len(sequence) % byte_length != 0:
        raise ValueError(f"Invalid input length for: {encoding}")

    for i in range(0, len(sequence), byte_length):
        byte_sequence = sequence[i:i+byte_length]
        try:
            decoded_char = byte_decode(encoding, byte_sequence)
            decoded_text += decoded_char
        except ValueError:
            raise ValueError("Invalid bytestring: not all bytes are uppercase ASCII characters")

    return decoded_text

"""
Teil C
"""
def mixed_decode(sequence):
    decoded_text = ""
    encoding_methods = ["nrz", "differential", "4b5b"]
    
    i = 0
    while i < len(sequence):
        valid_decoded_char = None

        # Jede Codierungsmethode versuchen
        for encoding in encoding_methods:
            byte_length = 10 if encoding == "4b5b" else 8
            if i + byte_length <= len(sequence):
                byte_sequence = sequence[i:i + byte_length]
                try:
                    decoded_char = byte_decode(encoding, byte_sequence)
                    if decoded_char.isupper():
                        valid_decoded_char = decoded_char
                        break
                except ValueError:
                    continue  # Wenn eine Methode fehlschlägt, versuche die nächste
        
        if valid_decoded_char:
            decoded_text += valid_decoded_char
        # Anstelle eines Fehlers, fahre mit dem nächsten Byte fort
        i += byte_length if valid_decoded_char else 8  # Standardmäßig um 8 Bits erhöhen

    return decoded_text

def main():
    encoding = sys.argv[1]
    sequence = sys.argv[2]

    # Abhängig von den übergebenen Argumenten von run.sh
    if encoding == "nrz" or encoding == "differential" or encoding == "4b5b":
        decoded_result = bytestring_decode(encoding, sequence)
        print("SOLUTION:", decoded_result)
    elif encoding == "mixed_decode":
        decoded_mixed_text = mixed_decode(sequence)
        print("SOLUTION:", decoded_mixed_text)
    else:
        print("Ungültige Codierungsmethode.")

# Hier startet die Ausführung der Tests
if __name__ == "__main__":
    main()