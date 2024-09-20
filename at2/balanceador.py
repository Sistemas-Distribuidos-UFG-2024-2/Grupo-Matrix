import socket
import threading

def obter_servidor_ativo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as balanceador:
        balanceador.connect(('127.0.0.1', 6001))  # Conectar ao verificador de serviços
        servidor_info = balanceador.recv(1024).decode()
        return servidor_info

def conectar_cliente(conn, addr):
    print(f"Cliente conectado de {addr[0]}:{addr[1]}")
    while True:
        data = conn.recv(1024)  # Recebe dados do cliente
        if not data:
            break  # Se não houver mais dados, encerra a conexão

        print(f"Balanceador recebeu '{data.decode()}' de {addr[0]}:{addr[1]}")
        servidor_info = obter_servidor_ativo()
        if servidor_info != 'Nenhum servidor ativo.':
            servidor_ip, servidor_porta = servidor_info.split(':')
            servidor_porta = int(servidor_porta)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
                # Comunicação com o servidor ativo
                servidor.connect((servidor_ip, servidor_porta))
                servidor.sendall(data)
                resposta = servidor.recv(1024)

                # Enviar resposta ao cliente
                conn.sendall(resposta)
                print(f"Balanceador enviou resposta '{resposta.decode()}' de volta ao cliente.")
        else:
            print("Nenhum servidor ativo disponível.")
            conn.sendall(f'Nenhum servidor ativo disponível.')

    conn.close()  # Fecha a conexão com o cliente
    print(f"Conexão com o cliente {addr[0]}:{addr[1]} encerrada.")

def balanceador():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 5000))  # Balanceador escutando na porta 5000
        s.listen()
        print("Balanceador aguardando conexões de clientes...")
        
        while True:
            conn, addr = s.accept()  # Aceita novas conexões de clientes
            threading.Thread(target=conectar_cliente, args=(conn, addr)).start()  # Cria uma thread para cada cliente

balanceador()
