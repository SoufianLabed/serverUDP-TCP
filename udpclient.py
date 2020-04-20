import socket
import sys

class udpclient:
    def __init__(self):
        self.PORT=int(sys.argv[1])                           # initialise le port et l'IP (broadcast)
        self.IP = sys.argv[2]
        self.sock = socket.socket(socket.AF_INET,         # création du socket qui communique entre le server et le client
                socket.SOCK_DGRAM)

    def sendMessage(self):
        self.sock.sendto(bytes(sys.argv[3], "utf-8"), (self.IP, self.PORT))     #envoie le message(récuperer par sys.argv[3]) à l'IP et par le port informé

    def receiveMessage(self):
        rep = True
        while rep == True:
            try:
                self.sock.settimeout(5)                                         # On attend 5 secondes une réponse
                data, addr = self.sock.recvfrom(1024)                           # récuperation du message envoyé par le server devant être inférieur à 1024 octets (Buffer)
                print("\"ok : "+ str(data.decode("utf-8"+'')) + "\"")           # Affichage dans le terminale
            except Exception as e:
                rep = False

clienttest=udpclient()
clienttest.sendMessage()
clienttest.receiveMessage()
