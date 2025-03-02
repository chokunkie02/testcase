def apply_caesar_cipher(text, shift):
    shift %= 26
    encrypted = []
    for char in text:
        if char.islower():
            encrypted.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif char.isupper():
            encrypted.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            encrypted.append(char)
    return ''.join(encrypted)