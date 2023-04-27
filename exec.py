import socket #biblioteca de redes
import tabela_rot  as Tabela_Rot

HOST = '127.0.0.1' #endereço de ip do roteador
PORT = 2402 #número da porta

#ip: porta
routes = {
    '192.168.0.1': 2403,
    '192.168.0.2': 2404,
    '192.168.0.3': 2405
}
#criação do socket do roteador
socket_rota = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_rota.bind((HOST, PORT))
socket_rota.listen()

print(f'Servidor rodando em {HOST}:{PORT}')

#loop do roteador:
#Enquanto aguarda uma conexão de entrada
while True :
    conn, addr = socket_rota.accept()
    print(f'Conexão recebida de {addr}')
    # Recebe a mensagem
    dado = conn.recv(1024).decode()
    print(f'Mensagem recebida: {dado}')

    # Verifica a tabela de roteamento para determinar o destino correto
    if dado in routes:
        porta_destino = routes[dado]
        print(f'Roteando mensagem -> {dado}:{porta_destino}')

        # Conecta-se ao destino para assim enviar mensagens
        socket_destino = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_destino.connect((dado, porta_destino))
        socket_destino.sendall(dado.encode())
        socket_destino.close()
    else:
        #Caso não, descarta mensagem
        print('Destino desconhecido,\n a mensagem foi descartada')
    conn.close()