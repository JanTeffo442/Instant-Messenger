import time
import socket
import sys

class ChatServer():
    def __init__(self, soc, host_name, ip, port):
        self.soc = socket.socket()
        self.host_name = socket.gethostname()
        self.ip = socket.gethostbyname(self.host_name)
        self.port = 1234

    def server_connect(self):
        print("Setup server")

        self.soc.bind((self.host_name, self.port))
        print(f"{self.host_name} : {self.ip}")

        name = input("Enter name: ")
        self.soc.listen(10)
        print("Waiting for incoming connections...")
        

        connection, addr = self.soc.accept()
        print(f"Received connection from {addr[0]}",f"{addr[1]}\n")
        print(f"Connection established. Connected from: {addr[0]}, {addr[1]}")

        client_name = connection.recv(4096)
        client_name = client_name.decode()
        print(f"{client_name} has connected.")

        self.connection.send(name.encode())

        while True:
            message = input("Me > ")
            if message == "[bye]":
                message = "Good  Night"
                connection.send(message.encode())
                print("\n")

            connection.send(message.encode())
            message = connection.recv(4096)
            message = message.decode()
            print(f"{client_name} > {message}")

if __name__ == "__main__":

    host_name= socket.gethostname()
    ip = socket.gethostbyname(host_name)
    server = ChatServer(soc=socket.socket(), host_name=socket.gethostname(), ip=socket.gethostbyname(host_name), port=1234)
    server.server_connect()

