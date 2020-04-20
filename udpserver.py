import socket
import sys

class udpserver:
    def __init__(self):
        self.PORT=int(sys.argv[1])     # Port auquel le server écoutera
        self.IP = ""                   # "" désigne l'IP de la machine sur laquelle se lance le serveur
        self.sock = socket.socket(socket.AF_INET,
                                    socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.PORT))

    def receiveMessage(self):
        while True:
            data, addr = self.sock.recvfrom(1024)                                  # data correspond à la donner récu du client et addr contient l'IP et le port d'écoute
            print("Client d'adresse " + addr[0] + " depuis port  " + str(addr[1])) # Affichage dans le terminale du message et du port d'où le message a  été envoyé
            print("ok :", data.decode("utf-8")+'')
            self.sock.sendto(data,addr)

test=udpserver()
test.receiveMessage()
