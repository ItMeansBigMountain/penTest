import socket

# run server.py first

class Network:
    def __init__(self):
        self.client = socket.socket(  socket.AF_INET, socket.SOCK_STREAM  ) #connection type
        self.server = '76.16.112.102'
        self.port = 5555
        self.addr = (self.server , self.port)

        self.id = self.connect() #this is the encoded message we get when we connect
        print(self.id)


    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self , data):
        try:
            self.client.send(   str.encode(data)   )
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)









n = Network()
print(n.send("HELLO"))
print(n.send("working"))