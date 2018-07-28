import socket
import time
host='192.168.4.254'
port=1234
addr=(host,port)
c=socket.socket()
c.connect(addr)
fname=input('>')+'\r\n'
c.send(fname.encode('utf8'))
while True:
    data=c.recv(1024)
    print(data)
    if data.rstrip()==b'ok':
        with open(fname.rstrip()) as fobj:
            for line in fobj:
                data=line.rstrip()+'\n'
                print(data)
                if data:
                    c.send(data.encode('utf8'))
                    time.sleep(1)
        data=input('> ')+'\r\n'
        c.send(data.encode())
        if data.strip()=='end':
            break
c.close()



