import socket

class Tabela_Rot:
    def __init__(self):
        self.route_table = {
    '192.168.0.1/2403': '192.168.1.1',  # Próximo salto para a sub-rede 192.168.1.0/24 é o endereço 192.168.1.1
    '192.168.0.2/2404': '192.168.2.1',  # Próximo salto para a sub-rede 192.168.2.0/24 é o endereço 192.168.2.1
    '192.168.0.3/2405': '192.168.3.1'  # Próximo salto para a sub-rede 10.0.0.0/8 é o endereço 10.0.0.1
}
#(i) rede de destino, (ii) interface de saída, (iii) métrica
# Exibição da tabela de roteamento
def table(self):
    print("Tabela de Roteamento:")
    print("#######################################################")
    for destino, next_hop, metrica in route_table.items():
        print(f"{destino} -> {next_hop} -> {metrica}")
