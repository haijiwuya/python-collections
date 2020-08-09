import socket

server = socket.socket()
print(server)
print(server.bind)
ipaddr = ('127.0.0.1', 9999)
# 绑定端口
server.bind(ipaddr)
# 监听
server.listen()

# 等待连接
# s为新的socket对象，addr为对端地址
s, addr = server.accept()
while True:
    data = s.recv(1024)
    print(data)
    if 'exit' in data:
        break
    s.send('ack.{}'.format(data.decode().encode()))
s.close()
server.close()
