import socket
host='192.168.4.254'
port=12345
addr=(host,port)

cs=socket.socket()
cs.connect(addr)

fname='/tmp/passwd'
cs.send(fname)
while True:
    with open(fname,'rb') as fobj:
        data=fobj.read(4096)
        cs.send(data)
    if not data:
        break