import socket
import sys

class tcpserver:
    def __init__(self):
        self.PORT=int(sys.argv[1])     #Port d'écoute
        self.IP = ""            #Adresse IP de la machine (automatique) ""=adresse IpV4
        self.sock = socket.socket(socket.AF_INET, # Internet
                                    socket.SOCK_STREAM) # UDP
        self.sock.bind((self.IP, self.PORT))
        self.sock.listen(1)

    def receiveMessage(self):
        while True:
            
            connect, addr = self.sock.accept()
            print("Client d'adresse " + addr[0] + " depuis port  " + str(addr[1]))
            data = connect.recv(1024)
            if not data : break
            print("ok :", data.decode("utf-8")+'')
            connect.send(data)
        connect.close()

test=tcpserver()
test.receiveMessage()



#port
