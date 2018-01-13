import socket
import sys
import subprocess

REQ_QUEUE_SIZE = 5 
PORT_NUMBER = 8001
class SocketServer:
    def __init__(self):
        self.sock = None

        
    def start_server(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # bind socket to port 
        self.sock.bind(('127.0.0.1', PORT_NUMBER))
        self.sock.listen(REQ_QUEUE_SIZE)
        print('listening on port {}'.format(PORT_NUMBER))

    def handle_requests(self):
        while True:
            client_socket, client_address = self.sock.accept()
            try:
                print('Received request from {}'.format(client_address))
                cmd = client_socket.recv(1024).decode() 
                print('Executing Command {}'.format(cmd))
                process = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE)
                output = process.communicate()[0]
                exit_code = str(process.returncode)
                print('sending output {} and retun code {}'.format(output, exit_code))
                client_socket.send(output)
                client_socket.send(exit_code.encode('utf-8'))
            except Exception as e:
                print('Excpetion occured while executing command : {} {}'.format(cmd, e))
            finally:
                client_socket.close()

if __name__=='__main__':
    
    server_object = SocketServer()
    server_object.start_server()

    server_object.handle_requests()

            

