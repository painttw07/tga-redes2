import socket

#(i) endereço IP de origem, (ii) endereço IP de destino, (iii) TTL e(iv) TOS.
#classe de dados - o que deveria conter no pacote de dados
class Dados:
    def _init_(self, orig, dest, TTL, TOS):
        self.host #host
        self.port #porta
        self.orig = ori #endereço origem
        self.dest = dest #endereço destino
        self.TTL = TTL #ttl
        self.TOS = TOS #tos


