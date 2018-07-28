import socket
from time import strftime
import os
host=''
port=12345
addr=(host,port)
s=socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)

while True:
    pid=os.fork()
    if pid:
        data,cli_addr=s.recvfrom(1024)
        clock=strftime('%H:%M:%S')
        data=data.decode('utf8')
        data='[%s]%s' %(clock,data)
        s.sendto(data.encode('utf8'),cli_addr)
    # else:
    #     while True:
    #         result=os.waitpid(-1,1)[0]
    #         if result==0:
    #             break