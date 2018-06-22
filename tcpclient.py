#-- coding:utf-8 --

from socket import *
import struct


def packData(data):
	res = struct.pack("<IBI%ds" %(len(data)),0x314518,2,len(data),data.encode('utf-8'))
	print(res)
	return res
def unpackData(data):
	macCode,t,length = struct.unpack("<IBI",data[:9])
	if macCode == 0x314518:
		msg = struct.unpack("%ds" %(length),data[9:9+length])
		print(str(msg))
host = '127.0.0.1'
port = 8322
buffsize = 1024
ADDR = (host,port)

client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)
while True:
    data = input(">")
    if not data:
        break
    client.send(packData(data))
    data = client.recv(buffsize)
    if not data:
        break
    print(data)
    unpackData(data)
client.close()


