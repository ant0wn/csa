from __future__ import print_function, unicode_literals
from os import urandom


def genkey(length: int) -> bytes:
    """Generate key."""
    return urandom(length)


def xor_strings(s, t) -> bytes:
    """xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])


with open('data/xor-with-xor.bin', 'rb') as cipher_bin:
    cipher_bytes = cipher_bin.read()

pass
message = 'This is a secret message'
print('Message:', message)

key = genkey(len(message))
print('Key:', key)

cipherText = xor_strings(message.encode('utf8'), key)
print('cipherText:', cipherText)
print('decrypted:', xor_strings(cipherText, key).decode('utf8'))

# Verify
if xor_strings(cipherText, key).decode('utf8') == message:
    print('Unit test passed')
else:
    print('Unit test failed')
