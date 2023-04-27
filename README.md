# tga-redes2

FILE: exec.py (main) ___________________________________________________________________________________
Foi usada a biblioteca do python "Socket" para lidar com as conexões (entrada e saída). 
Como exemplo de um roteador simples: foi setada o roteador com o endereço IP "127.0.0.1" e a porta "2402", e em seguida foi feita a criação dos sockets do roteador. 
No loop principal, enquanto aguarda conexão de entrada e quando for recebida, retorna um print informando, e tenta rotear a mensagem pra um destino/porta.

FILE: tabela_rot.py ___________________________________________________________________________________
Definição da tabela com as informações da tabela a serem exibidas -> destino, proximo salto (saída) e métrica (deveria ser definida por cada aluno).

FILE: dados.py ________________________________________________________________________________________
