
import binascii
res='123123123'
print binascii.crc32(res) & 0xffffffff
