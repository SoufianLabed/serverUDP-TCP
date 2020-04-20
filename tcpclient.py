import socket
import sys

class tcpclient:
    def __init__(self):
        self.PORT=int(sys.argv[1])                                              # initialise le port et l'IP (broadcast)
        self.IP = sys.argv[2]
        self.sock = socket.socket(socket.AF_INET,                               # création du socket qui communique entre le server et le client
                socket.SOCK_STREAM) 

    def sendMessage(self):
        self.sock.connect((self.IP,self.PORT))                                  #Demande au server de se connecter
        self.sock.sendto(bytes(sys.argv[3], "utf-8"), (self.IP, self.PORT))     #envoie le message(récuperer par sys.argv[3]) à l'IP et par le port informé

    def receiveMessage(self):
        rep = True
        while rep == True:
            try:
                self.sock.settimeout(5)
                data, addr = self.sock.recvfrom(1024)                           # Récupération du retour du serveur
                print("\"ok : "+ str(data.decode("utf-8"+'')) + "\"")           # Affichage dans le terminal
                self.sock.close()
            except Exception as e:
                rep = False

clienttest=tcpclient()
clienttest.sendMessage()
clienttest.receiveMessage()
