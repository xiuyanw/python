import socket
host='192.168.4.254' #服务器ip地址
port=12345       #服务器端口
addr=(host,port)

c=socket.socket()
c.connect(addr)
while True:
    data=input('> ')+'\r\n'
    c.send(data.encode('utf8'))
    if data.strip()=='end':
        break
    data=c.recv(1024)
    print(data.decode('utf8'))

c.close()