import socket

class SocketClient:
    def __init__(self):
        self.server = '127.0.0.1'
        self.server_port = 8001

    def execute_command_on_server(self, cmd):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.server_port))
        print('sending command {}'.format(cmd))
        self.sock.send(cmd.encode('utf-8'))
        out = self.sock.recv(1024).decode('utf-8')
        exit_code = self.sock.recv(1024).decode('utf-8')
        print('command completed with return code {}'.format(exit_code))
        print('output is \n {}'.format(out))
        self.sock.close()
        return out


if __name__=='__main__':
    client = SocketClient()
    client.execute_command_on_server('tree')

    

        

