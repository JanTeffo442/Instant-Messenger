import time
import socket
import sys

class Client():
    def __init__(self, soc, host, ip, port):
        self.soc = socket.socket()
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)
        self.port = 1234

    def client(self):
        print(f"Client server...\n {self.host} : {self.ip}")

        server_host = input("Enter server\'s IP address: ")
        name = input("Enter Client\'s name: ")

        print(f"Trying to connect to the server: {server_host} , {self.port}")

        time.sleep(20)

        self.soc.connect((server_host, self.port))
        print("Connected...\n")

        self.soc.send(name.encode())
        server_name = self.soc.recv(4096)
        server_name = server_name.decode()

        print(f"{server_name} has joined...")
        print("Enter [bye] to exit.")

        while True:
            message = self.soc.recv(4096)
            message = message.decode()

            print(f"{server_name} > {message}")

            message = input("Me > ")
            if message == "[bye]":
                message = "Leaving the chatroom"
                self.soc.send(message.encode())
                print("\n")
            
            self.soc.send(message.encode())


if __name__ == "__main__":

    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    start_chat = Client(soc=socket.socket(),host=socket.gethostname,ip=socket.gethostbyname(host),port=1234)
    start_chat.client()
