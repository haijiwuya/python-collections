import datetime
import logging
import socket
import threading

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.clients = {}
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()  # 启动服务
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set():
            s, raddr = self.sock.accept()
            # makefile
            # f = s.makefile(mode='rw')
            logging.info(s)
            self.clients[raddr] = s
            threading.Thread(target=self.recv, name='recv', args=(s, raddr)).start()
            # threading.Thread(target=self.recv, name='recv', args=(f, raddr)).start()

    def recv(self, sock, addr):
        # def recv(self, f, addr):
        while not self.event.is_set():
            try:
                data = sock.recv(1024)
                # data = f.readline() # string 换行符\n
                logging.info(data)
            # 处理服务器主动关闭异常
            except Exception as e:
                logging.error(e)
                data = b'quit'
                # data = 'quit'
            # 某一连接退出后，移除
            if data == b'quit':
                self.clients.pop(sock.getpeername())
                break
            msg = "ack{}. {} {}".format(sock.getpeername(), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                        data.decode()).encode()
            for s in self.clients.values():
                # s.send('ack{}'.format(data.decode()).encode())
                s.send(msg)

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.set()


def main():
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            cs.stop()
            threading.Event.wait(3)
            break
        logging.info(threading.enumerate())


if __name__ == '__main__':
    main()
